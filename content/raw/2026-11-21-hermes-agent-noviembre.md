---
title: "Hermes Agent: núcleo más pequeño, plugins separados y un benchmark propio (noviembre de 2026)"
source: "https://releasebot.io/updates/nousresearch/hermes-agent"
date: 2026-11-21
captured: 2026-11-21
---

# Hermes Agent en noviembre de 2026

Captura compuesta de `releasebot.io/updates/nousresearch/hermes-agent`,
`hermes-ai.net/news/hermes-agent`, `hermes-ai.net/changelog`, `nousresearch.com/press/hermes-enterprise-in-microsoft-teams`
y `benchlm.ai/agentic` (para el Hermes Index).

## 1. El núcleo se encoge: la modularización por plugins

Cambios de la ventana de noviembre:

- **`hermes mcp serve` se mueve al plugin oficial `mcp-serve`** (`hermes mcp-serve`).
- **`hermes import-agent` y la migración desde OpenClaw se mueven al plugin `agent-importers`.**
- `hermes setup` por primera vez ofrece **importar desde OpenClaw, Claude Code, Codex CLI o Cursor**
  cuando encuentra uno.
- **`hermes --cpu-profile PATH`**: escribe un perfil de CPU de cualquier ejecución de Hermes, más un
  resumen de texto de las funciones más costosas.
- **Backends de delegación conectables** y comandos slash interactivos de plugin.
- **Plan con ventana de uso** y **inicio de sesión simplificado en dispositivo Nous**.
- Recuperación de actualizaciones en CLI y Windows; los instaladores de escritorio esperan a la
  siguiente versión empaquetada.
- Carpeta **`~/.hermes/...`**: las imágenes Docker hornean un marcador de solo lectura
  (`/etc/hermes/image-provenance.json`) que identifica de forma autoritativa el sistema de ficheros como
  gestionado por imagen; `hermes update`, `hermes update --check` y el botón del dashboard lo consultan
  antes de tocar nada y, en una instalación gestionada por imagen, **se niegan limpiamente (código de
  salida 2)** e imprimen el comando real (`docker pull nousresearch/hermes-agent:latest`), escribiendo
  un recibo `refused` para que el tooling de flota vea que el intento ocurrió.
- Nix deja de ser una ruta de instalación soportada explícitamente (solo best-effort).

## 2. Versiones de la ventana

- **v0.22.7** (3 de noviembre de 2026) — actualización de parche en CLI, Microsoft Store, Docker y
  Hermes Cloud con colaboración en chat grupal, publicaciones de chat programadas, mejoras de flujo de
  trabajo y nuevas entradas del catálogo de plugins.
- **v0.23.2** — «Patch release. This tag rolls up the **1.989 PRs merged since v0.23.1** into a stable
  release para GitHub, Microsoft Store, Docker y Hermes Cloud. Full curated notes for this window ship
  with v0.24.0.» El mismo patrón de «rollup de parches con notas curadas diferidas» que ya apareció en
  informes anteriores.
- La release **Herald** añade voz conversacional natural, investigación anclada en fuentes, webhooks de
  sistema, **A2A**, plataforma de escritorio más fuerte y nuevos controles de CLI: streaming de voz con
  _barge-in_, palabras de activación y control manos libres; citas ancladas y verificación de hechos;
  webhooks salientes de ciclo de vida firmados; **A2A v1.0 para comunicación interoperable entre
  agentes**; artefactos de escritorio, SDK de plugins, entrada rápida y múltiples ventanas.
- El changelog incluye **GPT-6 Sol/Terra/Luna y Claude Opus 5.5 en los catálogos de Nous y OpenRouter**,
  además de integración de Blender Lab, plugins de NVIDIA y mejoras de rendimiento en rutas calientes.

## 3. Hermes Enterprise y el número que lo resume

> Nous Research, an M12 portfolio company and the team behind Hermes Agent, today announced that
> Hermes Agent is available in native Microsoft services for the enterprise. **Hermes Agent currently
> ranks number one among public open agents on OpenRouter, processing nearly 2 trillion tokens a
> day.** With Hermes Enterprise, every employee gets a managed, self-improving agent in the tools they
> already use, and the company gains shared intelligence that grows with every task.

- **Collective Wisdom**: las skills compartidas como activo privado de la organización («what one person
  figures out becomes shared intelligence the whole company can build on» — Dillon Rolnick, CEO).
- Aparición en Microsoft Ignite (17–20 de noviembre, San Francisco), sesión **BRK448** «Run secure agent
  loops in production with isolated sandboxes at scale», el 18 de noviembre.
- Para organizaciones con requisitos estrictos de residencia de datos, seguridad o compras, **Hermes
  Enterprise puede ejecutarse en el propio inquilino de Azure del cliente** con un modelo de producto y
  precios similar.

## 4. El Hermes Index: el harness medido, no solo el modelo

Del catálogo de benchmarks de BenchLM:

- **Hermes Index** — media de pass@1 sobre cuatro suites agénticas (**Hermes Bench, TerminalBench 4,
  TerminalBench Science y SkillsBench**), ejecutadas **dentro del harness de Hermes Agent** y reportadas
  con **coste medio por tarea**.
- **Hermes Bench** — **150 tareas en 25 categorías** que cubren skills de Hermes, investigación,
  diagramas y arte, memoria, uso de herramientas y seguridad. Cada agente arranca en un workspace con
  ficheros reales y **el grader comprueba lo que deja detrás**.

## 5. Otras capacidades documentadas del agente

Del sitio oficial y de guías de terceros: búsqueda web, automatización de navegador, visión, generación
de imágenes, texto a voz y razonamiento multimodelo; programación en lenguaje natural de informes,
copias de seguridad y briefings que se ejecutan desatendidos a través del gateway; **subagentes
aislados con sus propias conversaciones, terminales y scripts Python por RPC para pipelines de coste de
contexto cero**. Detener un agente local termina su proceso pero no borra conversaciones, memorias ni
skills guardadas.
