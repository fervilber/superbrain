---
title: "Modelos orientados a agentes: Ripple-65B, Kimi K3.1 Pro y el benchmark CloudOpsBench"
source: "https://agentic-ai-news.uk/?date=2026-11-05"
date: 2026-11-05
captured: 2026-11-05
---

# Agentic AI News Today — Nov 5, 2026

Agentic AI News, 5 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract`.

## Model & Weight Releases

- **Ripple-65B open model.** Ricursive Intelligence released a 65B dense open-weight model pretrained from scratch for agentic coding. It scores 80.5 on Terminal-Bench 2.1 (self-reported) and is available under Apache 2.0 with BF16 and NVFP4 checkpoints.
- **webAI TwIL-8B.** webAI released TwIL-8B, an 8.8B reasoning model post-trained from IBM Granite 4.2 8B. It scores 98.2 on MATH-500 and ships as a 4.98 GiB Q4 GGUF for CPU or modest GPU inference under a non-commercial license.
- **Kimi K3.1 Pro open weights.** Kimi K3.1 Pro is now open-weights, but some local LLM users argue its benchmarks are inflated. An audit claims Chinese models improve on new benchmarks only after release, suggesting heavy benchmark optimization.
- **Tencent Hy4 tease.** Tencent says its Hy4 model ranks among the best open models, putting it close to Claude Opus 5.5 and Kimi K3.1 Pro on computer use. The weights are not yet public.
- **Qwen3.8 Flash-Next quants.** Unsloth released Dynamic v3.1 GGUFs for Qwen3.8-Flash-Next, claiming 10-15% accuracy gains over GSQ-RCO on coding and agentic benchmarks.

## Tools & Coding Agents

- **Meta buys Conductor.** Meta acquired Conductor, an AI coding startup whose agentic teams let developers spin up software projects across parallel workspaces. Founder Charlie Holtz says new customers can expect something new early next year.
- **OpenAI buys Pierre.** OpenAI is acquiring Pierre Computer Company, the maker of Code Storage and open-source tools Trees, Diffs, and Highlights that already power Codex. The goal is to adapt Git workflows for developers and AI coding agents working side by side.
- **CloudOpsBench agent benchmark.** A new open-source benchmark, CloudOpsBench, evaluates AI agents on 45 AWS DevOps tasks. The best models solved only 53-60% of tasks, with about 80% of failures caused by reasoning errors rather than missing knowledge.

## Detalle adicional (munderdiffl.in, 5 de noviembre de 2026)

- **Kimi K3.1 Pro weights.** The model card lists 2.8T total parameters, 104B activated and a context length of 1,048,576 tokens.
- **Ripple-65B Preview.** Ricursive Intelligence says it "trained a language model from scratch" and released this "general-purpose variant" on 4 Nov, claiming "U.S. open-weight state-of-the-art (80.52) on TerminalBench 2.1" (the vendor's own figures). Its 4 Nov page puts the full R&D cost at "$32M".
- **AutoCua.** "Automate with computer-use agent (ComputerUse / CUA) for macOS, Windows, Linux, Browser, iOS & Android." Installs with `pip install AutoCua`. MIT, 1,245 stars on 5 Nov.
- **Scenario Agent Skills.** "Agent Skills that teach AI coding agents (Claude Code, Cursor, Codex, Copilot, and 70+ others) how to create production-ready content with Scenario through the Scenario MCP server". MIT, 2,516 stars.
- **Gauge CLI.** "An open-source CLI for hillclimbing Agent Experience." It "runs real agents against your product, captures where they get stuck". MIT, 53 stars.
- **shim.** "Tiny local-first AI harness: any model, MCP and Agent Skills, natural-language CLI. Zero dependencies." MIT, created 2 Nov, 452 stars.
- **verdict.** "A 197 KB local semantic verifier for AI agent tool calls. Exit code 0 is not proof." Apache 2.0, created 2 Nov, 236 stars.
