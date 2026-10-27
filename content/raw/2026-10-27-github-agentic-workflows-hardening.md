---
title: "GitHub Agentic Workflows: semana de hardening (v0.93.0–v0.93.5), Pi CLI 1.4.0 por defecto y el agente 'Daily Documentation Healer'"
source: "https://github.github.com/gh-aw/blog/2026-10-26-weekly-update"
author: "GitHub (github/gh-aw weekly update)"
date: 2026-10-26
captured: 2026-10-27
---

# Captura: Weekly Update – October 26, 2026 (GitHub Agentic Workflows)

> Texto completo extraído del blog oficial de github/gh-aw. Se reproduce íntegro salvo navegación.

It was a hardening week in github/gh-aw: six releases from v0.93.0 through v0.93.5 brought stronger static analysis, safer credential handling, and clearer failure diagnostics.

## Release Highlights

The latest, v0.93.5, landed on October 25th. Earlier releases this week were v0.93.4, v0.93.3, v0.93.2, v0.93.1 and v0.93.0.

- **Network credentials in safe-output integration jobs** (#71833): safe-output integration jobs can now use network credentials when they need them.
- **Engine driver crashes are classified** (#71883): failures now come with secret-safe stderr diagnostics, so triage is faster.
- **Pi CLI 1.4.0 is the new default** (#71899).
- **Sharper custom linters**: a new `readerstringconv` analyzer (#71891), detection of parenthesized `Flush` discards (#71896), and missing recovery in goroutines launched through local closures (#71897).
- **Fewer surprises at compile time**: indexing boundaries are guarded and cron-step overflow is prevented (#71889), and generated conclusion references and fetch warnings are fixed (#71898).

## Notable Pull Requests

- [Prevent skipped threat detection from reporting inherited agent tokens](https://github.com/github/gh-aw/pull/71933) keeps token reporting honest when detection is skipped.
- [Return stage-aware partial results for MCP compile and audit timeouts](https://github.com/github/gh-aw/pull/71886) means a timeout no longer throws away the work already done.
- [Stop treating gh-aw-detection as experimental](https://github.com/github/gh-aw/pull/71848) graduates threat detection from its experimental label.
- [Preflight agent assignment credentials before processing issues](https://github.com/github/gh-aw/pull/71611) fails early instead of halfway through.

## Agent of the Week: Daily Documentation Healer

The self-healing companion to the Daily Documentation Updater: it hunts for documentation gaps the updater missed and proposes fixes.

In its last three runs it ran at roughly 23:40 UTC each night, taking 7–8 minutes per run. The most recent run on October 25th succeeded, while the two before it failed in the conclusion job's "Handle agent failure" step. The healer is also running a model-size experiment, alternating between Claude Sonnet 5 and Claude Haiku 4.5 to see whether the cheaper model heals docs just as well.

The healer is a documentation doctor that is itself part of a clinical trial, with a pre-registered hypothesis and everything.

**Usage tip**: Pair a generator workflow with a second "healer" pass that audits its output, so gaps get caught the next day.

## Notas de release v0.93.0 (21 de octubre de 2026)

v0.93.0 focuses on security hardening, safer dry-run compilation, and more reliable safe outputs and sub-agent model resolution.

- Codex stages native TOML sub-agents with resolved models and fails closed before startup (#70945); Copilot SDK refuses silent model substitution (#70943).
- Model-routing `allowed-models` now expands aliases (#70942); Claude detection model aliases resolve before CLI launch (#70861).
- Pi main/sub-agent requests are attributed with `x-awf-caller` (#71043).
- CLI proxy and MCP gateway containers honor runner proxy settings (#70347).

## Contexto de diseño del producto (changelog de GitHub, 13 de febrero de 2026)

- Workflows de agente escritos en Markdown en lugar de YAML; el agente decide la lógica para triaje de issues, revisiones de PR, análisis de fallos de CI y mantenimiento de repositorios.
- Integración profunda con GitHub mediante el GitHub MCP Server; herramientas adicionales de automatización de navegador, búsqueda web y MCP personalizados.
- Diseño security-first: solo lectura por defecto, ejecución en sandbox, aislamiento de red, dependencias fijadas por SHA y escrituras sanitizadas a través de _safe outputs_.
- Múltiples agentes de código soportados (GitHub Copilot CLI por defecto u otros), con el mismo formato de workflow entre motores.
