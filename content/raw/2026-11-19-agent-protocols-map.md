---
title: "MCP, A2A, UCP, AP2... A Simple Map of AI Agent Protocols (November 2026)"
source: "https://dev.to/gde/mcp-a2a-ucp-ap2-confused-a-simple-map-of-ai-agent-protocols-november-2026-3ph"
date: 2026-11-15
captured: 2026-11-19
---

# MCP, A2A, UCP, AP2... Confused? A Simple Map of AI Agent Protocols (November 2026)

Karthigayan Devan for Google Developer Experts — 15 nov 2026.

MCP. A2A. AG-UI. A2UI. UCP. AP2. ACP. x402. And as of this week, Poppy. If your head spins every time a new agent protocol drops, you're not alone. Even the acronyms collide: "ACP" now means at least two different things depending on who you ask. Here's the good news: these protocols are not competing with each other. They are layers, like the network stack. Once you see the layers, the whole thing clicks.

## TL;DR: one question picks the protocol

Ask yourself: what is my agent talking to?

| My agent is talking to... | Use this     | In one line                                       |
| ------------------------- | ------------ | ------------------------------------------------- |
| Tools and data            | MCP          | Plug the agent into APIs, databases and files     |
| Another agent             | A2A          | Hand off work to an agent someone else built      |
| A user's screen           | AG-UI / A2UI | Show the user what the agent is doing, live       |
| A store or business       | UCP          | Search, cart, checkout and orders in one standard |
| A payment                 | AP2          | Prove the user really approved the purchase       |

## The stack at a glance

```
+---------------------------------------------------+
|  USER          AG-UI (live events) / A2UI (UI)     |
+---------------------------------------------------+
|  PAYMENTS      AP2 (signed mandates), x402         |
+---------------------------------------------------+
|  COMMERCE      UCP (catalog, cart, checkout)       |
+---------------------------------------------------+
|  AGENTS        A2A (agent to agent)                |
+---------------------------------------------------+
|  TOOLS         MCP (agent to tools and data)       |
+---------------------------------------------------+
```

One agent can use all five layers in a single task.

## Layer 1: MCP, the agent's hands

Model Context Protocol (MCP) connects an agent to tools and data: your database, GitHub, Slack, a weather API, anything. Build an MCP server once, and any MCP-compatible agent can use it.

**What's new:** the current spec is **2026-07-28**, and it's the biggest change yet. MCP moved from a stateful, session-based protocol to a **stateless request and response protocol**. What that means in practice:

- **No more sessions.** The session handshake is gone, so any request can go to any server instance. Great news for anyone running MCP servers behind a load balancer.
- **A new discovery call.** Clients can ask a server what it supports before sending other requests.
- **Some features are deprecated.** Roots, Sampling and Logging are now deprecated, and Tasks moved out of the core into an official extension.
- Old transport is on the way out.

## Brand new this week: Poppy

On **November 13, 2026**, Sierra released **Personal Agent Protocol 1.0**, nicknamed **Poppy**. It defines how your personal AI agent connects to a business, through its website, its APIs or the business's own agent. It came out of a draft shared in October and developed with Meta. It's two days old, so treat it as one to watch, not one to build on yet. But it points at where things are going: your agent talking to their agent.

## What's still missing (the honest part)

1. Start with **MCP**. Almost every agent needs tools. This is the one to learn first.
2. Add **AG-UI** or **A2UI** when a human watches the agent or needs to approve things.
3. Add **A2A** only when you work with agents you don't own. If all your agents live in one codebase, you probably don't need it yet.
4. Add **UCP** and **AP2** if your agent shops, books or pays. Start with a pilot, and follow the specs closely, because they're moving fast.

Rule of thumb: **MCP by default, A2A at the boundary, UCP and AP2 at the checkout.**

## For Google Cloud developers

Several of these protocols started at Google: A2A, UCP (with Shopify) and AP2, plus A2UI. Google's Agent Development Kit (ADK) works with MCP for tools and A2A for agent collaboration, and AP2's official guide pairs ADK, MCP, A2A and AP2 as one stack.

## Caveats

- Everything here is as of **November 15, 2026**. These specs change monthly.
- Some items are drafts or previews: A2A v1.1, UCP lodging and food, AP2 v0.2, and Poppy.
