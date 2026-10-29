---
title: "Roadmap de MCP: mensajería agéntica, transporte HTTP nativo, identidad de agente y primitivas mejoradas"
source: "https://modelcontextprotocol.io/development/roadmap"
author: "Model Context Protocol (Core Maintainers)"
date: 2026-08-22
captured: 2026-10-29
---

# Captura: Model Context Protocol — Roadmap

> Página de roadmap de MCP (última actualización: 2026-08-22), que define las áreas prioritarias para la próxima revisión de la especificación. Se incluye como fundamento del informe del 29 de octubre.

## Priority Areas

### 1. Agentic Messaging Primitives

Core Maintainers: Caitie McCaffrey, Clare Liguori, Peter Alexander.

Agentic workloads need messaging patterns beyond request and response: work that runs for minutes, servers that push, results that stream, and a way to steer work mid-flight. MCP has grown a set of concepts for this, including **Tasks**, `subscriptions/listen`, and progress notifications, spread across multiple Working Groups. The risk is three answers to "the server isn't done yet" that don't share a lifecycle, a cancellation model, or an error surface. We want them to compose. **This roadmap period:**

- **Server-initiated events**: Triggers & Events WG. Channels and subscriptions for push delivery, including webhooks. As we take on asynchronous workloads through Tasks and other events, we need extensions that let servers tell clients when work has finished, without relying purely on expensive client-side polling.
- **A composition review**: Agents, Transports, and Triggers & Events WGs. Primitives in the making, such as Tasks and Triggers, need to compose cleanly with each other and fit concrete use cases.

Beyond these, continued work on Tasks (SEP-2663) toward eventual inclusion of the extension in the core protocol.

### 2. HTTP-Native Transport Unification and Hardening

Core Maintainers: Kurtis Van Gent, Nick Cooper.

The 2026-07-28 release made a remote MCP server a normal HTTP workload, and we increasingly rely on HTTP specifics such as headers and status codes to carry transport-level information. Every HTTP-native feature needs a second stdio-specific design or doesn't work locally. SDKs maintain two transport pipelines, and protocol metadata is now duplicated across HTTP headers and message fields that servers have to cross-validate. We want one transport model, with standard HTTP practice on top of it. **This roadmap period:**

- **HTTP over stdio**: Transports WG. Streamable HTTP as the single binding, spoken over stdin/stdout for local servers. We believe we can use HTTP/2 over stdio to get multiplexed HTTP transport while retaining the security and lifecycle guarantees of a subprocess.
- **Caching**: Transports WG. The most recent protocol revision added `ttlMs` and `cacheScope` to list results and resource reads (SEP-2549). We want to extend caching to support ETags, allowing versioning of the results of primitives, in particular tool calls.

Beyond these: standardized error handling across all surfaces, capability scoping for tool lists after SEP-2575, and providing servers with configuration options in a secure way.

### 3. Agent Identity and Enterprise-Ready Security

Core Maintainers: Paul Carleton, Den Delimarsky.

MCP authorization assumes a person with a browser at consent time. Increasingly the caller is an agent: a cloud workload with its own identity, acting for a user who isn't present, or spawning sub-agents that should get narrower authority than their parent. Existing MCP servers lean on pasted API keys and long-lived refresh tokens. We need a standardized way for MCP servers to handle agent identities. **This roadmap period:**

- **DPoP**: Agent Identity WG (forming). Finalize the specification for Demonstrating Proof of Possession (DPoP) and focus on getting widespread adoption.
- **Agent identity and delegation**: Agent Identity WG. An opinionated way for MCP servers to be reached by agents through their own identity or a user-delegated identity. Focus on Workload Identity Federation (SEP-1933), the Identity Assertion JWT Authorization Grant (ID-JAG) used by Enterprise-Managed Authorization, and RFC 8693 token exchange, coordinated with the IETF OAuth and WIMSE working groups.

Beyond these: human-presence attestation for distinguishing interactive clients from headless agents and other agent identity concerns.

### 4. Improved Primitives

Core Maintainers: Kurtis Van Gent, Peter Alexander, Den Delimarsky.

`tools/call` allows returning both `content` and `structuredContent` at the same time, which has confused server and client authors alike and produced diverging implementations. We want to improve the shape of the `tools/call` interface for more consistent semantics. We're also starting a dedicated effort around **progressive discovery** to define what an experimental server-side discovery mechanism would look like. **This roadmap period:**

- **Tool result shape**: Core Primitives WG. Redesign the `tools/call` interface to resolve fidelity disparities among return types.
- **Progressive discovery**: Core Primitives WG. Clients learn a server's tools and resources as they need them instead of ingesting the full catalog up front.
- **Primitive annotations**: Content annotations in the specification declare a piece of content's intended audience and priority. Applying them to tool results could resolve visibility confusion (SEP-2200); if they aren't useful, consider deprecating them.

In addition, the File Uploads WG continues on scoped file operations and filesystem-like resource semantics (range reads, hierarchical listing).

### 5. Improved SDK Developer Experience

Core Maintainers: Den Delimarsky, David Soria Parra.

Our SDKs, reference servers, and quickstarts are maintained by hand. We believe the specification and a human-reviewed conformance test suite can serve as the source of truth from which more of these artifacts are derived. **This roadmap period:**

- **The extension contract**: SDK WG. Which role an extension binds (host, client, server, agent) and what each does when the capability is declared.
- **The generated-artifacts experiment**: SDK WG. Generate a candidate Tier 1 SDK and its quickstart examples from the specification, validate against the conformance test suite.

## SEP Prioritization

SEPs that fall within the priority areas above get expedited review and have the best chance of acceptance. SEPs outside them aren't rejected automatically, but expect a longer queue and a higher bar for justification.

## Notas del capturador

- **Transporte único HTTP**: la dirección es "Streamable HTTP como único binding", hablado sobre stdin/stdout para servidores locales (HTTP/2 sobre stdio). Elimina la duplicación de pipelines de transporte en los SDKs.
- **Caché con ETags**: versionado de resultados de primitivas, en particular _tool calls_ — necesario para razonar sobre cambios de estado y para cachés de prompt estables.
- **Identidad de agente como área de primera clase**: DPoP (proof of possession), Workload Identity Federation (SEP-1933), ID-JAG y RFC 8693 (token exchange), coordinado con IETF OAuth y WIMSE. Coincide con el anuncio de IBM Agent Identity del 28 de octubre: la identidad no humana es la frontera.
- **Atestación de presencia humana**: distinguir clientes interactivos de agentes headless — la misma pregunta que plantea la mensajería agéntica (Tasks, triggers, webhooks).
- **Mensajería agéntica**: servidores que empujan eventos, tareas de larga duración, streaming y "steering" a mitad de vuelo. Es el sustrato que necesitan los agentes de larga duración (Copilot cloud sessions, Akamai Agent Sandbox).
