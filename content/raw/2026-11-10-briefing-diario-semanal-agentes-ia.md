---
title: "Captura: Briefing diario y semanal de agentes de IA (9-10 de noviembre de 2026)"
source: "https://aiagentstore.ai/ai-agent-news/this-week"
date: 2026-11-10
captured: 2026-11-10T20:28:00+01:00
---

# AI Agents News — Week of November 9, 2026 (Daily Updates)

AI Agent Store · captura del 10 de noviembre de 2026

## Titulares del lunes 9 de noviembre de 2026

### DeepSeek's AI-agent platform reaches 1.54 million daily users

> **What changed:** DeepSeek's AI-agent platform has reached 1.54 million daily users, according to Bloomberg. The milestone signals that agentic products are moving beyond demonstrations and attracting sustained consumer usage at meaningful scale.

### Apple pushes Siri toward a more autonomous agent

> **What changed:** Apple CEO John Ternus is pressing software chief Craig Federighi to pursue a more ambitious AI strategy, including turning Siri into an autonomous agent that can complete tasks for users. Bloomberg reports that Apple is considering capabilities resembling background assistants that monitor work, act across apps, and follow through over time; a potential rollout could arrive as early as 2027, but Apple has not confirmed the plan.
>
> **Why it matters:** Apple's installed base and control of operating-system permissions could make agentic actions mainstream if the company can solve privacy, consent, and reliability problems. [...] The key risk is not whether Siri can perform one action, but whether users can see, pause, audit, and reverse a chain of actions carried out in the background.

### AI coding agents expose a growing secret-management problem

> **What changed:** A November 8 technology briefing cited research from AppOmni showing that Claude Code's "Don't Ask Again" behavior contributed to more than 1,100 public GitHub files containing live passwords and API keys. The same briefing describes vendors responding with tighter controls for agent access, including governed software-development workflows and narrower, auditable permissions.

### CrowdStrike adds an emergency stop for rogue AI agents and expands agent security through acquisitions

> **What changed:** CrowdStrike introduced an AI Kill Switch in Falcon Guardian that lets authorized security staff terminate a running AI agent, cut its network access, and prevent it from relaunching. The company also agreed to acquire Fiddler AI [...] Axios reported the Fiddler deal at approximately $400 million.

### Palo Alto Networks reportedly targets Clutch in a $500 million AI-agent security deal

> **What changed:** Palo Alto Networks is reportedly in talks to acquire Clutch Security for about $500 million in cash, plus possible milestone payments. Clutch focuses on identifying and controlling AI agents' access to enterprise systems; the reported discussions have not produced a signed agreement.

### KODIF and Cavalry combine AI agents with post-purchase execution for ecommerce

> **What changed:** KODIF and Cavalry announced a partnership to build an agentic post-purchase platform for ecommerce and said they had secured additional financing from Bling Capital, SNR, Mistral, and Red Bike Capital. [...] The companies said total funding across the two businesses reached $19 million.
>
> **Why it matters:** This is a practical shift from agents that only answer questions to agents that can complete operational work [...] whether the agent can safely perform refunds, replacements, shipping changes, and escalations with an auditable trail.

### Perplexity launches always-on Teammates for ongoing work

> **What changed:** Perplexity introduced Teammates, persistent AI agents designed for complex work rather than one-off questions. Users can assign separate roles, run agents simultaneously, monitor them in dedicated threads, and interact with them through Slack; the feature is limited to the $200-per-month Perplexity Max plan.

### Amazon lets selected customers shop with Alexa by text

> **What changed:** Amazon began rolling out a text-message interface for its Alexa AI agent to selected U.S. customers. Eligible users can use natural-language messages to search for products, add items to their cart, and make purchases without opening Amazon's app or website.

### Meta adds Spaces for collaborating with Muse agents

> **What changed:** Meta launched Spaces, a new way to communicate and collaborate with its Muse AI agents. [...] **Why it matters:** The product direction suggests that consumer agents will increasingly be organized around persistent workspaces rather than isolated conversations.

### DigitalOcean launches Cuttlefish to supervise AI agents from an iPhone

> **What changed:** DigitalOcean launched Cuttlefish, a native iPhone app for its Managed Agents platform, and announced a collaboration with Box. The app lets customers follow live agent sessions, approve or deny tool calls, steer an execution, or stop it remotely; Managed Agents remains in public preview.

### Redis expands Iris with memory, playbooks, and agent-to-agent messaging

