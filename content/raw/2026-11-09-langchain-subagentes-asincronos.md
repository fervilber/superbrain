---
title: "Captura: LangChain — los agentes se vuelven asíncronos (subagentes en segundo plano)"
source: "https://www.langchain.com/blog/agents-are-going-async"
date: 2026-11-05
captured: 2026-11-09T20:08:00+01:00
---

# Agents Are Going Async

Sydney Runkle, Thushanth Bengre · November 5, 2026 · LangChain

## Key Takeaways

- As agents take on bigger goals, they need to stay responsive to the user while making progress on many long tasks at once.
- Async subagents split an agent into an orchestrator that stays available to the user and subagents that run tasks in the background and report back to the orchestrator upon completion.
- Background work is becoming the norm for agent infrastructure, from coding agents like Claude Code to personal agents like OpenAI's dots.

Imagine a chief of staff who disappears every time you hand them a big project and only comes back once it's done. You'd probably fire them immediately. A good chief of staff keeps projects moving in the background while staying reachable and keeping you updated along the way. As we ask agents to work toward bigger goals, they need the same two properties. An agent has to be responsive, acting on a new instruction right away with the context of everything before it, and productive, making progress on many large tasks at once.

The architecture we've used to build agents for a while can't meet both requirements. In a standard ReAct loop, each long tool call blocks the loop and every other task queues behind it. Instead, we're seeing the ecosystem converge on a split between one agent that stays with the user and background workers that do the long work. Claude Code runs subagents in the background by default, OpenAI's dots hand work to background workers to make progress on several things at once, and DeepSeek Harness built its super agent around a router that talks to people and background workers that run tasks in parallel.

We're bringing this pattern to Deep Agents with async subagents. An orchestrator stays available to the user and keeps the conversation's context organized, while async subagents run as background workers and report back when they finish. The amount of work the agent can take on then grows with the number of background workers instead of the length of one loop.

## How async subagents work

An agent runs in a loop. The model calls a tool, waits for the result, and decides what to do next. Historically, tools and subagents blocked that loop until they returned, like code that awaits each slow call in turn. An async subagent works like a task started with `asyncio.create_task` or a `Promise` you don't await yet. The call returns right away, the work runs independently in the background, and the result comes back later.

The orchestrator hands work to async subagents and stays free to talk to the user.

Async work depends on two properties of the system:

- **The user can reach the orchestrator.** The orchestrator is the agent the user interacts directly with. Subagents no longer hold its loop, so the user can reach it whenever its own loop isn't busy, instead of waiting for every subagent to finish.
- **Tasks run in parallel without blocking.** The orchestrator starts subagents as work comes in, instead of waiting for a whole batch to return.

## Notas de estado (de búsquedas dirigidas)

- Disponible en Deep Agents (Python y JavaScript) activándolo con un único campo `"async": True`. El orquestador recibe herramientas para iniciar, comprobar, actualizar, cancelar y listar tareas en segundo plano; cada tarea pendiente aparece listada en el prompt de sistema del orquestador y puede consultarse vía `check_async_task`. Un orquestador ocupado recoge resultados a mitad de ejecución; uno inactivo se despierta con una nueva ejecución; uno pausado en una aprobación la mantiene intacta hasta que el usuario responde. Las notificaciones de tareas están en beta.
- El patrón coincide con la separación planificador/ejecutor de Muse Ember y con la durabilidad de Mistral: todos parten el bucle monolítico ReAct.
