---
title: "Learning to Steer LLM Agents and Multi-Agent Systems (arXiv 2610.22316) — captura"
source: "https://arxiv.org/html/2610.22316v1"
date: 2026-10-28
captured: 2026-10-31
---

# Learning to Steer LLM Agents and Multi-Agent Systems

> Captura del abstract, la introducción y las secciones 2–3 del preprint (arXiv:2610.22316v1), más los resultados destacados de la sección 4 y apéndice B recuperados de la versión HTML.

## Abstract

Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to **deviating from the overall goal** as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed **_goal drift_**. In this work, we propose a **steering agent** that supervises execution on the fly and steers the system back on track when drift occurs. The steering agent observes the execution context, deciding **when to intervene with a low-cost fast path** and **how to intervene with a high-cost slow path**. To unlock its steering intelligence, the ability to assess goal drift and generate effective interventions, we **jointly train the two paths with reinforcement learning**, combining a **pairwise ranking objective** with **group-relative policy optimization (GRPO)**. Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency. The learned steering intelligence **generalizes to out-of-domain tasks, transfers to unseen executors, and supports controllable intervention frequency without retraining**.

## 1. Introducción

- El fallo: _goal drift_, donde "agents deviate from the overall goal as execution unfolds". "A single agent may persist along an unproductive chain of actions, while an agent in a MAS may prioritize its local objective over the collective goal." El drift "can waste execution resources and lead to undesired outcomes, even when individual actions appear locally reasonable".
- Las defensas actuales son **planificación y verificación** (Claude Code, Codex). Pero "a plan does not ensure reliable execution", y "verification may uncover deviations after substantial effort has already been spent", con remediación post-hoc que puede llevar a consecuencias irreversibles y reintentos costosos.
- La propuesta: **supervisión en vuelo (on-the-fly supervision)**, donde un agente externo monitoriza la ejecución y devuelve el sistema a su objetivo cuando ocurre el drift, **complementando** (no sustituyendo) planificación y verificación.
- Fundamento conceptual: supervisión directa en organizaciones (Mintzberg, 1979), control supervisor de sistemas automatizados (Sheridan, 1992) y monitorización y control metacognitivos en la cognición humana (Nelson & Narens, 1990).
- Diseño de dos velocidades (Kahneman, 2011): el **fast path** estima la prioridad de intervención con una predicción de un solo token; **un umbral sobre esa prioridad controla la activación del slow path**, que usa razonamiento más costoso para generar acciones de corrección. "By separating fast judgment from deliberative generation, this design balances monitoring efficiency and steering effectiveness."

## 2. Trabajo relacionado y posicionamiento

- A diferencia del RL agéntico de horizonte largo (que optimiza el propio ejecutor, con rollouts computacionalmente caros) y del RL multi-agente conjunto, **aquí se mantienen congelados los LLM que ejecutan la tarea y se entrena un agente externo** para supervisar y corregir.
- Frente a trabajos centrados sólo en **detección** de errores o en corrección fácil (SupervisorAgent: errores y acciones repetitivas), el _goal drift_ "is more challenging to detect and correct in real time, **as it emerges gradually from locally plausible actions**".

## 3. Método

- **Espacio de observación** que expone al agente de dirección el objetivo de la tarea y el contexto de ejecución del sistema. "During execution, each observation update triggers a decision about whether and, if needed, how to intervene."
- **Entrenamiento conjunto de los dos caminos con RL**: objetivo de **ranking por pares** (Burges et al., 2005) para el juicio del fast path, y **GRPO** (Shao et al., 2024) para la generación de acciones del slow path.
- En el escenario de un solo agente, los slots de prompt incluyen la pregunta, el historial de acciones renderizado, el contador de acciones con el presupuesto restante de turnos y una línea con las acciones legales actuales del ejecutor. Una nota comprometida se inyecta en el prompt del ejecutor bajo el encabezado: **"A steering supervisor has reviewed your progress and left a note for your next action (follow the note):"**.
- En multi-agente, los slots llevan la tarea, el pipeline renderizado, los handoffs ya entregados, la submission bajo revisión con remitente y destinatarios, y cualquier feedback de rechazo ya emitido en ese handoff.

## Resultados (sección 4 y apéndice B)

- **Un solo agente**: a lo largo de siete benchmarks de question-answering, la dirección _zero-shot_ rinde sólo **+1.84 puntos**, mientras que el agente de dirección **optimizado con RL mejora el rendimiento en +6.66 puntos con sólo 0.93 acciones de dirección por tarea**.
- La inteligencia de dirección **generaliza a tareas fuera de dominio, transfiere a ejecutores no vistos y soporta frecuencia de intervención controlable sin reentrenamiento**: dirigir a la frecuencia más alta eleva la ganancia a **+17.11 puntos**.
- **Multi-agente**: se introduce el agente de dirección en un **sistema de cinco roles** (Xu et al., 2026). "In this more challenging steering task, where **zero-shot supervision degrades performance**, the RL-trained steering agent achieves a **gain of 5.34 points**."
- Con LLM-as-a-Judge, el mismo patrón: "RL raises the gain of steering from **1.60 to 6.77** points"; las tablas de ablación muestran `w/ RL` 53.86 frente a `w/ Filtered BC` 49.29 y frente al baseline.

## Contribuciones declaradas

1. Caracterizar el _goal drift_ en sistemas de uno y varios agentes, donde objetivos locales desplazan al objetivo global, y motivar la supervisión en vuelo.
2. Desarrollar un agente de dirección con **juicio rápido de intervención y generación deliberativa de acciones**, mejorado mediante RL.
3. Experimentos en ambos escenarios que demuestran ganancias de rendimiento, generalización, transferibilidad y controlabilidad.
