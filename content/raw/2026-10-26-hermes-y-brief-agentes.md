---
title: "Hermes Agent v0.22.5 (delegación conectable) y breves de agentes de la semana del 19 al 25 de octubre de 2026"
source: "https://github.com/NousResearch/hermes-agent/releases | https://agentic.ai/news | https://nousresearch.com"
author: "Nous Research / Agentic.ai"
date: 2026-10-22
captured: 2026-10-26
---

# Captura: Hermes Agent 0.22.5 y breves de agentes

> Captura por extractos verbatim de las notas de release de Hermes Agent y del agregador Agentic.ai (semana del 19 al 25 de octubre de 2026).

## Hermes Agent v0.22.5

**Fecha de release:** 22 de octubre de 2026 (publicada el 23 de octubre, 05:28). Commit `bf0203a794a07aac3ff764972ab9087baa4e4f4e`.

> "Patch release. This tag rolls up the ~81 PRs merged since v0.22.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.23.0."

Métricas de la ventana desde v0.22.4 (medidas en el commit `bf0203a794a`): **231 commits no-merge**, **804 archivos cambiados** (+35.212 / −17.885), **81 PRs fusionados**, **30 issues cerrados**.

Cambios de la ventana (intencionalmente no documentados en detalle en esta release):

- **Nous sign-in reworkeado**: todo inicio de sesión es el device login simple; el invitado de free-tier cede a la cuenta; el resultado muestra quién inició sesión; los conectores ofrecen iniciar sesión en vez de abrir un invitado.
- `hermes update` retiene un release estable que se niega a instalar, en lugar de ofrecerlo.
- Windows: `hermes update` ya no se queda atascado en el launcher antiguo tras un repin de Python.
- **Soporte de planes por ventana de uso** (gauges de plan, tarjetas de límite y recuperación al cambiar de modelo para planes basados en ventanas).
- **Backends de delegación conectables**: enrutar subagentes por mapa de modelos o por perfil, **conmutable por sesión**.
- **Comandos slash de plugin que pueden pedir al usuario elegir una opción.**
- `hermes import-agent`; migración desde OpenClaw; **`hermes mcp serve` y el backend Singularity salen del core a plugins** (el setup ofrece el importador cuando encuentra otro agente).
- Drag-to-pin en la barra lateral de Desktop; instalación de plugins en un clic con badges de tier; salto a **Electron 44** y **Pillow 13**; un lote de bumps de seguridad de dependencias.
- Mensaje claro cuando la carpeta de trabajo de un chat ha desaparecido.
- `hermes update` recupera gateways pausados tras un `.git` dañado.
- Respuestas largas de Claude DirectSDK ya no se cortan por el temporizador de estancamiento.
- Chats de grupo en Desktop vuelven a mostrar qué bot está trabajando.
- Cliente experimental de eventos MCP en modo webhook.

Actualización: app de Microsoft Store vía la Store; app Desktop instalada desde el instalador, sin cambios en esta release; CLI con `hermes update` o re-ejecutando el instalador; Docker / Hermes Cloud con `nousresearch/hermes-agent:stable` (o `:latest`).

## Contexto de la línea 0.22.x (v0.22.3, 21 de octubre)

Ventana desde v0.22.2 medida en `5b147ab036d`: **2.911 commits no-merge**, **4.206 archivos** (+360.278 / −64.308), ~**620 PRs**, **326 issues cerrados**. Incluye, entre otros:

- **Notificaciones de progreso MCP transmitidas como progreso de herramienta en vivo.**
- Diseño clásico de CLI renovado (transcripción con glifos, línea de estado bajo el compositor, cabecera de dos líneas).
- **Clientes OAuth que los plugins declaran** y Hermes inicia sesión y refresca.
- `hermes plugins update` ofrece todas las actualizaciones disponibles; botón Update para plugins instalados por git en Desktop.
- **Steering y edición de un prompt en cola** desde Desktop.
- **Selector guiado de modelo y proveedor para subagentes** en Desktop.
- Fila de cuenta atrás `/loop` en vivo en CLI y TUI.
- Transferencia opt-in de temas en DMs de Telegram.
- Hook de plugin `post_compaction`.
- Catálogo de capacidades.
- Build de Microsoft Store publicada automáticamente al publicar un release.
- Auto-prune de sesiones vuelve a ser opt-in, con aviso único cuando se acaba el disco.
- **Nemotron 3.5 Bolt** y borradores DFlash de una ranura en el runtime local.

