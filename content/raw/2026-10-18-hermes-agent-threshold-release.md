# Hermes Agent v0.22.0 "Threshold Release" - Raw Extraction

## Source 1: Tao.media Article

Nous Research Ships Hermes Agent “Threshold Release” With Guided Setup, App Connectors, and One-Click Local Models
October 14, 2026

The Threshold Release lowers the setup barrier for Hermes while adding more stable packaging for open agent workflows.

Nous Research has shipped Hermes Agent v0.22.0, a new release of its open-source agent platform focused on making first-time setup, app connections, and local model use easier for desktop users. The update, called "The Threshold Release", adds a guided first-launch chat, hosted app connectors for services such as Gmail, Linear, and Notion, one-click local model support through llama.cpp, stable SemVer release channels, and signed desktop packages, including Windows MSIX distribution through App Installer or the Microsoft Store.

The release is the largest Hermes window so far, covering roughly 24,200 commits, 6,080 merged pull requests, 2.045 million insertions, 7,180 closed issues, and 2,520 contributors since v0.21.0. It also rolls up the v0.21.1 through v0.21.7 patch releases into a more stable public milestone.

Guided Setup Lowers the First-Run Barrier
The most user-facing change is a new onboarding flow for fresh desktop installs. Instead of opening directly into settings, Hermes now starts with a setup chat that asks for a user name, theme preferences, apps to connect, plugins to install, and a few first tasks.

That setup flow runs on a free trial model, nous/welcome, once per operating-system user, so a newcomer can interact with Hermes before bringing an API key, choosing a paid model, or connecting to hosted services.

## Source 2: releases.sh/nousresearch/hermes-agent

Hermes Agent v0.22.2
Release Date: October 15, 2026
v0.22.1 was built from the wrong commit. It shipped unreleased gateway work, and the Microsoft Store app could stick on "Connecting."
0.22.2 is the release 0.22.1 was meant to be.

Known issue: Sessions that ran under the 0.22.1 gateway can't be deleted in 0.22.2.

Highlights:

- The gateway starts after a reboot again. After a restart, Linux can hand an early PID to an unrelated process, and the gateway could mistake it for a running gateway, so a supervised gateway (systemd, launchd, Docker) refused to start. Hermes now records the boot it started in, and when it can't tell, it asks the host lock, which only a live gateway holds. (#138594, fixes #133744)
- Long local-model turns survive on laptops. Local requests always stream with prompt-reading progress (shown in the status line), stall timers skip time the machine was asleep, a recovered local server gets another try instead of a breaker that failed every later message, and compression no longer times out while the server is still reading a long conversation. On Windows unified-memory machines, model launch and the prompt cache are sized to free memory. (#138560)

Hermes Agent v0.22.0 — The Threshold Release
Release Date: October 13, 2026
Since v0.21.0: ~24,200 commits · ~6,080 merged PRs · ~15,600 files changed · ~2,045,000 insertions · ~1,140,000 deletions · ~7,180 issues closed · ~2,520 contributors

The Threshold Release. Hermes was the god of thresholds: the doorway, the crossing, the boundary stone. v0.21.0 assembled the pantheon; v0.22.0 is about getting through the door. A fresh desktop install now opens on a guided setup chat that runs on a free trial model, so a newcomer is talking to Hermes before they own an API key. Connectors carry the agent across into the apps you already use, with no account needed to start. Local models bring it home to your own hardware with a one-click llama.cpp runtime. And the threshold itself got sturdier: tested SemVer stable releases that installs follow by default, signed desktop packages (including the Microsoft Store), and one package manager underneath everything.

Around that spine: a 600-plugin catalog, the Claude 5.5 / GPT-6 model wave, password-manager sign-in for the browser, a bot screen you can take over, one backend and one gateway for every profile, and a codebase a third smaller. This is the largest window Hermes has shipped, about 2.5x the v0.21.0 cycle, and it rolls up and fully documents the v0.21.1–v0.21.7 patch releases.

Highlights:

- A first launch that sets itself up — Open the desktop app on a computer where you have never used Hermes and it starts a short setup chat instead of a settings screen. One card at a time it asks your name, an accent color and a layout, which apps to connect, which plugins to install, then gives a quick tour and offers up to four first tasks picked for you. It runs on a free trial model (nous/welcome, once per OS user), so it needs no key; Skip setup ends it and Settings → Run onboarding again brings it back. The agent also gained set_theme, so "make it violet, dark mode" works in any desktop chat. (#137429, #137522, #137807, #134209, #105258 — @alt-glitch, @OutThisLife, @ethernet8023, @rewbs)
- Connectors: Hermes works inside your apps — The agent can now act in hosted apps such as Gmail, Linear and Notion through the Nous tool gateway: ask for an app, sign in once in your browser, and the tools are usable in the same turn. You do not need a Nous account to start; the first time you use an app, Hermes creates a free connectors-only identity. The desktop has a new Connectors page that puts hosted apps and your MCP servers in one list (it replaces the MCP tab), the same setup card appears in the TUI and CLI, and you can connect several named accounts of one app (a `work` and a `home` Gmail) and manage them with `/connectors` or `hermes connectors`. (#106842, #111008, #119074, #135143, #135072, #135097, #135151, #135173, #137426 — @alt-glitch, @rewbs)
- Local models in one click — Hermes can now run open models entirely on your machine with nothing leaving it: no account, no API key. It installs and maintains llama.cpp with the right engine for your hardware (CPU, CUDA, Metal, Vulkan or ROCm), rates every catalog model against your GPU and RAM, and picks the highest-quality build that fits. Downloads pause and resume, the server starts and stops with Hermes, and engine updates are one click. Start from Settings → Providers → Local Models on Windows, macOS and Linux, or `hermes model` → Local models in a terminal. The catalog includes Qwen3.8 27B, Qwen3.8 Flash Next

## Source 3: AT Pulse Article

Hermes Agent v0.22.0 lets its browser sign in through password managers and hand control to a person; browser control itself shipped in August · AT Pulse
Nous Research's Hermes Agent v0.22.0, released October 13, lets its built-in browser sign in through 1Password, Bitwarden or a Hermes vault and hand control to a person. The browser automation and job memory recently promoted as new arrived in August

## Technical Details Summary

- Guided first-launch chat for new users
- Hosted app connectors for Gmail, Linear, Notion
- One-click local model support via llama.cpp
- Stable SemVer release channels
- Signed desktop packages (Windows MSIX)
- Supervised gateway improvements (systemd, launchd, Docker)
- Long local-model turn handling with progress streaming
- Reasoning replay after hermes chat --resume
- Subagent completions staying in their chat
- Desktop regenerate confirmation before throwing away later turns
- Holographic memory moved out of core
- persistent_shell: false functionality
- browser_exec reaching LAN without cloud routing
- Multiple named accounts per connector
- hermes update on main fixed (no 403 errors)
- Qwen content filter improvements
- New plugins in catalog
