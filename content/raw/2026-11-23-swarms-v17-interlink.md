---
title: "Swarms v17 'InterLink': canales de comunicación, fan-out por fases y RouteHub"
source: "https://www.swarms.ai/blog/swarms-v17-interlink-release"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# Swarms v17 'InterLink' (changelog técnico, 2 oct – 2 nov 2026)

InterLink es un mes de trabajo: 227 commits entre el 2 de octubre y el 2 de noviembre de 2026, sobre 271 ficheros, +15.729 / −13.395 líneas. Por primera vez en una release mayor, `swarms/` en sí menguó: +5.845 / −8.080, un neto de 2.235 líneas eliminadas mientras aterrizaban once módulos nuevos. `tests/` creció +8.378 / −960, y la suite pasó de 944 funciones de test a 1.130.

Zena (v14) hizo el framework observable. Akira (v15) lo hizo honesto. Overclock (v16) lo hizo medible y rápido. InterLink lo hace **conectado y ligero**.

## Los cinco hilos

**1. Canales (de ahí el nombre).** La conversación de un agente vivía solo en su propia memoria. Ahora cualquier `Agent`, y nueve estructuras, aceptan un `channel=`: un lugar donde leen lo dicho antes de una ejecución y publican lo que dicen después. Se envían **seis canales**: un fichero Markdown que puedes abrir mientras los agentes hablan, una cola sobre la que bloquea un hilo consumidor, una tabla SQLite segura entre procesos, un servidor HTTP remoto, un hilo de correo en tu propia bandeja y un hilo de AgentMail al que la gente puede responder desde su cliente de correo. Una segunda ejecución sobre un canal no vacío continúa donde lo dejó la primera.

**2. Velocidad de arranque.** `import swarms` tardaba 1,91 s; ahora tarda 0,28 (mediana de nueve procesos frescos en la misma máquina, v16 contra v17). Ya no carga litellm, RouteHub, mcp, networkx, OpenTelemetry, starlette ni sqlite3 hasta que algo los usa, no escribe nada en disco, y construir un `Agent` con límites fijados no abre ninguna conexión de red. Instalar `swarms[fast]` enruta las llamadas a modelos por RouteHub, lo que recorta la sobrecarga por llamada a más de la mitad y la memoria pico de ~220 MB a 100 MB.

**3. Concurrencia a ancho completo.** `ConcurrentWorkflow` ejecutaba como máximo 32 agentes a la vez y `GraphWorkflow` dimensionaba su pool a los núcleos de CPU, así que una capa de 100 nodos en un portátil de 12 núcleos corría en oleadas de 11. Ahora ambos ejecutan cada nodo a la vez por defecto: un fan-out de 100 nodos pasa de 2,04 s a 0,21 s, frente a 1,44 s de LangGraph en el mismo grafo.

**4. Respuestas, no transcripciones.** `Agent.run` devuelve toda la conversación bajo su `output_type` por defecto; siete estructuras y helpers dejan de devolver transcripciones donde querían respuestas.

**5. `PhasedFanOutWorkflow`.** Una estructura nueva para tareas cuya anchura solo conoces en tiempo de ejecución ("encuentra cada bug en estos ficheros y luego verifica cada uno", "lee cada contrato y haz que cada cláusula candidata se revise de forma independiente"):

```python
from swarms.structs.phased_fan_out_workflow import PhasedFanOutWorkflow
workflow = PhasedFanOutWorkflow(model_name="gpt-5.4", worker_model_name="gpt-5.4-mini")
print(workflow.run("Find every bug in these files and verify each one: ..."))
workflow.last_plan   # el WorkflowPlan que escribió el lead
workflow.last_run    # salidas por paso, fallos, número de agentes
workflow.usage       # tokens del proveedor sobre el lead y cada worker
```

Funciona en cuatro etapas:

1. **Plan.** El lead devuelve un `WorkflowPlan` como JSON: agentes inline, fases de pasos y los pasos cuyas salidas quiere de vuelta. El plan es **datos, no código**, así que nada de lo que escribe el modelo se ejecuta.
2. **Validar.** Agentes desconocidos, referencias a pasos que no están en una fase anterior, `{item}` fuera de un fan-out, un `for_each` sobre un campo que el `output_schema` del paso fuente no declara como array, y el recuento estático de agentes, todo se comprueba antes de ejecutar nada. Un plan rechazado vuelve al lead con sus errores, hasta `max_plan_attempts`.
3. **Ejecutar.** Las fases corren en orden y los pasos de una fase en paralelo, acotados por `max_concurrent_agents`. Un paso `for_each` lanza un agente fresco por elemento de una lista que devolvió un paso anterior. Un fan-out que superase `max_agents` se detiene antes de que arranque ninguno de sus agentes.
4. **Combinar.** El lead lee solo las salidas solicitadas y escribe la respuesta.
