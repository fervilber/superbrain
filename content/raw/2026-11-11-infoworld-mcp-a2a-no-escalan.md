---
title: "MCP and A2A alone won't scale AI agents (InfoWorld)"
source: "https://www.infoworld.com/article/4246624/mcp-and-a2a-alone-wont-scale-ai-agents.html"
date: 2026-11-10
captured: 2026-11-11
---

# MCP and A2A alone won't scale AI agents

Por Isaac Sacolick, Contributing Writer. Nov 11, 2026, 9 min.

## Once you understand how to use the two protocols, it's time to tackle identity management, AI context governance, business process re-engineering, and agenticops.

Two protocols define how AI agents connect to internal resources and collaborate with other AI agents. The Model Context Protocol (MCP) is well known because it's promoted as a general protocol for connecting AI agents to resources and other AI agents. But that's not completely accurate. It's really the Agent2Agent protocol (A2A) that's enabling AI agent orchestration.

The confusion stems from how quickly platforms have adopted these protocols and marketed them as features. Users building their own AI agents with Claude, OpenAI, Microsoft Copilot, and other models are already being exposed to customizing skills, connectors, and other plug-ins that use MCP and A2A. Vibe coding and AI app-building tools like Bolt.new, Lovable, Pave, Replit, and v0 can connect to MCP servers and include built-in connectors. AI coding editors like Claude Code, Cursor, Devin Desktop, Gemini CLI, GitHub Copilot, and Kiro have MCP clients.

These protocols will shape how enterprises scale and manage AI agents. Gartner predicts that the average global Fortune 500 enterprise will run more than 150,000 AI agents over the next two years. But according to Collibra's 2026 Hallucination Tax Report, 76% have hit critical roadblocks while attempting to move from pilot to full production during the past 12 months.

## Differences between MCP and A2A

Scott Gerlach, cofounder and chief security officer at StackHawk, ofrece esta analogía: "If you think about doing some bathroom remodeling and you call a plumber to move a sink, he'd use tools in his MCP toolbox to complete his work. But when it's time to fix the drywall, repaint, and put the vanity back together, the plumber agent would use A2A to call other contractor agents to complete that work".

John Pettit, CTO at Promevo: "MCP is the secure USB port for an AI agent, or a universal power adapter for enterprise AI, and it allows an AI model to safely plug into local files, enterprise databases, or SaaS tools without engineering teams having to write and maintain custom API middleware for every connection. A2A is the negotiation protocol, like a general contractor managing a team of specialized subcontractor agents".

## Cuatro capas que faltan por encima de los protocolos

### Managing identity and authorizations

MCP and A2A define how agents present credentials but don't govern them. You're responsible for defining the agent's identities, what resources they can access, and which agents they can converse with.

"Both protocols sit under the Linux Foundation's Agentic AI Foundation, with one giving agents a dial tone to tools, the other a dial tone to each other, but neither saying who is authorized to place the call," says Kevin Paige, CISO at C1.ai. "MCP binds every token to a single-server audience and bars servers from transiting any other. A2A treats peer agents as opaque and halts at `AUTH_REQUIRED`, leaving the client to obtain that credential outside the protocol."

"From an enterprise security perspective, both protocols transform automated workflows into non-human identities (NHIs) that rely on programmatic secrets management to govern their API credentials, keys, and tokens," says Andrew Hartnett, CTO at Bitwarden. "Regardless of protocol, any agent authorized to act within sensitive systems must be managed as a privileged identity under strict least-privileged boundaries backed by human-in-the-loop guardrails for high-risk actions."

### Contexto y gobernanza del dato

Organizations will need to address unstructured data governance policies, especially around confidential data. Policies and implementation should determine which agents, under what circumstances, and for which actions access is granted to resources and at what granularity.
