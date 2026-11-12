---
title: "MCP and A2A alone won't scale AI agents"
source: "https://www.infoworld.com/article/4246624/mcp-and-a2a-alone-wont-scale-ai-agents.html"
date: 2026-11-11
captured: 2026-11-12
---

# MCP and A2A alone won't scale AI agents

InfoWorld, análisis de Isaac Sacolick, publicado el 10-11 de noviembre de 2026 (9 min de lectura). Captura en bruto.

## Extractos verbatim

> Once you understand how to use the two protocols, it's time to tackle identity management, AI context governance, business process re-engineering, and agenticops.

> Two protocols define how AI agents connect to internal resources and collaborate with other AI agents. The Model Context Protocol (MCP) is well known because it's promoted as a general protocol for connecting AI agents to resources and other AI agents. But that's not completely accurate. It's really the Agent2Agent protocol (A2A) that's enabling AI agent orchestration.

> The confusion stems from how quickly platforms have adopted these protocols and marketed them as features. Users building their own AI agents with Claude, OpenAI, Microsoft Copilot, and other models are already being exposed to customizing skills, connectors, and other plug-ins that use MCP and A2A. Vibe coding and AI app-building tools like Bolt.new, Lovable, Pave, Replit, and v0 can connect to MCP servers and include built-in connectors. AI coding editors like Claude Code, Cursor, Devin Desktop, Gemini CLI, GitHub Copilot, and Kiro have MCP clients.

> These protocols will shape how enterprises scale and manage AI agents. Gartner predicts that the average global Fortune 500 enterprise will run more than 150,000 AI agents over the next two years. But according to Collibra's 2026 Hallucination Tax Report, 76% have hit critical roadblocks while attempting to move from pilot to full production during the past 12 months.

> Reviewing the two protocols and which services are your responsibility to layer on top of them is key to scaling enterprise-ready AI agents.

### Diferencias entre MCP y A2A

> Scott Gerlach, cofounder and chief security officer at StackHawk, offers this analogy to help technologists better understand MCP and A2A's functions. "If you think about doing some bathroom remodeling and you call a plumber to move a sink, he'd use tools in his MCP toolbox to complete his work. But when it's time to fix the drywall, repaint, and put the vanity back together, the plumber agent would use A2A to call other contractor agents to complete that work," Gerlach says.

> Another approach [...] comes from John Pettit, CTO at Promevo [...] "MCP is the secure USB port for an AI agent, or a universal power adapter for enterprise AI, and it allows an AI model to safely plug into local files, enterprise databases, or SaaS tools without engineering teams having to write and maintain custom API middleware for every connection. A2A is the negotiation protocol, like a general contractor managing a team of specialized subcontractor agents," Pettit says.

> Arpita Soni, a senior member of IEEE, says that MCP and A2A solve two different layers of the agentic stack. "MCP is the vertical connection and standardizes how a single agent accesses external tools, data sources, and APIs, replacing the old pattern of writing a custom integration for every tool an agent needs. A2A is the horizontal connection, and it standardizes how independently built agents discover each other, negotiate capabilities, and hand off tasks, regardless of which framework or vendor built them. MCP gives each agent its own hands and eyes (tools and context or capabilities), while A2A gives separate agents a shared language to talk to one another and delegate work," Soni says.

> MCP and A2A are protocols, but scaling AI agents requires layers of capabilities developed on top of them. Here are four at the top of the list: identity and authorization, connecting AI agents to the business's context layer, business process re-engineering, and developing agenticops capabilities.

> "Both protocols sit under the Linux Foundation's Agentic AI Foundation, with one giving agents a dial tone to tools, the other a dial tone to each other, but neither saying who is authorized to place the call," says Kevin Paige, CISO at C1.ai. "MCP binds every token to a single-server audience and bars servers from transiting any other. A2A treats peer agents as opaque and halts at `AUTH_REQUIRED`, leaving the client to obtain that credential outside the protocol."

## Notas de captura

- Extraído con `web_extract` el 2026-11-12; el extracto anterior cubre el cuerpo principal disponible (la sección sobre las cuatro capas adicionales —identidad y autorización, capa de contexto del negocio, reingeniería de procesos y agenticops— se anuncia en los titulares y se desarrolla a lo largo del artículo).
- Datos: Gartner >150.000 agentes por empresa Fortune 500 en dos años; 76% de organizaciones con bloqueos críticos del piloto a producción (Collibra, Hallucination Tax Report 2026).
