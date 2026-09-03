# Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting

**Authors:** Ron Begleiter, Katya Egert Berg, Gilad Saban, Gil Shabat  
**Date:** September 2, 2026  
**Source:** arXiv:2609.02649v1 (Accepted to EMNLP 2026)  
**Category:** Artificial Intelligence, Computation and Language, Machine Learning, Root Cause Analysis (RCA)

## Abstract

Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world industrial settings. While monolithic Large Language Model (LLM) agents offer unbounded expressivity for tasks like Root Cause Analysis (RCA), they suffer from context limits, compounding hallucinations, and prohibitive inference latency. Traditional weak supervision offers statistical rigor but is mathematically restricted to discrete classes. We present Loom, a generative consensus framework deployed for real-world RCA that bridges these paradigms. Loom aggregates open-form hypotheses emitted by modular heuristics (diagnostic templates dynamically populated with episode-specific entities, times, and metrics) by projecting them into a continuous embedding space, and resolves conflicting signals with an iterative centroid-based reweighting algorithm. The resulting consensus weights ground a single lightweight LLM synthesis step. Evaluated on the OpenRCA benchmark, Loom occupies the accuracy--efficiency Pareto frontier: it matches a state-of-the-art autonomous agent on Bank and Market-2 and trails on Market-1 and Telecom, while using a single LLM call per incident on all four datasets ($\sim$26$\times$ faster; $\sim$33$\times$ with an 8B-parameter synthesizer). We discuss our deployment experience, highlighting lessons learned regarding the trade-offs between agentic depth and inference latency, negative results in redundancy detection, and how deterministic consensus fosters trust among Subject Matter Experts (SMEs).

## The RCA Challenge in Production

Root Cause Analysis (RCA) in IT and industrial cloud operations requires processing highly heterogenous telemetry data: logs, alerts, metrics, and incident timelines.

- **LLM Monoliths (Multi-agent Loops):** SOTA agents can analyze incidents by executing multiple investigative tools in a loop. However, this introduces high latency (minutes per incident), potential hallucinations, and massive API costs. In production incidents, every minute matters.
- **Weak Supervision:** Classic statistical aggregation is robust but cannot easily handle free-form textual output or rich entity extraction required for actionable tickets.

## Loom Architecture

Loom acts as a hybrid. It uses simple, parallelized heuristics to emit diagnostic text slices, then uses embedding-space math to resolve conflicts, and finally calls a single lightweight LLM to summarize the resolved signals.

### 1. Modular Heuristics

Loom runs a parallelized swarm of deterministic, template-based heuristics. Each heuristic listens to specific data signals (e.g., CPU spikes, database connection pool exhaustion, sudden latency spikes in an upstream microservice).
If triggered, the heuristic populates a diagnostic template with the exact entity names, timestamps, and metric deviations. This yields a set of "noisy hypotheses" (free-form texts).

### 2. Continuous Embedding Projection

Instead of doing text-matching or LLM-based clustering, Loom maps these diagnostic hypotheses into a continuous high-dimensional vector space using a text embedding model:
$$\mathbf{h}_i = \text{Embed}(\text{Hypothesis}_i)$$

### 3. Iterative Centroid-Based Reweighting

To handle conflicting hypotheses (e.g., Heuristic A says "DB Timeout" and Heuristic B says "Network Routing Drop"), Loom resolves the conflict in the embedding space.

- It computes a dynamic centroid of the hypothesis vectors.
- It calculates the cosine distance of each hypothesis to this centroid.
- It applies an iterative reweighting algorithm (reminiscent of robust M-estimators) that penalizes outliers (hypotheses far from the main consensus group) while emphasizing matching diagnostic strands.
- This creates a set of consensus weights: $w_i \in [0, 1]$ for each hypothesis.

### 4. Lightweight LLM Synthesis

Instead of feeding thousands of lines of raw telemetry, the lightweight LLM is fed only the weighted, high-confidence hypotheses. The LLM's role is narrowed to translating this structured, weighted consensus into a human-readable, actionable summary.

## Industrial Results

When evaluated on the **OpenRCA benchmark**:

- **Speed:** $\sim$26 times faster than standard multi-agent frameworks (which use up to 20-30 sequential LLM calls). With an 8B-parameter local model, it is $\sim$33 times faster.
- **Pareto Frontier:** Matches the accuracy of SOTA autonomous agents on complex environments like `Bank` and `Market-2` while using only **a single LLM call** per incident.
- **Trust:** Deterministic mathematical consensus in the embedding space ensures that identical inputs yield identical weights, fostering SME (Subject Matter Expert) trust, which is often broken by the stochastic behavior of pure LLM multi-agent planners.
