---
title: "Semana de avisos de seguridad en MCP (GHSA/CVE) y gobernanza AAIF"
source: "jarvisosorio.substack.com"
date: 2026-11-17
captured: 2026-11-25T20:07:00+01:00
---

# What's new in agentic AI this week: standards, security patches and observability (10–17 November 2026)

URL: https://jarvisosorio.substack.com/p/whats-new-in-agentic-ai-this-week
Author: Jarvis Nelson Osorio

## Standards: MCP and Agent Skills under vendor-neutral governance

On 11 November 2026, the Google Open Source Blog published a conversation with Kurtis Van Gent of Google Cloud, a core maintainer of both the Model Context Protocol (MCP) and Agent Skills, and Daryl Ducharme of the Google Open Source Programs Office: "Scaling AI agents with open standards: Kurtis Van Gent on MCP and Agent Skills joining the AAIF" (https://opensource.googleblog.com/2026/11/scaling-ai-agents-open-standards-mcp-aaif.html).

The post describes two complementary open standards. MCP connects agents to live tools and data. Agent Skills load procedural instructions and scripts on demand. Following Anthropic's donation of the Agent Skills specification to the Linux Foundation's Agentic AI Foundation (AAIF) alongside MCP, engineers from Google, Anthropic, OpenAI and the wider ecosystem are now co-maintaining the standard under vendor-neutral governance.

Van Gent argues that MCP commoditized tools, and the unintended consequence was tool and context bloat. Agent Skills address that with progressive disclosure: load only a lightweight YAML frontmatter name and description at startup, and pull the full SKILL.md instructions, reference files or scripts into context only when a task requires them. Skills teach an agent how to approach a problem; MCP is the live execution interface. The post also points to work on Agent Plugins and on serving Agent Skills over MCP, and says what comes next is packaging, discovery, naming-conflict resolution and versioning.

Portable-skill resources: https://agentskills.io, https://github.com/google/skills, https://github.com/agentskills

## Security: a week of MCP advisories

The same week produced a tight cluster of official disclosures around MCP servers, developer workbenches and gateways.

- **11 Nov 2026 — GHSA-6hqx-gqrx-c5r2 (mcp-server-git, high severity).** The reference Git MCP server ran Git commands inside client-chosen repositories without neutralizing the repository's own configuration. Git honors command-bearing keys such as `core.fsmonitor`, so a call to the read-only `git_status` tool on an untrusted repository could execute an attacker-chosen program with the MCP server's privileges. Patched release: mcp-server-git 2026.11.11. Advisory: https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2

- **12 Nov 2026 — GHSA-9w48-x22j-rrm7 (Inspector).** A connected MCP server that answers a JSON-RPC request with an unbounded `text/event-stream` POST response could make the Inspector web backend run out of memory and drop every session on that backend. Affected versions: 2.0.0 through 2.14.0; patch: 2.15.0. Advisory: https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-9w48-x22j-rrm7

- **12 Nov 2026 — CVE-2026-110278 (IBM ContextForge MCP Gateway).** Versions 1.0.0 through 1.1.0. When identity propagation is enabled, a per-server setting that should turn it off is ignored when invoking tools and reading resources. IBM's CVSS base score is 7.4. Fix: 1.1.1; workaround: disable identity propagation globally. Bulletin: https://www.ibm.com/support/pages/security-bulletin-ibm-contextforge-mcp-gateway-affected-information-exposure-vulnerability

- **16 Nov 2026 — GHSA-mqm3-w68j-75mw (AWS Pricing MCP Server).** Before version 1.0.31, the cost-report generation tool could, under certain circumstances, write attacker-influenced content outside the intended output directory. The tool had been annotated as read-only, so auto-approve clients could run it without confirmation. No managed AWS service is affected. Patch: 1.0.31; `readOnlyHint` is now False. Advisory: https://github.com/awslabs/mcp/security/advisories/GHSA-mqm3-w68j-75mw

The pattern is consistent: tool-level trust is still being granted too early, and "read-only" is not a safety property.

## Frameworks and enterprise observability

- Microsoft released Agent Framework Python 1.26.0 (GitHub release dated 13 November 2026; changelog section dated 12 November 2026). Verified additions include `loop_return_final_only` on `create_harness_agent()`; an optional experimental `SecureAgentConfig.message_labeler` callback; structured-output support in the GitHub Copilot integration through `response_format`; and a default 30-second Hyperlight execution budget.
- On 10 November 2026, Microsoft published "Microsoft Ignite 2026: Your Guide to Agent 365", ahead of Ignite (17–20 November 2026). Agent 365 is featured as the observability layer for agents, models and assistants, with session INV642 (18 Nov) and a lightning talk LTG1238 (19 Nov) on managing MCP servers, plugins and skills for AI agents.
