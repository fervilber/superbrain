---
title: "Google Antigravity: Dynamic Workflows convierte los equipos de agentes en scripts Python revisables"
source: "https://www.codeandchain.com/en/articles/2026-11-15/article-967ae0ef1a25"
date: 2026-11-15
captured: 2026-11-15
---

# Google Antigravity launches Dynamic Workflows, turning agent teams into reviewable Python scripts

Fuente: Code & Chain (codeandchain.com), artículo de 2026-11-15 (última actualización 14 de noviembre de 2026, 23:06 UTC).

## Resumen (verbatim)

> Google's Antigravity added Dynamic Workflows, allowing multi-agent coding tasks to run as reviewable Python scripts rather than free-form prompts. After users enter /run-workflow plus a task in the conversation, the main agent generates a Python script coordinating sub-agents, displays it for appro[val]…

## Puntos clave (verbatim)

> - Turns agent orchestration from prompts into version-controllable and reviewable code, suitable for team collaboration.
> - Replacing prompts with scripts to orchestrate multiple agents gives agent workflows an auditable and reusable engineering form for the first time.
> - Teams can review agent processes like code, reducing black-box risk and improving reuse efficiency.

## Notas de contexto (recuperadas de la cobertura semanal y del listado de noticias de agentes)

- El mecanismo descrito: el usuario escribe `/run-workflow` seguido de una tarea en la conversación; el agente principal **genera un script Python** que coordina sub-agentes y lo **muestra para aprobación** antes de ejecutarlo.
- La consecuencia arquitectónica es que la orquestación multiagente deja de ser un prompt en lenguaje natural (opaco, no versionable, difícil de revisar) y pasa a ser **un artefacto de código**: diffeable, revisable en un PR, reutilizable y auditable.
- Antigravity ya había introducido en noviembre `/teamwork` (sistema multiagente que apalanca los modelos Gemini 4 Argon, Carbon e Hydrogen) y `/swarm`; Dynamic Workflows es la capa que hace ese trabajo **revisable como código** en vez de efímero como conversación.
- El movimiento encaja en la tendencia del mes: convertir la coordinación de agentes en algo que un equipo de ingeniería pueda revisar y versionar, no en una caja negra de prompts.

## Implicación de ingeniería

Si la orquestación es código, hereda las propiedades del código: control de versiones, revisión por pares, pruebas de regresión y reutilización entre proyectos. Es el paso de «agente como asistente conversacional» a «agente como componente de un pipeline de ingeniería».
