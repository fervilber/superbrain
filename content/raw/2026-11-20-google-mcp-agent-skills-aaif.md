---
title: "Escalar agentes de IA con estándares abiertos: MCP y Agent Skills se unen a la AAIF"
source: "https://opensource.googleblog.com/2026/11/scaling-ai-agents-open-standards-mcp-aaif.html"
date: 2026-11-11
captured: 2026-11-20
---

# Scaling AI agents with open standards: Kurtis Van Gent on MCP and Agent Skills joining the AAIF

Kurtis Van Gent (Google Cloud) y Daryl Ducharme (Google Open Source Programs Office) — 11 de noviembre de 2026

Building production AI agents requires more than a capable reasoning model. Agents need a reliable way to connect to external systems and data, and they need procedural domain knowledge so they know how to use those tools safely without exhausting their context window.

Over the past year, open source communities have rallied around two complementary open standards to solve these challenges: the **Model Context Protocol (MCP)** for connecting agents to live tools, and **Agent Skills** for loading procedural instructions and scripts on demand. Following Anthropic's donation of the Agent Skills specification to the Linux Foundation's **Agentic AI Foundation (AAIF)** alongside MCP, engineers from Google, Anthropic, OpenAI, and the wider ecosystem are now co-maintaining the standard under vendor-neutral governance.

## From the N-by-M database problem to open source collaboration

Kurtis Van Gent: When I started my current role around three years ago, it was early in the generative AI cycle. My mission was to make it easy for developers to use cloud databases for their AI applications. As model reasoning improved, context and data were clearly the keys to making effective use of it, and there's no better place to store data than a database.

At the time, most database conversations focused on retrieval-augmented generation (RAG) using vector search. However, our team believed that agents and tools held the most interesting potential for large language models (LLMs) going forward. We immediately hit two scaling challenges: Google Cloud supports more than 15 different databases across its portfolio, and new open source agent frameworks (starting with LangChain and LlamaIndex) were emerging every week. That created a classic **N-by-M integration problem** between many clients and many data hosts. To solve it, we started GenAI Toolbox for Databases (now **MCP Toolbox for Databases**) as an open source framework for building and serving tools.

## De sesiones con estado a MCP sin estado

As MCP adoption accelerated across the industry, however, it became clear that early **stateful assumptions around persistent sessions and initialization** were holding MCP back at production scale. That effort culminated in a two-day **Transports Summit** where Google and fellow working group members hosted the MCP core maintainers at their San Francisco offices to work through the scaling bottlenecks and align on a path forward. Shortly afterward, Van Gent was invited to become an **MCP core maintainer**. The result of that collaboration was the **July 28, 2026 MCP specification, which transitioned MCP to a stateless model**.

## MCP y Agent Skills son complementarios

While some observers initially viewed MCP and Agent Skills as competing approaches, they have always been complementary: **Agent Skills package domain expertise into modular chunks** that teach an agent how to approach a problem, while **MCP provides the live execution interface** to carry it out. Today, the broader ecosystem has converged on combining them, including efforts around **Agent Plugins** and proposals for **serving Agent Skills over MCP** so platform maintainers can distribute domain instructions and live tools together.
