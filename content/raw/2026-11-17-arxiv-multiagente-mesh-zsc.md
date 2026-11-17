---
title: "Ola arXiv de noviembre de 2026: resiliencia, coordinación cero-shot y orquestación de sistemas multiagente LLM"
source: "https://arxiv.org/abs/2611.06389"
date: 2026-11-17
captured: 2026-11-17
---

# Sistemas multiagente LLM — seis trabajos de arXiv (noviembre de 2026)

Categoría: Investigación en sistemas multiagente basados en LLM. Capturado el 2026-11-17. Los abstracts se han recuperado vía resultados de búsqueda (los abstract de `/abs/` se inyectan en cliente, por lo que se citan como referencia bibliográfica y no se extraen cifras no confirmadas).

## MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing (arXiv:2611.06389)

> Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model **resilience** explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness. In this work, we propose **Multi-Agent Mesh (MA-Mesh)**, a framework that constructs a role-based self-healing layer on top of a collaboration pattern. Specifically, MA-Mesh generates resilience-aware system specifications and synthesizes them into executable multi-agent policy code. To enhance resilience, we introduce two self-healing mechanisms: **Cross-agent reflection**, a mechanism that allows agents to evaluate not only their own outcomes but also the performance of their peers, enabling informed behavioral adjustments and collective policy refinement; and **Role-based failover**, a strategy which dynamically reassigns roles and enables agents to substitute for one another when sub-tasks fail or agents underperform, ensuring continuity of task execution. Experimental results across diverse tasks (e.g., software development, tool use, scientific reasoning) demonstrate that MA-Mesh significantly outperforms existing multi-agent systems in both task performance and robustness under system uncertainty.

## Zero-Shot Coordination among LLM Agents (arXiv:2611.06409)

> We study **zero-shot coordination (ZSC)**, where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. […] We focus on simple, general-purpose scaffolds in minimal environments designed to isolate specific coordination challenges. Our results show that even in these controlled settings, **frontier LLM agents struggle to coordinate, largely due to limited understanding of the coordination problem and weak reasoning about their partner's beliefs.** While LLMs introduce semantic information as an additional axis for coordination, they nonetheless fail to exploit this structure effectively. Towards this, we propose **Coordination-friendly definitions (CFDs)** as a principled approach for enabling robust coordination among LLM agents. Finally, we show that coordination-friendly definitions can be discovered automatically, removing the need for manual engineering.

## Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks (arXiv:2611.11714)

> Ten identical LLM agents play repeated group-decision games […] a manager with a fixed budget then adds directed observation links, where a link from i to j lets i observe j's past actions. Across **1,080 episodes and six games** spanning coordination, anti-coordination, social dilemmas, and discovery, we ask two questions in sequence: how much information to share, and—at a fixed budget—who should observe whom. […] **the value of information is alignment-contingent:** more peer information tends to improve or leave welfare unchanged when individual behavior is broadly aligned with the collective goal, but under free-riding or congestion externalities it amplifies individually attractive yet collectively harmful behavior, so more is no longer better—in a public-goods game the group does best with no information at all. […] These results argue against a default of full transparency for agent collectives: before deciding how much information to reveal or how to route it, an operator should ask what behavior greater visibility will amplify.

## Learning Multi-Agent Orchestration: Higher-Order Interactions in Policy Improvement (arXiv:2611.07495)

> Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. […] we introduce **IAPO**, an interaction-aware policy optimization framework that explicitly accounts for interactions among decisions. […] we prove [interactions] can account for half of the attainable gain […] On long-input versions of GSM8K, MATH, DROP, MBPP and HumanEval, against fifteen published multi-agent and workflow-search systems on the same 7B executor, IAPO's deployed plans reach the strongest system's accuracy with fewer tokens, and **removing the interaction term costs 7 to 17 points of accuracy on the two code benchmarks.**

## Stream of Belief: Eliciting Collective Intelligence through Latent Belief Dynamics (arXiv:2611.21250)

> In this work, we view multi-agent reasoning as a process of seeking a collective equilibrium of implicit belief dynamics and introduce **Stream of Belief (SoB)**, where agents maintain continuous latent beliefs and iteratively refine them through communication and reflection. Our method seeks a collective belief state of a multi-agent system where further communication induces no meaningful information propagation.

## Turning Multi-Agent Communication into Token-Level Credit with On Policy Self Distillation (arXiv:2611.16206)

> Reinforcement learning improves problem solving in large language model multi-agent systems. Existing approaches overlook communication knowledge or compress it into scalar rewards, leaving coarse credit with little guidance on which decisions each agent should reinforce or revise. **OPSD4MAS** converts future communication into fine-grained token-level credit through On Policy Self Distillation (OPSD). […] Our method improves mathematical pass@4 over GRPO by up to **20.00 percentage points.** Code: https://github.com/Camel-Prince/OPSD4MAS.
