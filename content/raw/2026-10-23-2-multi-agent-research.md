---
title: "Investigación multi-agente — DHCG y RCM (octubre 2026, captura por extractos)"
source: "https://arxiv.org/html/2610.07835"
date: 2026-10-23
captured: 2026-10-23
---

# Raw Content: Multi-Agent Systems Research — October 2026

## DHCG: Dynamic Construction of Hierarchical Collaboration Graphs

URL: https://arxiv.org/html/2610.07835
Published: October 2026

### Abstract

LLM-based multi-agent systems (MAS) have demonstrated strong capabilities in solving complex problems across diverse domains. Recently, the dynamic orchestration of agent systems has become an important research direction. However, existing methods suffer from limited composition, misaligned dependencies, and inflexible scale.

DHCG reframes MAS design as a partially observable Markov decision process, in which both the composition and scale of the MAS are dynamically determined. The framework coordinates three modules (Planner, Worker, and Generator) to progressively construct a dynamic hierarchical collaboration graph from scratch based on the query and evolving execution feedback.

At each step, guided by feedback, the Planner generates a set of distinct and complementary roles tailored to the current reasoning needs and selectively routes relevant information to each role. It can also finalize the hierarchical collaboration graph early or progressively expand it when additional reasoning is required.

### Key Innovation

- Action-aware preference optimization to train the Planner to make more effective decisions when constructing hierarchical collaboration graphs
- Evaluated across code generation, mathematical reasoning, and domain-specific reasoning benchmarks
- Achieves state-of-the-art average performance, improving over single-agent baseline by 13.06 points
- Outperforms both static and dynamic MAS baselines by 2.77–8.02 points
- Demonstrates generalization across different Planner backbones and unseen Worker models

---

## RCM: Responsibility-Centered Coordination Mechanism for Decentralized MAS

URL: https://arxiv.org/html/2610.21243
Published: October 2026 | Monash University

### Abstract

Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibility for delegated dependencies and failure recovery unclear.

RCM proposes a responsibility-centered coordination mechanism that leverages commitments to couple task delegation with explicit responsibilities of the involved parties. Through recursive delegation, agents retain their upstream responsibilities while locally orchestrating downstream commitments, thereby preserving accountability across delegation chains, creating a network of local orchestration.

### Key Innovations

- Responsibility-constrained decision-making guides each agent's actions according to its current responsibilities
- Responsibility-oriented communication protocol (RCP) enables agents to autonomously establish, manage, and terminate commitments
- Agents act in parallel; local actions continuously evolve the commitment graph
- Global coordination emerges and adapts toward a shared mission without centralized control

### Results

- Outperforms strong centralized and decentralized coordination baselines by up to 18.7 points in task performance
- 10.2 points improvement in Responsibility metric
- Better failure and harm detection without task-specific training

---

## SquidAgent: Parallelize Wisely, Coordinate Efficiently

URL: https://arxiv.org/html/2610.08647
Published: October 2026 | NeurIPS 2026

### Abstract

LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline.

SquidAgent identifies two hidden costs:

1. **Re-exploration cost**: redundant effort spent by parallel workers reconstructing context the orchestrator already possesses
2. **Alignment cost**: overhead required to reconcile inconsistencies across independently generated outputs

### Key Innovations

- Decision criterion: a layer should be parallelized only when its critical-path cost, plus re-exploration and alignment overheads, is lower than the corresponding serial cost
- Measures cost in predicted output tokens (LLMs estimate tokens more reliably than wall-clock time)
- Workers fork the orchestrator's session to eliminate re-exploration cost
- Pre-generated shared convention block converts alignment into a bounded upfront cost
- Deterministic scheduler applies the criterion layer by layer

### Results

- 2.2× mean throughput improvement over Claude Code
- 2.6× mean wall-time speedup over Claude Code
- 2.0× throughput improvement over the strongest multi-agent baseline
- Code: https://github.com/tmllab/2026_NeurIPS_SquidAgent

---

## Inherit-MAS: Test-Time Evolution of Multi-Agent Systems

URL: https://arxiv.org/abs/2610.02396
Published: October 1, 2026

### Abstract

Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation.

Inspired by the interplay of inheritance and selection in biological evolution, Inherit-MAS makes inheritance explicit at the workflow and execution levels.

### Key Innovations

- **Workflow inheritance**: starts from the latest completed candidate, may discard removable nodes judged unhelpful, and applies a validated edit to address the diagnosed deficiency
- **Execution inheritance**: inherits eligible stored results only if the complete resolved request and execution context match, avoiding redundant model and tool calls

### Results (GPT-4o-mini workers)

- 55.4% completion on WorkBench
- 49.7% joint F1 on HotpotQA FullWiki
- Outperforms EvoAgent, EvoMAS, and TacoMAS
- Execution inheritance reduces worker-token usage by 29.1% (WorkBench) and 34.6% (HotpotQA)
- Total token usage reduced by 5.3% and 18.1%

---

## MultiAgent-OPD: End-to-End Training of Hierarchical MAS with On-Policy Distillation

URL: https://arxiv.org/html/2610.23234
Published: October 2026

### Abstract

In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents.

MultiAgent-OPD combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader–Searcher–Answerer team end to end.

### Key Innovations

- Two-stage framework: (1) train Teacher in Searcher-Answerer workflow with answer correctness rewards; (2) frozen Teacher provides token-level supervision on Searcher trajectories
- Teacher–student log-probability differences yield local advantages for query generation and evidence summarization
- Leader learns from team success; Answerer learns from candidate correctness
- All three roles jointly update a shared student model

### Results

- 38.68% macro avg@4 across seven datasets
- Exceeds Prompted Critic by 4.06 percentage points
- Exceeds C-MAS + RL by 2.61 percentage points
- Exceeds all five RL-based search agents in comparison

---

## Persistent LLM Orchestration of Heterogeneous Robot Teams

URL: https://arcxiv.org/abs/2610.15224
Published: October 10, 2026 | UC Berkeley

### Abstract

Natural language specifications let non-expert users task robot teams, and LLMs have recently proven effective at grounding such semantic specifications into plans. Existing approaches assume missions that terminate and static environments — both assumptions fail in disaster-response and similar applications.

### Key Innovations

- **Markovian state summary**: rebuilt from semantic map at every invocation, replacing growing interaction history
- **Partial delegation**: orchestrator assigns a subset of robots to an autonomous multi-agent protocol, reserving reasoning for subtasks requiring detailed parameters
- **Observation staleness**: surfaced explicitly in the prompt, with task- and event-triggered re-prompting

### Results

- Rescues 98% of civilians vs 89% for strongest baseline in disaster-response simulation
- Uses six times fewer tokens than baseline

---

## Tensor-Space Joint Optimisation of Topology-Role Configuration in MAS

URL: https://www.nature.com/articles/s41467-026-78717-0
Published: October 21, 2026 | Nature Communications

### Abstract

Topology-role coupling is central to multi-agent formation control, yet its combinatorial complexity makes analytical treatment challenging. A three-tensor framework separately encodes graph structure, time-varying channel states, and role assignments. Their contraction yields a coupling metric equal to the mean of non-trivial Laplacian eigenvalues — a tractable joint optimisation objective.

### Key Innovations

- Optimal leader emerges intrinsically from tensor algebra (no heuristic rules)
- Optimisation via spectral gradient flow restricted to Tucker-compressed subspace
- Tucker compression guarantees polynomial complexity under mild assumptions
- Gradient flow proven to converge
- Substantially better scaling than exhaustive combinatorial search
