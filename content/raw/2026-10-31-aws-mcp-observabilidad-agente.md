---
title: "Why MCP servers should tell agents what to do next (The New Stack) — captura"
source: "https://thenewstack.io/aws-mcp-agent-observability"
date: 2026-10-29
captured: 2026-10-31
---

# Why MCP servers should tell agents what to do next

> Captura del artículo patrocinado por AWS Marketplace, publicado en The New Stack el 29 de octubre de 2026 por Matthew Burns. La pieza recoge la intervención de **James Ward** (AWS) en conferencia. El extractor devolvió navegación del sitio y el cuerpo parcialmente truncado; se reproduce el tramo sustantivo.

## La tesis: la respuesta de la herramienta debe llevar guía

In practice, that means **a tool response carries guidance with the data**. It tells the agent what it just did, what it might want to do next, and where to find more.

The other half of his pitch is **visibility**. Web developers can trace a click on a page all the way down to the database. **"MCP by default doesn't have any way to do trace ID," Ward said.**

## El workaround: parámetros de sesión y de objetivo

The workaround AWS uses is rather low-tech. **Add a session ID parameter to the tools and tell the agent to pass it on every call**, so individual calls can be stitched into one journey. **A second parameter can carry the user's prompt or a summary of their goal.** Teams can then compare what the user wanted with the path the agent took, build an eval around it, adjust a tool description or parameter, and measure whether more tasks get completed. Ward said AWS built much of this for the MCP servers its own developers use.

## Cronología del MCP Server de AWS

In May, AWS opened its MCP Server to everyone and added **Lambda diagnostics in September**. In an **Agentic AI Foundation profile** published before the conference, Ward described an agent fetching customer records one at a time because the server only offered a one-record tool. Watching the full journey is how teams spot that pattern and build a **batch tool** to fix it.

## MCP no es la única vía

Ward didn't present MCP as the only solution. AWS also ships **a CLI and skills**, he said, partly because **MCP's OAuth model can't toggle between AWS user profiles the way the CLI can**. Which works best depends on the model, the tool descriptions, and how the agent discovers tools, so AWS tests them against each other with **evals**.

## Cierre

None of this is exotic, and Ward knows it. "There's nothing new under the sun," he said. **Observe the journey, reproduce it, measure it, and improve it.** The difference is that teams now have to understand the path a human and an agent take together, and test whether changes to their tools actually help them finish the task.
