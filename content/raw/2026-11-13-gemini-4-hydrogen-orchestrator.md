---
title: "Google Gemini 4 Hydrogen y Orchestrator: el modelo de ejecución rápida y el enrutado bidireccional dentro de una misma trayectoria"
source: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/ ; https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/ ; https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen ; https://www.infoworld.com/article/4248403/google-adds-multi-model-orchestrator-gemini-4-hydrogen-to-antigravity.html"
date: 2026-11-13
captured: 2026-11-13
---

# Gemini 4 Hydrogen y Orchestrator (Google, 12-13 de noviembre de 2026)

Captura por extractos del anuncio oficial de Google DeepMind, del blog de Google Antigravity, de la guía _What's new in Gemini 4 Hydrogen_ de la Gemini API y del análisis de InfoWorld. Fecha de captura: 2026-11-13.

## Anuncio oficial (blog.google)

> Today, we're introducing Gemini 4 Hydrogen, bringing cutting-edge intelligence to everyone — with speed and efficiency for everyday coding and agentic workflows. While our frontier models, Gemini 4 Carbon and Gemini 4 Argon, excel at deep, long-horizon reasoning on your hardest problems, Hydrogen is built for rapid execution across diverse agentic workflows.

> Hydrogen surpasses Argon on the Artificial Analysis Intelligence Index at its default high thinking level (51 vs. 50, and reaching 54 at its highest xhigh thinking setting), while often completing tasks faster than models in its class. Gemini 4 Hydrogen is priced flat across its entire 1 million-token context window at $1.50 per million input tokens and $7.50 per million output tokens.

> To help make this multi-model collaboration automatic, we're introducing Orchestrator in Google Antigravity. Rather than using a single model from start to finish, Orchestrator dynamically switches between models like Carbon and Hydrogen within the same session. On Terminal-Bench 4.0, Orchestrator reached near-Carbon task success rates while, on average, consuming 24% less quota and completing 19% faster.

> It delivers significant leaps in both speed and intelligence — finishing tasks 2.5 times faster at its high default setting while more than tripling Terminal-Bench 4.1 scores (57% vs. 18.2%), cutting fabricated claims by more than 5x, and adapting cleanly when a tool call fails or a search returns empty.

## Google Antigravity (blog de producto)

> Today, we're rolling out Gemini 4 Hydrogen inside Google Antigravity alongside a new model dropdown option called Orchestrator, which pairs Hydrogen with our strongest models for long-horizon tasks, including Gemini 4 Carbon, in an optimized balance of quality, efficiency, and latency.

> A common industry approach is to use a static "model router" that guesses task difficulty from your first prompt and routes the entire task to the cheapest model that is good enough to complete the task. Unfortunately, these start breaking down as agents become longer running, requiring different levels of complexity at different stages, often discovered as the task evolves.

> Orchestrator takes a dynamic, bidirectional approach between Carbon and Gemini 4 Hydrogen within the evolution of a single trajectory. For example, Carbon can start in a read-only phase to explore dependencies, resolve ambiguities, and build a concrete plan with explicit re-planning triggers. Hydrogen could then take over to write edits, update packages, and run tests. If Hydrogen hits friction, it would hand back to Carbon to inspect the state, repair the plan, and resume execution.

> Explicit multi-model pipelines with the Antigravity SDK: When you want programmatic control over which model handles each role, you can wire Hydrogen and Carbon together directly with the Antigravity SDK.

## Gemini API — What's new (AI Studio)

> Gemini 4 Hydrogen (`gemini-4-hydrogen`) brings cutting-edge intelligence to everyone, with speed and efficiency for everyday coding and agentic workflows. [...] It also adds a fourth thinking level, `xhigh`, alongside `low`, `medium`, and the default `high`.

> - Fast agentic execution: Writes cleaner code, cuts fabricated claims by more than 5x compared to Gemini 3.8 Flash by flagging missing context instead of guessing, batches read and search tool calls in parallel, and better adapts when tool calls fail.
> - Built for multi-model orchestration: Works standalone for coding and agentic work, or pairs with Carbon and Argon to power parallel worker and verifier agents at lower latency without driving up token cost.
> - Default model for Managed Agents: The Antigravity agent now uses Gemini 4 Hydrogen (`gemini-4-hydrogen`) by default.
> - Unified 1M context window and long decode: Input, thinking, and output tokens share one 1,048,576-token window.

## InfoWorld — análisis crítico

> While the planner models explore the codebase, identify dependencies, and develop an implementation plan, Hydrogen handles execution, including editing files, writing code, and running builds and tests [...] That execution differs from conventional model routing, which typically selects a model based on a prompt and assigns it the entire task.

> "CIOs need visibility into which model made a particular decision or code change. Without model-level logs and clear attribution, enterprises could find it difficult to audit AI-generated code, investigate errors, establish accountability when something goes wrong, or understand why a particular model was selected for a task," [Jain] said.

> In addition, Jena pointed out that Antigravity's documentation does not currently describe per-step logs identifying which model performed each action. [...] "Enterprises, therefore, should give coding agents dedicated identities, restrict credentials to the specific tasks they perform, and require human approval before code changes are merged," he added.

> Currently, the hyperscaler offers Orchestrator with Carbon as the planner model to Google AI Ultra subscribers, while Orchestrator with Argon as the planner is available to both Google AI Pro and Ultra subscribers.
