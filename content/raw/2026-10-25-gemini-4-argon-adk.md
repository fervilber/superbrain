---
title: "Optimizar 205.000 líneas de Python durante la noche con Gemini 4 Argon (google/adk-python)"
source: "https://developers.googleblog.com/optimizing-a-200000-line-python-codebase-overnight-with-gemini-4-argon/ | https://www.infoq.com/news/2026/10/google-argon-optimizes-adk/"
author: "George Weale, Bo Yang, Andrew Biernat (Google Cloud)"
date: 2026-10-13
captured: 2026-10-25
---

# Optimizing a 200,000-line Python codebase overnight with Gemini 4 Argon

## Contexto del experimento

Los demos de lanzamiento muestran apps greenfield desde una carpeta vacía; no dicen nada sobre cómo trata el modelo un código existente. Google eligió un problema más duro: encontrar y arreglar cuellos de botella de rendimiento **entre archivos** en `google/adk-python` — ~205.000 líneas, ~800 archivos fuente, ~17.000 tests unitarios.

## Ronda 1: sin instrucciones de repositorio

Prompt único de un párrafo:

> Make ADK add no noticeable overhead to any agent: at startup, in long sessions, in multi-agent and workflow setups. Keep what the model receives and the public API unchanged, and back each change with a test that would catch a regression.

Dos horas. Argon escribió un script de benchmark a los 7 minutos, pasó **70 minutos midiendo y leyendo código antes de editar una sola línea** y encontró cuellos de botella reales en la copia de sesiones y en la importación de paquetes. Falló en las convenciones de mantenimiento: enganchó un hook a la autenticación alterando sutilmente el esquema JSON público, se le escaparon casos límite de eventos simulados en su copiador, ejecutó solo **216** tests cercanos y no incluyó números de benchmark en la descripción del PR.

## Ronda 2: `.agents/skills` + modo `/goal`

1. Las guías de mantenimiento entran en `.agents/skills`, "como una guía de onboarding para un ingeniero nuevo". Cada skill abre con un índice corto `SKILL.md` que apunta a archivos `references/` bajo demanda, para no inundar la ventana de contexto en cada turno. Al arrancar a las 21:11, Argon leyó `visibility.md` (regla de módulos privados con prefijo `_`) e `imports.md` (comprobaciones de carga diferida) antes de tocar código.
2. Modo `/goal` en Google Antigravity, que **preserva el objetivo a través de las compactaciones de contexto**. Se añadieron dos frases pidiendo un PR sin fusionar con números antes/después.

Prompt final:

> /goal Make ADK add no noticeable overhead to any agent: at startup, in long sessions, in multi-agent and workflow setups. Keep what the model receives and the public API unchanged, and back each change with a test that would catch a regression. Open one pull request against main that the ADK maintainers would approve, with before and after numbers in its description. Don't merge it.

## Comportamiento observado en 11 horas

- Leyó **12 archivos de guía** antes de tocar código.
- Corrió un benchmark de línea base sobre cuatro cargas: arranque de paquete, conversación de 200 pasos, app de test con 20 subagentes pasándose tareas y un workflow de 12 nodos, **30 veces cada uno**.
- Tres minutos antes de terminar seguía auditando su propio diff, detectó un bug en su propia caché multiagente y volvió a correr los **16.892** tests unitarios antes de parar por su cuenta.
- Hizo el trabajo transversal que un profiler no hace: rastrear cada llamador, objetivo de mock y referencia compartida en **40 archivos** para acelerar rutas sin romper apps existentes.

## Seis propuestas, dos aceptadas

**1. Filtrar el historial de sesión antes de copiarlo.** `InMemorySessionService` hacía deep-copy de toda la conversación en cada lectura antes de filtrar los eventos pedidos; incluso listar sesiones sin eventos copiaba todo primero. Argon filtra antes de copiar y reemplaza el deep-copy genérico de Pydantic por un copiador rápido y seguro ante ciclos que preserva diccionarios de estado compartidos y mocks de test.

**2. Cargar paquetes pesados solo cuando hacen falta.** `import google.adk` arrastraba módulos de audio/vídeo en vivo, trazas OpenTelemetry y servidores web (FastAPI, Starlette) incluso para un agente de texto. Borrar imports de nivel superior rompe tests que parchean atributos en módulos: al quitar tres imports en `llm_agent.py` pasaron los 16.892 tests públicos, pero fallaron **25 objetivos internos de Google** que parcheaban esos atributos exactos. La solución enviada usa _lazy module accessors_: los paquetes pesados cargan al primer uso y cada atributo público sigue siendo parcheable.

Las otras cuatro se rechazaron en revisión: una caché de eventos multiagente aceleraba 17 % un benchmark sintético pero dependía de una referencia débil que podía devolver datos obsoletos entre sesiones tras el GC; una comprobación de telemetría leía un atributo privado del tracer de OpenTelemetry; una reescritura del formateo de historial hacía más difícil de leer una ruta central sin mover la latencia en el benchmark _holdout_; y un índice para replays de eventos añadía complejidad de seguimiento de estado que solo ayudaba a tests sintéticos.

Resultado: **22 archivos** y **17 funciones de test nuevas**, fusionado en `main` con la nota de commit "Argon generated these changes."

## Números (benchmark holdout `bench_turn.py`, que Argon nunca vio)

- Preparación de sesión en sesiones largas: **−40 %**.
- Importación en frío de `google.adk`: **−21 %**.
- Tiempo de proceso nuevo hasta primera petición: plano (3,07 s → 3,09 s), porque los módulos diferidos cargan en el primer turno — recomendación: enviar una petición de calentamiento antes de recibir tráfico.
- Impacto compuesto: un run de **158 turnos** baja de **65,6 s a 56,1 s** (~10 s de overhead de framework puro).

Las tiendas de sesión externas (base de datos, SQLite, Gemini platform, Firestore, Redis) deserializan desde almacenamiento en lugar de hacer deep-copy en memoria, así que sus tiempos de lectura no cambian.
