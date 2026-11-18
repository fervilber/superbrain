---
title: "Hermes Agent canary v0.23.2+canary.20261118T064620Z: soporte de GPT-6.2 y capa de persistencia en curso"
source: "https://github.com/nousresearch/hermes-agent/releases"
date: 2026-11-18
captured: 2026-11-18
---

# Hermes Agent — canary del 18 de noviembre de 2026 (Nous Research)

## Release

- **Tag:** `v0.23.2+canary.20261118T064620Z`
- **Fecha:** 18 de noviembre de 2026 (publicado a las 07:55)
- Release inmutable: solo el título y las notas pueden modificarse.

## Descargas

**Hermes Desktop:** macOS Apple Silicon (M-series) DMG; Windows x86 (64-bit) MSIX; Windows ARM (arm64/aarch64) MSIX. Los _bundles_ de Linux están deshabilitados.

Estado de _smoke_ de instalación/chat nativo:

| Paquetes                | Estado |
| ----------------------- | ------ |
| macOS DMG + ZIP (arm64) | Passed |
| Windows MSIX (arm64)    | Passed |
| Windows MSIX (x64)      | Passed |

La disponibilidad de descarga es independiente del estado de _smoke_.

## Novedades destacadas (features)

- **Modelos:** soporte de **GPT-6.2 Astra y Sol** (`786314ce`) — @vortexopenclaw.
- **image_gen:** **GPT Image 2.6 Flare y Sunburst** se unen al catálogo de FAL (`8f2c6064`).
- **Plugin-catalog:** incorporaciones de `barrier-shield`, `chaos-takens`, `eigen` (`4841eebc`), `axiom` (verificador neural-simbólico de leyes de conservación y SMT) (`2bff853a`), `safari`, `relatedb-memory`, `scansift`, `covsift`, `sound-cut`, `lazybird`, `hermes-voice-gateway`, `hermes-axiom-coach` y `sleek`, además de un **paquete de idioma ucraniano** (`593f35c6`).
- **hermes-safeguard:** configuración del plugin (`781cc939`) — @robberdom.
- **Capa de persistencia (Persistence):** serie de commits de @yoniebans que introducen la interfaz de almacenamiento —registros centrales, errores, alcance de perfil y vista _awaitable_ (`4a66e4b1`)— y las operaciones sobre ella: almacenamiento de conversación (`f1fd5674`), autoridad y enlace de sesión (`516f3c31`), enrutado y entrega del gateway (`db2296e1`), ejecución de workers y libro de delegación (`d333146d`), y operaciones de _housekeeping_ y mantenimiento (`84035b4c`).
- **session_rules:** reglas de sesión puras compartidas entre llamantes y backends (`5bf76580`) — @yoniebans.

## Lectura

El canary del 18 de noviembre es, sobre todo, trabajo de cimientos: la serie de **Persistence** formaliza una interfaz de almacenamiento única con operaciones separadas por dominio (conversación, sesión, gateway, workers/delegación, mantenimiento), lo que apunta a un **plano de persistencia unificado** para sesiones, delegación y entrega. Esto conecta directamente con la línea del informe del 17 de noviembre sobre **subagentes durables que sobreviven al reinicio del gateway**: la persistencia no es solo guardar conversaciones, es poder reconstruir la autoridad y el enrutado tras un fallo. En superficie, el canary añade soporte para **GPT-6.2 Astra/Sol** y amplía el catálogo de plugins y el paquete de idioma ucraniano.
