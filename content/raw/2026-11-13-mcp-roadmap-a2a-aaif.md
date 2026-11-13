---
title: "El estado de la capa de protocolos: el roadmap de MCP y su modelo sin estado, A2A v1.0 y la Agentic AI Foundation"
source: "https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ ; https://modelcontextprotocol.io/specification/2026-07-28/changelog ; https://www.neuralpartners.ai/resources/mcp-a2a-agent-interoperability/ ; https://a2a-protocol.org/latest/topics/a2a-and-mcp/"
date: 2026-11-13
captured: 2026-11-13
---

# MCP, A2A y la Agentic AI Foundation — estado de la capa de protocolos

Captura por extractos del blog oficial de MCP (roadmap), del changelog de la especificación 2026-07-28, del análisis de Neural Partners y de la página comparativa oficial de A2A. Fecha de captura: 2026-11-13.

## El nuevo roadmap de MCP (blog oficial)

> One of the biggest changes we shipped is that protocol-level sessions and the initialization handshake are gone, so a server can scale horizontally without holding state (SEP-2575, SEP-2567). Additionally, clients can now call `server/discover` to learn a server's supported versions and capabilities before doing anything else. List results are also cacheable (SEP-2549).

> The brand-new Multi Round-Trip Requests pattern (SEP-2322) replaced server-initiated requests so that elicitation and similar flows work on stateless servers. The Server Card Working Group continues to work through the `.well-known` metadata conventions for MCP servers, so a server can be discovered and reasoned over without connecting to it.

### Las cinco áreas prioritarias

> **Agentic messaging primitives** — Modern agentic workloads no longer fit the standard request-and-response pattern. Loops can run for longer, servers can push streamed results, and there is a clear need to steer work mid-flight. [...] The work here spans server-initiated events (webhooks and channels, so clients aren't left polling for results).

> **HTTP-native transport unification and hardening** — With the 2026-07-28 release, a remote MCP server is now no different from any other HTTP workload, making it easy to host and operate one on any infrastructure.

> **Agent identity and enterprise-ready security** — MCP authorization today is built around a person approving access in a browser. [...] more and more of the callers are agents running as cloud workloads with their own identity, acting on behalf of a user who isn't present, or delegating narrower authority to sub-agents. [...] The work here covers finalizing Demonstrating Proof of Possession (DPoP) and driving its adoption, and defining an opinionated path for agent identity and delegation through Workload Identity Federation, the ID-JAG grant behind Enterprise-Managed Authorization, and standard token exchange.

> **Improved primitives** — Connecting to a server with a hundred tools means the model pays for that entire surface before the user has asked a single question, and tool selection tends to get worse as the list grows. We're starting a progressive discovery effort so a server can offer a small entry point and reveal more of its catalog as the conversation narrows.

## Changelog de la especificación 2026-07-28

> 1. Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport. [...] Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments (SEP-2567).
> 2. Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every request now carries its protocol version and client capabilities in `_meta`.
> 3. Add `server/discover`: servers MUST implement this RPC to advertise their supported protocol versions, capabilities, and identity.
> 4. Move experimental tasks out of the core protocol and into an official extension (`io.modelcontextprotocol/tasks`).
> 5. Remove SSE stream resumability and message redelivery [...] A broken response stream loses the in-flight request; clients MUST re-issue it as a new request with a new request ID (SEP-2575).

> 5. Require `ttlMs` and `cacheScope` fields on results returned by `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list` via a new `CacheableResult` interface.

## Neural Partners — «The agent interoperability stack»

> MCP connects an agent to tools and data. [...] A2A connects an agent to another agent. [...] If you're wiring Claude into your data warehouse, that's MCP. If you're letting your logistics agent coordinate with a carrier's agent, that's A2A. Most organizations need the first one long before they need the second.

> Anthropic created MCP and released it in late 2024. On 9 December 2025 it donated the protocol to the Agentic AI Foundation, a directed fund under the Linux Foundation that Anthropic co-founded with Block and OpenAI, with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg. [...] On 22 October four more arrived — Agent Skills (from Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face) and OpenSandbox (Alibaba) — bringing the foundation to ten hosted projects. Membership passed 240 organizations in August.

> Authority runs through individuals, not company seats — Lead Maintainers, then Core Maintainers, then Maintainers. No organization holds a bloc. [...] There's a published feature lifecycle with a twelve-month minimum deprecation window.

> Through 2025 it moved fast and broke things across 0.x releases. [...] That position expired on 12 March 2026, when A2A shipped v1.0.0 — its first stable release. It carried breaking changes to the interaction protocol, added multi-tenancy and signed Agent Cards, and moved to a stateless, layered, web-aligned architecture with three bindings: JSON over HTTP, gRPC, and JSON-RPC.

> On 17 August 2026 A2A became a hosted project of the Agentic AI Foundation, alongside MCP.

## A2A — comparativa oficial MCP/A2A

> MCP is vertical. It deepens a single agent. [...] A2A is horizontal. It connects agents across that boundary. [...] Used together, MCP gives each agent depth, and A2A gives your system reach.

## Oracle Autonomous Database (10 de noviembre de 2026)

> You can now enable and disable Agent-to-Agent (A2A) Server and Model Context Protocol (MCP) Server from the Tool configuration page in Autonomous AI Database.
