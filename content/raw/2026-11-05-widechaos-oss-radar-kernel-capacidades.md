---
title: "Open Source Radar: los frameworks de agentes separan el kernel de las capacidades (Octopus-SI-OS, AgentScope-Java)"
source: "https://widechaos.cn/blog/oss-radar-2026-11-04-en"
date: 2026-11-04
captured: 2026-11-05
---

# Open Source Radar · 2026-11-04: Agent frameworks start separating the kernel from the capabilities

Wide Chaos, 4 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract`.

This issue covers five projects drawn from one candidate pull on 2026-11-04: a pool of 95 entries, a de-duplication ledger of 313, and 12 candidates as the script's default output limit. The daily GitHub Trending fetch timed out during that pull (the script records it under `errors`); the weekly Trending entry point and topic searches did return results, and those two paths supplied the candidates. I picked five on three grounds: whether the approach can be borrowed by another system, whether it has something no one else has, and only then heat. For each project I read the README, the release notes where a release exists, and recent commits. Nothing was installed or run, so nothing below is my own measured claim about performance, deployment or stability.

### 1. miuuyy/Octopus-SI-OS ⭐ 679 · Rust

GitHub: https://github.com/miuuyy/Octopus-SI-OS

In one line: An agent runtime rebuilt on operating-system lines: eight primitives in the kernel, models and tools outside it, and an agent that can rewrite its own interfaces and tools when policy allows.

What it is: A research-preview agent desktop system for macOS 14 and later. The repository was created on 2026-10-09 and had 679 stars and 73 forks by 11-04. The README and `docs/architecture.md` tell the same story: a kernel of roughly 45,000 lines of Rust, with Codex CLI moved in and running as one interface among many. The shape is a handful of primitives plus thousands of JSON descriptors, so a new capability arrives by declaration rather than by a new branch inside the loop.

What stands out:

- **Eight primitives and no orchestrator.** Interface (a typed port), Artifact (the only thing that crosses a boundary), Run (a durable execution record that parks and wakes on artifacts; it is data, not a process), Execution environment (a goal with a policy; environments nest and inner ones are narrower), Worker (a role plus a ceiling, not a program), Worker environment (the room where tools act), Policy (never stored, formed on each arrival), and Mark (recorded only after a verifier passes).
- **The kernel decodes nothing and pushes nothing.** Resident interfaces such as providers, channels and tool rooms are each their own process reading their own movements; a worker is only a descriptor plus a policy ceiling, with no code. The provider interface builds what the model sees, and the room's door checks a tool against the grant before running it. One turn is a set of rows in a ledger.
- **A refusal is also a row.** Blocked calls are recorded with a type instead of being dropped silently. That is harder than logging the calls that succeed, and more useful.
- **Authority is formed per call.** Policy is computed at each arrival rather than stored, so a worker's ceiling is re-evaluated on every attempt instead of cached at startup.

### 2. agentscope-ai/agentscope-java ⭐ 6,237 · Java

GitHub: https://github.com/agentscope-ai/agentscope-java

In one line: Agents treated as stateful, long-lived services: event stream, permission gate, sandbox and cross-replica session recovery are built into the framework instead of assembled by the user.

What it is: The Java implementation of AgentScope, positioned in the README as production-ready, distributed and enterprise-grade. Version 2.0 reached GA in 2026-07; the repository dates from 2025-09-23 and had 6,237 stars and 1,562 forks. JDK 17 or newer is a hard requirement. Session state can sit in memory or a JSON file, and a multi-replica deployment needs it externalized to Redis, MySQL, PostgreSQL or object storage; the sandbox can run as a local subprocess or be switched to Docker, Kubernetes or the E2B cloud. Since 2026-08 there is also an AgentScope Service, a control plane and dashboard that declares compatibility with LangChain, ADK, Claude/Qoder and other external agents.

### Lecturas del autor

- Agent frameworks are separating the kernel from the capabilities. Octopus moves both the model and the loop out of the centre, leaving primitives and descriptors; agentscope-java takes the other road, building events, permissions and session state into the framework. Both stop treating "one very long prompt loop" as the architecture.
- What makes long-running sessions hard is recovery and permission. Externalized session state, cross-replica recovery, three-state tool authorization and a record of refusals decide whether an agent can run for days and whether it can be handed to someone else.
- The moat for RAG platforms is the permission boundary. MaxKB's batch of fixes included cross-tenant content injection, unauthorized reads and configuration leaking from an anonymous endpoint, alongside decompression and verification-code problems that a single instance is exposed to as well.
- The right abstraction for writing tools is structured assets. No context window holds a whole book. Splitting setup, cast, blueprint and foreshadowing into assemblable assets and fetching only what a chapter needs gives every chapter a stable set of facts, instead of betting on a longer context window.
