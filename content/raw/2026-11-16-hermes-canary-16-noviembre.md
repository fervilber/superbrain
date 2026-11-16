---
title: "Hermes Agent: canary v0.23.1+canary.20261116T070005Z y estado del proyecto (noviembre 2026)"
source: "https://hermes-agent.ai/changelog"
date: 2026-11-16
captured: 2026-11-16
---

# Hermes Agent — canary del 16 de noviembre de 2026 y estado del proyecto

Fuente primaria del canary: GitHub releases de NousResearch/hermes-agent vía releasebot.io y hermes-agent.ai/changelog. Capturado el 2026-11-16. Cobertura secundaria: hermesatlas.com (informe "State of Hermes Agent", 12-nov-2026), secufocus.com, riseproductive.com, haiai123.com.

## Canary v0.23.1+canary.20261116T070005Z (16 de noviembre de 2026)

> Hermes Agent releases a canary update with fixes for tool timeouts, credential redaction, approval handling, and running from a missing terminal directory. Native macOS and Windows packages passed smoke tests.

### 🐛 Bug Fixes (verbatim)

> - Code-health: packaged-imports models namespace packages; AGENTS.md names its exceptions (aa6d201d) — @alt-glitch
> - Agent: generic tool deadline no longer clips a tool's own timeout (e1ac37eb) — @huanshan5195
> - Redact: mask an `.npmrc` auth value that only starts with a `${VAR}` reference (81fd6d89) — @c2h5oh
> - Plugin-catalog: commonly-hermes-plugin re-pinned; its server asks before writes (467b8f7d) — @lilyshen0722
> - Security: mask passwords in DB URL query strings (5b3168ea) — @thejesh23
> - Approval: read git option substitutions nested up to four levels as one word (234bd742) — @c2h5oh

### 📦 Other Changes (verbatim)

> - Review: trim deadline-floor tests to the two runner invariants; slim the registry guard (ec931428)
> - Port from lobehub/lobehub#20735: run in a usable directory when the terminal cwd is gone, and say so (#20735)

## Canaries previos de la semana

- **v0.23.1+canary.20261115T064406Z** (15-nov): nueva build de escritorio con catálogo de plugins ampliado y correcciones en gateway, chat, seguridad y flujos de perfil; paquetes macOS y Windows pasaron smoke tests de instalación nativa y chat.
- **v0.23.1+canary.20261114T064334Z** (14-nov).
- **v0.23.1+canary.20261113T064447Z** (13-nov).

## Hermes Agent v0.23.1 (9 de noviembre de 2026) — patch (verbatim, extractos)

> Patch release. This tag rolls up the ~618 PRs merged since v0.23.0 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0. What this patch ships for plugin users: since the plugin catalog's site deploy on November 9, the published `plugin-catalog.json` was larger than the 2 MiB cap clients accept, so every install silently fell back to the catalog it shipped with. `hermes plugins install` could not find plugins added since your last update, installed the pin your release shipped instead of the current one, and missed newer `removed` entries. This release raises the cap to 16 MiB, so the live catalog is used again (#151860, fixes #151856, thanks @100yenadmin). Installs that stay on v0.23.0 or older keep falling back until they update.

> Measured at commit `3b421578588`, the window since v0.23.0 contains 2,578 non-merge commits across 2,781 changed files (+151,690 / −62,595), 618 merged PRs and 409 closed issues. Also in the window, undocumented here on purpose: Esc backtrack in the TUI and classic CLI, group chats that run on a gateway without Desktop and can seat bots from other computers, saved gateway connections shared by Desktop and the Webapp, `hermes gateway attach` for local clients, `hermes clipboard image --json`, new plugin API (session-scoped environment values, plugin JSON-RPC methods and events, `llm.oneshot` auxiliary tasks, a compression-stable `conversation_id`, an `on_session_open` hook in the gateway, a `post_curator_run` hook), and a large batch of new plugin-catalog entries.

## Estado del proyecto — "The State of Hermes Agent, November 2026" (Hermes Atlas, 12-nov-2026)

> The two named releases since then spent their headlines not on new agent abilities but on how people get into Hermes and where everything in it runs. As of November 12, 2026:
>
> - 262,917 stars on the core repo (+16,162 since September 18, +6.5%)
> - v0.23.1 is the latest tagged release; 13 release tags landed in this window, from v0.21.5 through v0.23.1
> - 318 Atlas-tracked projects (+70 like-for-like) with 1,494,338 combined GitHub stars (+192,394, +14.8% like-for-like)
> - Memory & Context was the biggest mover: 57 repos / 305,374 stars, up 19 repos and 27.1%
> - Skills & Skill Registries is still the largest category at 53 repos / 499,579 stars, but it grew by only five projects
> - v0.22 "Threshold" let a fresh desktop install set itself up on a free trial model with no API key, and added hosted-app connectors, one-click local models, tested SemVer stable releases, signed desktop packages (including the Microsoft Store), and a 600-entry reviewed plugin catalog
> - v0.23 "Hearth" made one gateway own every session on a machine, served the Desktop workspace in a browser tab (the Webapp, off by default), and grew the plugin catalog from about 600 to over 1,050 entries
> - Upstream changed how it ships: v0.21.6 was the first release cut by a new stable release pipeline, tags moved from calendar `v2026.M.D` to plain SemVer, and source installs now follow tagged releases by default
> - The new process misfired twice: v0.22.1 was built from the wrong commit, and v0.23.1 fixed a plugin catalog clients had silently ignored since November 9

> The shorthand: September was about continuity and coordination. November is about the front door and the hearth. Hermes is moving from a system you assemble toward a product you install, update, and keep living in, with more of the experience in upstream's hands. Built-in skills went from 58 to 44.

## Hermes Cloud (10-nov-2026, haiai123.com)

> On November 10, 2026, Nous Research announced via its X account (@NousResearch) that Hermes Cloud agents are launching. According to the announcement, Hermes Cloud agents open in a browser tab and offer the same interface as Hermes Desktop, so users get a consistent experience across desktop and web. To create a personal agent, a user picks a name and a model in Nous Portal. Nous Research hosts the agent on the user's behalf; each agent runs in its own container with 24/7 availability and can handle scheduled jobs, meaning it continues working even when the user is not signed in.
