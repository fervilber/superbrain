---
title: "Google dona Agent Substrate, gVisor y OpenRL a la CNCF; Agent Substrate llega a 1.0 y a GA en GKE"
source: "https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf"
date: 2026-11-05
captured: 2026-11-05
---

# Open infrastructure for autonomous agents comes to CNCF

Google Cloud Blog — Drew Bradstock, VP Product Management, Orchestration & Kubernetes, 5 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract`.

## Agent Substrate, gVisor, and OpenRL have been accepted into the CNCF Sandbox; Agent Substrate has reached 1.0, and is GA on GKE

As AI shifts from human scale to agent scale, from systems of record to systems of action, and from simple requests to complex agentic workflows, the workload underneath your platform changes completely. An agent works in a continuous, stateful loop: It proposes an action, spins up subagents, executes code or tool calls inside a sandbox, and feeds the results back into the model for the next turn. Running that loop at scale requires the same open foundation and neutral governance that Kubernetes and the Cloud Native Computing Foundation (CNCF) brought to containers in the 2010s.

Today, we are announcing the donation of Agent Substrate, gVisor, and OpenRL, three open source projects that started at Google, to the CNCF following their acceptance last month into the CNCF Sandbox. To bring this open stack into managed production and accelerate it across TPUs and GPUs, we are also announcing that Agent Substrate has reached its 1.0 milestone and is now generally available as Agent Substrate on GKE.

Each project is now working through CNCF Sandbox onboarding with community maintainers and independent build infrastructure, and gVisor is on a path toward Incubation. These releases deliver an open stack that runs on any Kubernetes cluster, on any cloud, across CPUs, GPUs, or TPUs, by:

- **Scaling isolated agent environments without idle compute overhead with Agent Substrate (now 1.0 and GA on GKE):** Agents execute code or tests for a few seconds, then wait on model turns, external APIs, or human input. Keeping a dedicated container alive during those pauses ties up memory and compute. Agent Substrate decouples stateful agent sessions and identities from active compute, snapshotting idle agents to storage and restoring them in under 500 milliseconds to run millions of sandboxes at 10x container density.
- **Isolating untrusted code within a sandbox with gVisor:** Agents routinely generate and run unreviewed code and external packages, making standard containers that share a host Linux kernel a security risk. gVisor isolates generated code inside a lightweight userspace application kernel at container packing density on any Linux node.
- **Distributing post training and serving efficiently with OpenRL:** Training agents with reinforcement learning (RL) gives builders an open loop to learn across millions of parallel sandboxed rollouts. OpenRL orchestrates self-hosted RL post-training loops in plain Python on Kubernetes.

### Scale fully isolated agent environments with Substrate

Agents need isolated compute resources and strict access boundaries, yet spend most of their time waiting: executing code for a few seconds, then blocking on a model turn, an external API, or a human approval. Agent Substrate snapshots idle agent sessions to storage and restores them in under 500 ms, so a platform can hold millions of logical sandboxes at roughly ten times the container density without paying for idle memory or compute.

## Notas de captura

El artículo completo continúa describiendo la arquitectura de Substrate, el aislamiento de gVisor y el bucle de RL de OpenRL, así como la ruta de cada proyecto hacia Incubation dentro de la CNCF. La captura conserva la sección de anuncio y los tres bloques de capacidades; el cuerpo extendido (detalles de implementación por proyecto) se resume en el informe.
