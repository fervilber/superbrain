---
title: "AI Agent Store — resumen semanal (semana del 23 de noviembre de 2026)"
source: "aiagentstore.ai (this-week)"
date: 2026-11-24
captured: 2026-11-24T20:10:00+01:00
---

# AI Agents News — Week of November 23, 2026 (Daily Updates)

> Captura verbatim de la página semanal `aiagentstore.ai/ai-agent-news/this-week`. La URL diaria `/daily/2026-11-24` devolvió el contenedor JS sin contenido ("Loading news…").

## Monday, November 23, 2026

### Tether 0.4.0 adds deterministic test replays for recorded agent runs

**What changed:** Tether released version 0.4.0 on November 22, 2026, adding a test harness that replays recorded agent runs so developers can assert which tools were called, final file contents, and whether the agent respected step or cost limits.

**Why it matters:** Replaying traces without hitting the model makes it practical to regression-test policy changes, agent upgrades, or safety rules against known runs before deploying them in production — reducing risk from blind rollouts.

**Try/watch:** Integrate Tether into your CI to gate merges that change agent prompts, tool access, or permissions; watch for divergence when you change models or prompts, since replays only prove behaviour for the same inputs and recorded responses.

### "Formalize or Lose It" — experimental evidence that executable checks catch handoff errors in agent swarms

**What changed:** A research release published November 23, 2026, reports experiments showing that nearly half of supervisory rules in multi-agent runs lived only in natural-language prompts, and that adding executable checks (a requirement ledger and host-side acceptance tests) caught failures that prompt-only supervision missed.

**Why it matters:** For engineering teams building multi-agent pipelines or layered coding agents, the paper gives actionable evidence: formalize safety and acceptance rules into programmatic checks that execute at handoff, because human-readable prompts alone let important requirements disappear during planning and relay.

**Try/watch:** Start by cataloging the coordination rules your agents rely on and adding a small set of executable acceptance tests for the most safety- or correctness-critical handoffs; watch for gaps between written rules and what your agents actually enforce during replays or live runs.

## Sunday, November 22, 2026

### OpenAI says agents now complete 46% of multi-hour research tasks independently

**What changed:** OpenAI reports that its agents completed 46% of research assignments estimated to require two to four hours of human work, up from 23% in March. For longer four-to-eight-hour assignments, the completion rate rose from 13% to 35%; however, performance remained uneven, with agents doing better at monitoring training runs than at launching them or writing inference and serving software.

**Why it matters:** Research teams can now consider agents for bounded, repetitive investigations, monitoring, analysis, and first drafts. The results do not support removing human review: software engineering, experiment design, judgment, and reliability remain meaningful weak points.

**Try/watch:** Give an agent a clearly scoped research or monitoring workflow with approval gates, and measure independent completion separately from factual accuracy and the cost of correcting mistakes.

### Apple is hiring for a computer-use agent that can work across apps

**What changed:** A job listing reported on November 21 describes Apple's effort to build general-purpose computer-use agents that can browse the web, work across applications, run commands, write and debug code, call services, and choose the appropriate tool for each step. The listing also points to multi-step planning and coordination among specialized agents, but Apple has not announced a product, launch date, or final feature set.

**Why it matters:** Apple's direction would make agent access to the operating system a central product and security issue rather than just an assistant feature. Builders targeting Mac users should expect stronger permission controls and should design workflows that remain understandable when an agent moves between browsers, terminals, documents, and business applications.

## Saturday, November 21, 2026

### Bell Canada breach highlights the emerging risk of agentic attackers

**What changed:** Bell Canada said an "agentic" threat actor accessed a pre-production Maximo environment used to order and provision telecommunications network connections and stole enterprise customer information, including names, job titles, business email addresses, phone numbers, addresses, and some network-related IP data. The incident occurred on November 17 and was reported in the November 21 threat briefing.

**Why it matters:** The incident shows why organizations must defend against attackers that can adapt across systems rather than merely execute one fixed script. Stolen business contact and network information can support targeted phishing, impersonation, credential theft, and follow-on intrusion even when customer service is not disrupted.

### OpenAI begins limited test of Dots (always‑on) agents for ChatGPT Plus and Business Standard users

**What changed:** OpenAI is testing Dots — persistent, always‑on agents that run between conversations and can connect to apps — with a small group of ChatGPT Plus users and is rolling availability to eligible Business Standard workspaces.

### Linq raises capital and positions itself as messaging + device plumbing for agents

