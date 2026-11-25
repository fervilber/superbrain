---
title: "Towards a Trustworthy and Governable Internet of Agentics (arXiv:2611.03066)"
source: "arxiv.org"
date: 2026-11-02
captured: 2026-11-25T20:06:00+01:00
---

# Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services

URL: https://arxiv.org/html/2611.03066v1
Published: 2026-11-02
Authors: Haoyi Xiong, Yi Liu, Jiang Bian, Peng Diao, Bin Zhu, Tingting Hu, Yi Wang, Sumi Helal (Microsoft Corporation; University of Bologna)

## Abstract

Large language model applications are increasingly being organized as tool-using and multi-agent workflows rather than as isolated chat interfaces. This perspective paper examines the architectural problem that follows from that shift: agents may reason, invoke tools, and delegate work, but dependable deployment still requires interoperability across frameworks, runtimes, data boundaries, and organizational control domains. We study this problem through the lens of the Internet of Agentics (IoA), an emerging service-computing view in which heterogeneous agents are treated as governable service participants rather than only as stand-alone model endpoints.

The paper organizes the landscape as a three-layer progression: from today's fragmented agent ecosystem, to interoperable agents, and ultimately to trustworthy and governable autonomy. First, it examines the protocol stack centered on the Agentic AI Foundation, including MCP for agent–tool interaction; A2A for agent–agent coordination; AGENTS.md and Skills-style procedural manifests; and discovery, transport, and trust mechanisms such as AGNTCY and SLIM. Second, it reviews the systems abstractions that make agents deployable as service components, including logical agent architectures, orchestration patterns, gateways, registries, runtime control loops, and hardware-aware inference infrastructure. Third, it situates these developments within services computing, arguing that agentic systems reinterpret classical concerns from SOA and microservices — discovery, composition, governance, pricing, and trust — at the level of cognitive capabilities rather than deterministic functions. The paper concludes that the central IoA research challenge is trustworthy autonomy: ensuring that interoperable agent services are observable, auditable, privilege-bounded, economically controllable, and sufficiently dependable for real-world production use.

## I. Introduction (extracto)

Recent agentic systems have moved beyond single-turn assistants toward networks of specialized agents that plan, delegate, invoke tools, and interact with enterprise services. This shift changes the principal systems challenge. Model capability remains necessary, but production deployment increasingly depends on whether heterogeneous agents can interoperate across frameworks, tools, data boundaries, and organizational control domains.

## III-B. Model Context Protocol (MCP) (extracto)

MCP standardizes how an agent discovers and invokes external capabilities. Its practical value lies in replacing bespoke adapters for each model–tool pair with a common protocol for exposing tools, resources, and prompts through a stable interface. For services computing, MCP is the main bridge between probabilistic reasoning and deterministic back-end functions, and more concretely a response to the N×M integration problem that earlier API- and plugin-centric ecosystems handled poorly. Architecturally, MCP uses JSON-RPC and supports both local and remote transports. The important abstraction is not the wire format itself but the separation of concerns: servers expose capabilities, clients mediate access, and the model decides when to call a tool or retrieve a resource. This reduces integration cost while preserving the possibility of policy control at the host boundary. The client-mediated sampling model is especially important because it prevents servers from directly controlling model outputs and keeps authority with the host application.

MCP also highlights the main deployment challenge of agentic services: capability exposure is easy to standardize, but trust is not. Community servers vary in quality, permission models remain inconsistent, and enterprise use still depends heavily on local isolation, auditing, and approval flows. MCP should therefore be read as a necessary interoperability layer, not as a complete governance solution. A capability contract can tell an agent what a tool does and how to invoke it, but it does not by itself guarantee that the tool invocation is authorized, safe in context, or aligned with organizational policy. The operational burden therefore shifts toward runtime mediation, which makes MCP most defensible for production use when paired with explicit host-side controls.

## III-C. Delegation and Coordination Layer / A2A (extracto)

Above capability access, the coordination layer treats agents themselves as addressable service actors. Its design problem is horizontal delegation: how one autonomous agent discovers another, negotiates a task, receives progress, and obtains artifacts without requiring shared internals.

A2A specifies delegation among autonomous agents. If MCP answers "how does an agent call a capability?", A2A answers "how does one agent ask another agent to do work?" The protocol introduces a task model, asynchronous execution semantics, streaming updates, and a discovery mechanism based on Agent Cards. That design is directly relevant to service ecosystems because it makes agents addressable participants in distributed workflows and consolidates prior inter-agent designs such as ACP into a broader industry-facing coordination model.

The key architectural choice in A2A is opaque execution. Agents publish their capabilities and interaction requirements, but they do not have to expose their internal plans, tools, or prompts. This is attractive for enterprise and cross-organizational coordination because it preserves implementation autonomy while still permitting capability-based delegation. At the same time, the same opacity makes debugging, verification, and liability assignment more difficult. In practice, production use will require richer telemetry and audit trails than the protocol alone currently guarantees.

The service-computing implication is that A2A effectively turns agents into discoverable service endpoints with long-running, stateful task semantics. That is materially different from REST-style request/response integration. Task state, streaming updates, human escalation, and artifact return all become part of the service contract. This richer interaction model is useful, but it also raises the bar for observability and conformance. AAIF's incorporation of ACP into the broader A2A direction reduces fragmentation, but important questions remain open: how Agent Cards should be validated at scale, how multiple bindings should converge operationally, and how coordination failures should be diagnosed when task state alone is insufficient. These are not merely ergonomic issues; they determine whether A2A can support reliable service composition rather than isolated demonstrations.
