---
title: "Google Cloud developer plugin en el Marketplace de Antigravity: skills preautorizadas y guardrails para agentes"
source: "https://aiagentstore.ai/ai-agent-news/2026-november"
date: 2026-11-02
captured: 2026-11-03
---

# Google Cloud plugin in Antigravity Marketplace: pre-authorized cloud developer skills and safety for agents

Captura verbatim del boletín diario AI Agent Store (3 de noviembre de 2026), sección correspondiente al anuncio del 2 de noviembre de 2026.

## What changed

Google Cloud published a blog announcing the `google-cloud-developer` plugin is available in the Antigravity Marketplace (Nov 2). The plugin bundles curated skills, live documentation grounding via a pre-authorized Developer Knowledge MCP server, and safety/cost guardrails (IAM checks, blocking destructive CLI commands) to make cloud-focused agents safer and more accurate out of the box.

## Why it matters

If you're running coding or ops agents that interact with Google Cloud, this lets you ground agent answers in live docs and adds execution checks that reduce dangerous or outdated commands—so product teams and consultants can deploy agents with fewer custom safety filters and faster time to safe production.

## Contexto de la jornada (mismo boletín, 3 de noviembre de 2026)

### Agentic engineering assistant blueprint: AWS shows how to build a multi-agent system for regulated engineering workflows

What changed: AWS published a hands-on Machine Learning blog that provides a full recipe (five Jupyter notebooks + GitHub repo) for a multi-agent engineering assistant built with Amazon Nova Multimodal Embeddings and Amazon Bedrock AgentCore. The pattern uses a planner and three specialist agents (Catalog, Evaluation, Knowledge), deterministic Python checks for spec/tolerance rules, visual similarity via Nova embeddings, and AgentCore Evaluations for continuous online scoring.

Why it matters: The post is a practical, production-oriented example you can reuse: it explains how to combine deterministic checks (so results can feed formal reviews) with agentic retrieval and modular specialists, and it shows how to deploy and instrument agents for continuous quality tracking—useful for founders and operators in regulated industries who need auditable, repeatable agent behavior.

Try / watch: watch tool-selection accuracy and how the evaluation handles safety prompts (the post notes correct refusals lower "goal success" scores if your evaluator treats refusals as failures).
