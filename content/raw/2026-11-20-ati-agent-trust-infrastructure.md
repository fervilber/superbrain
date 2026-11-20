---
title: "Agent Trust Infrastructure (ATI): confianza federada para agentes multi-organización"
source: "https://www.arxivnews.org/en/articles/58b869cf-51ad-46cb-a496-93fd884113c7"
date: 2026-11-19
captured: 2026-11-20
---

# Agent Trust Infrastructure (ATI) Boosts Security for Multi-Organization AI Agents

arXiv: 2611.23202v1 — 19 de noviembre de 2026

**Agent Trust Infrastructure (ATI)** creates federated trust among organizations **without a shared root authority**. It uses **peer-to-peer Certificate Authorities (AgentCAs)** and validates agent certificates before any request.

ATI works as an **external layer that plugs into existing agent frameworks**. A **five-plane reference monitor** checks agent identities, approved models, tools, system prompts, and authorizations tied to each organization.

## Resultados experimentales

In a simulated federation of **eight organizations with six agent frameworks**, researchers tested ATI against **11 distinct attack scenarios**. With all enforcement mechanisms turned on, **attack containment rose from 43 % to 84 %** — a 40-point improvement in the consistently evaluated set of scenarios. The added protection costs about **174 microseconds per request**.

## Limitación declarada

One limitation is that ATI's **attestation plane runs in the same process as the agent** and relies on host-reported measurements. It can spot unauthorized configuration changes made by ordinary software but **cannot guarantee integrity against an adversary who controls the underlying host**.

## Implementación

ATI is released as an **open-source, framework-independent package** that uses **IETF WIMSE token formats** for identity verification and **Entity Attestation Tokens (EAT)** for model, tool, and system-prompt integrity.

Las cinco planos (_planes_) del monitor de referencia:

1. Identidad del agente.
2. Modelo aprobado.
3. Herramientas aprobadas.
4. _System prompt_ aprobado.
5. Autorizaciones ligadas a cada organización.
