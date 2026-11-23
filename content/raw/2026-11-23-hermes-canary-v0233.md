---
title: "Hermes Agent canary v0.23.3: catálogo de plugins y commit claims en stable-release"
source: "https://github.com/NousResearch/hermes-agent/releases"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# Hermes Agent canary v0.23.3+canary.20261123T065600Z (23 nov 2026)

**Release Date:** November 23, 2026
Commit: `249dc60308a1ea3e13e8cd281433552cd25d36ab`

## Descargas — Hermes Desktop

| OS      | Arquitectura             | Descarga |
| ------- | ------------------------ | -------- |
| macOS   | Apple Silicon (M-series) | DMG      |
| Windows | x86 (64-bit)             | MSIX     |
| Windows | ARM (arm64 / aarch64)    | MSIX     |

## Estado de smoke

| Paquetes                | Smoke status |
| ----------------------- | ------------ |
| macOS DMG + ZIP (arm64) | Passed       |
| Windows MSIX (arm64)    | Passed       |
| Windows MSIX (x64)      | Passed       |

## Features destacadas

- **Release:** cablear "commit claims" en `stable-release.yml` con legs nativos de solo lectura (`0c55aa60`) — @ethernet8023
- Expansión masiva del **catálogo de plugins comunitarios** en esta canary (decenas de entradas): creatorplaybooks, valetudo, deny-record, polytropos-router, katara (proveedor de memoria), beeper-platform, Lot Map 0.2.0, utcp-bridge, rook-agent-utils, stats (panel Hermes Stats), Hermes for UniFi, PipoPapo, HybridOps (recuperación), commons, tmux-watch, warm, aisecuritywarden (fuente de secretos), quick-prompts, oxylabs-web-api, instabox (backend de terminal), quote-selection, slack-history, chinadrivetest, chinavisacard, cutout, ai-executive, jetson reboot monitor, entre muchos otros.

## Canaries anteriores de la serie 0.23.x

- v0.23.2+canary.20261119T064637Z — 19 nov 2026 (`fe8b920cae0980cef854f478236f525aaf2b93ce`)
- v0.23.2+canary.20261118T064620Z — 18 nov 2026 (`f7e2898aaefc8f967dbf7345e3999a65672fe60e`) — la capa Persistence (sesiones durables de subagentes que sobreviven al reinicio del gateway)
- v0.23.1+canary.20261114/15/16 — serie 0.23.1
- v0.23.2 (canary.20261117T064624Z)

## Contexto del ecosistema Hermes (19-20 nov 2026)

Nous Research anunció el 18 de noviembre la llegada de **Hermes Agent a Microsoft Teams, la Microsoft Store y Azure Container Apps Sandboxes**, junto con **Hermes Enterprise** (desplegable en el propio tenant de Azure del cliente) y la función **Collective Wisdom** (compartir skills revisadas dentro del equipo). Hermes Agent figura como el agente abierto público número uno en el ranking de OpenRouter y procesa cerca de 2 billones de tokens al día. La financiación de 90 M$ se anunció el 7 de octubre de 2026 (NVIDIA, M12 de Microsoft, Samsung, Robot Ventures, Union Square Ventures, Y Combinator, Menlo Ventures).
