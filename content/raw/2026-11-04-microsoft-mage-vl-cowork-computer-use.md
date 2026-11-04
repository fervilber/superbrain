---
title: "Microsoft publica Mage-VL-Cowork: agente de computer-use de 4B con 66,0% en OSWorld-Verified (4 de noviembre de 2026)"
source: "https://tpsreport.news/news/microsoft-mage-vl-cowork-4b-computer-use-osworld-1"
date: 2026-11-04
captured: 2026-11-04
---

# Microsoft releases Mage-VL-Cowork, a 4B computer-use agent scoring 66.0% on OSWorld-Verified

TPS Report, 4 de noviembre de 2026 · 2:06 AM. Captura verbatim. Extraído vía `web_extract`.

**TL;DR** — Microsoft has published Mage-VL-Cowork on Hugging Face, a 4B-parameter vision-language policy that combines GUI control and code/terminal execution in one checkpoint. According to the model card, it reaches 66.0% on OSWorld-Verified under a 50-step budget, the best among 4B models. It is released under Apache-2.0.

## What it is

Mage-VL-Cowork is a single vision-language policy (image + text in, text out) that handles screenshot-grounded GUI interaction (`computer_use`) and persistent code/terminal execution (`bash`) with no external orchestrator. It was trained from an intermediate 4B Mage-VL checkpoint through a five-stage specialize-then-unify curriculum.

## Specifications

- **Developer:** Microsoft Mage Team
- **Parameters:** 4B (9.48 GB in bfloat16 across 2 safetensors shards)
- **Backbone:** Mage-ViT (16×16 patch grid, spatial_merge_size=2, 3D RoPE) plus Qwen3-4B (Qwen3-4B-Instruct-2507)
- **Architecture:** llava_onevision2
- **Context length:** 32,768 tokens for active training and inference; the architecture supports up to 262,144
- **Working memory:** asymmetric sliding window of the 3 most recent screenshots, 4 full responses and a folded Action: history
- **Action channels:** `computer_use` (11 GUI primitives in [0, 999] normalized coordinates) and `bash` (persistent shell and Python environment)
- **Output format:** a rationale, an Action: summary and a `<tool_call>`
- **Training compute:** 7.79 ZFLOPs nominal LM compute across 5 stages, on 32 NVIDIA B200 GPUs plus 1,120 CPU sandbox slots for RL
- **Pricing:** not yet disclosed (open weights)

## Benchmark results

According to Microsoft, the model scores 66.0% on OSWorld-Verified, with 87.5% on Operating System tasks and 62.7% on Multi-Application Workflows. Standalone grounding improved from 30.6% to 56.9% on OSWorld-G and from 78.8% to 87.2% on ScreenSpot-v2. Across the hybrid stages, accuracy moved from 45.56% to 55.84% to 66.0%.

Online GRPO with verifiable task rewards added 10.16 percentage points over Hybrid SFT. Mean model calls fell from 21.57 to 18.77 (13.0% fewer) and output tokens from 7,374 to 5,499 per task (25.4% fewer).

## Training pipeline

Microsoft describes two upstream components:

- **Evolved teacher harness:** the team pruned overlapping tools such as xdotool and accessibility trees and pre-installed domain Python libraries. This lifts the GPT-5.4 teacher to 92.0% with 29.2% fewer steps, and the student gain at 4B is +12.5 pp (37.6% vs. 25.1%).
- **Mage-CUA-Forge:** a workflow-first synthesis engine that generates 293,806 tasks across 6,915 [workflows].
