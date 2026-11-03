---
title: "Anthropic Message Threads: hilos de mensajes en la Messages API para agentes de larga duración"
source: "https://thenewstack.io/anthropic-claude-message-threads"
date: 2026-11-02
captured: 2026-11-03
---

# Anthropic launches message threads to cut Claude API agent latency

Captura verbatim por extractos de varias fuentes que cubren el lanzamiento (2 de noviembre de 2026): The New Stack, Unite.AI, AI Chat Daily, CellCog y daily.dev.

## Qué se lanzó

Anthropic introduced message threads in public beta on November 2, 2026, allowing Messages API applications on the Claude Platform to send only new messages after an initial full-conversation request. The public beta lets agents send only new messages each turn; Anthropic says median time to first token falls about 35% on 500k–1M token requests.

Message threads, as it's called, is available now in public beta for Anthropic's Messages API and is already enabled by default for "most" Claude Code users, according to an article published by Anthropic on Monday.

## Mecánica

After the first request, agents send only new messages plus the ID of Claude's previous response. A thread keeps the conversation on Anthropic's server between turns, so a long agent loop sends only its new messages and the id of the last response instead of the whole history. The initial request creates a thread by including `thread={"type": "create"}`, alongside the full conversation history, system prompt, and any tools being used.

Because the feature remains in beta, developers making requests directly must also include the `anthropic-beta` header with the value `message-threads-2026-08-12`. In the Python SDK, this can be supplied through `betas=["message-threads-2026-08-12"]`. Anthropic also provides a simpler approach through its SDK thread helper, which manages the conversation history and API parameters automatically.

## Latencia y coste

Median time to first token fell about 35% on 500k–1M token requests, measured on Claude Code users. Do they cost less? No. Anthropic says threads do not change pricing or rate limits; the gain is a lower, steadier time to first token. It does not reduce cost: prices and rate limits stay the same as before.

## Ciclo de vida y limitaciones

Threads expire 5 minutes after the last request and are held encrypted in memory, not written to disk. A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use.

The beta is available on the native Claude Platform, Claude Platform on AWS, Claude in Microsoft Foundry, and Claude Models on Google Cloud under Anthropic management, with beta support on every model. There is no API to list, read or delete threads. Threads do not support Message Batches, token counting, compaction on demand or most context editing, and they are unavailable to organizations with Inference hooks enabled.

Cached threads expire five minutes after the last request. They are held only in memory, encrypted, and never written to disk, so developers must keep their own copy of the conversation since the server's cached version can disappear after the timeout.

## El problema de fondo: el estado del cliente

That means you can improve responsiveness while still needing careful client-side state management and privacy planning. Threads materially reduce latency and request sizes without changing model billing; but they also introduce operational constraints (threads expire, are held in memory, and aren't eligible for zero-data-retention or HIPAA workflows). Implement the beta header and thread handling in a development agent and keep a robust client copy of conversation history to handle expirations; monitor for edge cases where a thread refusal or thread_not_found forces a full replay.

## Casos de uso previstos

The feature is intended for active sessions where latency matters, including long-running coding agents, computer-use agents whose screenshots remain with the thread, and document- and image-heavy workflows. "My bet — computer-use agents adopt it before coding agents do, since a screenshot per step is what makes the resend heavy, and most have it on by the end of December," writes one commentator.

## Recepción

Developers see server-side message threads as a solid latency/efficiency win for long agent sessions, but many are probing the fine print around caching costs, data retention, thread expiry, and editing/branching behavior (45% positive, 35% mixed, 20% skeptical en daily.dev).
