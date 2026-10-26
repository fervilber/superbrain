---
title: "Infinity: un runtime para concurrencia extrema de agentes (AWS + UC Berkeley)"
source: "https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/"
author: "Shadaj Laddad (AWS Open Source Blog)"
date: 2026-10-23
captured: 2026-10-24
---

# Introducing Infinity: a runtime for extreme agent concurrency

By Shadaj Laddad, 23 OCT 2026, Announcements.

Agents spend much of their time waiting on tools. A coding agent may start a build that runs for twenty minutes, a triage agent may wait hours for the next pull request on a repository, and an assistant may wait until the next morning for an approval. Most agent harnesses run the agent loop as a sequence of blocking steps: the harness calls the model, invokes a tool, waits for the tool to return, and repeats. While the agent waits, it holds a process and its memory, and it cannot respond to events that arrive in the meantime.

Today, we're releasing Infinity under the Apache 2.0 open source license as part of the Hydro project, a collaborative effort between AWS and UC Berkeley. Infinity is a research project that re-imagines agent runtimes, based on the techniques that programming languages use to suspend and resume asynchronous functions. When an agent calls a tool, Infinity dispatches the call, saves the conversation, and suspends the agent. When the tool result arrives, the runtime resumes the agent from its saved state.

With Infinity, concurrent agents are extremely lightweight. For example, we can fit 75,000 concurrent agents in the 8 GB of a Raspberry Pi 5. Infinity also makes it possible to deploy concurrent agents on standard serverless platforms. When Infinity suspends an agent during a tool call, the serverless function can end. So even if a tool call takes days, nothing needs to run while the agent waits.

Infinity is an early research release, and we are sharing it to get early feedback. The rest of this post describes the ideas behind Infinity and its architecture. We start with an overview of how languages suspend asynchronous functions with stackless coroutines, and why an agent can be suspended in the same way. We'll explore how Infinity uses this to run many agents concurrently, even on serverless platforms. We then describe synthetic tool calls, which Infinity uses to deliver asynchronous events to existing models, and we use synthetic events for agent-to-agent communication. Finally, we discuss some open questions that we hope to explore further.

## The Infinity Runtime

The Infinity Runtime uses this idea to suspend and resume long-running agents. It executes each agent as a sequence of bounded slices. In a slice, the runtime loads the agent's history from a pluggable store, runs one model completion, persists the output, and dispatches at most one tool call. The slice then ends. Tool calls play the role of `await` points: a slice never blocks for a tool, a timer, or any other external operation.

## Running agents concurrently

Since a suspended agent occupies no memory, the runtime can manage a large number of agents and schedule them as messages arrive. Agents run inside an agent system, which is a pool of agent threads that share stores, tools, and a model. The runtime organizes the agent threads in a way similar to an actor system. Each conversation thread has its own input queue, threads do not share mutable state, and threads communicate only by sending messages to each other's queues. Each message carries a `thread_id` that identifies its destination thread. The runtime guarantees that messages for the same thread are processed in order, one slice at a time, while slices for different threads run in parallel.

## Benchmark

We ran the benchmark with 80,000 agents, for a total of 3.2 million completions, on a single thread of an AMD EPYC 9R14 with in-memory stores. Resident memory grew linearly, at about 100 KB per idle agent. At this rate, about 75,000 agents fit in 8 GB, which is the memory of a Raspberry Pi 5. Most of this memory is taken up by the conversation histories, since an idle agent has no task, stack, or connection associated with it.

## Synthetic tool calls

Synthetic tool calls let the runtime deliver asynchronous events to existing models, and the same mechanism carries messages between parent and child agents.

## Conclusion

Agents are increasingly expected to run for long periods, react to events, and divide work among subagents. Infinity explores an execution model for such agents based on stackless coroutines: the runtime treats each tool call as a suspension point, saves the conversation history as the agent's continuation, and resumes the agent when a message arrives. With this model, an idle agent costs about as much memory as its history, many agents can share a small number of threads, and the same agent code can run in a local process or on a serverless platform. Synthetic tool calls let the runtime present asynchronous events to the model within the structure that model APIs already support, and the same mechanism carries messages between parent and child agents. Infinity is available now on GitHub. In the quickstart, you can build a simple agent running on Infinity in just a few minutes! This is an early research release, and we welcome feedback on both the ideas and the implementation.
