---
title: "Captura: AgentScout Weekly #4 — Auto Review de OpenAI, agent-desktop de Vercel Labs y red-teaming automatizado (AgentScout)"
source: "https://agentscout.beehiiv.com/p/agentscout-weekly-4-openai-auto-review-10-new-ai-agents"
date: 2026-11-08
captured: 2026-11-08T20:09:00+01:00
---

# AgentScout Weekly #4: OpenAI Auto Review + 10 new AI agents

_Captura verbatim de las noticias sustantivas del boletín (4 de noviembre de 2026). Autor: @clampdown19 / AgentScoutHQ._

AgentScout now tracks 2,087 AI agents and 281 MCP servers across 2,699 indexed pages, with every listing link rechecked daily.

**⚡ Breaking Agent & MCP News:** OpenAI's Agents API adds Auto Review for risky commands, Vercel Labs open-sources agent-desktop, and Anthropic sets thousands of Claude agents on red-teaming.

Safer agent runs by default, computer use without screenshots, and agents testing other agents' safety.

🛡️ **OpenAI ships Agents API updates** — Auto Review flags risky commands before they run, async compaction keeps long sessions going, and time awareness lets agents reason about deadlines.

🖥️ **Vercel Labs open-sources agent-desktop** — An Apache-2.0 CLI that lets agents read and operate macOS, Windows and Linux apps through the accessibility tree, acting on stable element refs instead of screenshots.

🧪 **Anthropic automates red-teaming with Claude agents** — Thousands of Claude agents tried to sneak subtly misaligned training data past a safety monitor, and Anthropic is using the results to harden its screens.

## Coming in Hot — New & Featured AI Agents & MCP Servers

🖥️ **Agent Desktop** - Vercel Labs' open source computer-use layer that lets AI agents read and operate desktop apps on macOS, Windows and Linux through the OS accessibility tree.

📈 **SigNoz MCP Server** - Official SigNoz MCP server that lets agents query metrics, traces and logs in plain English, investigate alerts and manage dashboards.

🐘 **PGX** - Lightweight Postgres-compatible database written in Rust that gives every coding agent its own disposable Postgres.

🧩 **xmcp** - Open source (MIT) TypeScript framework from basement.studio for building and shipping MCP servers with file-based tools and prompts.

✋ **Agent Control** - Claude Code hook that makes the agent ask before a Slack post, a CRM edit or a deploy; a no, or no answer, blocks the action.

🚀 **DeployHQ MCP Server** - DeployHQ's hosted MCP server: add one URL to Claude Code, Codex, Gemini CLI or Cursor, sign in, and run your deployments.

📬 **Artil** - Gives each AI agent its own identity: a real email inbox on Artil's domain or yours, plus a dedicated US or UK SMS number on the Pro plan.

🗂️ **Context Nest** - Structured, versioned context vault for AI agents with typed Markdown nodes, selector queries and hash-chained versions.

🧊 **Open Reality** - Turns a handheld phone video into a persistent, queryable 3D scene and exposes it to Claude Code, Codex or Cursor through an MCP server.

## 3-Step Agent Workflow of the Day

**Step 1 — Pick your stack and wire live context:** add Context7 MCP for version-specific library docs and Serena MCP for semantic code retrieval, so the agent works from your real SDK versions and code.

**Step 2 — Paste this MCP config, then isolate the run:** Drop the config below into Cursor, Claude Code or Windsurf. Give each run its own throwaway database with PGX and run generated code inside an E2B sandbox instead of your laptop.

```json
{
  "mcpServers": {
    "agentscout": { "url": "https://agentscouthq.com/mcp" },
    "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] }
  }
}
```

**Step 3 — Gate, trace, then ship:** Put Agent Control in front of deploys so the agent has to ask before it ships, ship through the DeployHQ MCP Server, and check the result with the SigNoz MCP Server before you merge the pull request.
