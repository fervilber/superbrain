---
title: "Agensh: escalar la inteligencia organizacional a 1.024 agentes (Microsoft Research)"
source: "https://arxiv.org/abs/2609.26781 | https://github.com/microsoft/Agensh | https://agens-harness.github.io/project/ | https://www.marktechpost.com/2026/10/24/microsoft-agensh-multi-agent-harness-1024-agents/"
author: "Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei (Microsoft Research)"
date: 2026-10-24
captured: 2026-10-25
---

# Agensh: Scaling Organizational Intelligence to 1,024 Agents

## Abstract (verbatim)

> A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers. To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, continuously gathering context, claiming and self-assigning sub-tasks, taking action and sharing findings, verifying results, and merging progress in an asynchronous manner. The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions. To test the scalability of Agensh, we evaluate it on the five hardest ProgramBench tasks with GPT-5.6-sol (high). Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement. Larger organizations reach comparable test-pass rates earlier. On pandoc, scaling from 1 to 1,024 agents raises the final test-pass rate from 33.89% to 55.06%. Worker trajectories further show that different forms of self-organized cooperation gradually emerges and standardizes as the organization grows. These results reveal the number of agents as a new scaling dimension for multi-agent organizations to expand the frontier of general intelligence, offering a practical solution for complex tasks under hard latency constraints or time budgets.

## Infraestructura de organización

Tres componentes, deliberadamente aburridos:

- **Workspace compartido** (Gitea): issue #1 es la tarea; cada worker abre sus propios issues para las áreas que reclama y los PRs transportan el trabajo. Dirección interna `http://gitea:3000`.
- **Interfaz de mensajes** (Mattermost): canal `pbench-task` para lo general; mensaje directo para colisiones inminentes, porque un DM interrumpe al par _dentro de su turno actual_.
- **Contexto compartido** (tablero append-only, adaptado de DeLM): entradas de 100 caracteres (300 para `PATCH_SUMMARY`), con tipos `OBSERVED`, `FACT`, `FAIL`, `CLAIM`, `PATCH_SUMMARY`. El tablero se renderiza en el prompt de cada worker bajo `==== SHARED CONTEXT ====` y lo que un par escribe después llega **a mitad de turno**, anexado al resultado de herramienta que el worker estaba esperando. `board_read` devuelve las últimas 2.000 entradas; `board_grep` busca sobre todo el historial con `,` como OR y `&` como AND.

## Bucle de cooperación (5 pasos, todos asíncronos)

1. **Gather context** — lee objetivo compartido, estado, progreso de pares, mensajes y hallazgos acumulados.
2. **Claim sub-task** — propone una subtarea y anuncia su alcance como `CLAIM` en el contexto compartido; las superposiciones se resuelven por DM.
3. **Take action** — trabaja localmente con las herramientas disponibles y publica hallazgos intermedios.
4. **Verify results** — contrasta contra criterios de aceptación de la subtarea; itera hasta cumplirlos.
5. **Merge progress** — fusiona en el workspace compartido y publica qué cambió, la idea subyacente y la evidencia de verificación. Si hay conflicto, incorpora el progreso del par y reintenta.

"Agensh is an organization harness layered above a single-agent harness rather than a replacement for it." El harness subyacente (Copilot) mantiene estado conversacional, invoca el modelo y ejecuta herramientas; Agensh añade identidad de worker, protocolos de cooperación, enrutado de eventos, dispatch robusto, acceso al workspace, mensajería, contexto compartido y mecanismos de recuperación y liveness.

## Resultados (ProgramBench, 6 h, sin Internet)

Cinco tareas más difíciles: FFmpeg (10.090 archivos, 1,55 M líneas), gromacs (8.982 / 815 K), pandoc (2.767 / 104 K), PHP-src (26.266 / 2,81 M), ctags (7.313 / 246 K).

GPT-5.6-sol (high), media de las cinco tareas:

| Agentes | Pass rate final |
| ------- | --------------- |
| 1       | 19,31 %         |
| 8       | 20,68 %         |
| 32      | 26,52 %         |
| 128     | 28,78 %         |

Pandoc aislado: 33,89 % (1) → 41,75 % (8) → 43,11 % (32) → 50,94 % (128) → **55,06 % (1.024)**. Con GPT-6.1-sol (high): 56,19 % (1) → **79,59 % (32)**, +41,64 % relativo.

Latencia: en pandoc, 128 agentes superan el 30 % de pass rate en el checkpoint de 30 minutos; 32 y 8 lo hacen a los 60 y 90 minutos; el agente único no lo alcanza en las primeras dos horas.

## Infraestructura de ejecución

- Límites por worker: 272.000 tokens de entrada, 128.000 de salida.
- Linux + Docker Compose; por defecto un nodo con 8 workers.
- El run de 1.024 agentes: **16 nodos × 64 agentes**, techo de 64 GiB de memoria por worker.

## Roles emergentes según escala

- **Pocos agentes**: coordinación entre pares.
- **Escala media**: integración entre múltiples workers.
- **Escala alta**: flujos estandarizados y roles especializados. A 1.024 agentes varios workers asumen el mismo rol (p. ej. integradores): un worker contacta varios integradores candidatos, se queda con el primero que responde válido, cancela el resto y entrega el código solo tras esa selección. Workers del mismo área técnica pueden recuperar y asumir el trabajo de otro que falló, lo que reduce la dependencia de cualquier individuo.

## Prompt de sistema de un worker (extracto literal)

> You are pbench-team1-worker1. [...] You work with 1024 peers. Work is tracked in **gitea**; you talk on **mattermost**; you share findings on the **shared context board**. [...] 1024 coders, all equal. You claim what to build, you build it, you merge it, and you choose the next thing. Your peer coders are working simultaneously: sync your codebase with the latest `main` branch before merging your own code to `main`, and sync up with peers to avoid duplicated work. Always focus on reproducing the reference; reach for the coordination tools only when your information can greatly impact others' work.

Nota operativa: el binario de referencia está en `/opt/pbench/executable` en todos los contenedores; el agente puede ejecutarlo para observar comportamiento y debe reconstruir la implementación desde cero, sin red.
