---
title: "Protocolos de interoperabilidad de agentes: MCP, A2A y OSI explicados (2026)"
source: "https://atlan.com/know/agent-interoperability-protocols"
date: 2026-11-02
captured: 2026-11-02
---

# Agent Interoperability Protocols: MCP, A2A, OSI Explained [2026]

Emily Winks — Atlan. Captura verbatim de los tramos sustantivos.

## Key takeaways

- MCP, A2A, and OSI solve different interoperability layers: tool access, agent delegation, and shared business meaning.
- Protocol compliance alone does not prevent semantic conflict: compliant agents can still disagree on shared definitions.
- A governed context layer, not just protocols, is what makes multi-agent systems reliable in production.

## What are agent interoperability protocols?

Agent interoperability protocols are open standards that let AI agents built on different frameworks discover each other, exchange tasks, and share data without custom point-to-point integrations. The three key protocols operate at distinct stack layers: MCP standardizes how agents access tools and data, A2A standardizes how agents delegate tasks to other agents, and OSI standardizes how agents share business definitions and meaning across platforms.

### Key protocols

- MCP — Model Context Protocol (Anthropic): standardizes agent-to-tool access
- A2A — Agent-to-Agent Protocol (Google): standardizes agent-to-agent task delegation
- OSI, now Apache Ossie: standardizes shared meaning and semantic definitions

## Why agent interoperability matters

Enterprise AI teams are no longer building single agents. They are building systems of agents: specialized models that handle SQL generation, data quality monitoring, workflow orchestration, business reporting, and anomaly detection, each running in parallel or in sequence.

The problem: these agents are built on different frameworks, by different teams, using different vendors. An analytics agent built on LangChain needs to hand data to a governance agent built on LlamaIndex. A workflow orchestrator running on Microsoft Copilot Studio needs to delegate a subtask to an on-premise agent running on a private LLM. Without shared protocols, every one of these connections requires custom integration code.

The result is brittle, expensive, and slow. The Berkeley MAST study, "Why Do Multi-Agent LLM Systems Fail?", annotated more than 1,600 execution traces across seven open-source frameworks and found multi-agent LLM systems failing at rates between 41% and 86.7%. Specification and design issues accounted for 41.8% of failures and inter-agent misalignment for 36.9%, so roughly four in five trace back to how the system was specified and coordinated rather than to the underlying models.

Gartner projects that 40% of enterprise applications will feature task-specific AI agents by 2026, up from less than 5% in 2025. As agent counts multiply, the integration surface area grows faster than any team can hand-code it.

## The protocol stack: three layers explained

Agent interoperability is not a single problem. It is three distinct problems that require three distinct solutions, each operating at a different layer of the stack.

## MCP deep dive: how it works and what it solves

Before MCP, every AI agent needed a custom integration for every external tool or data source it used. An analytics agent connecting to Snowflake, Salesforce, a REST API, and an internal knowledge base required four separate connectors, each written differently, maintained separately, and breaking whenever the underlying tool changed. The integration surface area grew quadratically as agents and tools multiplied.

MCP, introduced by Anthropic in November 2024, is an open standard built on JSON-RPC 2.0. It creates a three-component architecture:

- MCP Host: the AI application the user interacts with (Claude, Cursor, a custom enterprise app)
- MCP Client: the translation layer inside the host that speaks MCP to servers
- MCP Server: the external system that exposes capabilities to agents (a database, a REST API, a catalog, a code repository)

MCP defines three core primitives: Tools (actions an agent can invoke), Resources (data an agent can read), and Prompts (templated instructions an agent can execute). Any tool that publishes an MCP Server can immediately be accessed by any MCP-compatible agent, with no custom integration required.

### MCP adoption today

Anthropic donated MCP to the Linux Foundation's Agentic AI Foundation on 9 December 2025. Anthropic, Block and OpenAI co-founded the AAIF, with Google, Microsoft, AWS, Cloudflare and Bloomberg backing it. MCP reported over 97 million monthly SDK downloads at that December announcement, and by July 2026 "close to half-a-billion downloads a month, with both TypeScript and Python SDKs crossing the 1 billion total downloads threshold." Client support now spans ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot and Visual Studio Code.

## A2A deep dive: how it works and what it solves

MCP solved how agents access tools. It left open a different problem: how does one agent hand a task to another agent? In a multi-agent system, an orchestrator agent might need to delegate a data validation task to a specialist agent, get a result, then pass it forward to a reporting agent. Without a standard, this delegation is custom code that is fragile, framework-specific, and hard to scale.

Google released the Agent-to-Agent (A2A) protocol in April 2025, built on HTTP, Server-Sent Events (SSE), and JSON-RPC, all standards already embedded in enterprise IT stacks. A2A enables four capabilities:

1. Capability discovery: agents advertise what they can do via "Agent Cards," JSON files published at a well-known URL. An Agent Card includes the agent's name, description, service endpoint, supported modalities, and authentication requirements. Think of it as a machine-readable resume an agent publishes so other agents can find it.
2. Task management: A2A defines a standard task lifecycle (submitted, working, input-required, completed, failed, canceled), so client agents can track task state across the full execution cycle.
3. Agent-to-agent collaboration: a client agent identifies the right remote agent via its Agent Card, delegates a task using A2A, and receives results regardless of what framework each agent is built on.
4. UX negotiation: agents communicate what response formats and modalities they support, adapting to different consumption contexts.

Google created A2A in April 2025 and moved it to the Linux Foundation as the Agent2Agent Protocol Project that June, with what the Foundation described as "growing support from more than 100 leading technology companies," AWS, Cisco, Microsoft, Salesforce, SAP and ServiceNow among them. A2A is a separate Linux Foundation project from the AAIF that MCP later joined.

### MCP and A2A together

MCP and A2A solve adjacent, non-overlapping problems. MCP is how an agent connects to a tool (Layer 1). A2A is how an agent delegates to another agent (Layer 2). In practice:

- A workflow orchestrator agent uses A2A to delegate a data validation task to a specialist agent
- The specialist agent uses MCP to pull data from Snowflake, check quality rules, and return results
- Results flow back through A2A to the orchestrator

## Governance gap

Protocols have no memory. MCP and A2A are stateless communication standards. They do not track what an agent did, what data it accessed, or how its outputs were used. Enterprise AI governance requires audit trails, policy enforcement, and lineage. None of these are native to any current protocol. This is measurable, not hypothetical: independent 2026 scans found more than 12,000 MCP servers exposed to the public internet, roughly 40% running with no authentication at all.
