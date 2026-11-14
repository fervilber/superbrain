---
title: "arXiv cs.MA (13-14 de noviembre de 2026): DecArena y MULTILOOP — la colaboración multiagente descentralizada y la optimización del harness"
source: "https://arxiv.org/list/cs.MA/new ; https://arxiv.org/abs/2611.15521 ; https://arxiv.org/abs/2611.15754 ; https://arxiv.org/abs/2611.14780 ; https://arxiv.org/abs/2611.15017"
date: 2026-11-14
captured: 2026-11-14
---

# Nuevos envíos de arXiv cs.MA (Multiagent Systems) — 13-14 de noviembre de 2026

Captura por extractos del listado `arxiv.org/list/cs.MA/new` (nuevos envíos del viernes 13 de noviembre de 2026) y de los abstracts servidos por el índice de búsqueda.

## DecArena — colaboración multiagente descentralizada a gran escala

> Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to agents, resources, and communication. In decentralized environments, global visibility is unavailable. Agents need to proactively discover non-local resources (e.g. tools, skills), and collaborate with other agents to solve tasks. We study decentralized multi-agent collaboration under graph-constrained communication, a natural reflection of human structures. Each agent observes only its local state and can interact only with neighboring agents.

> We introduce a benchmark with synthetic scalable distributed tool calling with 100K+ tools. Our experiments reveal that recent LLM agents struggle to discover non-local relevant resources and collaborate in decentralized setting. Moreover, standard reinforcement learning fails to reliably overcome this limitation, suggesting that decentralized MAS needs more explicit harness mechanisms for effective collaboration, even using SOTA LLMs.

> We then present a strong baseline **GraphHarness**, combining topology-aware warmup with self-improving LLM-based routing. Results show that GraphHarness substantially improves task success (+48.5) and produces higher quality collaboration (+30.6), while using fewer costs (+34.0) than baselines.

_(Referencia: arXiv:2611.15521, Jiali Cheng, Oleg Rokhlenko, Joo-Kyung Kim, Hadi Amiri, Xingzhi Guo; sujetos cs.MA, cs.AI, cs.CL.)_

## MULTILOOP — evolución automática de harnesses multiagente

> Multi-agent harnesses are harder to optimize as fixing them requires changing how agents interact in addition to how each behaves. We study whether automated harness optimization can diagnose and repair failures in multi-agent systems through a case study on complex information-seeking tasks from DeepSearchQA.

> We apply MULTILOOP, a simple optimization loop in which a coding agent iteratively analyzes, evaluates and edits the harness. With only 10 training samples, the evolved harness improves accuracy by 4.6% over the base harness and by 3.2% over the best single-agent system. However, a taxonomy of failure modes before and after optimization shows that the orchestration failures that characterize multi-agent systems largely persist. Our findings motivate harness optimization methods that encourage structural changes to how agents delegate tasks and share information.

_(Referencia: arXiv:2611.15754.)_

## RE-PRESENT — triangulación de evidencia para inferencia por ensambles de LLM

> Heterogeneous large language models (LLMs) exhibit complementary strengths, motivating routing and multi-model inference methods that seek to identify reliable predictions for each input. However, exploiting this complementarity remains challenging even when a correct prediction is available within the ensemble. [...] We introduce RE-PRESENT, a training-free framework that selectively re-presents disputed questions and directly aggregates candidate-level evidence across alternative views. Across seven multiple-choice benchmarks and two heterogeneous model ensembles, RE-PRESENT improves over strong single-round aggregation while offering a favorable accuracy–cost trade-off compared with self-consistency and multi-model debate.

_(Referencia: arXiv:2611.14780, Juming Xiong et al.)_

## Instituciones económicas como espacio de diseño para agentes artificiales

> Multiagent research inherited its economic vocabulary of auctions, markets, prices, bargaining, and matching from a single observed case: human societies. Those institutions bundle identity, competence, execution, ownership, commitment, and settlement in ways that suit agents whose minds are private, who learn rather than copy skills, and who each persist as one person. Engineered agents need not share any of these constraints, making the list of familiar institutions look less like the entirety of economic organization and more like a sample from a larger, unmapped space. We sketch one way to make that space concrete: a provisional chart that records each institution, separately from the agents that run it, as a typed structure over positions, rights and duties, allocation, information, time, state, process, value, and external recognition.

_(Referencia: arXiv:2611.15017, Nikolos Gurney y Fred Morstatter.)_
