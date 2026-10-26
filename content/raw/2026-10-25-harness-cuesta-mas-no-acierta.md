---
title: "¿Qué compra un harness? Tokens, sobre todo (Zhongyi Han, Shandong University)"
source: "https://arxiv.org/abs/2610.04433 | https://arxiv.org/html/2610.04433v1 | https://the-decoder.com/fancy-harnesses-make-coding-agents-more-expensive-but-not-better-study-finds | https://venturebeat.com/orchestration/a-coding-agents-harness-can-triple-its-cost-without-making-it-more-accurate-study-finds"
author: "Zhongyi Han et al., Shandong University"
date: 2026-10-24
captured: 2026-10-25
---

# What Does a Harness Buy? Tokens, Mostly.

## Pregunta y método

Un agente de código es un modelo envuelto en un harness: el system prompt, el conjunto de herramientas y las reglas de gestión de contexto. El estudio mide cuánto aporta realmente el harness **manteniendo el modelo constante**.

- Cinco (seis en algunas tablas) modelos a través de **tres harnesses de producción**: Claude Code (pesado), OpenCode (intermedio) y mini-SWE-agent (minimalista, ~100 líneas de Python, solo una herramienta Bash, sin gestión de contexto).
- Banco: **SWE-bench Verified**, con un conjunto principal de **447 tareas**.
- Control clave: se repiten las mismas configuraciones para calibrar cuánto se mueve una puntuación **cuando no cambia nada** salvo la ejecución.

## Resultado principal

> The answer to the title question is: not pass rate.

- En el conjunto de 447 tareas, Claude Code y mini-SWE-agent —el harness más pesado y el más ligero— quedan **a menos de dos puntos porcentuales** entre sí.
- El coste por tarea, con el mismo modelo, las mismas tareas y una única lista de precios, **difiere hasta 3×** entre harnesses.
- En GLM-5.3-Flash, un ensayo en Claude Code costó casi el doble que en mini-SWE-agent y **más de tres veces** que en OpenCode (aunque OpenCode también se detuvo tras menos llamadas al modelo).

## De dónde sale la factura

El coste lo determinan el system prompt fijo y los esquemas de herramientas, **reenviados en cada paso**:

| Harness        | Tokens en la primera llamada |
| -------------- | ---------------------------- |
| Claude Code    | 16.581                       |
| OpenCode       | 7.025                        |
| mini-SWE-agent | 829                          |

En términos monetarios citados: 1,81 CNY por tarea bajo Claude Code frente a 0,97 CNY bajo mini-SWE-agent.

## El ruido es mayor que la señal

Repetir configuraciones idénticas sobre SWE-bench Verified movió las puntuaciones entre **2,2 y 6,0 puntos porcentuales**, es decir, **más ancho que la mayoría de las diferencias harness-contra-harness medidas**. Ejemplos: Qwen3-...-A3B mejora +2,2 y +3,4 puntos en Claude Code y OpenCode respectivamente sobre dos ejecuciones, con aproximadamente tantas tareas que suben como que bajan; en mini-SWE-agent pierde 11 puntos (p = 0,04).

## Lectura

Cualquier leaderboard que mezcle harnesses sin reportar la varianza de reejecución está midiendo, en buena parte, ruido de muestreo. El harness no es gratis: se paga en tokens por paso, y en tareas de 40-150 pasos ese peaje se multiplica. Lo que un harness sí puede comprar es **fiabilidad operativa** (recuperación, gestión de contexto, herramientas especializadas), no puntos de precisión.
