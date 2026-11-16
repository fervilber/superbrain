---
title: "OpenAI Developer Community: la escritura MCP nativa aprobada se ejecuta dos veces tras una lectura programática"
source: "https://community.openai.com/t/responses-api-approved-native-mcp-write-executes-twice-after-a-programmatic-read/1416736"
date: 2026-11-16
captured: 2026-11-16
---

# Responses API: approved native MCP write executes twice after a programmatic read (OpenAI Developer Community, 16 de noviembre de 2026)

Categoría: Bugs (api, mcp, responses-api). Capturado el 2026-11-16. Cobertura secundaria: aiagentstore.ai (Daily AI Agent News, 16-nov-2026).

## Extractos verbatim

> One native MCP write approval causes **two actual `tools/call` executions** when the same approval-resumption response continues with a hosted programmatic read.

> When/how often: November 15, 2026 UTC. All three tested hosted-programmatic continuation samples replayed the write; the three non-programmatic controls did not. This is a sample description, not a claim about the rate across models or all requests.

> Successful-write reproduction: **2026-11-15 22:40:57.565–22:41:04.870 UTC**.

> This report is separate because it uses OpenAI's native remote MCP directly, **without that framework or `previous_response_id`**, and replays within the same approval-resumption response after a hosted programmatic read. The symptoms are related; a shared root cause has not [been confirmed].

## Respuesta de la comunidad (verbatim)

> Thanks for packaging this so clearly. Until it's fixed on the API side, a few ways to keep writes safe: [idempotency keys, transactional checks, "do-once" markers].

## Resumen de aiagentstore.ai (verbatim)

> **What changed:** An OpenAI Developer Community bug report (Nov 16) documents a reproducible behavior where an approved, native MCP write sometimes executes twice when the same response continues with a hosted programmatic read — the report includes a reproduction, request/response evidence, and links to related framework issues.
>
> **Why it matters:** Builders that rely on in‑response approval flows and Model Context Protocol (MCP) writes (for example: creating DB records, publishing content, or triggering external state changes) can observe duplicate side‑effects that break idempotency and data integrity; that risk increases for long, multi‑step agent programs that mix approval resumption and hosted programmatic continuations.
>
> **Try/watch:** Immediately add idempotency guards to write endpoints (idempotency keys, transactional checks, or "do‑once" markers), run the reproduction in staging, and monitor for duplicated writes in production.

## Contexto relacionado (OpenAI Developer Community)

- Hilos relacionados en la misma categoría Bugs: "Incorrect behavior of Conversation API with MCP Approval output item" (duplicado de `mcp_approval_request` con IDs `mcpr_` repetidos → error 400 "Duplicate item found with id mcpr\_..."); "Response API - MCP Tool - require_approval filter issue" (el filtro `never`/`always` se comporta mal con arrays vacíos); "URGENT: Production workflows blocked — Make MCP works directly, OpenAI returns 424" (fallos de descubrimiento de herramientas MCP desde el 3-nov-2026).

## Notas de síntesis

- El fallo es un problema de **idempotencia** en el plano de aprobación + continuación programática: una escritura MCP aprobada puede ejecutarse **dos veces** dentro de la misma respuesta de reanudación.
- Afecta directamente a flujos de agentes que mezclan aprobación en la respuesta con lecturas programáticas alojadas; rompe la integridad de datos.
- Mitigación recomendada por la comunidad: **claves de idempotencia, comprobaciones transaccionales y marcadores "do-once"** en los endpoints de escritura.
