---
title: "Captura: llm-d 1.0 — inferencia distribuida lista para el Día 2"
source: "https://llm-d.ai/blog/llm-d-v1.0-state-of-the-art-inference-ready-for-day-2"
date: 2026-10-20
captured: 2026-11-10T20:16:00+01:00
---

# llm-d v1.0: State-of-the-art inference, ready for Day 2

llm-d maintainers · 20 de octubre de 2026 · 14 min de lectura

## Apertura (verbatim)

> llm-d v1.0 is here, and it is the project's most important release so far. In under a year and a half, llm-d has gone from a shared idea among a handful of contributors to the open standard for distributed inference, built by more than 500 contributors from over 25 organizations: proven in production across every major accelerator, running on public clouds and sovereign on-prem fleets alike, and serving open models through both vLLM and SGLang. The founding vision, any model, any accelerator, any cloud, is now something you can deploy.
>
> v1.0 brings that performance to the realities of Day 2 operations: serving multiple tenants, balancing competing priorities, upgrading without downtime, and supporting emerging agentic workloads, all within one suite of co-designed components that compose into your platform. Serving a frontier model fast is no longer the hard part. Running it reliably, for many tenants, through upgrades, under real load, is. That is what v1.0 is built for.

## Por qué el Día 2 es difícil (verbatim)

> Getting a model to serve fast is Day 1. Keeping it serving, for many tenants, through upgrades, under unpredictable load, is Day 2, and it is where most inference stacks show their seams.

Secciones del post: Multi-Tenant Quality of Service · Zero-Downtime Operations · A Stable Foundation to Build On · **Agent-Aware Serving** · Any hardware, any engine, any cloud.

## Rendimiento y adopción en producción (verbatim)

> - **Google Cloud** builds the GKE Inference Gateway on the llm-d Endpoint Picker, cutting time-to-first-token by more than 35% in Vertex AI production while doubling its prefix-cache hit rate from 35% to 70%, and is integrating llm-d 1.0 into GKE across its TPU and NVIDIA portfolio.
> - **AWS** runs disaggregated inference on Amazon SageMaker HyperPod with llm-d, pairing prefix-cache-aware routing with prefill/decode disaggregation and NIXL over Elastic Fabric Adapter to report up to a 70% increase in tokens per second versus standard vLLM.
> - **DigitalOcean** builds its distributed inference stack on llm-d for native GPU-type heterogeneity, serving the trillion-parameter Kimi K3 model across both AMD and NVIDIA hardware.
> - **Oracle Cloud Infrastructure** runs llm-d on OCI bare-metal AMD MI300X with RDMA networking, and developed and validated the upstream AMD deployment guide on OCI.
> - **Tesla and Red Hat** run Llama 3.1 70B on llm-d across AMD MI300X GPUs and, in a coauthored KServe case study, report a 3x increase in output tokens per second and a 2x reduction in time to first token from prefix-cache-aware routing.
> - **Prime Intellect** integrates llm-d into its large-scale reinforcement learning stack, pairing the router with prefill/decode disaggregation and KV cache offload for multi-node rollouts.
> - **IBM Research** self-hosts frontier open models on llm-d for coding agents and chip-design agents, serving up to 3,000 concurrent coding agents on 544 NVIDIA H100 GPUs and reaching a roughly 98% prefix-cache hit rate at about $0.11 per million tokens, around 11.5x lower cost than a proprietary stack.
> - **Mistral AI** serves open models in production on llm-d as part of its regional inference offering.
> - **JetBrains** runs llm-d behind Junie, its AI coding agent, using the scheduler's predicted-latency routing to keep responses fast under heavy agent load.
> - **Red Hat** ships llm-d as the distributed inference stack in Red Hat AI, generally available on OpenShift and on managed Kubernetes including Microsoft Azure and CoreWeave.

## Novedades de la v1.0 (resumen del post)

- **v1 APIs y ruta de petición endurecida**, validada en múltiples nubes y tipos de acelerador.
- **Router de alta disponibilidad y actualizaciones sin caída**, con `DisaggregatedSet`, que orquesta rolling updates conscientes de prefill/decode sin soltar contexto ni interrumpir sesiones activas.
- **Agent-aware serving**: enrutado consciente de sesión, planificación con prioridad de turno y estado nativo de la Responses API, para que los agentes reutilicen contexto entre turnos.
- **Integración ampliada con TPU**: serving nativo de PyTorch con TorchTPU y time-slicing cooperativo para elevar el rendimiento y la utilización de las flotas de TPU.
- Más de **25 organizaciones** adoptantes y **5.100 estrellas** en GitHub.
