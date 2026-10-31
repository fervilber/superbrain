---
title: "TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving (arXiv 2610.37230) — captura"
source: "https://arxiv.org/html/2610.37230"
date: 2026-10-28
captured: 2026-10-31
---

# TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving

> Captura del abstract y de las secciones 1–3 del preprint (arXiv:2610.37230), recuperados de la versión HTML. Autores de Shanghai Jiao Tong University y Stanford University, según la ficha de HyperAI/papers. El trabajo se detectó por primera vez en el tracker de AI Weekly con fecha 28 de octubre de 2026.

## Abstract

Agentic services alternate between model inference on clustered GPUs and external tools on distributed CPUs. In this scenario, existing systems (1) overlook tool-return readiness in service evaluation, wasting limited resources, and (2) use heuristic strategies to decide admission and placement on GPUs, resulting in suboptimal scheduling decisions. To bridge this gap, we present **TAO**, a tool-aware joint scheduling framework for LLM-based agentic serving. Its value interface combines **near-term tool readiness, node-specific cache credit with time-aware decay, and token footprint**; a **dynamic program jointly selects and places waiting sessions under capacity constraints**. Across the 12 reported model–workload–concurrency settings, TAO reduces latency by up to **26.8%**, reduces mean time to first token (TTFT) by up to **36.3%**, and increases decode throughput by up to **29.5%** relative to the best evaluated state-of-the-art baseline for each metric.

## 1. Introducción: el escenario CGDC

Recent advances in language models have expanded their use beyond basic chatbots to complex agents, making **CPU-based tool execution a substantial source of latency alongside GPU-based inference**. Specifically, an agent operates through an agent session that alternates between LLM inference and external tools, such as compilers and retrievers, to complete multi-step tasks. When tools run outside the inference service, a session's demand for GPU computation becomes **interruptible**. We call this serving scenario **Clustered-GPUs with Distributed-CPUs (CGDC)**: clustered GPUs, i.e. nodes, provide shared inference capacity, while external tool calls introduce delays between LLM requests.

We find that existing serving systems generally follow an **evaluate-then-decide** scheduling pattern (llm-d, SGLang, vLLM Production Stack). They evaluate node features at the session level and then decide where and when to serve each session. This separates the problem into two related challenges: (1) how to value a session's next model turn, and (2) how to select and place sessions under shared capacity constraints.

Para (1), los sistemas existentes **ignoran la latencia de las llamadas a herramientas**: los sistemas cache-aware reutilizan prefijos KV y equilibran carga; los workflow-aware anticipan llamadas futuras; los latency-aware priorizan por latencia o trabajo restante. El _tool timing_ se usa sólo como subproducto del reuso de KV o del recuento de tokens: Li et al. (2025) predicen la duración de la herramienta para elegir tiempos de retención de KV-cache, y Kang et al. (2026) descuentan el token footprint de las sesiones que ejecutan herramientas conforme pasa el tiempo. Estos rasgos entran en reglas de puntuación fijas o umbrales elegidos a mano.

Para (2), los sistemas aplican **heurísticas por sesión**, que son miopes: asignar una sesión puede impedir que se sirva una combinación más valiosa de otras sesiones. "As shown in Figure 1 (Right), they fail to formulate scheduling jointly across multiple sessions."

## 2. Fondo: interrupción y reinicio de sesión

An agent session is a persistent interaction that alternates between model requests and external tool calls. During a model request, it uses a serving node; during tool execution, it awaits a result outside the inference service. A later model request can reuse the KV prefix produced by earlier turns and avoid prefill computation.

During tool execution, **a session can release its GPU resources safely, although its cached prefix may subsequently be evicted**. In contrast, preempting an active inference session requires recomputation. Repeated recomputation and reconstruction cause **KV-cache thrashing**. Therefore, **at a tool boundary, the scheduler can apply session interruption**: it interrupts the agent session's model admission and releases its node resources while the external tool continues. When inference service is needed again, **session restarting** restores admission on an eligible node and resumes the existing interaction. Interruption and restarting are state transitions decoupled from the underlying inference engine, and both can be decided from the same session evaluation; las sesiones interrumpidas se unen a las nuevas llegadas en un **waiting pool**.

## 3. Método

We present TAO, which combines agentic session evaluation with decision making, i.e. **dynamic programming for joint selection and placement**. Para incorporar la latencia de herramientas a la evaluación de sesión, se propone **tool-return readiness**, integrada explícitamente con rasgos establecidos como el reuso de KV-cache. Siguiendo a Kang et al. (2026), **las sesiones se interrumpen durante las llamadas a herramientas y pasan a un waiting pool**. Tool-return readiness estima qué sesiones necesitarán inferencia dentro de la próxima ventana de scheduling. Para cada par sesión–nodo se forma una **terna de valor**: readiness, reuso de KV-cache con decaimiento temporal, y token footprint. Dadas esas ternas, se diseña un algoritmo de scheduling conjunto que considera todas las sesiones del waiting pool: el optimizador **maximiza la suma de las ternas mediante programación dinámica**, y sus coordenadas evolucionan con la edad de la caché y el progreso de la herramienta, de modo que distintas señales guían las decisiones a lo largo del tiempo **sin una suma ponderada**. Separar la optimización de la evaluación de sesión hace el framework extensible.

## Contribuciones declaradas

- We identify the **Clustered GPUs with Distributed CPUs (CGDC)** serving scenario in the era of LLM-based agents, which shifts the key bottleneck of latency to tool calls.
- We propose TAO, a tool-aware joint scheduling framework, improving the evaluate-then-decide paradigm with session evaluation with explicit tool-return readiness and decision making with joint modeling and optimization.
- **TAO can be generalized and extended to different workloads such as multi-agent orchestration and Looped Agents. Moreover, it is also compatible with non-agent chatbot scenarios.**
- Across the 12 reported model–workload–concurrency settings, TAO reduces latency by up to 26.8%, reduces mean time to first token by up to 36.3%, and increases decode throughput by up to 29.5% relative to the state-of-the-art baseline for each metric.

## Trazabilidad y cautelas

- Según AI Weekly (alerta del 28 de octubre de 2026), los números son "up to": doce números a nivel de configuración sobre tres modelos (DeepSeek-V4 Flash, Qwen3-32B, GLM-4.7) son los mejores recortes entre configuraciones, no una garantía plana para cualquier carga. La sobrecarga del scheduler se declara por debajo del **0.12%**.
- El trabajo relacionado citado incluye AgentSysBench (latencia no-LLM sustancial y demandas de recursos dependientes del despliegue), MARS (coordinación de inferencia en GPU, presión de herramientas en CPU, admisión y retención de KV) y mecanismos complementarios que cambian la línea de tiempo de ejecución (Conveyor, Sutradhara, PASTE, SmoothAgent, Pie).
