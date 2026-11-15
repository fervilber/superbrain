---
title: "Anthropic describe el proceso de revisión de código asistido por IA del equipo de Claude Code"
source: "https://www.infoq.com/news/2026/11/claude-code-review/"
date: 2026-11-15
captured: 2026-11-15
---

# Anthropic Outlines Its AI-Powered Code Review Process for Claude Code

Fuente: InfoQ, Robert Krzaczyński, 15 de noviembre de 2026 (2 min de lectura). Fuente original citada: claude.dev.

## Contenido (verbatim)

> Anthropic has outlined how the Claude Code team handles code reviews as AI agents increasingly contribute to its codebase. The approach relies on multiple layers of automated verification, AI-powered reviews, and risk-based human approval, aiming to reduce manual review time without increasing regressions or production incidents.

> Addy Osmani, Morgan Westlee Lunt and Qing Wang described how the team's review process has evolved alongside the growing volume of AI-generated code. Between June and September, merged pull requests to the Claude Code repository more than doubled, while the proportion of changes requiring a revert fell by over 40%.

> Rather than relying on traditional line-by-line reviews, the team has moved much of the verification earlier in the development process. Before opening a pull request, Claude runs tests, builds, and linters, while a separate agent reviews the changes in a fresh context.

> Every pull request then goes through several automated checks. Claude-powered reviewers inspect code changes for potential bugs, with multiple agents independently investigating findings before another group verifies them. A separate security review can also block a merge if unresolved issues remain.

> Human involvement depends on the risk associated with a change. Low-risk modifications, such as documentation updates or internal features behind feature flags, may require no human approval. Medium-risk changes require one person, while high-risk modifications need two approvals. Changes to particularly sensitive areas, including CI workflows, always require human oversight.

> The team also introduced mechanisms to prevent automated reviews from generating excessive feedback. Review cycles are capped at three rounds before the author is asked to reconsider the implementation. Subsequent reviews focus on new changes rather than repeatedly examining the entire pull request.

> These adjustments have improved review efficiency. According to Anthropic, the share of internal pull requests passing after one review and fix round increased from 65% to 78%. Meanwhile, the proportion requiring five or more rounds dropped from 8.9% to 1.5%.

> Human reviewers nevertheless remain responsible for architectural decisions, product direction, high-risk changes, and the final outcome. The team also emphasizes that the person directing an AI agent remains accountable for the code it produces.

## Lectura técnica

- **Dato duro**: entre junio y septiembre, los PR fusionados en el repo de Claude Code **más que se duplicaron**, mientras la proporción de cambios que exigieron revertir **cayó más del 40%**.
- **Verificación desplazada a la izquierda**: antes de abrir el PR, Claude ejecuta tests, builds y linters, y **un agente separado revisa los cambios en contexto limpio**.
- **Revisión en capas**: revisores con IA buscan bugs; **varios agentes investigan hallazgos de forma independiente** y otro grupo los verifica; una **revisión de seguridad aparte puede bloquear el merge**.
- **Aprobación humana por riesgo**: riesgo bajo = sin aprobación humana; medio = una persona; alto = dos; áreas sensibles (flujos de CI) = supervisión humana obligatoria.
- **Control de ruido**: ciclos de revisión limitados a **tres rondas**; después, se pide al autor que reconsidere la implementación. Las revisiones posteriores miran solo los cambios nuevos.
- **Eficiencia**: PRs internos que pasan tras una ronda de revisión y arreglo suben del **65% al 78%**; los que exigen cinco o más rondas caen del **8,9% al 1,5%**.
- **Responsabilidad**: la persona que dirige al agente sigue siendo responsable del código que produce.
