---
title: "Versionar herramientas MCP sin romper agentes en ejecución (Scalekit, 4 de noviembre de 2026)"
source: "https://www.scalekit.com/blog/mcp-tool-versioning"
date: 2026-11-04
captured: 2026-11-04
---

# Versioning MCP Tools Without Breaking Running Agents

Scalekit — Nishant Choudhary, 4 de noviembre de 2026. Captura verbatim. Extraído vía `web_extract`.

A tool named `search_issues` had, for six months, a description that read "Search Jira issues by JQL." Someone on the server team changed it to "Search Jira issues by JQL. Prefer this over listing issues when the user mentions a project." The schema did not change. The version string did not change. No client noticed, because there was nothing in the protocol for them to notice.

Within a week, three agents that had been calling `list_issues` to build a daily digest started calling `search_issues` instead, with JQL the model improvised, returning fewer results, with no error anywhere. The behavior change shipped in a sentence.

## TL;DR

- An MCP tool has four things that version independently: the protocol revision, the server package version, the tool's input and output schema, and the tool's description. Only the first two have an agreed versioning scheme. The description, which is the one that most often changes agent behavior, has none.
- Most agent harnesses call `tools/list` once per session and cache the result. Whether your change reaches a running agent depends on the client, not on you.
- The 2026-07-28 protocol revision made MCP stateless over HTTP. The long-lived stream that `notifications/tools/list_changed` relied on is now a legacy-era mechanism; clients on the modern revision discover changes by re-listing. Design for re-listing, not for push.
- Classify every change as additive, behavioral or breaking, and treat behavioral changes (description edits) with the same discipline as breaking ones. A new description is a new tool in everything but name.
- The reliable pattern is to version the surface, not the tool: ship a new scoped server for the new behavior, point new runs at it, and retire the old one when no run depends on it. A Virtual MCP server, defined once per agent role with a static URL, is that pattern by construction.

## Four axes, two of them governed

When someone says "we versioned the MCP server," they usually mean one of four different things.

| Axis                   | What it governs                               | Who sets it           | Versioning scheme                                                                                                         |
| ---------------------- | --------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Protocol revision      | Wire format, transport, lifecycle             | The MCP specification | Dated revisions, with a feature lifecycle and a 12-month minimum deprecation window                                       |
| Server package version | What the client installs or connects to       | The server publisher  | SemVer in server.json, recommended by the registry                                                                        |
| Tool schema            | `inputSchema`, output shape                   | The server author     | None agreed; proposed registry guidance is that names stay stable across minor versions and schema breaks require a major |
| Tool description       | How the model decides when and how to call it | The server author     | None                                                                                                                      |

The first two axes are solved problems with tooling. The 2026-07-28 revision introduced a formal feature lifecycle: anything deprecated in that revision cannot be removed before roughly August 2027. The specification's own versioning [continues].

## Notas adicionales de la fuente

- Client support was uneven for over a year: Claude Code only honored the notification from version 2.1.0 in February 2026, Cursor's CLI still had an open request for it in 2026, and stateless HTTP wrappers that treated `tools/list` as cacheable on a TTL never saw it at all.
- The 2026-07-28 revision removed the initialize handshake and protocol-level sessions; protocol version and client info travel per request in `_meta`, and `Mcp-Method` and `Mcp-Name` are required headers on every call. Server-initiated requests are only permitted while the server is processing a client request.
- The model's belief that a tool exists is not evidence that it was disclosed. This matters for additive changes mid-session.
