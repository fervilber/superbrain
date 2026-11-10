---
title: "Captura: Spacefast de Automattic — la capa de publicación de lo que construyen los agentes"
source: "https://spacefast.com/about"
date: 2026-11-09
captured: 2026-11-10T20:18:00+01:00
---

# Spacefast — A home for what agents make

Automattic · research preview · anunciado el 9 de noviembre de 2026

## Página «About» (verbatim)

> People make pages, prototypes, reports, and small apps with agents every day. Most of it never leaves a local folder or a chat. Spacefast publishes the files, gives you a live URL, and lets you choose who can open it.
>
> Each change becomes a version with its own address, and the live address can roll back without a rebuild. The dashboard, CLI, API, and MCP server work on the same spaces, so an agent can manage the work as well as publish it.
>
> Spacefast is made by Automattic, the company behind WordPress.com, WooCommerce, Tumblr, Jetpack, Day One, Pocket Casts, and Beeper.
>
> **A space is the durable home for that work.** Each publish creates an immutable version with its own address. The live address can move forward or roll back without rebuilding. Access starts private, then widens only when you choose who should see it.
>
> **What stays true.** The result should outlive the chat. A useful page should not disappear when a conversation ends. Spacefast keeps its address through revisions and lets you restore a retained version when an update goes wrong.
>
> **Agents get the same product.** The dashboard, CLI, API, and MCP server are different doors into the same spaces and versions. An agent can publish and manage the work without asking a person to repeat every click.

## Documentación (developers.spacefast.com/docs) (verbatim)

> Spacefast hosts the sites people build with AI agents. You hand it a folder, it hands back a URL. Everything you can do in the dashboard you can also do from the sf CLI, the HTTP API, or an MCP server, so the agent that built the site can publish it too.
>
> ```
> npm install -g spacefast
> sf publish ./dist
> ```
>
> No account needed for the first publish. The CLI creates a Space, uploads the files, and prints a live URL plus a claim link. Sign in later to keep it.
>
> ```
> Published: https://quiet-harbor.view.fast
> Version URL: https://v1--quiet-harbor.view.fast
> Version: v1 (ready)
> Files: 12
> Duration: 3.2s
> ```
>
> **A Space is one site with a stable hostname. Every publish creates a version, an immutable snapshot with its own URL that never changes. The live channel points at one version. Promoting or rolling back moves that pointer. Nothing gets rebuilt.**
>
> Static output is the default path. Point sf publish at a build directory and it uploads only the files that changed. If you'd rather publish source, Spacefast detects the framework and builds it. Sites that need a database, server functions, or scheduled jobs opt into the Zero runtime with one line of config.

## Página para desarrolladores (spacefast.com/for-developers/)

> **Publish, roll back, leave**
>
> ```
> $ sf publish ./dist
> ✓ 128 files · live in 8s → https://quiet-sun.space.fast
>   this version → https://quiet-sun--v7.space.fast
> ```
>
> **CI** — Run the CLI or curl from any pipeline step with a scoped key. `sf api-keys create --preset ci_deploy` mints a least-privilege key, shown once. Every command takes `--json` and exits with a stable code (0 ok, 2 validation, 10 auth, 20 not found, 30 conflict, 40 network, 50 timeout).
>
> **Agents** — The same CLI, API and typed errors work when an agent is at the keyboard. Every docs page is fetchable as Markdown, and a hosted MCP server gives agents typed tools to publish, check status, diff and roll back.
>
> **No terminal at all** — Drop a folder, a zip or a single index.html onto drop.fast.
>
> **Everything is a version** — A publish that changes files freezes an immutable version with its own URL [...] so visitors never see a half-published space.
>
> **Rollback is a pointer flip** — `sf rollback v6` promotes an earlier version to live. No rebuild, no redeploy.
>
> **Leaving is one command** — `sf spaces download` writes files from a retained version to a folder.

## Plataformas (spacefast.com/docs/platforms)

> Offer hosting under your own brand. Spacefast runs the infra, and your product keeps the customer, the pricing, and the relationship. [...] Platforms is part of WP Cloud, the platform hosting companies use to power their own WordPress hosting products. It runs on the same infra as Automattic, WP Cloud, Pressable, and WordPress.com. The Partner API extends it to the sites and apps your customers build with agents.

## Agentes compatibles listados en la web

Claude, ChatGPT, Grok Bot, Muse, Cursor, Instinct, OpenClaw, **Hermes**, OpenCode, Grok (+19 más).

## Resumen del briefing diario (aiagentstore.ai/ai-agent-news/daily/2026-11-10)

> **Automattic launches Spacefast — instant hosting for agent-built apps.** What changed: Automattic announced Spacefast, a new service and standalone company that lets users publish apps and websites directly from the AI assistant or coding agent they already use; the blog post was published November 9, 2026.
>
> Why it matters: Builders and small teams can skip a lot of ops work (hosting, databases, DNS, rollbacks and per-publish URLs) so agent-driven prototypes and low-touch products can go live faster without hiring dedicated infra engineers.
>
> Try/watch: Try the free preview to validate end-to-end agent publishing in your workflow and watch pricing and auth controls (the post highlights "approval checks" for sensitive actions) before you put production data or payments behind an agent-published endpoint.
