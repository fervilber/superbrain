---
title: "Memoria compartida gobernada para sistemas multi-agente LLM (arXiv:2606.24535)"
source: "arXiv"
date: 2026-11-24
captured: 2026-11-24T20:09:00+01:00
---

# Governed Shared Memory for Multi-Agent LLM Systems

## Abstract

AI memory systems are increasingly moving beyond isolated chatbot histories toward shared state used by fleets of cooperating agents. In this setting, memory is not only a retrieval problem: it becomes a governed distributed-systems problem involving scoped access, temporal correctness, provenance, synchronization, and policy-controlled propagation. We introduce a systems architecture for governed shared memory in multi-agent LLM environments. The architecture formalizes the fleet-memory problem, identifies four failure modes—unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse—and defines primitives for scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation.

We instantiate these primitives in MemClaw, a production multi-tenant memory service, and evaluate them using ArgusFleet, a reproducible harness that exercises the live REST API along four governance dimensions. Provenance is the cleanest positive result: all 50 depth-four derivation chains reconstruct with correct writer identity at sub-second per-hop latency. Propagation is correct where measured, with high intra-fleet visibility and no observed cross-fleet leakage.

The live evaluation also surfaces two production-relevant architectural issues. First, scope enforcement was initially asymmetric across API paths: tenant isolation held, but sub-tenant scope was not enforced on direct GET-by-id for agent-scoped credentials; the gap was disclosed and remediated during the study. Second, contradiction supersession works when conflicting writes are admitted, but a synchronous near-duplicate gate can reject contradictory writes before the asynchronous contradiction detector observes them. These findings support the central claim that long-context retrieval alone is insufficient for production multi-agent memory: governed shared memory requires explicit systems-level abstractions, and live evaluation is necessary to expose the enforcement and pipeline-ordering failures that design-only treatments miss.

## 1 Introduction

Large-language-model systems are rapidly evolving from isolated assistants into fleets of interacting agents. Most existing memory systems, however, were designed around a single-agent abstraction — one user, one conversation, one retrieval stream, one context window — and this assumption breaks under fleet-scale deployments.

When multiple agents interact through shared memory, new correctness and governance requirements emerge. The system must answer who is allowed to retrieve which memory, how conflicting facts are resolved when two agents disagree, how knowledge propagates safely across agent boundaries, whether each retrieved memory can be traced back to its writer, and how stale memories are invalidated when the underlying state changes. These are not retrieval-quality questions. They are distributed-systems and database-consistency questions in retrieval clothing.

We argue that AI memory is therefore evolving from a context-window problem into a governed distributed-memory problem, and that this transition warrants the same systems-level attention historically devoted to databases, event-sourcing, and synchronization infrastructure.

## 2 Background and Related Work

A line of recent agent-memory architectures — including MemGPT and its successor Letta, Mem0, Zep, LangMem, A-MEM, and the memory subsystems of AutoGen — treats memory as a stand-alone component layered on top of an LLM. Most assume single-agent retrieval against an append-only store with largely unconstrained access, weak provenance semantics, and limited temporal resolution.

A second, very recent line moves explicitly to _shared_ multi-agent memory: G-Memory formalizes multi-agent memory as a three-tier interaction/query/insight graph and argues that single-agent memory does not transfer to multi-agent systems; MIRIX organises a multi-agent memory across typed stores; and Collaborative Memory adds _dynamic access control_ and immutable provenance over a shared multi-user store. None treats temporal contradiction-resolution and supersession as a first-class memory operation.

## 2.4 Memory Governance, Security, and Privacy

A parallel line treats agent memory as a security and privacy surface rather than a retrieval index. MEXTRA shows that an agent's memory module is a concretely extractable attack surface: crafted queries alone recover private user–agent interactions in a black-box setting, motivating scoped-retrieval. On the enforcement side, CaMeL attaches capability and provenance metadata to values and enforces policy at tool-call time, while Fides gives a formal information-flow-control model with confidentiality and integrity labels. For the propagation question — whether a memory _should_ cross an agent boundary — the canonical framing is contextual integrity: ConfAIde shows that capable LLMs leak information in contexts humans would withhold, reframing access as a question of appropriate flow rather than static permission. Our unauthorized-leakage finding is an instance of the classic confused-deputy problem: a read handler that resolves but then ignores caller identity.

## 3 The Fleet-Memory Problem

The architecture formalizes the fleet-memory problem, modeling shared memory as governed operational state with scope, provenance, and temporal supersession. Four failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.
