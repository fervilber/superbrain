---
title: "La memoria multi-agente como problema de arquitectura de computadores (arXiv:2603.10062)"
source: "arXiv (position paper)"
date: 2026-11-24
captured: 2026-11-24T20:08:00+01:00
---

# Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

## Abstract

As LLM agents evolve into collaborative multi-agent systems, their memory requirements grow rapidly in complexity. This position paper frames multi-agent memory as a computer architecture problem. We distinguish shared and distributed memory paradigms, propose a three-layer memory hierarchy (I/O, cache, and memory), and identify two critical protocol gaps: cache sharing across agents and structured memory access control. We argue that the most pressing open challenge is multi-agent memory consistency. Our architectural framing provides a foundation for building reliable, scalable multi-agent systems.

## 1. Introduction

LLM agents are quickly moving from "single agent" tools to multi-agent systems: tool-using agents, planner–orchestrator stacks, debate teams, and specialized sub-agents that collaborate to solve tasks. At the same time, the _context_ these agents operate within is becoming more complex: longer histories, multiple modalities, structured traces, and customized environments. This combination creates a bottleneck that looks surprisingly familiar to computer architects: memory.

In computer systems, performance and scalability are often limited not by compute but by memory hierarchy, bandwidth, and consistency. Multi-agent systems are heading toward the same wall—except their "memory" is not raw bytes, but semantic context used for reasoning.

## 3. Shared vs. Distributed Agent Memory

In _shared memory_, all agents access a shared pool (e.g., a shared vector store or document database). In _distributed memory_, each agent owns local memory and synchronizes selectively.

Shared memory makes knowledge reuse easy but requires coherence support; without coordination, agents overwrite each other, read stale information, or rely on inconsistent versions of shared facts. Distributed memory improves isolation and scalability but requires explicit synchronization; state divergence becomes common unless carefully managed. Most real systems sit between these extremes: local working memory with selectively shared artifacts.

## 4. An Architecture-Inspired Memory Hierarchy

- **Agent I/O layer:** Interfaces that ingest and emit information (audio, text documents, images, network calls).
- **Agent cache layer:** fast, limited-capacity memory for immediate reasoning (compressed context, recent tool calls, short-term latent storage such as KV caches and embeddings).
- **Agent memory layer:** large-capacity, slower memory optimized for retrieval and persistence (full dialogue history, vector DBs, graph DBs, and document stores).

Agent performance is an end-to-end data movement problem. If relevant information is stuck in the wrong layer (or never loaded), reasoning accuracy and efficiency degrade. As in hardware, caching is not optional.

## 5. Protocol Extensions for Multi-Agent Scenarios

This layer is best viewed as _agent context I/O_, e.g. MCP. That is necessary—but not sufficient. Two missing pieces stand out.

**Missing piece 1: Agent cache sharing protocol.** Recent work explores KV cache sharing, but we lack a principled protocol for sharing cached artifacts across agents. The goal is to enable one agent's cached results to be transformed and reused by another, analogous to cache transfers in multiprocessors.

**Missing piece 2: Agent memory access protocol.** Agentic memory frameworks propose many strategies, yet even when some frameworks support shared state, the standard access protocol (permissions, scope, granularity) remains under-specified. Key questions include: Can one agent read another's long-term memory? Is access read-only or read-write? What is the unit of access: a document, a chunk, a key-value record, or a trace segment?

## 6. The Next Frontier: Multi-Agent Consistency

The largest conceptual gap is consistency. For agent memory systems, _multi-agent memory consistency_ decomposes into two requirements: read-time conflict handling under iterative revisions, where records evolve across versions and stale artifacts may remain visible, and update-time visibility and ordering that determines when an agent's writes become observable to others and how concurrent writes may be observed in a permissible order. This is harder than classical settings because memory artifacts are heterogeneous (evidence, tool traces, plans), and conflicts are often semantic and coupled to environment state. A practical direction is to make versioning, visibility, and conflict-resolution rules explicit.

## 7. Conclusion

Many agent memory systems today resemble human memory: informal, redundant, and hard to control. To move from ad-hoc prompting to reliable multi-agent systems, we need better hierarchies, explicit protocols for cache sharing and memory access, and principled consistency models that keep shared context coherent.
