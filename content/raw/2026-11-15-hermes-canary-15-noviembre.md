---
title: "Hermes Agent canary v0.23.1+canary.20261115T064406Z y release candidate rc.5-v0.23.2"
source: "https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.1%2Bcanary.20261115T064406Z"
date: 2026-11-15
captured: 2026-11-15
---

# Hermes Agent v0.23.1+canary.20261115T064406Z (canal canary, 15 de noviembre de 2026)

Fuente: GitHub Releases de NousResearch/hermes-agent. Publicado: 2026-11-15T07:52:37Z. Autor: github-actions[bot]. Pre-release: sí.

## Estado del build (verbatim)

> **Release Date:** November 15, 2026

Descargas: macOS Apple Silicon (M-series) DMG, Windows x86 (64-bit) MSIX, Windows ARM (arm64/aarch64) MSIX. Los bundles de Linux están deshabilitados; los envelopes de Store sin firmar no pasan el smoke de instalación.

| Paquetes                | Smoke status |
| ----------------------- | ------------ |
| macOS DMG + ZIP (arm64) | Passed       |
| Windows MSIX (arm64)    | Passed       |
| Windows MSIX (x64)      | Passed       |

## Novedades (features del canary, verbatim, selección)

- Plugin "dosbox-mcp" (`4c02a304`) — @shakeyourbunny
- hermes-eye-memory añadido al catálogo de plugins (`e71d2da7`)
- plugin-catalog: añade permission-tiers (`c2779be8`)
- plugin-catalog: añade neuralwatt-provider (`5dcd3b55`)
- QMD Workspaces al catálogo (`09adb261`)
- Catálogo: Asset Curator (`36890962`)
- Catálogo: video-xray (banco de análisis de vídeo) (`57c44c75`)
- Catálogo: ascii-worlds a 1.4.0 (`56a81b86`)
- Catálogo: vibe-relay a 0.4.0 (`8f0e84b1`)
- plugin-catalog: progression 1.2.0 (marca un chat o subagente esperando entrada) (`9f75669b`)
- Catálogo: luminary (proveedor de memoria autoalojado) (`1f4a6b50`)
- Catálogo: Apple Health Data adapter (`5703eed4`)
- Catálogo: us-filings (`66cefccf`)
- Catálogo: modelscout a 0.3.11 (`61fadb96`)
- Hermes-hostd plugin configuration (`0e62767c`)
- Hive.yaml plugin configuration file (`a636863f`)

## Estado del canal de release (contexto)

- `v0.23.1` (10 nov) sigue siendo la última release estable: sube el tope del catálogo de plugins de 2 MiB a 16 MiB para que el `plugin-catalog.json` publicado vuelva a usarse (los clientes ≥ v0.23.0 lo aplican; los que se queden en v0.23.0 o anteriores siguen cayendo al catálogo empaquetado).
- `rc.5-v0.23.2` (publicado 2026-11-13T22:40:55Z, autor BearHuddleston) marca el quinto intento del release candidate de la v0.23.2, con `autopublish:false`. También aparece un tag `abandoned-rc.5-v0.23.2` del 14 nov.
- El canal canary publica builds diarios (06:44 UTC) con smoke de macOS y Windows; el de hoy (15 nov) es el primer canary tras el de ayer (14 nov, `20261114T064334Z`).

## Lectura

La v0.23.2 sigue en fase de release candidate (quinto intento, sin autopublish), mientras el catálogo de plugins crece con decenas de entradas nuevas por canary —memoria autoalojada, permisos por niveles, adaptadores de datos—. La superficie de extensión del agente se está poblando más rápido que el ciclo de release estable.
