---
title: "Captura: Hermes Agent v0.23.0 — The Hearth Release"
source: "https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0"
date: 2026-11-05
captured: 2026-11-09T20:10:00+01:00
---

# Hermes Agent v0.23.0 — The Hearth Release

- Tag: v0.23.0
- Repository: NousResearch/hermes-agent
- Published: 2026-11-05T21:32:33Z
- Author: teknium1

**Release Date:** November 5, 2026
**Since v0.22.0:** ~10,080 commits · ~1,950 merged PRs · ~8,720 files changed · ~725,200 insertions · ~201,400 deletions · **~850 issues closed** · 666 contributors

> **The Hearth Release.** In the old hymns Hermes kept the threshold and Hestia kept the hearth, and the two were honored side by side. v0.22.0 got newcomers through the door; v0.23.0 builds the fire they gather around. The headline: your whole Desktop workspace now opens in a browser tab, served by your own gateway. Underneath it, every conversation lives in one place: a single gateway owns each session, and the CLI, TUI, Desktop, editors, bots and cron all sit down at the same table instead of each running its own agent. From that one hearth, Desktop keeps every machine you run Hermes on connected at once, Group Chats route their own conversations, and the terminal finally draws your images inline and lets you rewind a conversation. Around it: plugins that keep themselves updated, price tags and spend limits on paid MCP tools, pluggable delegation, a plugin catalog that grew from about 600 to over 1,050 entries, a leaner built-in skill set, and a long run of memory and latency work for long-lived gateways. This release rolls up and fully documents the v0.22.1–v0.22.7 patch releases.

## Highlights

- **Your Desktop workspace in a browser tab** — The new Webapp serves the full Desktop workspace from your own gateway: the same chats, Group Chats, plugins and settings, in any browser on your network or behind a public URL with sign-in. The Docker image and Nix package ship it. It is off by default; turn it on with `webapp.enabled` or Web Access in Settings. (#141864, #145598, #145536, #145072, #145153 — @jquesnelle, @BearHuddleston, @IAvecilla, @Adolanium)

- **One gateway owns every conversation** — Before, the CLI, TUI, Desktop, editors (ACP), messaging bots and cron could each run their own copy of the agent against the same chat, which is how messages got written twice or went missing between surfaces. Now each machine runs one gateway that owns every session, and every surface attaches to it as a client: a chat you open anywhere is the same chat, with one queue and one history. You can even steer or edit a queued prompt from Desktop without it running twice. (#106742, #140334 — @unsupportedpastels, @kshitijk4poor)

- **Pictures in the terminal** — When you paste an image, or a tool takes a screenshot, the CLI and TUI now draw it right in the chat instead of printing a file path: real pixels in kitty and Ghostty (CLI and TUI) and in iTerm2, WezTerm and Konsole (CLI), coloured blocks everywhere else, and full resolution in VS Code's terminal when its image support is on. (#147293, #148874 — @Adolanium)

- **Rewind a conversation** — Press Esc twice or type the rewind command to roll a chat back to an earlier point, editing the message that comes next.

## Notas de estado (de búsquedas dirigidas)

- El catálogo de plugins pasó de ~600 a más de 1.050 entradas; el conjunto de skills integradas se redujo; la delegación es ahora conectable (pluggable); y los plugins se autoactualizan.
- Precios y límites de gasto sobre herramientas MCP de pago: la misma línea de "economía de la ejecución" que Muse Ember y Mistral.
- Esta release consolida y documenta las versiones parche v0.22.1–v0.22.7 (incluida la v0.22.7 del 3–4 de noviembre).
