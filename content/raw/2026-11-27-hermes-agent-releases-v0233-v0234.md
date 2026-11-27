---
title: "Hermes Agent v0.23.3/v0.23.4: subagentes durables que sobreviven al reinicio, ventana de 7.918 commits y CVE-2026-130164 corregido"
source: "GitHub NousResearch/hermes-agent Releases"
date: 2026-11-25
captured: 2026-11-27T20:10:00+01:00
---

# Hermes Agent: releases v0.23.3 y v0.23.4

URL: https://github.com/NousResearch/hermes-agent/releases

## Hermes Agent canary canary.20261125T064800Z-v0.23.4

**Fecha de publicación:** 25 de noviembre de 2026.

### Ventana de cambios

Medida en el commit `ae2a81ccc00`, la ventana desde v0.23.1 contiene **7.918 commits no-merge** sobre **5.211 ficheros cambiados** (+239.733 / −22.788), **1.989 pull requests mergeados** y **940 issues cerrados**.

También en la ventana, deliberadamente sin documentar aquí: **subagentes durables que sobreviven a un reinicio o caída del gateway** y pueden continuarse en su propia conversación, un **reloj de caché de prompt por sesión**, `hermes fallback check` para la preparación de la cadena de fallback, `hermes update --force` para detener gateways de inmediato en lugar de drenarlos, códigos de **browser_vault** de un solo uso introducidos desde Telegram y Discord, hilos de DM de Telegram compartidos opt-in, la **Gemini Interactions API** por defecto para Gemini 3 y posteriores más Gemini 4 Carbon, **fast mode** para Claude Mythos 5.2, opciones de cron por trabajo (`wrap_response`, un hilo nuevo por ejecución), nuevas APIs de plugin (`ctx.fork_session`, `ctx.redact_text()`, `ctx.register_idle_task`), shims de compatibilidad para que las actualizaciones funcionen a través de movimientos de módulos, un bundle de macOS más ligero que instala Chromium en el primer uso, y un lote grande de nuevas entradas del catálogo de plugins.

Las notas de release curadas completas de esta ventana salen con **v0.24.0**, que documentará todo desde v0.23.0 en adelante —destacados, áreas de funcionalidad y créditos completos de contribuidores—. Nada en esta ventana se omite.

### Corregido en el release candidate

- Los chats de Desktop creados por una compilación de agosto con un proveedor `custom` desnudo pueden enviar de nuevo tras actualizar (#156545).
- Una respuesta de Desktop o TUI que hacía streaming junto a una llamada de todo o memoria ahora se asienta en lugar de dejar el botón Stop arriba (#156553).
- Una caída a mitad de stream en Telegram y otros chats con streaming por edición ya no muestra una «Recovered reply» duplicada; una palabra que sostiene un prefijo de clave a mitad de palabra (`program_id`) se muestra a tiempo de nuevo (#156546).
- Desktop ya no pierde ni desordena lo que escribes mientras arranca y reanuda tu último chat (#156615, #156642).
- Tras una reconexión a mitad de respuesta, Desktop muestra la respuesta una vez y completa, adjuntos incluidos (#156611).
- En la Webapp, abrir agentes de Hermes Cloud cuando esta instalación no tiene sesión iniciada en Nous Portal ahora te dice que inicies sesión en Nous Portal en lugar de enviarte al login de la Webapp (#156652).
- Salir del CLI mientras su comprobación de actualización de arranque espera a GitHub ya no deja `git` corriendo (#156616).

### Seguridad

- Corrige **GHSA-p22p-9ph6-gmrh** (**CVE-2026-130164**, **Alta**): cuando Bot Desktop corre dentro de un backend de terminal `docker` o `ssh`, su fichero `env` de pantalla ahora está en lista de permitidos y validado, y los valores de una pantalla alojada en el backend ya no se mezclan en procesos iniciados en la máquina del agente (#154487).

### Actualización

- App de Microsoft Store: se actualiza por la Store.
- App de Desktop instalada desde el instalador (.exe / .dmg): sin cambios en este release; se actualiza con el siguiente release empaquetado.
- CLI: `hermes update`, o re-ejecutar el one-liner del instalador.
- Docker / Hermes Cloud: `nousresearch/hermes-agent:stable` (o `:latest`).

## Canaries previos en la ventana

- **canary.20261125T064800Z-v0.23.4** (25 de noviembre de 2026): smoke de instalación pasado en macOS DMG + ZIP (arm64), Windows MSIX (arm64) y Windows MSIX (x64). El catálogo de plugins recibe decenas de entradas nuevas: SolverForge Workbench, chinadoccheck, phone-bud, hermes-warden 0.1.6, igni, AgentRouter, 0g-provider, olostep, deapi-provider, memory-fit, AirPrompter (MCP alojado), senpi 0.5.1, gpu-monitor, hermes-declines, crowdwisdom-mcp, allscale, venice, palisade (MCP alojado), linux-notify, bf16-provider, agentinbox, bark (push iOS), gmat-mx (MCP alojado), offline-zim, trismegistus, ficelle-compression, delegation-gate, vaultwarden-secret-source, repeat-pause, run-receipts, right-suite, hermes-wavespeed, fastpath (dieta de contexto), galaxymem, hermes-roi, entre otros.
- **canary.20261124T064706Z-v0.23.3**: canary intermedio.
