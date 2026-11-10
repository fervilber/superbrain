---
title: "Captura: La pila abierta AI-native sobre Kubernetes (Google Cloud, KubeCon NA 2026)"
source: "https://cloud.google.com/blog/topics/developers-practitioners/the-open-ai-native-stack-on-kubernetes-from-open-models-to-distributed-inference-and-agents"
date: 2026-11-10
captured: 2026-11-10T20:14:00+01:00
---

# The open AI-native stack on Kubernetes: From open models to distributed inference and agents

Abdelfettah Sghiouar, Cloud Developer Advocate, Google Cloud · 10 de noviembre de 2026 (KubeCon + CloudNativeCon North America 2026)

## Tesis del artículo (verbatim)

> Over the past decade, Kubernetes established itself as the standard for orchestrating microservices and containerized applications. Today, we're witnessing the next major architectural shift in distributed computing: **AI workloads moving from isolated research prototypes into large-scale, multi-tenant production fleets.**
>
> For modern engineering teams, production AI is rapidly moving beyond generic calls to closed, black-box APIs. Organizations are realizing that their long-term competitive advantage lies in domain specialization. Platform engineers, ML researchers, and AI builders want the autonomy to run high-performing **open-weight models** (such as the Gemma family). They want to adapt them to proprietary enterprise datasets by using **reinforcement learning (RL)** and serve them with predictable latency, high throughput, and maximum hardware efficiency.
>
> [...] the objective is the same: **achieving frontier-level task performance at a fraction of the serving cost and latency.**

## Los cuatro obstáculos (verbatim)

> **Accelerator underutilization in RL**: When you alternate between training and rollout generation, expensive GPUs and TPUs remain idle for most of the training run.
>
> **Cache-blind load balancing**: When you use standard Kubernetes round-robin and least-connections routing, multi-turn agent calls are scattered across arbitrary pods and wipe out key-value (KV) cache locality.
>
> **Framework fragmentation**: When you operate parallel, siloed compute clusters (such as bespoke Ray or Slurm setups) alongside Kubernetes, you fragment capacity and multiply maintenance toil.
>
> **Agent security in multi-tenant clusters:** When you execute untrusted, model-generated shell commands and scripts in shared environments, you expose clusters to sandbox escapes and privilege escalation.

## Los seis componentes

- **OpenRL** (CNCF Sandbox, openrl.dev): servicio de post-entrenamiento nativo de Kubernetes que simplifica el RL post-training y maximiza el uso de aceleradores.
- **llm-d 1.0** (CNCF Sandbox, llm-d.ai): plano de control de inferencia distribuida abierto con enrutado consciente de la caché de prefijos, serving disagregado y gestión de KV cache en varios niveles.
- **Ray on GKE con KubeRay** (CNCF Sandbox): ciclo de vida empresarial, autoscaling elástico y planificación dirigida por Kueue para cómputo distribuido Ray.
- **Agent Substrate** (CNCF Sandbox, ate.dev): runtime de orquestación abierto para el ciclo de vida y los destinos de ejecución de flujos multi-turno de agentes.
- **gVisor** (CNCF Sandbox, gvisor.dev): sandbox de contenedores a nivel de kernel con fuerte aislamiento de llamadas al sistema para código de agente no confiable en clústeres multi-inquilino.
- **TorchTPU** (pytorch.org/blog/introducing-torchtpu/): backend con soporte nativo de PyTorch en Cloud TPUs y GPUs dentro de vLLM y SGLang upstream.

### OpenRL — cuatro primitivas (verbatim)

> **Clean 4-primitive Python abstraction**: Researchers write standard Python training code that's centered around four core primitives (`forward_backward`, `optim_step`, `sample`, and `save_state`). OpenRL translates these primitives into Kubernetes scheduling workflows without requiring developers to learn Kubernetes internals or manage infrastructure code.
>
> **Cooperative accelerator time-slicing**: OpenRL interleaves training steps and rollout inferences on the same physical accelerators. This approach avoids the need to dedicate separate, static clusters to compute-bound training and latency-sensitive rollout generation.
>
> **Delta-weight synchronization**: Shipping full multi-gigabyte model weights over cluster networking after every optimization step creates massive network saturation. OpenRL transmits only parameter deltas to rollout workers, eliminating rollout cold starts.
>
> **Zero-config dynamic resource allocation (DRA)**: OpenRL automatically profiles model context lengths, batch dimensions, and LoRA versus full fine-tuning configurations. It then dynamically bin-packs workloads across a heterogenous accelerator fleet by using native Kubernetes DRA claims.