## v0.22.4 (21 de octubre, 13 PRs)

Desktop deja de mostrar "suggestion pills" sobre el compositor (aparecían sin motivo claro, empujando a configurar servidores MCP) y se eliminan los helpers que solo ellas usaban. Plugins que no instalan nada se saltan el paso de consentimiento de dependencias. Dashboard: WhatsApp se puede reemparejar con seguridad tras cerrar sesión. El chip de modo de aprobación sigue el modo del perfil activo. Nuevos en el catálogo de plugins: **`bubblewrap`** (backend de terminal bwrap en Linux), Singularity/Apptainer, **`mcp-serve`** (Hermes como servidor MCP), `agent-importers` (`hermes import-agent`, ahora con Cursor), `inbox` y `workflow-record` desde Hermes Labs. Telegram Business pasa al tier comunitario de Hermes Labs.

## Breves de agentes: semana del 19 al 25 de octubre de 2026 (Agentic.ai)

- **19 oct — Blue Language Labs lanza MyOS Business** en Money20/20 USA (Las Vegas): sistema operativo para que los agentes coordinen trabajo comercial (pedidos, fulfillment, pago) entre empresas y sistemas. Los agentes actúan sobre acuerdos aceptados, con acciones auditables y personas en control.
- **19 oct — Axonius lanza AI Workforce** dentro de su Asset Cloud, con _virtual workers_ autónomos para tareas de remediación continuada; también salen a producción **AI Companion** y un **MCP Server**. El problema: los datos de activos están repartidos por muchas herramientas y los jobs predefinidos solo capturan condiciones anticipadas.
- **19 oct — Santander AI Lab, con apoyo de NVIDIA**, desarrolla métodos para **evaluar modelos y agentes para aplicaciones bancarias**, identificando modelos adecuados por tarea antes de un despliegue más amplio. El reporte no nombra las tareas bancarias ni cómo se mide qué modelo encaja mejor.
- **18 oct — PentestMCP** (Harbin University of Science and Technology e Intelligent Policing Key Laboratory de Sichuan): framework multiagente para **pruebas de penetración autónomas** que usa LLMs para buscar debilidades. El reporte describe capacidades, no sus controles de salvaguarda.
- **15 oct — DE-CIX lanza un servidor MCP open source** para gestión de red: agentes pueden buscar, procurar, desplegar y gestionar conexiones de red en lenguaje natural, y los ingenieros obtienen opciones de conectividad y estado de servicio en tiempo real.
- **7 oct — Estudio de Apple Machine Learning Research**: un único agente de código con acceso básico a shell **igualó o superó** a sistemas multiagente complejos en tareas autónomas de ML. El estudio desafía la tendencia a agentes que planifican, delegan y se critican entre sí.
- **7 oct — Vijil lanza DART** (_Diamond Adaptive Red Teaming for Agents_), que usa sus propios agentes adversarios para sondear sistemas objetivo. Vijil afirma encontrar hasta 1,5× más problemas que la alternativa líder, aunque el release no especifica qué problemas explican la diferencia.
- **Investigación — FHIR-AgentEval**: sandbox modular para evaluar agentes clínicos, con configuraciones que añaden memoria; aborda la complejidad de usar HL7 FHIR en flujos clínicos.

## Contexto de Nous Research

- Nous Research anunció una ronda de **90 millones de dólares** para "crear IA que sirva a la gente".
- Post de Teknium: **"Refactoring Hermes with 1,393 agents"** — Hermes Agent refactorizó su propio código: 1.393 subagentes durante unas diecinueve horas activas recortaron el Python no-test un **34,4 %**, por unos **19.300 USD** de gasto en modelos frente a una estimación de 150.000 USD a 1,8 M USD haciéndolo a mano.
- **22 oct**: Hermes Agent tiene un plugin oficial para **MeshyAI**; pide a Hermes que haga un cofre del tesoro de 70 millones de polígonos para Godot, o que convierta la foto de una taza en un modelo imprimible, y lo hace a través del servidor MCP de Meshy. En Hermes Desktop los modelos se renderizan en el chat, los personajes riggeados se animan en línea y una galería guarda cada modelo y prompt. En apps de mensajería, Hermes envía un vídeo de vista previa corto.
- **16 oct**: Hermes Agent es _launch partner_ de **RTX Spark** de NVIDIA en la nueva generación de portátiles.
