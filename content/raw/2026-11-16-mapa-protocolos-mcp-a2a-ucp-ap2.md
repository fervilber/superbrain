---
title: "DEV (GDE): MCP, A2A, UCP, AP2... Confused? A Simple Map of AI Agent Protocols (November 2026)"
source: "https://dev.to/gde/mcp-a2a-ucp-ap2-confused-a-simple-map-of-ai-agent-protocols-november-2026-3ph"
date: 2026-11-16
captured: 2026-11-16
---

# MCP, A2A, UCP, AP2... Confused? A Simple Map of AI Agent Protocols (November 2026)

Autor: Karthigayan Devan, Google Developer Experts. Publicado el 15 de noviembre de 2026. Capturado el 2026-11-16.

## TL;DR — una pregunta elige el protocolo (verbatim)

| My agent is talking to... | Use this     | In one line                                       |
| ------------------------- | ------------ | ------------------------------------------------- |
| Tools and data            | MCP          | Plug the agent into APIs, databases and files     |
| Another agent             | A2A          | Hand off work to an agent someone else built      |
| A user's screen           | AG-UI / A2UI | Show the user what the agent is doing, live       |
| A store or business       | UCP          | Search, cart, checkout and orders in one standard |
| A payment                 | AP2          | Prove the user really approved the purchase       |

## El stack de un vistazo (verbatim)

```
+---------------------------------------------------+
|  USER          AG-UI (live events) / A2UI (UI)     |
+---------------------------------------------------+
|  PAYMENTS      AP2 (signed mandates), x402         |
+---------------------------------------------------+
|  COMMERCE      UCP (catalog, cart, checkout)       |
+---------------------------------------------------+
|  AGENTS        A2A (agent to agent)                |
+---------------------------------------------------+
|  TOOLS         MCP (agent to tools and data)       |
+---------------------------------------------------+
```

> One agent can use all five layers in a single task.

## Capa 1 — MCP, las manos del agente (verbatim)

> Model Context Protocol (MCP) connects an agent to tools and data: your database, GitHub, Slack, a weather API, anything. Build an MCP server once, and any MCP-compatible agent can use it. What's new: the current spec is 2026-07-28, and it's the biggest change yet. MCP moved from a stateful, session-based protocol to a stateless request and response protocol. What that means in practice:
>
> - No more sessions. The session handshake is gone, so any request can go to any server instance. Great news for anyone running MCP servers behind a load balancer.
> - A new discovery call. Clients can ask a server what it supports before sending other requests.
> - Some features are deprecated. Roots, Sampling and Logging are now deprecated, and Tasks moved out of the core into an official extension.
> - Old transport is on the way out. If your server still uses HTTP+SSE, the spec tells you to migrate to Streamable HTTP.

## Capa 2 — A2A, agentes hablando con agentes (verbatim)

> Agent2Agent (A2A) lets agents built by different teams, vendors or companies work together. Each agent publishes an "Agent Card" describing what it can do, and other agents discover it and delegate tasks. MCP vs A2A in one line: MCP is for tools you control. A2A is for agents you don't own, which have their own brains and make their own decisions. What's new:
>
> - v1.0 shipped on March 12, 2026, the first stable version, with JSON-RPC, gRPC and HTTP+JSON bindings. The v1.0.1 patch followed in May.
> - v1.1 is in the works. A release candidate tagged in late October adds two-way streaming while a task runs.
> - It moved in with MCP. A2A joined MCP in the Agentic AI Foundation (under the Linux Foundation) in August 2026.
> - Big vendors are on board. Microsoft Copilot Studio now lets you expose an agent as a remote MCP server or an A2A agent.

## Lo que sigue faltando (verbatim)

> The stack is real, but it isn't finished. Before you bet a product on it, know the gaps:
>
> - No shared memory standard. No foundation-backed protocol exists for agents to share one memory. Most teams expose memory through an MCP server and hope for the best.
> - No privacy signal. A recent academic audit found that neither MCP nor A2A carries a privacy field. If a user opts out of ad data sharing, that choice can't travel with a delegated task.
> - Identity is still open. "Which agent is this, and who does it work for?" doesn't have one standard answer yet.
> - Commerce and payments are early. Lodging and food specs in UCP are drafts, and AP2 is at v0.2. Build pilots, not your whole checkout.

## Notas de síntesis

- Los protocolos son **capas**, no competidores: MCP (herramientas), A2A (agentes), AG-UI/A2UI (usuario), UCP (comercio), AP2/x402 (pagos).
- **Gaps declarados honestamente**: no hay estándar de memoria compartida; ningún protocolo lleva campo de privacidad (una auditoría académica lo encontró); la identidad sigue sin una respuesta única; comercio y pagos están verdes (UCP en borrador, AP2 en v0.2).
- El mapa sitúa a Poppy como protocolo recién llegado esta semana ("And as of this week, Poppy").
