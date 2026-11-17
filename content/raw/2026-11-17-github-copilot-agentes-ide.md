---
title: "GitHub Copilot: deprecación de modelos efectiva el 16 de noviembre y controles de agente en el IDE"
source: "https://aiagentstore.ai/ai-agent-news/daily/2026-11-17"
date: 2026-11-17
captured: 2026-11-17
---

# GitHub Copilot — deprecaciones y releases semanales (AI Agent Store Daily News, 17 de noviembre de 2026)

Categoría: Herramientas de agente / mantenimiento de políticas de modelo. Capturado el 2026-11-17 desde la página diaria estable `aiagentstore.ai/ai-agent-news/daily/2026-11-17`, que trae los titulares del día con los campos _What changed / Why it matters / Try/watch_.

## Titular 1 — Deprecación de modelos de Copilot (efectiva el 16 de noviembre de 2026)

> **What changed:** GitHub announced the deprecation of several Copilot models — **Claude Opus 4.8, Claude Opus 5, and GPT-5.6 Terra** — effective **November 16, 2026**, and recommended alternatives such as **Claude Opus 5.5 and GPT-6.1 Sol / Luna**.

> **Why it matters:** If you run agent workflows or CI automation that pins those models, your agents may silently fall back or stop behaving the same; enterprise admins should update model policies or enable the suggested alternatives to avoid regressions.

> **Try/watch:** Audit repository and org-level agent policies (.github/agents or your Copilot settings) this week and update model selections or tests to verify results on the recommended models.

## Titular 2 — Releases semanales: controles de agente en el IDE y nuevos modelos (16 de noviembre de 2026)

> **What changed:** The Copilot changelog for the week highlights new Copilot app features (support for GitHub Enterprise Server in the mobile/desktop app) and VS Code agent workflow improvements such as an **Agents inbox** that surfaces sessions that need your attention and an experimental **"Compare Models"** agent tool; **Claude Fable 5.2 and Gemini 4 Carbon** are also listed as new options.

> **Why it matters:** These are practical quality-of-life updates for teams running multi-agent or long-running agent sessions inside IDEs — you can now route attention to high-priority agent sessions and run model-comparison experiments from VS Code without manual orchestration.

> **Try/watch:** Enable the Agents window in a non-production VS Code workspace, turn on experimental model tools, and run a short A/B comparison between a current model and the new options to measure differences in code edits or suggestions before rolling them into CI.

## Nota de contexto

La deprecación convierte la selección de modelo en **trabajo de mantenimiento de políticas**, no en una decisión puntual: un agente o workflow de CI que fija (`pin`) un modelo retirado puede degradar silenciosamente sin que nadie toque el código, porque el fallback ocurre en la capa de política, no en la del repositorio.