### llm-d 1.0 — capacidades (verbatim)

> **Prefix-cache-aware routing (Endpoint Picker)**: The Endpoint Picker integrates into the **Kubernetes Gateway API Inference Extension**, and GKE manages it natively through **GKE Inference Gateway**. The Endpoint Picker evaluates real-time KV cache residency across worker pods. In production deployments, it's doubled KV cache hit rates from 35% to 70% and cut median time-to-first-token (TTFT) by 70-85% on multi-turn agent workloads.
>
> **3-Tier KV cache offload**: When accelerator high-bandwidth memory (HBM) nears capacity during long-context interactions, llm-d cascades KV cache blocks from **HBM → host CPU RAM → local NVMe SSD / Google Cloud Managed Lustre / Cloud Storage.** This offload prevents expensive context recalculations.
>
> **EPD Disaggregation with DisaggregatedSet**: Decouples **Encoding, Prefill, and Decode (EPD)** onto specialized hardware pools that are connected by high-speed interconnects. DisaggregatedSet is built on Kubernetes **LeaderWorkerSet (LWS)**. It enables independent horizontal scaling and coordinated, zero-downtime rolling upgrades.
>
> **Native TorchTPU upstream support**: PyTorch models run natively on Google Cloud TPUs inside upstream vLLM and SGLang through TorchTPU. Developers get day-zero parity across TPU v5e, v6e, and v7x alongside NVIDIA GPUs without the need to maintain private forks or rewrite pipelines.
>
> **Latency-tolerant async processing & flow control**: The llm-d-async-processor component pulls background, latency-tolerant tasks from Pub/Sub or Redis into cluster slack capacity. It applies strict traffic prioritization so background processing never degrades interactive user experiences.
>
> **Fleet observability with Prism**: Track cluster-wide throughput, inter-token latency (ITL), TTFT, and cache hit ratios by using Prism, the llm-d open-source benchmarking and performance dashboard.

### KubeRay (verbatim)

> **Declarative cluster lifecycle**: Platform engineers can spin up ephemeral, self-healing Ray clusters on demand for ad-hoc training runs, or run long-lived clusters for batch pipelines.
>
> **Native Kueue queueing & multi-tenancy**: KubeRay integrates directly with **Kueue** for multi-tenant fair sharing, priority preemption, and quota management across shared GPU and TPU capacity.
>
> **Elastic autoscaling**: KubeRay dynamically scales worker pods based on active Ray tasks and actor placement, preventing idle resource consumption.

## Demo de referencia

En la keynote del PyTorch Conference, Google mostró **1.000 agentes en sandbox sobre Agent Substrate en GKE** golpeando un único endpoint llm-d a través de vLLM, SGLang y una flota mixta de TPUs y GPUs de Google Cloud.

## Citas de contexto de la keynote (llm-d 1.0 blog)

- **IBM Research** autohospeda modelos abiertos frontera en llm-d para agentes de código y de diseño de chips: **hasta 3.000 agentes de código concurrentes en 544 GPUs NVIDIA H100**, con ~**98% de aciertos de caché de prefijos** y ~**$0,11 por millón de tokens**, unas **11,5× más barato** que una pila propietaria.
- **Google Cloud** construye el GKE Inference Gateway sobre el Endpoint Picker de llm-d: TTFT recortado >35% en producción de Vertex AI y caché de prefijos duplicada de 35% a 70%.
- **AWS** corre inferencia disagregada en SageMaker HyperPod con llm-d: hasta +70% de tokens por segundo frente a vLLM estándar.
- **DigitalOcean** sirve Kimi K3 (billón de parámetros) sobre llm-d en hardware AMD y NVIDIA.
- **Tesla y Red Hat** reportan 3× más tokens de salida por segundo y 2× menos TTFT con enrutado consciente de caché.
