---
title: "Observabilidad de agentes de IA en Google Data Cloud: telemetría unificada en BigQuery y dashboards en Looker"
source: "https://cloud.google.com/blog/products/data-analytics/enterprise-ai-agent-observability-with-bigquery-and-looker"
date: 2026-11-14
captured: 2026-11-14
---

# Observabilidad de agentes de IA con BigQuery y Looker (Google Cloud Blog)

> Nota de captura: `web_extract` devolvió HTTP 429 del tier gratuito de Exa para esta URL en el momento de la ingesta; el texto que sigue son los extractos verbatim devueltos por el índice de búsqueda (párrafos completos del blog oficial de Google Cloud). Fecha de captura: 2026-11-14.

## Qué se anuncia

> As enterprises move AI agents from experimental prototypes into production, data and platform teams are discovering that deploying an agent is only half the battle — you also need to see how it reasons, which data it touches, and what it costs to run. Today, we are announcing expanded AI agent observability and evaluation capabilities across Google Data Cloud, giving you unified visibility into your first-party (1P) data agents in [BigQuery](cloud.google.com/bigquery) and [Looker](cloud.google.com/looker) as well as custom third-party (3P) agents built with agent development frameworks such as [Agent Development Kit (ADK)](google.github.io/adk-docs/) or LangGraph.

> Putting conversational and autonomous agents into production requires solving three operational challenges: tracing multi-step reasoning while protecting sensitive data, controlling token consumption and query spend, and evaluating answer accuracy before prompt or schema changes reach users.

## Los tres pasos del marco unificado

> Running agents at scale means you need to see how they perform, what they cost, and what actions they take. We're rolling out a unified telemetry framework across Google's Agentic Data Cloud that works the same way for every agent: Capture telemetry from the agent, land it in BigQuery tables you own, and analyze it wherever your teams already work.

> **1. Capture telemetry from every first-party and custom agent.** First-party data agents: Out-of-the-box Conversational Analytics agents emit telemetry automatically with no setup required. Queries routed to BigQuery data agents in Gemini Enterprise through agent-to-agent (A2A) workflows (now GA) send Cloud Monitoring metrics, Cloud Trace spans, and BigQuery conversation logs straight into your agent's project. Custom agents: Agents built with ADK or LangGraph stream the same structured telemetry into BigQuery through single-line SDK instrumentation.

> **2. Land telemetry in one governed home in BigQuery.** Conversation logging in BigQuery (GA): Managed 1P conversation logging writes to BigQuery tables you own, so you can inspect Conversational Analytics traces, including prompts and responses, directly in your data warehouse. Governed by default: The Conversational Analytics API, now GA, includes always-on admin audit logs and optional data-read audit logs in Cloud Audit Logs, and supports VPC Service Controls, customer-managed encryption keys (CMEK), and regional and multi-regional data residency.

> **3. Analyze with dashboards wherever your teams work.** In BigQuery (GA): Agent monitoring provides prebuilt dashboards in BigQuery Studio to track usage, active sessions, top knowledge sources, and latency across BigQuery Conversational Analytics agents. In Looker (GA): System Activity dashboards for Conversational Analytics, now GA in Looker (Google Cloud core) and Looker (original), track engagement and token usage, while user ratings and query review in the Responses & feedback tab are in preview.

## Implicación

> Unified agent observability framework capturing logging telemetry across 1P and 3P agents into BigQuery to surface performance and usage insights across developer and admin tools.
