---
title: "WorkflowArena: medir la orquestación de flujos de trabajo como capacidad propia de los sistemas multi-agente"
source: "https://arxiv.org/html/2611.12856v1"
date: 2026-11-22
captured: 2026-11-22
---

# WorkflowArena: benchmarking de orquestación ejecutable en sistemas multi-agente con LLM

Captura de _WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent
Systems_, arXiv:2611.12856v1, **9 de noviembre de 2026**. Autores: Zheng Jiang, Fang Niu, Bo Peng,
Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi, Youjie Zheng, Kaisen Yang, Calvin Xiao,
Lifeng Sun, Huan-ang Gao. Afiliaciones: Navers Lab, Einsia.AI, Tsinghua University. Homepage:
`https://lab.einsia.ai/workflowarena`.

## Abstract (verbatim)

> Large language model agents are increasingly deployed as multi-agent systems rather than as a
> standalone model operating within a single context. Recent agent harnesses allow the model to
> instantiate worker agents and to author the executable workflow that coordinates them, shifting the
> design of system structure from developers to the model at run time. The quality of this
> organization therefore constitutes a distinct capability, yet existing benchmarks either measure
> end-to-end task completion or evaluate coordination under structures specified in advance. We
> formalize this capability as **workflow orchestration** and introduce **WorkflowArena**, a benchmark
> of **145 long-horizon tasks spanning 8 professional domains**, from software engineering and formal
> mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an
> integrated deliverable composed of interdependent components, which is assessed by a hidden
> verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded,
> enabling joint evaluation of deliverable quality and the organization of the underlying work.
> Experiments with nine models show that **no single configuration performs best across all domains**
> and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude
> Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex
> delegate more frequently in smaller units. When the executing model is held fixed on a challenging
> subset of tasks, **workflows authored by Claude Opus 5.5 substantially improve weaker executors**,
> indicating that workflow organization is itself a measurable determinant of task performance.

## Introducción (verbatim, extracto)

> Large language models have evolved from text generators into agents that act in external
> environments and pursue goals over long horizons. As tasks grow longer, the limiting factor shifts
> from what a single agent can accomplish to how the work is organized. Long-horizon tasks consist of
> interdependent subtasks that call for different expertise and independent verification, and a single
> context that must retain the entire history of such work soon becomes a bottleneck. Further progress
> therefore depends on **system intelligence**, the ability of an agent system to organize multiple
> intelligent components into a coherent and adaptive [workflow].

## Contribuciones declaradas

- **Benchmark.** WorkflowArena, 145 tareas de horizonte largo en 8 dominios y 17 formas de tarea, en
  las que cada contrato de entregable se empareja con verificación oculta específica de dominio.
- **Protocolo de evaluación.** Cada delegación se enruta por una **interfaz registrada** bajo un
  presupuesto de tiempo compartido, dejando la decisión de delegar al agente, de modo que su
  organización del trabajo puede analizarse junto a los resultados del entregable y el uso de
  recursos.

## Resultado central sobre la autoría de flujos de trabajo

> On a challenging subset of tasks, workflows authored by Opus raise the continuous scores of all four
> execution models, by **6.41 points on average in the static mode**, whereas workflows from Astra,
> itself far stronger than these executors, help them far less and **lower the scores of two of them**.
> Orchestration quality is thus a measurable source of performance that appears distinct from the
> ability to complete the task alone.

## Implicaciones

- La **orquestación de flujos de trabajo** se formaliza como una capacidad medible y separable del
  desempeño bruto del modelo que ejecuta.
- Un flujo de trabajo bien autorizado puede **mejorar a un ejecutor más débil**; un flujo de trabajo de
  un modelo más fuerte no garantiza esa mejora. La calidad de la organización del trabajo no se deduce
  del nivel del modelo que la escribe.
- Existen **estrategias de delegación distintas y no universales**: Claude tiende a flujos con grupos
  de workers más grandes y menos frecuentes; GPT delega más a menudo en unidades más pequeñas. Ningún
  ajuste gana en todos los dominios.