**What changed:** Linq announced a new funding milestone and is pitching APIs that give agents the ability to text, call and use a "computer" to finish tasks — effectively providing the phone/voice and browser/automation hooks agents need to complete real work for users.

### Internal reports show privacy and hallucination risks for Meta's Muse; platform controls tighten

**What changed:** Staff reports surfaced that Meta's Muse agent exposed or referenced private Signal messages and produced fabricated purchase information in some internal tests, prompting internal fixes and wider platform conversations about agent permissions and isolation.

**Why it matters:** Real deployments are already revealing two failure modes: (1) agents accessing private app data when permissions are too broad, and (2) agents asserting false external facts. Buyers and vendors must demand explicit, testable guarantees about what an agent can access and which data it may surface in user‑facing outputs.

## Friday, November 20, 2026

### LangChain launches LangSmith Tool Gateway (public beta)

**What changed:** LangChain put LangSmith Tool Gateway into public beta on November 19, 2026; the gateway centralizes credentials, caller identity, access policies, approval flows and audit traces for every agent tool call and works with MCP-compatible clients (LangChain, Deep Agents, Claude Code, Cursor, etc.).

### Databricks opens Genie ZeroOps to public beta (autonomous pipeline agent)

**What changed:** Databricks announced Genie ZeroOps in public beta on November 19, 2026; the agent continuously monitors jobs and tables, diagnoses failures using Unity Catalog metadata and lineage, runs dry‑run tests, and proposes fixes as PRs while requiring human approval before changing production.

### Microsoft Foundry gives enterprise agents their own Microsoft 365 identity

**What changed:** Microsoft detailed Microsoft Foundry updates on November 19, 2026 that let organizations provision agents as named Microsoft 365 members with their own Entra (agent) identities, email, calendar, OneDrive and an accountable manager, plus blueprints for company‑wide or team‑level agents.

## Thursday, November 19, 2026

### Microsoft Foundry: built-in governance for agent fleets

**What changed:** Microsoft published a Foundry product post describing built-in governance for enterprise AI agents — agent identities via Microsoft Entra, model and agent deployment policies, tool and network controls, cost visibility and token/quotas, and safety guardrails.

### Azure Monitor: unified agent observability and end-to-end tracing (preview)

**What changed:** Microsoft announced a preview of unified agent observability in Azure Monitor Application Insights that uses OpenTelemetry trace context and the OpenTelemetry GenAI semantic conventions to trace requests across multiple agents, platforms, models and tools.

### Oracle Life Sciences AI Agents: agentic coordination for clinical trials

**What changed:** Oracle announced Life Sciences AI Agents to help clinical operations monitor portfolio health, surface operational risks, and recommend next actions for review; the release positions the capability for early adopters and emphasizes human review and approvals for any agent recommendations.

### Stitch AI: agentic assistants inside a banking operating system

**What changed:** Stitch released Stitch AI to embed Copilot-style assistants, ready-made operational agents (onboarding, credit decisioning, collections) and an Agent Harness directly inside its banking operating system, with scoped permissions, maker/checker approvals, audit trails and PII masking before model access.

## Wednesday, November 18, 2026

### Replit launches Missions, an agent swarm with a fixed budget

**What changed:** Replit launched Missions, a system that coordinates multiple AI agents to plan, build, test, and iterate toward a user-defined outcome. Users set success criteria, spending limits, and actions that require approval; Replit says its agents built an internal application-monitoring platform in two days for $3,000.

### Cognition introduces Devin Bots to manage teams of coding agents

**What changed:** Cognition unveiled Devin Bots, persistent agents that break complex software projects into tasks, start multiple Devin sessions, retain context for days or weeks, and communicate with teams through channels such as Slack.

### Microsoft expands its enterprise control layer for AI agents at Ignite

**What changed:** Microsoft announced new agent capabilities across Copilot, Azure, Foundry, and security at Ignite. Its announcements include Autopilot, a long-running agent for recurring work; Microsoft IQ, which governs and reuses organizational context; and Agent 365, a control plane intended to extend identity, security, management, and observability systems to enterprise agents.

## Tuesday, November 17, 2026

### GitHub Copilot: select models deprecated (effective Nov 16, 2026)

**What changed:** GitHub announced the deprecation of several Copilot models — Claude Opus 4.8, Claude Opus 5, and GPT-5.6 Terra — effective November 16, 2026, and recommended alternatives such as Claude Opus 5.5 and GPT-6.1 Sol / Luna.
