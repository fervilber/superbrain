---
title: "Hermes Agent: delegación conectable (advanced-delegation) y orquestación en vivo de subagentes"
source: "https://github.com/NousResearch/hermes-agent/releases"
date: 2026-11-12
captured: 2026-11-12
---

# Hermes Agent — delegación conectable y orquestación en vivo de subagentes

Captura por extractos de las notas de release y del changelog comunitario de Hermes Agent (Nous Research). Fecha de captura: 2026-11-12.

## Extractos verbatim (changelog de gradually.ai y notas de release)

> •Choose how subagents are run — Delegation is now pluggable: keep the default, or install the official `advanced-delegation` plugin to send each subagent task to a named model or into a separate profile. Switch with `/delegation`. (#142563, #142564, #143423)

> •Steer your subagents while they run — `delegate_task` gained live orchestration: list running children, steer one mid-flight with a course correction, or stop it early and keep the partial result. Add optional JSON-schema validation on child outputs, per-delegation cost surfaced in results, and raised defaults (250 iterations, 10 concurrent children) — delegation went from fire-and-pray to actually managed parallel work. (#85232, #81144, #81142, #86506, #86745 — @teknium1)

> •Watch your subagents work — live transcripts + durable background delegation — `delegate_task` dispatches now return live transcript files you can `tail -f` the moment the subagents launch: every tool call, result, and streamed reply, one human-readable log per child. And background delegation completions are now durable — if the process restarts mid-run, results are restored and delivered through an ownership-checked ledger instead of vanishing.

## Contexto de release

> Hermes Agent v0.23.1 — Patch release. This tag rolls up the ~618 PRs merged since v0.23.0 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. [...] since the plugin catalog's site deploy on November 9, the published `plugin-catalog.json` was larger than the 2 MiB cap clients accept, so every install silently fell back to the catalog it shipped with. [...] This release raises the cap to 16 MiB, so the live catalog is used again (#151860, fixes #151856, thanks @100yenadmin).

> Measured at commit `3b421578588`, the window since v0.23.0 contains 2,578 non-merge commits across 2,781 changed files (+151,690 / −62,595), 618 merged PRs and 409 closed issues.

## De la v0.23.0 «The Hearth Release»

> your whole Desktop workspace now opens in a browser tab, served by your own gateway. Underneath it, every conversation lives in one place: a single gateway owns each session, and the CLI, TUI, Desktop, editors, bots and cron all sit down at the same table instead of each running its own agent. [...] plugins that keep themselves updated, price tags and spend limits on paid MCP tools, pluggable delegation, a plugin catalog that grew from about 600 to over 1,050 entries, a leaner built-in skill set, and a long run of memory and latency work for long-lived gateways.

## Delegación como backend conectable (documentación oficial)

> The active provider is `delegation.backend` in `config.yaml`; a provider's own settings live under `delegation.backends.<backend name>`. The `default` strategy is today's behaviour: every child follows the `delegation` section (`delegation.provider`, `delegation.model`, `delegation.base_url`, ...), or inherits the parent's route when those are empty. It is itself a plugin, the bundled `plugins/delegation/default/` (`kind: backend`, always loaded).

> `display_name` and `summary` [...] label your backend in pickers such as `/delegation`. [...] Core code calls `agent.delegation_backends` directly.

Ejemplo de configuración YAML (documentación oficial):

```yaml
delegation:
  backend: tiers
  backends:
    tiers:
      tiers:
        - {
            name: quick,
            description: Lookups and summaries.,
            provider: openrouter,
            model: google/gemini-3-flash-preview,
          }
```

> `hermes plugins enable delegation-tiers`

## Notas de captura

- **Captura por extractos**: reconstruida a partir de los fragmentos verbatim que devolvió `web_search` (notas de release del repositorio `NousResearch/hermes-agent`, el changelog comunitario de gradually.ai, la documentación oficial `hermes-agent.nousresearch.com/docs/developer-guide/delegation-provider-plugin` y un vídeo divulgativo sobre el plugin `advanced-delegation`). No se extrajo una única página completa.
- Sin cambios de versión nuevos respecto al informe de 2026-11-11 (que ya cubrió la v0.23.1); esta raw documenta la arquitectura de delegación conectable para el análisis de hoy.
