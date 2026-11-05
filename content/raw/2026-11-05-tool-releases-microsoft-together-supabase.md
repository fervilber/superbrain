---
title: "Lanzamientos de herramientas: Foundry Local con Qwen3.8-27B, Together Compiler y Supabase MCP 0.16.0"
source: "https://theagenticweekly.com/news/tools"
date: 2026-11-05
captured: 2026-11-05
---

# AI tool release news, updated Nov 5, 2026

The Agentic Weekly, 5 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract`.

Tool releases only: 56 briefs on new versions of AI tools and agent software from 39 vendors, newest first.

- **Mistral Studio adds managed agents, a workflow builder and HTTP connectors** · Reported · Mistral AI · first seen 2026-11-05 15:49 UTC. On November 5, 2026 Mistral expanded its Studio enterprise platform with managed agents and apps, plus new workflow, enterprise context, observability and evaluation features. Mistral says Studio can run in its cloud, a customer VPC or on-premises, and that one internal workflow built on it saves its product operations team about 35 hours a week.
- **Microsoft Foundry Local runs Qwen3.8-27B as a local coding model inside GitHub Copilot** · Reported · Microsoft · first seen 2026-11-05 14:27 UTC. Microsoft says "Foundry Local brings agentic coding directly to developer hardware": its November 5, 2026 post shows Foundry Local CLI 0.13.0 or later running a 4-bit Qwen3.8-27B (about 18 GB) on NVIDIA GPUs with 24 GB or more of VRAM, connected to GitHub Copilot as a Bring Your Own Key model provider.
- **Supabase MCP server 0.16.0 turns on notebook tools for agents** · Reported · Supabase · first seen 2026-11-05 14:28 UTC. Supabase released mcp-server-supabase 0.16.0 on November 5, 2026. It enables the `create_notebook` and `run_notebook` tools by default, adds `delete_notebook` with an elicitation confirmation, lets agents run selected notebook cells, and bounds `run_notebook` cost (notebooks with more than 50 cells are refused).
- **Semantic Kernel python-1.47.0 drops Python 3.10, adds MCP and agent fixes** · Reported · Microsoft · first seen 2026-11-05 12:57 UTC. Microsoft released Semantic Kernel python-1.47.0 on November 5, 2026.
- **Together Compiler: agent-driven continual compilation for production inference** · Reported · Together AI · first seen 2026-11-05 08:57 UTC. Together AI announced Together Compiler on November 4, 2026: agents propose GPU forward-pass changes that a persistent engine verifies before shipping. Compiled kernels are on by default for supported serverless models at the same price; Together claims 1.3 to 3x Blackwell throughput vs the best open engines after under 24 hours of compilation.
- **Dify 1.19.0 adds nested workflow tracing, portable Workflow Tools and Skill commands in difyctl** · Reported · LangGenius · first seen 2026-11-04 10:04 UTC. Dify 1.19.0, published November 4, 2026 (UTC), sends nested workflow traces to observability tools: "Child steps appear beneath the Tool span that invoked them, preserving the hierarchy across nested and repeated calls." Self-hosted installs now need Docker Compose 2.35.0 or later.
- **Agent Autoloop 1.0 runs Claude Code and Codex in the background** · Reported · Agent Autoloop (open source) · first seen 2026-11-04 02:06 UTC. An MIT-licensed open-source project, tagged v1.0.0 on GitHub on November 3, 2026. It runs command-line agents such as Claude Code and Codex in the background from schedules and events, and its README says "Any CLI tool that takes a prompt and prints a final reply can plug in."
- **llama.cpp v0.9.0 adds FP8 E4M3 quantization, Mistral Large 4 and Chatterbox TTS** · Reported · ggml-org · first seen 2026-11-04 13:17 UTC. Adds an OCP FP8 E4M3 quantization type, support for four new architectures (Clover, Limite, Metis-1.6 and Mistral Large 4), Chatterbox TTS and Nemotron 3.5 Transcribe, and updates its ggml library to v0.29.0.
