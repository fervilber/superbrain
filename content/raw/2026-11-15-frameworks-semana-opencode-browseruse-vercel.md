---
title: "Herramientas de agentes de la semana: opencode v2.3.0, browser-use 1.0.5 con juez, Vercel AI SDK y CopilotKit OpenBot 1.0"
source: "https://aiagentnews.io/topics/frameworks"
date: 2026-11-15
captured: 2026-11-15
---

# Frameworks for AI agents — AI Agent News

Fuente: aiagentnews.io/topics/frameworks (actualizado 15 de noviembre de 2026).

## Entradas (verbatim)

> **Nov 15 — Anthropic details how Claude Code's team reviews AI-written code.** Anthropic has described how the Claude Code team reviews code as AI agents write a growing share of its codebase. The process layers automated checks, AI reviewers and risk-based human approval to cut manual review time without more regressions.

> **Nov 14 — browser-use 1.0.5 adds a judge that grades every agent run.** browser-use 1.0.5 sends each run through one extra low-effort model request that fills a judgement field on the result. The release also adds a judge_context option for custom criteria and a judge=False switch to turn the check off.

> **Nov 14 — opencode v2.3.0 runs subagents in the background by default.** The opencode project released v2.3.0, which makes subagents run in the background and report back when they go idle. The release also collapses tool-call transcripts into one activity row by default.

> **Nov 13 — Vercel's @ai-sdk/workflow 2.0.105 adds tool approval and timeouts to WorkflowAgent.** Vercel released @ai-sdk/workflow 2.0.105, which adds toolApproval, toolOrder and a timeout object to WorkflowAgent. The patch also fixes several abort, tool-result and logging behaviors so WorkflowAgent matches ToolLoopAgent more closely.

> **Nov 13 — Claude Code v2.1.325 fixes a zstd decoding flaw and changes sandboxed Bash prompts.** Anthropic's Claude Code v2.1.325 patches a security issue in how zstd-compressed responses are decoded, along with many smaller fixes. Sandboxed Bash commands now go through the normal permission flow by default.

> **Nov 12 — Vercel's AI SDK adds a TypeSafe AI decision model catalog in @ai-sdk/typesafe-ai 3.0.39.** Vercel has released @ai-sdk/typesafe-ai 3.0.39, a patch that adds a TypeSafe AI decision model catalog.

> **Nov 12 — Leeroo open-sources Kapso, an engine that learns from experiments on enterprise data.** Leeroo has open-sourced Kapso, an engine that runs experiments on enterprise data, deploys the best solution it finds, and records lessons from each run. The team reports benchmark results on RelBench, MLE-bench and the 2026 International Olympiad in AI, though those figures are self-reported.

> **Nov 12 — CopilotKit releases OpenBot 1.0, a self-hostable AI coworker with governance.** CopilotKit has released OpenBot 1.0, an MIT-licensed AI coworker workspace that can be self-hosted. The product lets companies bring their own agents, models and infrastructure.

## Otras entradas del ecosistema (verbatim, selección de la búsqueda)

> **Amazon Quick publishes a taxonomy of agentic primitives.** The Amazon Quick team has set out a shared vocabulary for agentic work built on four questions: When, What, Who and How. The framework separates triggers, persistent agents, tools, skills and workflows, so a request such as a daily Slack digest maps to a clear design choice.

> **Perplexity launches Teammates, always-on AI agents for work.** Perplexity has launched Teammates, always-running agents that can each take a different job inside a workspace. The feature builds on Perplexity Computer and requires the company's $200 per month Max plan.

> **Microsoft releases installable Agent Framework builder skills for .NET and Python coding agents.** Microsoft has added installable Agent Framework builder skills for .NET and Python that give coding assistants maintained guidance for building and modifying Agent Framework applications. The skills are installed into the coding assistant at development time and are not loaded by the shipped application.

> **OpenAI ships Agents SDK v0.24.0-alpha.7 with durable sessions and usage budgets.** OpenAI released alpha 7 of its Agents SDK, adding durable root sessions, hosted tools and observed usage budgets to the native runtime. The alpha also changes several defaults and names, so existing projects should review the upgrade steps before moving over.

> **Google DeepMind uses AI agents to formally verify Signal's protocol code.** Google DeepMind researchers used AlphaProof Code, a multi-LLM agentic framework, to mathematically prove key security properties of the code behind Signal's cryptographic protocol.

## Lectura técnica

La semana consolida tres patrones en las herramientas de agentes:

1. **El juez como parte del bucle**: browser-use 1.0.5 añade un juez que califica cada ejecución (una petición extra de modelo de bajo esfuerzo que rellena un campo `judgement`, con `judge_context` para criterios propios y `judge=False` para desactivarlo). Es la misma idea que el «learning» con verificación de AgentRun.
2. **Subagentes en segundo plano por defecto**: opencode v2.3.0 los ejecuta en background y reportan al quedar ociosos, colapsando las trazas de tool-calls en una sola fila de actividad. La orquestación asíncrona se vuelve el comportamiento por defecto, no una opción.
3. **Aprobación y presupuesto como ciudadanos de primera**: Vercel añade `toolApproval`, `toolOrder` y timeouts a `WorkflowAgent`; OpenAI añade sesiones raíz durables, herramientas hospedadas y **presupuestos de uso observados** a su Agents SDK. El control del gasto y la aprobación de herramientas se integran en el runtime.
