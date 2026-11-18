---
title: "Vercel eve 1.0 GA: sesiones multijugador, modo ambiente y agentes multiinquilino"
source: "https://vercel.com/blog/eve-is-now-generally-available"
date: 2026-11-18
captured: 2026-11-18
---

# Vercel eve 1.0 (17 de noviembre de 2026)

## Qué es eve

eve es el framework **open source (Apache 2.0)** de Vercel para construir agentes de producción. Un agente en eve es un **directorio de ficheros**: uno para el modelo, un _system prompt_ en Markdown, y un fichero TypeScript por herramienta. Alcanzó el 1.0 tras una _preview_ pública iniciada en junio, con **más de 230 releases** y miles de pull requests fusionados.

Vercel describe eve como «el arnés que posees»: el _harness_ es el bucle que llama a modelos, ejecuta herramientas y delega trabajo a subagentes. El desarrollador elige el modelo, añade o reemplaza herramientas, edita instrucciones y decide qué acciones requieren aprobación. El **Workflow SDK** de código abierto guarda el progreso mientras el agente corre, de modo que puede reanudar desde el último paso completado tras un _crash_. Las sesiones multijugador y las llamadas agente-a-agente están integradas.

## Novedades del GA respecto a la preview

- **Sesiones multijugador (multiplayer sessions):** varias personas trabajan con un agente en una única sesión compartida. eve registra quién dijo qué y dirige las aprobaciones y los inicios de sesión a la persona correcta. En el canal nativo de Slack, cada _thread_ es una sesión compartida; las aprobaciones aparecen como botones que solo la persona correcta puede responder, y una tarjeta de tarea en vivo muestra progreso y tiempos. Se puede configurar memoria por usuario o para todo el equipo.
- **Modo ambiente (ambient mode):** un agente puede escuchar en canales elegidos y decidir por sí mismo cuándo hablar. Un modelo de decisión pequeño filtra primero los mensajes para contener costes.
- **Agentes multiinquilino (multi-tenant agents):** memoria, credenciales de conexión y políticas de aprobación se pueden acotar por inquilino o por usuario. Las herramientas, skills e instrucciones se cargan dinámicamente antes de cada llamada al modelo.
- **Memoria integrada:** memoria nativa entre sesiones vía `fileMemory` (en memoria durante `eve dev`, un almacén privado de Vercel Blob en Vercel) o un proveedor externo.
- **Trazado OpenTelemetry:** las trazas muestran esperas en humanos, aprobaciones, elecciones de modelo, uso y coste. Las conversaciones de producción privadas envían solo metadatos por defecto.
- **Extensiones:** herramientas, skills, canales, horarios y hooks se empaquetan y comparten entre agentes (`npx eve@latest extension init`).
- **Workflow tools:** `defineWorkflowTool` convierte las herramientas propias en tareas de fondo durables que pueden esperar a personas, webhooks o temporizadores y sobrevivir a reinicios.
- **Integraciones:** Next.js, Nuxt, SvelteKit, TanStack Start y Vite. Los agentes son accesibles desde Slack, Microsoft Teams, Discord, Telegram, GitHub, Linear, iMessage y más, además de cualquier adaptador de Chat SDK.
- eve corre sobre **Workflow SDK 5.5** y sigue _semantic versioning_ desde 1.0, con guía de actualización para usuarios de la preview.

## Casos en producción citados

- **Rillet** construyó una «fábrica de software» sobre eve que recibe peticiones de clientes, las convierte en especificaciones, prueba los cambios y abre PRs para revisión humana; triplicó su ritmo de entrega en tres meses.
- **Clay** construyó _monty_, un agente de datos que responde preguntas de empleados en Slack; en poco más de dos meses, entre el 30% y el 40% de la empresa lo usaba cada semana.
- **Mitchell Hashimoto** lo cita como la mejor solución para agentes de backend durables.

## Implicación

eve 1.0 empuja tres ideas a producción: (1) el **harness es tuyo y es código revisable**; (2) la **durabilidad** (Workflow SDK, `defineWorkflowTool`) es una propiedad de primera clase, no un añadido; y (3) la **colaboración humano-agente** se modela explícitamente con sesiones multijugador, aprobaciones dirigidas y multiinquilinato. Es la misma dirección que Devin Bots, Replit Missions y Durable Task: el agente como trabajador persistente dentro de una organización, no como chatbot de un solo turno.