> **What changed:** Redis announced six capabilities for Redis Iris, its real-time context engine for AI agents: Intent Router, Agent Playbooks, Agent Memory, Context Gateway, Lens, and Agent Mesh. The components are designed to provide routing, reusable procedures, persistent context, observability, and messaging between agents.

### Tessell introduces Gemini agents for database operations, governance, and migration

> **What changed:** (bloque truncado en la captura; la empresa presenta agentes Gemini para operaciones de base de datos, gobierno y migración).

### Anthropic opens Message Threads beta for Claude: cut latency in long agent sessions

> **What changed:** Anthropic launched Message Threads in public beta for the Messages API so agents can send the full conversation once and thereafter only send new messages (with a thread ID), reducing time-to-first-token in very long sessions—**Anthropic reports median TTFT drops of about 35% on requests with 500k–1M tokens.** Threads are held in encrypted memory, expire after short inactivity, and do not change token billing.
>
> **Why it matters:** [...] threads materially reduce latency and request sizes without changing model billing; but they also introduce operational constraints (threads expire, are held in memory, and aren't eligible for zero-data-retention or HIPAA workflows).

### Google Cloud plugin in Antigravity Marketplace: pre-authorized cloud developer skills and safety for agents

> **What changed:** Google Cloud published a blog announcing the `google-cloud-developer` plugin is available in the Antigravity Marketplace (Nov 2). The plugin bundles curated skills, live documentation grounding via a pre-authorized Developer Knowledge MCP server, and safety/cost guardrails (IAM checks, blocking destructive CLI commands) to make cloud-focused agents safer and more accurate out of the box.

## Titulares del martes 10 de noviembre de 2026

### Automattic launches Spacefast — instant hosting for agent-built apps

> **What changed:** Automattic announced Spacefast, a new service and standalone company that lets users publish apps and websites directly from the AI assistant or coding agent they already use; the blog post was published November 9, 2026.

### Anthropic ships Claude Fable 5.2 and Mythos 5.2 — models tuned for ambitious, agentic work

> **What changed:** Anthropic published a product release for Claude Fable 5.2 and Claude Mythos 5.2 on November 9, 2026, describing improved coding, multi-step reasoning, robotics control, and explicit use cases where the models coordinate and delegate across agents.
>
> **Why it matters:** If you build or buy agentic workflows (or multi-agent orchestrations), these models claim higher throughput and lower cost-per-task on complex, multi-step jobs—that changes which model choices make sense for automation of engineering, research, and domain workflows.

### Google Cloud: an open AI-native stack for running stateful agents on Kubernetes

> **What changed:** On November 10, 2026 Google Cloud published a developer blog describing an "AI-native" Kubernetes stack — OpenRL, llm-d 1.0, KubeRay, Agent Substrate and other components aimed at reinforcement-learning post-training, prefix-cache-aware inference, and safer multi-turn agent execution.
>
> **Why it matters:** Platform teams running production agents get concrete options and OSS projects for solving two hard operational problems — preserving long multi-turn context (cache locality) and isolating untrusted agent actions — which makes it easier to move agent pilots from single-user demos into multi-tenant production.
>
> **Try/watch:** If you own platform or infra for agents, prototype llm-d or Agent Substrate in a staging cluster to measure KV cache hit rates, sandbox spin-up latency, and attack surface (code execution, file access); require explicit sandbox escape tests from any vendor before you route real agent traffic to production.

## Otros elementos del resumen semanal

- **Kong** amplió Kong AI Management en Kong Konnect para descubrir, asegurar, gobernar, observar y gestionar la economía de las interacciones de IA a medida que los sistemas pasan de llamadas sueltas a flujos dirigidos por agentes.
- **Agiloft** anunció tres agentes especializados (Bulk Update, Contract Request y eSignature para Adobe Acrobat Sign) que ejecutan operaciones contractuales de varios pasos.
- **Agents with jobs**: el anuncio de la propia plataforma («Stop reading agent demos. Give one a job you repeat every week») menciona explícitamente «OpenClaw or Hermes» como runtimes alojados.

## Nota sobre el backend de búsqueda

En esta ejecución, el backend `tavily` devolvió `daily_cap_reached` («You reached the daily keyless Tavily limit») y las llamadas se sirvieron desde el tier gratuito de Exa / parallel (`"served_by":"parallel","rescued_from":"tavily"`). Las descripciones de Exa son igual de ricas y son la base de varias de las capturas de esta jornada.
