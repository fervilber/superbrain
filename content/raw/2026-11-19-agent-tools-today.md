---
title: "Agent Tools Today (19 Nov 2026): GPT-6.2 Astra and Sol, Gemini 4 Neon and MAI Code 2"
source: "https://munderdiffl.in/blog/agent-tools-today-2026-11-19/"
date: 2026-11-19
captured: 2026-11-19
---

# Agent Tools Today, 19 Nov 2026

Chaitanya Giri — 19 nov 2026, 5 min. Los principales lanzamientos, skills, movimientos multiagente, repos en ascenso y temas de conversación en agentes de IA del 16 al 19 de noviembre de 2026, cada uno con su fuente y fecha.

Agent tools today, 19 Nov 2026, in one line: OpenAI shipped GPT-6.2 Astra and Sol, Google launched Gemini 4 Neon, and Microsoft released MAI Code 2. It covers the three days since the 16 Nov brief (no brief shipped 17 or 18 Nov), 16 Nov 04:00 UTC to 19 Nov 04:00 UTC, checked 19 Nov.

## Top 5 launches

1. **GPT-6.2 Astra and Sol.** OpenAI's model pages call Astra "Our most capable model for your hardest projects". Both list a **1,050,000 token context window**. Astra costs **$8 per million input tokens and $40 per million output**; Sol costs **$2 and $10**, checked 19 Nov. Above **272K input tokens**, "input and cache rates double". 1,337 points on Hacker News, posted 17 Nov at 17:46 UTC.
2. **Gemini 4 Neon.** Google's post, dated 18 Nov, prices it at **$3 per million input tokens** and **$15 per million output tokens, with a 1 million-token context window**. It ranks Neon **#1 overall on the Artificial Analysis Coding Agent Index (58.6)**: Google's own figures. 540 points on Hacker News, posted 18 Nov at 21:34 UTC.
3. **MAI Code 2 and MAI Code 2 Flash.** Microsoft AI's post, dated 17 Nov, says MAI Code 2 gives **"98% of the performance of GPT-6.1 Sol at 40% of the cost"**, with cost "shown at its 50% promotional price": Microsoft's own figures. Both are "explicitly not yet tuned" for "very long-horizon agentic work", and both are in GitHub Copilot. They are two of seven new models Microsoft released for Ignite. 417 points on Hacker News, posted 17 Nov at 18:25 UTC.
4. **Claude Code v2.1.326 to v2.1.328.** Three releases, from 16 Nov at 22:11 UTC to 19 Nov at 01:14 UTC. v2.1.327 adds `claude mcp add-json -`, which reads JSON from stdin "so tokens can stay off the command line"; it is "not available inside a Claude Code session". v2.1.328 lets `mcp_tool` hooks take `"onFailure": "block"`: "a hook whose call fails blocks the action".
5. **OpenCode v2.3.1 and v2.3.2.** Published 18 Nov. In v2.3.1, a shell command still running at its timeout "now moves to the background instead of being killed". v2.3.2 stops GPT-6.2 models "re-billing the system prompt as uncached input on every step": on GitHub Copilot `gpt-6.2-sol`, uncached input per step "dropped from about 14,000 tokens to 3". A good week for a cache.

## Top 2 skills, MCP servers and plugins

1. **OpenCode Browse v0.1.0.** New since the 9 Nov brief: v0.1.0, published 16 Nov at 16:47 UTC, rewrites it "in Rust: one small binary for the CLI, relay and MCP server". Agents use "your real browser, with your tabs, your logins and your extensions", its page says. 331 points on Hacker News, posted 16 Nov at 21:20 UTC; MIT, 912 stars.
2. An **agent skill that researches a topic across social sites, YouTube, Hacker News, Polymarket and the web**, its repo says. v4.3.0, published 16 Nov at 23:57 UTC, leads entity topics "with their most interesting markets". 1,059 stars in a day on GitHub trending on 19 Nov, 70,140 in total; MIT.

## Top 2 moves from multi agent tools

1. **Paperclip v2026.1117.0.** Published 18 Nov at 22:20 UTC, it "carries 1,586 commits". "The Coordinator layout and Agent Chat are now standard", and task chat "shows what a Runner agent actually did". Planning runs put Codex and Claude "into their native plan mode", and Approve resumes the agent. The built in Google Workspace connector "is off by default".
2. **Agent Relay v18.10.0.** Published 17 Nov at 19:17 UTC. It adds "support native GitHub Copilot desktop sessions" and lets "sessions in an organization's repositories join by themselves".
