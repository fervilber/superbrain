---
title: "AI Agents Info: AI agent frameworks — 13 MCP clients, 5 servers, 6 A2A"
source: "https://www.aiagentsinfo.com/research/ai-agent-framework-mcp-a2a-support-november-2026"
date: 2026-11-16
captured: 2026-11-16
---

# AI agent frameworks: 13 MCP clients, 5 servers, 6 A2A (13 de noviembre de 2026)

Autor: AI Agents Info Editorial. Capturado el 2026-11-16.

## Key takeaways (verbatim)

> - All 13 frameworks in this note document an MCP client on an official docs page read November 13, 2026.
> - Five document exposing the agent, or a workflow, over MCP: LangGraph Agent Server at /mcp, Google ADK, Pydantic AI, Mastra's MCPClient and MCPServer, and LlamaIndex's workflow-to-MCP-app example.
> - Six document A2A on a page that matches the installable release: CrewAI 1.15.41, Google ADK, Microsoft Agent Framework, Mastra, Agno, and Strands. smolagents 1.26.0's docs say the A2A page does not exist in that version.
> - docs.ag-ui.com/integrations lists 11 names that overlap this set. smolagents, the Vercel AI SDK, and AutoGen are not on that list. AG2 is, and AG2 is not AutoGen's repository.
> - PyPI agent-framework 1.26.0 was uploaded 2026-11-12T18:25:37Z. GitHub's latest release is python-1.25.0, published 2026-11-07, and GET /releases/tags/python-1.26.0 returned 404.

## Abstract / summary (verbatim)

> Thirteen agent frameworks with a current installable release document an MCP client. Five document a way for the agent to be the MCP server: LangGraph Agent Server, Google ADK, Pydantic AI, Mastra, and a LlamaIndex workflow turned into an MCP app. Six document A2A in the docs that match the installable release: CrewAI, Google ADK, Microsoft Agent Framework, Mastra, Agno, and Strands. Agno's page documents exposing an agent. The other five document calling a remote agent and serving one.

> An MCP client lets the agent call a tool server. An MCP server lets some other client call the agent. A2A is a third wire, agent to agent, and it is the short list. AG-UI is a fourth, and most of the "support" is an adapter named on docs.ag-ui.com/integrations, not a module inside the framework package.

## Tabla de soporte (verbatim)

| Framework                        | MCP client | MCP server   | A2A           | AG-UI               | Streaming              | Human in the loop | Tracing or evals |
| -------------------------------- | ---------- | ------------ | ------------- | ------------------- | ---------------------- | ----------------- | ---------------- |
| LangGraph 1.2.21                 | Yes        | Agent Server | —             | LangChain is listed | Yes                    | Yes               | LangSmith        |
| CrewAI 1.15.41                   | Yes        | —            | Yes           | Listed              | —                      | —                 | —                |
| OpenAI Agents SDK 0.24.0         | Yes        | —            | —             | Listed              | Yes                    | Yes               | —                |
| Google ADK 2.14.1                | Yes        | Yes          | Yes           | Listed              | —                      | Yes               | —                |
| Microsoft Agent Framework 1.26.0 | Yes        | —            | Yes           | First-party docs    | Yes, on the AG-UI page | Yes               | —                |
| AutoGen 0.7.5                    | Yes        | —            | —             | Not listed          | —                      | —                 | —                |
| LlamaIndex 0.14.25               | Yes        | MCP app      | —             | Listed              | —                      | —                 | —                |
| Pydantic AI 2.68.0               | Yes        | Yes          | —             | Listed              | —                      | Yes               | —                |
| Mastra 1.83.0                    | Yes        | Yes          | Yes           | Listed              | —                      | —                 | —                |
| Agno 3.2.0                       | Yes        | —            | Expose        | Listed              | —                      | —                 | —                |
| smolagents 1.26.0                | Yes        | —            | Not in 1.26.0 | Not listed          | —                      | —                 | —                |
| Strands 1.64.0                   | Yes        | —            | Yes           | Listed              | —                      | —                 | —                |
| Vercel AI SDK 7.0.171            | Yes        | —            | —             | Not listed          | Yes                    | —                 | —                |

## Por qué importa (verbatim)

> A framework comparison that stops at stars, downloads, or the latest tag cannot tell a builder whether the library can call a tool server, be the tool server, or talk to another vendor's agent. Those are three different wires. MCP client is the common one. MCP server and A2A are the short lists. Treating an AG-UI adapter in someone else's repository as a feature of langgraph 1.2.21 is how the matrix lies.

> Call MCP when the agent needs someone else's tools. Every framework in the table documents that, and the docs are not interchangeable. CrewAI wants an `mcps` list. ADK wants `McpToolset`. The OpenAI SDK wants a hosted tool or a transport class. Copying one project's snippet into another project is how the tool call fails before the model sees it. Expose MCP when some other host, a coding agent or a second product, has to call your agent. The list is Agent Server, ADK, Pydantic AI, Mastra, and the LlamaIndex MCP app. Use A2A when the other party is an agent with its own card, not a tool with a JSON schema. On the installable docs, that is CrewAI, ADK, Microsoft Agent Framework, Mastra, Agno, and Strands.
