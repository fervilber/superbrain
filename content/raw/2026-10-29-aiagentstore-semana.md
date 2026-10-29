---
title: "AI Agent Store — Noticias de agentes de IA, semana del 29 de octubre de 2026"
source: "https://aiagentstore.ai/ai-agent-news/this-week"
author: "AI Agent Store (Daily Updates)"
date: 2026-10-29
captured: 2026-10-29
---

# Captura: AI Agents News — Week of October 29, 2026

> Recopilación semanal de AI Agent Store, con entradas fechadas entre el 23 y el 29 de octubre de 2026. Se reproducen los ítems más relevantes para el informe del 29 de octubre.

## Thursday, October 29, 2026

### Copilot cloud sessions and Automations: persistent agent sessions, cross-device continuity, and self-improving automations

**What changed:** GitHub rolled out a connected Copilot cloud experience so cloud agent sessions persist across web, mobile, app, CLI and IDEs starting Oct. 28, 2026. Copilot Automations can now run in the cloud and learn from outcomes, surfacing suggested improvements that teams can approve or reject.

**Why it matters:** Engineers and operators can let agent work continue off-host (useful for long-running refactors or batch tasks) while keeping human checkpoints; teams can convert repetitive workflows into cloud automations that self-improve but still require explicit approvals to change behavior.

**Try/watch:** Enable cloud sessions in a staging project, require human approvals for any automation that modifies production-facing code, and log automation suggestions to measure how often the "self-improvements" reduce manual work versus introducing noisy or risky changes.

## Wednesday, October 28, 2026

### Snowflake adds explicit reasoning controls, extra system instructions, and stage mounts for its Cortex coding agents

**What changed:** Snowflake's documentation shows an Oct. 28, 2026 update to Cortex Agents' coding API that adds three public controls: a `thinking_effort` param to tune orchestration-model reasoning effort, `instructions.system` to append system-level directions, and `stage_mounts` to mount versioned Snowflake stages into the agent's sandboxed runtime.

**Why it matters:** For teams using data-aware coding agents, these controls let operators balance speed vs. depth of reasoning, provide safer system-level constraints without editing the core sandbox, and give agents direct, versioned access to notebooks, apps, or datasets inside the environment they already use — reducing context-mismatch and fragile file-copy flows.

**Try/watch:** Use `thinking_effort` to run the same integration task at two levels (e.g., `medium` vs `high`) and compare correctness, latency, and token usage; mount a read-only stage with test data to validate reproducible agent runs before giving agents write access.

### Akamai launches Akamai Inference and an Agent Sandbox (beta)

**What changed:** Akamai introduced two beta products — Akamai Inference, a managed model-serving service, and Akamai Agent Sandbox, an isolated runtime for executing agent-generated code and workflows — positioning its global edge cloud to host models and run agents with default outbound blocks and isolation controls.

**Why it matters:** If you build or buy agents that must touch sensitive systems or customer data, running models close to your users and data (edge inference) plus an execution sandbox that blocks unsafe outbound actions reduces latency and the blast radius of accidental or malicious agent behavior. That gives smaller teams a practical path to ship agentic features while preserving containment.

**Try/watch:** Evaluate Akamai's sandbox using a red-team checklist: verify outbound restrictions, credential vaulting, and the ability to require human approval for high-risk actions; measure latency and cost for your real workflows against a central-cloud deployment.

### Oracle and Google bring Google TPUs to Oracle Cloud (announced at Oracle AI World)

**What changed:** Oracle and Google announced that Google's Tensor Processing Units (TPUs) will be offered on Oracle Cloud Infrastructure (OCI) starting in 2027, explicitly calling out support for agentic, long-context, and multi-step reasoning workloads.

**Why it matters:** For builders and buyers of enterprise agents this widens the choice of purpose-built AI hardware (an alternative to GPU-only clouds) and can materially change economics for large, low-latency agent deployments or for training larger in-house models used as private agent brains.

## Tuesday, October 27, 2026

### GitHub Agentic Workflows hardens agent platform with six releases

**What changed:** GitHub published a weekly update on Oct 26 describing six releases (v0.93.0–v0.93.5) that tightened static analysis, added safer handling for network/credential usage in integration jobs, improved failure diagnostics, and made Pi CLI 1.4.0 the default.

**Why it matters:** If you run CI/CD or automated issue workflows that rely on GitHub's agent tooling, these fixes reduce surprise failures and the risk that an agent exposes or misuses credentials.

### Bubble debuts Agent 2 and MCP beta in founder AMA — editor preview and import flows

**What changed:** In an Oct 26 AMA, Bubble showed Agent 2 (a rebuilt Bubble AI Agent), a Bubble MCP (beta) integration that runs inside Claude and ChatGPT, in-editor previews with the Agent pinned, and an import path for apps built by other AI tools; the Agent now also checks its own work using an issue checker and screenshots.

**Why it matters:** For non-engineering founders and ops teams, this lowers the barrier to iterate on app ideas created by coding agents; the MCP connector means you can use your preferred chat/code model to drive edits directly in Bubble.

### Agent Tree: terminal-first observability for Claude Code agents

**What changed:** An open-source tool called Agent Tree launched (announced Oct 27) as a terminal-based live monitor for Claude Code agent workflows, showing task trees, decision branches, and live updates.

