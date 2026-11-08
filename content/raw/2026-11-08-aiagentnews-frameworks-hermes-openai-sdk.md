---
title: "Captura: Frameworks for AI agents — Hermes Agent v0.22.0, OpenAI Agents SDK v0.24.0 y los releases de frameworks (AI Agent News)"
source: "https://aiagentnews.io/topics/frameworks"
date: 2026-11-08
captured: 2026-11-08T20:08:00+01:00
---

# Frameworks for AI agents | AI Agent News

_Captura verbatim de los titulares del agregador `aiagentnews.io/topics/frameworks`. La página rota el listado, así que se conserva la captura tomada el 2026-11-08._

### Hermes Agent v0.22.0 adds guided desktop setup, hosted app connectors and one-click local models

NousResearch has released Hermes Agent v0.22.0, which it calls the Threshold Release, with a guided first-run setup chat, hosted app connectors, and one-click local model support via llama.cpp. The release also adds tested SemVer stable channels, signed desktop packages and a unified package manager called hermes pm.

github.com/NousResearch/hermes-agent/releases/tag/v0.22.0

### Hermes Agent v0.21.7 moves source installs to tagged releases by default

Hermes Agent v0.21.7 is a patch release in which source installs of the official repository update to the latest published tagged version instead of every commit on main. It also keeps reasoning intact across resumed sessions and makes updates work behind some firewalls.

github.com/NousResearch/hermes-agent/releases/tag/v0.21.7

### OpenAI Agents Python SDK releases v0.24.0 with run-wide tool error formatting

OpenAI's openai-agents-python SDK version 0.24.0 adds a run-wide tool error formatter and optional MCP annotations on converted tools. The minor release also changes how saved run snapshots and custom error formatters behave, so existing code may need updates.

github.com/openai/openai-agents-python/releases/tag/v0.24.0

### Pydantic AI v2.57.0 adds Meta model provider and tool-call approval reviewer

Pydantic AI released v2.57.0 with a MetaProvider for Meta Muse models and a Harness ApprovalReviewer that lets a model approve low-risk tool calls before a person sees them. The release also changes how several realtime, background tool and Skills behaviors work, so existing agents should be checked against the compatibility notes.

github.com/pydantic/pydantic-ai/releases/tag/v2.57.0

### Agno v3.1.5 adds repository pinning and S3 checkpoints for sandboxed agents

Agno has released v3.1.5, which lets sandboxed Claude and Codex agents start sessions in a pinned repository and stores sandbox checkpoints in S3-compatible buckets. The release also adds KeenableTools for keyless web search and page extraction, along with several bug fixes.

github.com/agno-agi/agno/releases/tag/v3.1.5

### AWS introduces Strands Decider 2B and Strands Box for agent development

AWS has open-sourced Strands Decider 2B, a two-billion-parameter model that picks from predefined options for agent decisions, and Strands Box, a sandbox in developer preview that enforces execution policies. The two projects target different parts of agent work: choosing actions and controlling how those actions run.

www.infoq.com/news/2026/10/aws-strands-agents/

### LangGraph's Postgres checkpoint package 3.2.0 adds a prune method

LangChain's langgraph-checkpoint-postgres 3.2.0 was released on 14 October, adding a prune method to PostgresSaver and AsyncPostgresSaver. The release is a feature addition on top of version 3.1.3.

github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.0

### Google releases ADK for Kotlin 1.0 for building production AI agents

Google has released version 1.0 of the Agent Development Kit (ADK) for Kotlin, generally available now. The release reaches feature parity with ADK 1.0 Core and adds Android-first, on-device extensions.

### Pydantic AI v2.55.0 drops Python 3.10 and adds conversation and caching features

Pydantic AI released v2.55.0, which requires Python 3.11 or newer in every package and adds a Conversation object that carries history across runs. The release also adds a unified cache setting and a Caching capability for prompt caching across providers.
