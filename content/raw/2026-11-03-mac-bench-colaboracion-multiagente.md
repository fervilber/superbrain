---
title: "MAC-Bench: evaluar la colaboración multiagente mediante tareas interconectadas (arXiv:2611.01728)"
source: "https://arxiv.org/abs/2611.01728"
date: 2026-11-03
captured: 2026-11-03
---

# MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks

Zerui Chen, Qinggang Zhang, Qichuan Liu, Zhishang Xiang, Zhimin Wei, Yunbo Tang, Zhuo Li, Jinsong Su, Zhihong Zhang — arXiv:2611.01728 [cs.MA], 3 de noviembre de 2026. Captura verbatim del abstract y extractos de la introducción (vía `https://arxiv.org/html/2611.01728v1`).

## Abstract

Large language model (LLM)-based multi-agent systems (MAS) tackle challenging tasks by dividing work among agents and coordinating their contributions toward shared objectives. Evaluating these systems therefore requires benchmarks that assess not only task-solving performance but also the ability to handle interdependent work. However, existing benchmarks often emphasize task difficulty without substantial collaboration requirements or evaluate only a limited range of predefined collaboration patterns. In this paper, we introduce MAC-Bench, a comprehensive benchmark for evaluating multi-agent collaboration through interconnected tasks. Rather than imposing predefined agent roles or communication protocols, MAC-Bench embeds collaboration requirements directly into task dependencies and shared-resource constraints. Specifically, we mine reusable collaboration structures from selected benchmark tasks at two levels. Local collaboration patterns capture recurring interactions among subtasks, while global task structures characterize how these interactions contribute to complete workflows. Through coarse-to-fine composition, these structures are recombined into task graphs combining different collaboration requirements. Tasks are instantiated in executable environments with automated verification of partial progress and complete task resolution.

## Extractos de la introducción y resultados

MAC-Bench provides substantial, interconnected tasks across business operations and software engineering by mining and composing reusable task structures. Tasks combine varied dependencies, integration, and shared-resource constraints; targeted checks show effects of selected relation violations. Across two LLM backbones, Meta-Team leads in progress, while AOrchestra and Magentic-One trail ReAct. No configuration resolves more than 6.25% of tasks. MAC-Bench separates partial progress from complete task resolution.

## Contexto de la jornada: otras dos contribuciones de cs.MA (3 de noviembre de 2026)

### Automated Stateful Specialization for Adaptive Agent Systems (arXiv:2611.01870)

Myan Vu, Harrish Ayyanar, Jiang Pang, Anwiketh Reddy, Mayank Goel. Abstract: Current automated agent design frameworks produce either static workflows that lack adaptability or per-query optimizers that prevent the accumulation of deep, agent-level task expertise. We propose a new direction that reconciles these paradigms: creating stateful teams of specialist agents that accumulate knowledge over time and can be reconfigured for novel tasks entirely without human intervention. To this end, we introduce ASpec, a framework that manages this full agent lifecycle by first autonomously discovering specialist archetypes via evolutionary search and then cultivating their expertise through experience, mirroring how human experts learn through practice and reflection. We further introduce a lightweight hierarchical control policy, "retain-then-escalate," which governs when to leverage the established agent system versus when to adapt its structure. Through comprehensive experiments, we demonstrate that this approach leads to significant performance gains on expert-level scientific benchmarks like GPQA while matching the state-of-the-art on broader domain tasks. Code at https://github.com/myanvoos/ASpec.

### Evaluating Context Sensitivity of Collaboration Behavior in Multi Party Simulation Frameworks (arXiv:2611.00089)

Anvesh Rao Vijjini, Sheshera Mysore, Pegah Jandaghi, Ashish Sharma, Snigdha Chaturvedi, Bahareh Sarrafzadeh. Abstract: Group Social Behavior is increasingly used as a lens to study LLM simulations to aid model training and evaluation. However, little prior work has examined how contextual factors such as team size and goal type manifest in long running simulations. We conduct a controlled, full-factorial study examining how contextual factors affect collaboration behavior across multi-party simulation frameworks. Our analyses reveal significant effects of contextual factors such as simulators consistently favor smooth collaboration over disagreement, negotiation pressure, and coordination breakdown.
