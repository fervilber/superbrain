---
title: "Anthropic: cuándo plegar los subagentes en el bucle principal (y el kit de migración)"
source: "https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop | https://github.com/anthropics/single-agent-loop-kit | https://the-decoder.com/anthropic-says-one-ai-agent-beats-many-subagents-now-that-models-can-handle-complexity-alone/"
author: "Anthropic Applied AI"
date: 2026-10-22
captured: 2026-10-25
---

# Building agents: When to fold subagents into your main agent loop

## Tesis

Usar menos subagentes a favor de contexto y herramientas con _divulgación progresiva_ puede mejorar la calidad y reducir coste y latencia. En comparaciones sobre varias implantaciones empresariales, **un solo agente con skills superó con frecuencia tanto al diseño de un único prompt para todo como al diseño de subagentes**, y a menudo con menor coste y latencia por tarea.

Advertencia central: muchas empresas dan a cada equipo o tipo de problema su propio subagente y la arquitectura termina siendo **una copia del organigrama** — ley de Conway aplicada a agentes. El resultado es un "Frankenprompt" donde cada equipo añade reglas al system prompt que acaban contradiciéndose.

## Cuándo siguen teniendo sentido los subagentes

1. Un solo bucle sufre degradación medible por **hinchazón de contexto**.
2. Hay tareas que deben correr **en paralelo con ventanas de contexto frescas** que se descartan al terminar.
3. El agente único **falla al elegir herramientas** o hay instrucciones en conflicto en el system prompt.

## Diseño objetivo del bucle único

- Un modelo, una ventana de contexto, un bucle de herramientas abierto, con límites (presupuesto de turnos y coste, _write gates_) fijados en el harness.
- Cada turno el modelo emite un lote de llamadas a herramienta; el harness las ejecuta en paralelo y devuelve resultados crudos al mismo modelo, que decide el siguiente paso.
- El modelo escribe su plan en contexto en el primer turno y lo revisa según llegan resultados: **quien planifica es quien ejecuta**, así que puede cambiar el plan a mitad de turno.
- El orden y el procedimiento de dominio se mueven a **skills**; los límites duros (validación, puertas de aprobación) y lo que surge a mitad de conversación (consulta de memoria) se mueven a **herramientas**.
- Se elimina el paso de código que reescribía el plan desde un catálogo de reglas.

## Evals

Un conjunto end-to-end compartido, propiedad de un equipo central, más conjuntos pequeños que cada equipo envía con su skill. **Diez ejemplos dorados bastan para empezar.** Mientras exista orquestador se mide también _routing accuracy_; tras plegar, se mide si el agente cargó la skill correcta o llamó a la herramienta correcta.

## Migración en cuatro pasos

1. **Measure** — puntuar el sistema tal como está hoy.
2. **Combine** — fusionar los subagentes que siempre corren juntos (los que encadenan salida, tocan los mismos datos o se llaman juntos con frecuencia).
3. **Fold** — convertir cada subagente restante en skill + herramientas del agente principal, **de uno en uno**, comparando contra la línea base.
4. **As tool** — conservar el subagente pero llamarlo como herramienta con resultado estructurado, para que el agente principal mantenga la conversación con el usuario.

Después, mantenimiento: un equipo pequeño es dueño del system prompt y del eval compartido; cada equipo de dominio es dueño de sus skills.

## Números citados

- En una comparación, la arquitectura de agente único corrió **aproximadamente el doble de rápido** que el montaje multiagente.
- Claude Code redujo su system prompt para modelos avanzados **más de un 80 %**, incluyendo recortes ligados a la divulgación progresiva de skills y herramientas.
- La selección de herramientas se degrada por encima de **30-50 definiciones** de herramienta en el system prompt.
- Modelos desde Opus 4.5 (y Opus 5.5, Fable 5.1) gestionan planes complejos en un solo bucle; en Opus 5.5 no se puede desactivar el pensamiento.

## Riesgo documentado del plegado

En una prueba con un agente de soporte, plegar un subagente redujo la latencia **pero rompió un proceso que antes pasaba**: el agente principal tenía la herramienta de consulta de pedidos y respondió por su cuenta sin preguntar al especialista de envíos por la fecha de entrega. La rotura solo apareció en **una de dos ejecuciones** — de ahí la insistencia en repetir cada tarea del eval y revisar qué tareas cambiaron de resultado, no solo la puntuación final.

## Contenido del kit (`anthropics/single-agent-loop-kit`)

- `skill/SKILL.md` — puerta de entrada; apunta a un archivo de paso cada vez.
- `steps/00-audit.md` — inventario de cada subagente con veredicto: plegar, fusionar, llamar como herramienta o conservar.
- `steps/01-baseline.md` — reutilizar evals existentes, rellenar huecos o construir uno.
- `steps/02-merge.md`, `steps/03-fold.md`, `steps/04-as-tool.md`, `steps/05-upkeep.md`.
- `scripts/coupling_map.py` — desde un export de trazas: qué subagentes llevan el tráfico y cuáles corren juntos.
- `scripts/compare.py` — dos ejecuciones de eval lado a lado: finalización, latencia, llamadas al modelo, tokens, coste.
- `scripts/chain_coverage.py` — verifica que el eval tiene una tarea por cada cadena de subagentes que producción usa.
- `scripts/estimate.py` — estimación de tokens para la siguiente ejecución de eval.
- `reference_loop/loop.py` — bucle de agente único mínimo: lotes de herramientas en paralelo, skills bajo demanda, búsqueda de herramientas, presupuestos, _write gate_, verificador opcional.
- `examples/support-desk/` — ejemplo ejecutable antes (`app/`) y después (`single_loop/`).

El kit se detiene en puntos fijos: tras la auditoría, antes de cualquier ejecución de pago, tras la línea base y tras cada cambio. Antes de una ejecución de pago incluye estimación de tokens. Está marcado como implementación de referencia, sin mantenimiento.
