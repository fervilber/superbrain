---
title: "Introducing Infinity: a runtime for extreme agent concurrency (AWS Open Source Blog) — captura"
source: "https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/"
date: 2026-10-23
captured: 2026-10-31
---

# Introducing Infinity: a runtime for extreme agent concurrency

> Captura del texto completo publicado por Shadaj Laddad (research lead del equipo Hydro, AWS) en el AWS Open Source Blog el 23 de octubre de 2026, más el detalle técnico y la reproducción independiente del benchmark publicados por AgentStack (agentopsguide.com) el 24 de octubre de 2026. El texto se reproduce/parafrasea de forma fiel a los extractos obtenidos.

## Tesis de la publicación

Agents spend much of their time waiting on tools. A coding agent may start a build that runs for twenty minutes, a triage agent may wait hours for the next pull request on a repository, and an assistant may wait until the next morning for an approval. Most agent harnesses run the agent loop as a sequence of blocking steps: the harness calls the model, invokes a tool, waits for the tool to return, and repeats. While the agent waits, it holds a process and its memory, and it cannot respond to events that arrive in the meantime.

Today, we're releasing **Infinity** under the Apache 2.0 open source license as part of the **Hydro** project, a collaborative effort between AWS and UC Berkeley. Infinity is a research project that re-imagines agent runtimes, based on the techniques that programming languages use to suspend and resume asynchronous functions. When an agent calls a tool, Infinity dispatches the call, saves the conversation, and _suspends_ the agent. When the tool result arrives, the runtime _resumes_ the agent from its saved state.

With Infinity, concurrent agents are extremely lightweight. For example, we can fit **75,000 concurrent agents in the 8 GB of a Raspberry Pi 5**. Infinity also makes it possible to deploy concurrent agents on standard serverless platforms. When Infinity suspends an agent during a tool call, the serverless function can end. So even if a tool call takes days, nothing needs to run while the agent waits.

## Agents as stackless coroutines

Many languages, including Rust, JavaScript, and Python, let developers write asynchronous logic with `async` and `await`. When a function awaits an async operation, such as a network request, the function is suspended, and the thread that was running it moves on to other work. When the operation completes, the runtime resumes the function from the point where it was suspended. To make this possible, the runtime has to save the function's _continuation_, which is the state it needs in order to resume.

Languages save this state in one of two ways. Operating system threads and stackful coroutines keep the task's entire call stack in memory while it waits. Stackless coroutines, which Rust uses to implement `async fn`, instead have the compiler turn each function into a state machine that holds only the relevant values at each `await`. This approach results in a smaller memory footprint, so an executor can efficiently run a large number of stackless coroutines.

An LLM agent can be suspended in the same way as a stackless coroutine. At the moment an agent calls a tool, its conversation history contains everything needed to continue the agent once the result is available. If the runtime persists this history, it can discard all in-memory state, and any process with access to the store can resume it later.

The Infinity Runtime uses this idea to suspend and resume long-running agents. It executes each agent as a sequence of bounded _slices_. In a slice, the runtime loads the agent's history from a pluggable store, runs one model completion, persists the output, and dispatches at most one tool call. The slice then ends. Tool calls play the role of `await` points: a slice never blocks for a tool, a timer, or any other external operation.

## Running agents concurrently

Since a suspended agent occupies no memory, the runtime can manage a large number of agents and schedule them as messages arrive. Agents run inside an _agent system_, which is a pool of _agent threads_ that share stores, tools, and a model. The runtime organizes the agent threads in a way similar to an actor system. Each conversation thread has its own input queue, threads do not share mutable state, and threads communicate only by sending messages to each other's queues. Each message carries a `thread_id` that identifies its destination thread. The runtime guarantees that messages for the same thread are processed in order, one slice at a time, while slices for different threads run in parallel.

Ordering within a thread is required for correctness, because two slices that read and write the same history at the same time would overwrite each other's turns. Different threads have nothing to coordinate. In a long-running process, the agent system gives each active thread a channel and a lightweight task, and schedules the pool in the same way that an async executor schedules futures. When a thread has no queued messages and no pending tool results, its task exits, and the runtime starts a new one when the next message for that thread arrives.

## Benchmark de memoria (AWS)

Because a suspended agent consists only of its history, the memory needed to keep agents resident is close to the size of their histories. To measure this, we wrote a benchmark that launches waves of agents in one agent system, backed by a simulated model. Each agent runs twenty turns, and each turn makes a full round trip through the runtime: the model streams a completion of about 1.2 KB that calls a tool, the tool result returns through the input queue, and a second completion ends the turn.

We ran the benchmark with **80,000 agents, for a total of 3.2 million completions**, on a single thread of an AMD EPYC 9R14 with in-memory stores. Resident memory grew linearly, at about **100 KB per idle agent**. At this rate, about 75,000 agents fit in 8 GB, which is the memory of a Raspberry Pi 5. Most of this memory is taken up by the conversation histories, since an idle agent has no task, stack, or connection associated with it.

## Herramientas que no bloquean

```rust
let system = AgentSystemBuilder::new_local(
    InMemoryConversationStore::new(),
    InMemoryStateStore::new(),
    StaticModel::new(provider, "global.anthropic.claude-sonnet-4-6").await?,
)
.tool(Box::new(GetBuildStatus { builds }))
.start();
let mut thread = system.thread_builder().launch().await;
thread.send_user_text("Is build 42 green yet?").await?;
while let Some(event) = thread.recv().await {
    println!("{event:?}");
}
```

