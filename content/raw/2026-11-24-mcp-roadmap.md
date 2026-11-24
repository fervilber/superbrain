---
title: "Roadmap del Model Context Protocol (actualizado 2026-08-22)"
source: "modelcontextprotocol.io"
date: 2026-08-22
captured: 2026-11-24T20:11:00+01:00
---

# Roadmap — Model Context Protocol

Last updated: **2026-08-22**

This page outlines the Core Maintainers' vision for the protocol over the coming six to twelve months, highlighting objectives targeted for the next specification update and beyond.

SEPs that fall within the priority areas below get expedited review and have the best chance of acceptance.

## Priority Areas

### 1. Agentic Messaging Primitives

Core Maintainers: Caitie McCaffrey, Clare Liguori, Peter Alexander

Agentic workloads need messaging patterns beyond request and response: work that runs for minutes, servers that push, results that stream, and a way to steer work mid-flight. MCP has grown a set of concepts for this, including Tasks, `subscriptions/listen`, and progress notifications, spread across multiple Working Groups. The risk is three answers to "the server isn't done yet" that don't share a lifecycle, a cancellation model, or an error surface. We want them to compose. This roadmap period:

- **Server-initiated events**: Triggers & Events WG. Channels and subscriptions for push delivery, including webhooks. As we take on asynchronous workloads through Tasks and other events, we need extensions that let servers tell clients when work has finished, without relying purely on expensive client-side polling.
- **A composition review**: Agents, Transports, and Triggers & Events WGs.

Beyond these, we expect continued work on Tasks (SEP-2663) toward eventual inclusion of the extension in the core protocol.

### 2. HTTP-Native Transport Unification and Hardening

Core Maintainers: Kurtis Van Gent, Nick Cooper

The 2026-07-28 release made a remote MCP server a normal HTTP workload, and we increasingly rely on HTTP specifics such as headers and status codes to carry transport-level information. Every HTTP-native feature needs a second stdio-specific design or doesn't work locally. SDKs maintain two transport pipelines, and protocol metadata is now duplicated across HTTP headers and message fields. We want one transport model. This roadmap period:

- **HTTP over stdio**: Transports WG. Streamable HTTP as the single binding, spoken over stdin/stdout for local servers. We believe we can use HTTP/2 over stdio to get multiplexed HTTP transport while retaining the security and lifecycle guarantees of a subprocess.
- **Caching**: Transports WG. The most recent protocol revision added `ttlMs` and `cacheScope` to list results and resource reads (SEP-2549). We want to extend our caching approach to support ETags, which should allow versioning the results of primitives, in particular tool calls.

### 3. Agent Identity and Enterprise-Ready Security

Core Maintainers: Paul Carleton, Den Delimarsky

MCP authorization assumes a person with a browser at consent time. Increasingly the caller is an agent: a cloud workload with its own identity, acting for a user who isn't present, or spawning sub-agents that should get narrower authority than their parent. Existing MCP servers lean on pasted API keys and long-lived refresh tokens. We need a standardized way for MCP servers to handle agent identities. This roadmap period:

- **DPoP**: Agent Identity WG (forming during this roadmap period). Finalize the specification for Demonstrating Proof of Possession (DPoP) and focus on getting widespread adoption.
- **Agent identity and delegation**: Agent Identity WG. An opinionated way for MCP servers to be reached by agents through their own identity or a user-delegated identity. Focus on Workload Identity Federation (SEP-1933), the Identity Assertion JWT Authorization Grant (ID-JAG) used by Enterprise-Managed Authorization, and RFC 8693 token exchange, coordinated with the IETF OAuth and WIMSE working groups.

Beyond these: human-presence attestation for distinguishing interactive clients from headless agents.

### 4. Improved Primitives

Core Maintainers: Kurtis Van Gent, Peter Alexander, Den Delimarsky

`tools/call` allows returning both `content` and `structuredContent` at the same time, which has confused server and client authors alike and produced diverging implementations. We want to spend this roadmap period improving the shape of the `tools/call` interface for more consistent semantics. We also hear repeatedly from the community that servers need more options to guide clients through large sets of tools, resources, and other primitives. This roadmap period:

- **Tool result shape**: Core Primitives WG. Redesign the `tools/call` interface to resolve fidelity disparities among return types and streamline the handling of structured and unstructured output.
- **Progressive discovery**: Core Primitives WG. Clients learn a server's tools and resources as they need them instead of ingesting the full catalog up front, with a defined interaction with the caching work.
- **Primitive annotations**: Core Primitives WG. Content annotations declare a piece of content's intended audience and priority. Applying them to tool results and resources could resolve the visibility confusion described in SEP-2200, but most implementers haven't adopted these annotations and may not be aware of their purpose. If they aren't useful, we should consider deprecating them.

### 5. Improved SDK Developer Experience

Core Maintainers: Den Delimarsky, David Soria Parra

Our SDKs, reference servers, and quickstarts are maintained by hand. We believe the specification and a human-reviewed conformance test suite can serve as the source of truth from which more of these artifacts are derived, so that both SDKs and examples are regenerated and revalidated as part of each release rather than repaired after it. This roadmap period:

- **The extension contract**: SDK WG with the Core Maintainers. Which role an extension binds (host, client, server, agent) and what each does when the capability is declared; what SDKs must support natively; how extensions are packaged; capability additions as versioned changes to the extension; auth treated as its own area.
- **The generated-artifacts experiment**: SDK WG. Generate a candidate Tier 1 SDK and its companion quickstart examples from the specification, validate both against the conformance test suite, and publish findings with a recommendation for the next cycle.
