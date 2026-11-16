---
title: "Google Open Source Blog: Scaling AI agents with open standards — MCP and Agent Skills joining the AAIF"
source: "https://opensource.googleblog.com/2026/11/scaling-ai-agents-open-standards-mcp-aaif.html"
date: 2026-11-16
captured: 2026-11-16
---

# Scaling AI agents with open standards: Kurtis Van Gent on MCP and Agent Skills joining the AAIF (11 de noviembre de 2026)

Autores: Kurtis Van Gent (Google Cloud) y Daryl Ducharme (Google Open Source Programs Office). Entrevista. Capturado el 2026-11-16.

## Extractos verbatim

> Building production AI agents requires more than a capable reasoning model. Agents need a reliable way to connect to external systems and data, and they need procedural domain knowledge so they know how to use those tools safely without exhausting their context window.

> Over the past year, open source communities have rallied around two complementary open standards to solve these challenges: the Model Context Protocol (MCP) for connecting agents to live tools, and Agent Skills for loading procedural instructions and scripts on demand. Following Anthropic's donation of the Agent Skills specification to the Linux Foundation's Agentic AI Foundation (AAIF) alongside MCP, engineers from Google, Anthropic, OpenAI, and the wider ecosystem are now co-maintaining the standard under vendor-neutral governance.

> When I started my current role around three years ago, it was early in the generative AI cycle. My mission was to make it easy for developers to use cloud databases for their AI applications. As model reasoning improved, context and data were clearly the keys to making effective use of it, and there's no better place to store data than a database. At the time, most database conversations focused on retrieval-augmented generation (RAG) using vector search. However, our team believed that agents and tools held the most interesting potential for large language models (LLMs) going forward. We immediately hit two scaling challenges: Google Cloud supports more than 15 different databases across its portfolio, and new open source agent frameworks (starting with LangChain and LlamaIndex) were emerging every week. That created a classic N-by-M integration problem between many clients and many data hosts. To solve it, we started GenAI Toolbox for Databases (now MCP Toolbox for Databases) as an open source framework for building and serving tools. We built our own server, clients, and protocol to standardize how agents look up and invoke database tools.

> As MCP adoption accelerated across the industry, however, it became clear that early stateful assumptions around persistent sessions and initialization were holding MCP back at production scale. That effort culminated in a two-day Transports Summit where Google and fellow working group members hosted the MCP core maintainers at our San Francisco offices to work through the scaling bottlenecks and align on a path forward. Shortly afterward, I was invited to become an MCP core maintainer, both in recognition of our work identifying those transport challenges and to keep the Transports Working Group closely aligned with the core specification. The result of that collaboration was the July 28, 2026 MCP specification, which transitioned MCP to a stateless model.

> As agents grew more capable and connected to dozens of MCP servers, [context exhaustion became the next bottleneck]. Agent Skills introduced a remarkably simple, effective pattern for solving that problem through progressive disclosure. By loading only a lightweight YAML frontmatter name and description at startup, and pulling the full `SKILL.md` instructions, reference files, or scripts into context only when a task requires them, Agent Skills commoditized context the same way MCP commoditized tools. While some observers initially viewed MCP and Agent Skills as competing approaches, they have always been complementary: Agent Skills package domain expertise into modular chunks that teach an agent how to approach a problem, while MCP provides the live execution interface to carry it out. Today, the broader ecosystem has converged on combining them, including efforts around Agent Plugins and proposals for serving Agent Skills over MCP so platform maintainers can distribute domain instructions and live tools together.

> At the platform level, our Google Cloud Databases team pairs MCP and Agent Skills together inside our Agent Plugins. When a developer using Antigravity connects to a PostgreSQL database on Cloud SQL or AlloyDB, they can install the corresponding Cloud SQL or AlloyDB plugin. From MCP, the agent gets a list of safe actions it can take against the database. From the bundled Agent Skills, it gets step-by-step instructions on how to use those tools for specific tasks, like provisioning an instance or configuring Identity and Access Management (IAM) database authentication securely—and because both specifications are open standards, the same `SKILL.md` and MCP pattern works across any open source database or agent harness.

## Notas de síntesis

- MCP y Agent Skills son complementarios, no competidores: MCP es la interfaz de ejecución viva (herramientas), Agent Skills es el conocimiento procedimental modular (instrucciones) con revelación progresiva.
- Ambos están ya bajo gobernanza neutral de la Linux Foundation (AAIF), co-mantenidos por Google, Anthropic, OpenAI y el ecosistema.
- El spec MCP del 28 de julio de 2026 pasó el protocolo a un modelo sin estado (stateless).
- El patrón de referencia (Agent Plugins de Google Cloud Databases) combina MCP (acciones seguras) + Agent Skills (instrucciones paso a paso) para PostgreSQL en Cloud SQL/AlloyDB.
- Se están proponiendo "Agent Plugins" y "servir Agent Skills sobre MCP" para distribuir instrucciones y herramientas juntas.
