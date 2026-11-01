---
title: "Hermit: framework de adaptadores de harness para agentes (Infini-AI-Lab) — captura"
source: "https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework"
date: 2026-10-25
captured: 2026-11-01
---

# Hermit — Harness Adapter Framework (Infini-AI-Lab, v0.1.0)

> Captura del análisis de MarkTechPost (29-oct-2026). El primer release, v0.1.0, se publicó el 25 de octubre de 2026; el postdoc de CMU Haizhong Zheng lo anunció en X el 27 de octubre. El extracto reproduce los pasajes verbatim del artículo.

## TL;DR (verbatim)

> - **Footprint:** A Python framework. No parameters of its own. Apache-2.0, `pip install hermit-harness`.
> - **Runs on:** The offline Quick Start needs no GPU, model account or dataset. Real runs use any API backend or a local vLLM, SGLang or Ollama server.
> - **Performance:** Reported gains over no-adapter baselines on OfficeQA, CL-Bench and ServeLearnBench, all with GLM 5.3 Flash.
> - **Best:** MWM adapter hits 0.795 accuracy on CL-Bench database exploration, vs 0.580 for the in-context baseline.
> - **Worst:** The prompt-only adapter scores 0.470 on the same venue, below that 0.580 baseline.
> - **Bottom line:** Best: one training loop for 5 harness evolution methods. Worst: most results are single runs, self-reported.

## Qué es un harness adapter (verbatim)

> A harness adapter is a trainable external harness. It works like a plugin with training support built in. A model adapter, such as LoRA, adapts a model. A harness adapter adapts an existing agent instead.

> The adapter can hold instructions, skills, memory, tools, executable code and agent coordination logic. It can even be a whole repository. Its specification says which parts are learnable and how updates get checked. The base model and harness never change.

> The team gives 3 reasons for this design. Many harnesses are closed-source. Editing open ones can break carefully tuned component interactions. And a learned adapter can move between compatible models and harnesses.

## Cómo entrena (verbatim)

> Hermit uses an RL-style training loop. A Trainer runs a batch of tasks through the acting agent with the current adapter. A judge scores the outputs. An Evolver reads the trajectories and feedback, then proposes a new adapter. The Trainer checks it against the template and commits it as the next version.

> Every adapter version lives in a git tree. You can inspect, roll back or ship any version. Learner programs can run sandboxed, which requires Linux with bubblewrap.

> Five evolution methods ship today: GEPA, SkillOpt, MetaWorld Model (MWM), Harness² and Continual Harness. ACE and ReHarness are listed as coming soon. You can also write your own Evolver.

## Resultados (verbatim, auto-reportados; modelo actuante GLM 5.3 Flash)

**OfficeQA** (172 preguntas sobre boletines del Tesoro de EE. UU., exact match):

| Method            | Accuracy |
| ----------------- | -------- |
| No adapter        | 0.541    |
| Initial skill     | 0.576    |
| GEPA              | 0.580    |
| SkillOpt          | 0.600    |
| Continual Harness | 0.634    |
| Harness²          | 0.651    |

> The team reports a +7.6 point gain for Harness² over its reference run, with a 95% interval of +1.7 to +13.4.

> **CL-Bench** … On database exploration, MWM reaches 0.795 accuracy. The benchmark's in-context baseline scores 0.580. On exploitable poker, MWM wins 3.08 big blinds per hand, vs 2.51 for in-context learning.

> **ServeLearnBench** streams 624 retail support requests under a hidden, shifting policy. MWM scores 45.3 on hidden-policy tests. The best learning method on the leaderboard, CH, scores 28.7. An oracle given the policy scores 89.2.

## Comparativa (tabla verbatim)

| Feature               | Hermit                                     | GEPA                                     | ACE                           | Agent Lightning                               |
| --------------------- | ------------------------------------------ | ---------------------------------------- | ----------------------------- | --------------------------------------------- |
| What it trains        | External harness adapter                   | Any text parameter (prompts, code)       | Context playbook              | Prompts and model weights                     |
| Changes model weights | No                                         | No                                       | Not disclosed                 | Yes, via RL or SFT                            |
| Methods               | 5 built in, custom Evolvers                | Reflective evolution, Pareto selection   | Generator, Reflector, Curator | RL, prompt optimization, SFT                  |
| Deploy targets        | Codex, Claude Code, Pi; plugin export      | DSPy (`dspy.GEPA`)                       | Not disclosed                 | LangChain, OpenAI Agents SDK, AutoGen, CrewAI |
| License               | Apache-2.0                                 | MIT                                      | Apache-2.0                    | MIT                                           |
| Key result            | 0.795 on CL-Bench database (self-reported) | AIME 2025: 46.6% to 56.6% (GPT-4.1 Mini) | +10.6% on AppWorld            | Not disclosed                                 |

## Despliegue (verbatim)

> The CLI covers `check`, `train`, `eval`, `deploy` and `convert`. […] Supported backends include Fireworks, OpenAI, Anthropic, DeepSeek, vLLM, SGLang and Ollama.

> `hermit deploy` writes a workspace for Codex, Claude Code or Pi. `hermit convert` exports a trained adapter as a native plugin for Codex, Claude Code, Pi or Hermes. A finished Lean collaboration adapter coordinates 5 Codex agents proving one theorem together.