The difference from most agent frameworks is in how tools are written. Rather than returning its result, a tool's `execute` method starts the work and returns immediately. When the work completes, the tool sends the result to the agent's input queue. When the model calls `get_build_status`, the runtime persists the turn containing the call, invokes `execute`, and ends the slice. If the status lookup takes a hundred milliseconds, the next slice begins almost immediately. If it takes three days, the agent occupies only its stored history in the meantime. The tool and agent code are the same in both cases.

## Synthetic tool calls y comunicación agente-a-agente

Model APIs expect one result per tool call, so Infinity delivers later events as **synthetic tool calls** named `receive_event__injected`. The runtime never offers that name to the model and rejects it if the model tries to call it. A built-in `spawn_thread` tool uses the same mechanism, so child agents report back to their parent as events. Spawning a child (`spawn_thread`) and reporting to a parent (`report_to_parent`) are ordinary tool calls whose results and events travel through the input queues; a parent and its children run concurrently as separate threads in the same agent system. El runtime también decide _dónde_ se procesa cada evento: por defecto cada evento se procesa en un hilo hijo temporal que hereda el contexto del padre y decide si actuar o cerrarse sin informe (el historial del padre queda intacto); un evento puede marcarse como _associative_ para inyectarse directamente en el historial del hilo suscriptor (pensado para eventos que actualizan una operación en curso, como la salida de un test lanzado en segundo plano).

## RAP: el protocolo reactivo

Del material de documentación recogido por AgentStack:

- Infinity ships with an asynchronous tool protocol called the **Reactive Agent Protocol (RAP)** and a coding agent called **Infinity Code**.
- The Reactive Agent Protocol makes tool calls asynchronous. The agent posts a call over HTTP, the tool acknowledges it, and the agent can shut down. When the work finishes, the tool posts the result to the agent's callback URL. **MCP keeps a request open until the tool returns.**
- RAP replaces MCP's synchronous request and response model with fire-and-forget tool calls, adding subscriptions and long-running tool calls.
- The documentation says **any MCP server works as a RAP tool through a compatibility layer**, so the MCP servers teams already run stay usable. It also says MCP works fine for agents that only need quick request and response calls.
- In **step mode**, nothing stays in memory between calls, and AWS says an agent waiting on a three-day CI pipeline uses no compute until the result arrives. Each input carries a stable ID, and the state store records processed IDs, so a redelivered queue message is skipped. Turns are written to storage only after they complete.
- The AWS reference deployment uses **SQS FIFO queue per thread group, Lambda for each delivery, Aurora DSQL for histories, DynamoDB for deduplication, and EventBridge Scheduler for timers**, provisioned with CDK constructs.
- The `hydro-project/infinity` repository is Rust and splits into 21 crates, including providers for Amazon Bedrock and the Rig library. The core crate `infinity-agent-core` is at version 0.2.0 on crates.io.

## Reproducción independiente del benchmark (AgentStack)

AgentStack rebuilt the `agent_scale` benchmark from commit `341f6c2` and ran it on an 8 vCPU Intel Xeon machine (single-threaded, in-memory stores, scripted model):

- Baseline run: 10,000 agents × 20 turns = 400,000 completions in 32.3 seconds. Process memory ended at 1,056 MB, or **105.6 KB per agent** → about 75,700 agents per 8 GB (matches AWS within 1%).
- Memory grew about **5 KB per tool-calling turn**. Agents with 160 turns fit about **10,100** in 8 GB.
- Throughput fell from about **18,200 completions/second at 5 turns to 2,500 at 160 turns** — still under a millisecond of runtime work per completion.
- Caveat declared by the authors of the rerun: the benchmark uses a scripted model with compaction off; Infinity is pre-release (v0.2.0 crates).

Tabla de la reproducción:

| Turns per agent | Agents in run | Memory per agent | Agents per 8 GB | Completions per second |
| --------------- | ------------- | ---------------- | --------------- | ---------------------- |
| 5               | 2,000         | 26.0 KB          | 308,000         | 18,200                 |
| 10              | 2,000         | 51.5 KB          | 155,300         | 18,200                 |
| 20              | 2,000         | 101.8 KB         | 78,600          | 14,800                 |
| 40              | 2,000         | 201.5 KB         | 39,700          | 9,200                  |
| 80              | 2,000         | 398.6 KB         | 20,100          | 5,000                  |
| 160             | 1,000         | 794.8 KB         | 10,100          | 2,500                  |

## Conclusión del anuncio

Agents are increasingly expected to run for long periods, react to events, and divide work among subagents. Infinity explores an execution model for such agents based on stackless coroutines: the runtime treats each tool call as a suspension point, saves the conversation history as the agent's continuation, and resumes the agent when a message arrives. With this model, an idle agent costs about as much memory as its history, many agents can share a small number of threads, and the same agent code can run in a local process or on a serverless platform. Synthetic tool calls let the runtime present asynchronous events to the model within the structure that model APIs already support, and the same mechanism carries messages between parent and child agents.

Infinity is available now on GitHub (`hydro-project/infinity`), with a quickstart for launching a first agent in a few minutes. It is an early research release; feedback on both the ideas and the implementation is welcome.
