---
title: "MCP como superficie de integración empresarial: Narmi+Copilot, Interact MCP, Bubble MCP beta y Functionize para agentes de código"
source: "https://agentic.ai/news y https://aiagentstore.ai/ai-agent-news/this-week"
author: "Agentic.ai (Agentic News) y AI Agent Store (weekly digest)"
date: 2026-10-26
captured: 2026-10-27
---

# Captura: conectores MCP y plataforma agéntica empresarial (semana del 26 de octubre de 2026)

> Captura por extractos verbatim de dos digests técnicos (Agentic.ai y AI Agent Store) correspondientes a los anuncios del 23 al 26 de octubre de 2026.

## Narmi: MCP hacia Microsoft 365 Copilot en banca (26 de octubre de 2026)

Narmi announced on Oct. 26 that its Model Context Protocol capabilities now connect to Microsoft 365 Copilot, giving it secure access to customer financial data in banking workflows. The integration is aimed at banks and credit unions handling relationship management, lending and daily operations. For those tracking agentic AI products, it shows how connectors can bring assistants into sensitive, practical work without moving users to a separate tool. The announcement's emphasis on secure access makes the exact permissions and safeguards worth examining.

Fuente original: [Yahoo! Finance](https://finance.yahoo.com/technology/ai/articles/narmi-launches-microsoft-365-copilot-130000636.html).

## Interact Software: Interact MCP, 700 capacidades de intranet (26 de octubre de 2026)

Interact Software announced Interact MCP on Oct. 26, 2026, connecting enterprise AI systems to 700 capabilities across 26 intranet areas. Built on Cue and Conductor, the tool links assistants to workplace knowledge and actions. For those tracking AI personal assistants, this points to enterprise tools gaining access to systems where they can act on users' behalf. The announcement does not specify which actions assistants can perform through the 700 capabilities.

Fuente original: [The Manila Times / GlobeNewswire](https://www.manilatimes.net/2026/10/26/tmt-newswire/globenewswire/interact-brings-700-intranet-capabilities-to-enterprise-ai-assistants-with-interact-mcp/2453976).

## Bubble: Agent 2 y MCP beta (AMA de fundadores, 26 de octubre de 2026)

**What changed:** In an Oct 26 AMA, Bubble showed Agent 2 (a rebuilt Bubble AI Agent), a Bubble MCP (beta) integration that runs inside Claude and ChatGPT, in-editor previews with the Agent pinned, and an import path for apps built by other AI tools; the Agent now also checks its own work using an issue checker and screenshots.

**Why it matters:** For non-engineering founders and ops teams, this lowers the barrier to iterate on app ideas created by coding agents: you can import an AI-generated app, preview and adjust it inside the visual editor, and have the Agent self-audit changes so QA overhead falls. The MCP connector also means you can use your preferred chat/code model to drive edits directly in Bubble.

**Try/watch:** Try the in-editor preview and the import flow with a small prototype; validate the Agent's self-checks by forcing a known error and seeing whether the issue checker catches it. Monitor workload usage closely — Bubble flagged potential cost growth as apps scale.

## Functionize: servidor MCP para agentes de código (23 de octubre de 2026)

Functionize released an MCP server connecting its testing platform with coding agents such as Claude Code, Cursor and GitHub Copilot. Developers and testers can request smoke or regression tests in plain language and receive results in the chat interface. For those tracking agentic AI products, the release gives coding agents a way to run checks against live applications. The specific compatible clients determine which teams can use the workflow today.

Fuente original: [SecurityBrief Asia](https://securitybrief.asia/story/functionize-launches-mcp-server-for-ai-coding-agents).

## Material Security: agente de seguridad para Google Drive (23 de octubre de 2026)

**What changed:** Material Security announced a Google Drive Security Agent that inspects Drive content and sharing patterns, synthesizes findings, and can remediate over-permissioned files automatically — aimed at risks introduced when third-party AI tools get OAuth access to workspaces. The release cites an internal study about widespread exposure when agents or tools are granted access and positions the product as an automated remediation layer for that risk surface.

**Why it matters:** For buyers and security teams, this is a concrete example of agent-aware tooling: instead of treating agents as invisible users, security tooling now treats agent access and behavior as first-class telemetry and can automate remediation where manual triage doesn't scale.

## F5 + Google Cloud: patrones para asegurar flotas de agentes (23 de octubre de 2026)

**What changed:** F5 published a technical blog describing how Google Cloud's Agent Gateway can pair with F5 AI Guardrails to centralize routing, policy enforcement, and prompt/API inspection for fleets of agents at enterprise scale. The post explains an architecture where Agent Gateway handles traffic control while F5 inspects prompts and agent tool calls to block sensitive data and malicious intent in real time.

**Why it matters:** Enterprises moving from single agents to hundreds or thousands of agent deployments need centralized controls to avoid policy drift, accidental data leaks, and inconsistent access rules; this integration shows a practical path to inherit security and auditability without rewriting each agent.

## TanStack AI 1.0 (23 de octubre de 2026)

**What changed:** TanStack published a 1.0 release of its TanStack AI stack, stabilizing 76 packages and formally supporting agents, subagents, coding-agent workflows, sandboxes, provider adapters, and an experimental harness for running agents in multiple environments. The post lists concrete additions (portable agent skills, subagents, computer-use tooling, MCP server support, and 23 provider adapters) and upgrade steps for existing 0.x users.

**Why it matters:** Builders who need a portable, framework-agnostic agent runtime can now rely on a stable open-source API to run chat UIs, tool-calling agents, and coding agents across providers and sandboxes — reducing lock-in and integration work when swapping model providers or embedding agents in web apps and editors.