**Why it matters:** Observability is the practical blocker for deploying coding agents safely. A terminal monitor lets engineers spot bad decisions, runaway API calls, or expensive loops early.

## Monday, October 26, 2026

### SK Telecom treats AI agents as a managed workforce

**What changed:** SK Telecom published its first AI Governance Report and said it is considering AI agents as a new form of labor, including potentially linking agent performance to organizational KPIs. The carrier assigns agents employee ID numbers, records each agent's role and supervisor, and monitors operating status, token use, and work history. Agents with greater autonomy or business impact must have a senior human supervisor. Agents can be suspended or retired when performance reviews show they are no longer needed.

### Dell expands its AI Factory for on-premises agent workloads

**What changed:** Dell announced an expanded AI Factory with NVIDIA at NVIDIA GTC Berlin, including new rack-scale systems, an air-cooled two-socket server, a workstation with NVIDIA's GB10 platform, and validated software and deployment templates for agentic workloads. Dell said more than 6,500 enterprises are using the platform.

### NVIDIA signals a recurring software charge for agent infrastructure

**What changed:** NVIDIA CEO Jensen Huang discussed a possible annual software license of about $2,000 per GPU for software used to run AI agents. NVIDIA has not said which products would be covered or when the fee would begin, so this is a pricing signal rather than a confirmed commercial launch.

**Why it matters:** Infrastructure budgets for agentic AI may include a substantial software charge tied to GPU capacity, not just model API usage or hardware depreciation.

## Saturday, October 25, 2026

### Four major agent projects move under vendor-neutral governance

**What changed:** The Agentic AI Foundation added Agent Skills from Anthropic, Open Responses from OpenAI, OpenEnv from Hugging Face, and OpenSandbox from Alibaba. The projects cover reusable agent instructions, a common model interface, training and evaluation environments, and isolated execution; the foundation now hosts 10 projects.

### Daytona raises $60 million at a $1 billion valuation for long-running agents

**What changed:** Daytona Platforms announced a $60 million Series B led by FirstMark Growth at a $1 billion valuation, bringing total funding to $91 million. The company is building cloud infrastructure for agents that create many short-lived, stateful jobs, with sandboxed Linux, Windows, and macOS environments plus GPU access.

### Google Cloud expands perimeter controls for autonomous agents

**What changed:** Google Cloud announced generally available improvements to VPC Service Controls, including folder-based perimeter membership, more granular exceptions, and guided troubleshooting for access denials. Google positioned the changes as a way to scale autonomous agents while keeping data inside enterprise security boundaries, with no additional charge.

### Cisco introduces a benchmark for multi-step cybersecurity agents

**What changed:** Cisco introduced Agentic FAITH, an extension of its FAITH evaluation framework for tasks in which an agent chooses tools, interprets results, and acts through multiple steps. Its first integrated benchmark, VulnLoc, tests whether agents can locate vulnerable files in a code repository while avoiding false positives on patched code.

## Friday, October 23, 2026

### TanStack AI reaches 1.0 with stable agent toolkit

**What changed:** TanStack published a 1.0 release of its TanStack AI stack, stabilizing 76 packages and formally supporting agents, subagents, coding-agent workflows, sandboxes, provider adapters, and an experimental harness for running agents in multiple environments. The post lists portable agent skills, subagents, computer-use tooling, MCP server support, and 23 provider adapters.

### F5 and Google Cloud describe integration patterns to secure agent fleets

**What changed:** F5 published a technical blog describing how Google Cloud's Agent Gateway can pair with F5 AI Guardrails to centralize routing, policy enforcement, and prompt/API inspection for fleets of agents at enterprise scale. Agent Gateway handles traffic control while F5 inspects prompts and agent tool calls to block sensitive data and malicious intent in real time.

### Material Security launches a Google Drive Security "agent" for workspace risk remediation

**What changed:** Material Security announced a Google Drive Security Agent that inspects Drive content and sharing patterns, synthesizes findings, and can remediate over-permissioned files automatically — aimed at risks introduced when third-party AI tools get OAuth access to workspaces.

## Notas del capturador

- **Ejecución persistente y sandboxing como patrón de la semana**: Copilot cloud sandboxes (GitHub), Akamai Agent Sandbox (borde), Daytona (infra de jobs de vida corta), Dell AI Factory (on-prem). La pregunta se desplaza de "¿puedo construir un agente?" a "¿dónde se ejecuta y cómo contengo su acceso?".
- **Cómputo especializado para agentes**: TPUs de Google en Oracle Cloud (2027) y licencia de software por GPU de NVIDIA (~$2.000/GPU/año) — el coste por acción del agente deja de ser solo tokens.
- **Gobernanza agéntica madura**: SK Telecom trata agentes como plantilla (ID de empleado, supervisor, retiro), la AAIF absorbe cuatro proyectos más (10 en total), Cisco introduce Agentic FAITH/VulnLoc (evaluación de trayectoria, no solo resultado).
- **Observabilidad**: Agent Tree (monitor de terminal para agentes de Claude Code) ataca el cuello de botella real de desplegar agentes de codificación.
- **F5 + Google Agent Gateway**: inspección de prompts y tool calls en tiempo real para flotas de agentes — la capa de política centralizada.
