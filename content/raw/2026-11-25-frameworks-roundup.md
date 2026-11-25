---
title: "Frameworks for AI agents — roundup (Claude Code, Pydantic AI, OpenHands, Sierra)"
source: "aiagentnews.io"
date: 2026-11-25
captured: 2026-11-25T20:06:00+01:00
---

# Frameworks for AI agents | AI Agent News

URL: https://aiagentnews.io/topics/frameworks

## Nov 24 — Claude Code v2.1.332 adds skills from MCP servers and a skill shell hook

Anthropic has released Claude Code v2.1.332, which adds beta support for skills served by MCP servers and a new hook that can block a skill's inline shell commands. The release also fixes a range of freezes and hangs and changes which Sonnet and Opus versions several cloud providers and aliases resolve to.

## Nov 24 — Pydantic AI v2.74.0 adds computer use support across sandboxes and models

Pydantic AI released v2.74.0, which adds a core computer tool contract and desktop support for computer use across several sandbox providers. The release also changes how GPT-6.2 instructions and Gemini streaming usage totals are handled, so some existing code may behave differently.
github.com/pydantic/pydantic-ai/releases/tag/v2.74.0

## Nov 24 — datasette-agent 0.7a1 improves side panel navigation with fragment hashes

datasette-agent 0.7a1, an LLM-powered agent for Datasette built by Simon Willison, changes how chat session side panels navigate between pages by using fragment hashes. The change is meant to support closer integration with other Datasette plugins that update fragment hashes when their state changes.
simonwillison.net/2026/Nov/24/datasette-agent

## Nov 24 — Hermes Agent v0.23.4 ships patch across CLI, Store app, Docker and Cloud

NousResearch has released Hermes Agent v0.23.4, a patch that rolls up about 229 merged pull requests since v0.23.3. The release covers the GitHub release and CLI, the Microsoft Store app, Docker and Hermes Cloud, while full curated notes are deferred to v0.24.0.

## Nov 24 — Sierra closes $1.75B Series F led by Greenoaks and Lightspeed

Sierra Technologies has closed a $1.75 billion late-stage investment, its Series F round led by Greenoaks and Lightspeed. The round follows an annualized revenue figure above $400 million that the company disclosed a few weeks earlier.
siliconangle.com/2026/11/23/ai-agent-provider-sierra-closes-1-75b-investment-amid-rapid-revenue-growth

## Nov 24 — OpenHands v1.45.0 adds Projects in Canvas and nested sub-agent conversations

OpenHands released v1.45.0 on 24 November with an experimental Projects feature in Canvas and nested sub-agent conversations in the frontend. The release also adds factory worklogs and deletion, and fixes a range of mobile, accessibility and settings bugs.
github.com/OpenHands/OpenHands/releases/tag/v1.45.0

## Nov 23 — Pydantic AI v2.73.0 raises OpenAI floor and adds agent capability overrides

Pydantic AI v2.73.0 adds capabilities to Agent.override, voice instructions for GPT-Live realtime sessions, and a warning for requests to deprecated models. The release also raises the minimum openai version to 3.50.0 and changes how some model settings are sent.

## Nov 23 — OpenAI Agents Python SDK v0.26.0 changes Docker mounts and Realtime tracing

OpenAI has released v0.26.0 of its Agents Python SDK with changes to Docker mounts and Realtime tracing.

---

## Frameworks for AI agents (resumen previo, aiagentnews.io)

### AWS Quick adds conversational flow building, a redesigned web app and multi-agent orchestration

AWS has released updates to Quick, its AI workspace, including flows that can be built and refined in chat, a reworked web app with a daily briefing, and multi-agent orchestration that combines answers from several specialized agents. The release also adds Meta ads and Amplitude connectors, guardrails for prompts in preview, and support for four more languages.

### Agno v3.2.0 adds direct tools to Super Agent and moves A2A to protocol v1.0

Agno has released v3.2.0, which lets Super Agent do work itself with direct tools instead of routing requests through manager members. The release also moves A2A to the v1.0 protocol, switches the Slack interface to Slack Bolt, and makes external agents storable components.

### Google's ADK Python v2.14.0 makes sandboxes, A2A and evaluation stable

Google's adk-python v2.14.0 graduates execution environments, the A2A integration and evaluation modules from experimental status. The release also adds multi-run evaluation, semantic tool argument matching, and Microsoft Teams and OpenAI Decisions integrations.
