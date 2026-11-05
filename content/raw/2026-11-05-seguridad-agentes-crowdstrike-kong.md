---
title: "Seguridad y gobierno de agentes: CrowdStrike (Kill Switch) y Kong AI Management"
source: "https://aiagentstore.ai/ai-agent-news/2026-november"
date: 2026-11-05
captured: 2026-11-05
---

# Daily AI Agent News - November 2026

AI Agent Store, 5 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract`.

### CrowdStrike adds detection and shutdown controls for enterprise AI agents

What changed: CrowdStrike introduced Agent Insider Threat Detection to identify abnormal behavior by AI agents, even when the activity does not violate an explicit rule. It also announced Agentic Adversary Emulation, which uses purpose-built security models to simulate how an autonomous attacker could chain weaknesses into an attack path, and a Falcon Guardian AI Kill Switch that can terminate a suspicious agent.

Why it matters: As agents gain access to business systems, traditional policy checks may miss harmful behavior that is individually permitted but unusual in context. Security teams can now treat agents as monitored identities and test whether their defenses can stop an automated attack before it reaches sensitive assets.

Try/watch: Inventory every production agent, its operator, tools, credentials, and accessible data; then define who can invoke an emergency shutdown and how the decision will be recorded.

### Kong expands its platform for governing agent-driven systems

What changed: Kong announced an expansion of Kong AI Management in Kong Konnect to help enterprises discover, secure, govern, observe, and manage the economics of AI interactions as systems move from individual model calls to agent-driven workflows.

Why it matters: The operational challenge is no longer only choosing a model; it is controlling which agents can call which tools, tracking usage and cost, and understanding multi-step interactions. A centralized management layer can give platform teams a common place to enforce controls as more agents are deployed across applications.

Try/watch: Require each agent workflow to have an owner, budget, allowed tools, logging requirements, and an approval threshold before it reaches production.

### Honeycomb ships Personal and Team AI SRE agents (early access)

What changed: Honeycomb announced Personal and Team Agents that run goal-oriented investigations against high-cardinality telemetry, remember findings across runs, and can act only within team-set limits; the product went into early access on November 3, 2026.

Why it matters: Honeycomb's agents are explicitly built to use production traces and observability queries as their data source, so they're designed to catch regressions and instrumentation gaps earlier (before alerts hit customers) — a useful pattern if you want agents that surface reproducible evidence rather than speculative fixes.
