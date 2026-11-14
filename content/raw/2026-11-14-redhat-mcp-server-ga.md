---
title: "Disponibilidad general del servidor MCP para Red Hat Enterprise Linux: diagnóstico con Performance Co-Pilot"
source: "https://www.redhat.com/en/blog/announcing-general-availability-mcp-server-red-hat-enterprise-linux"
date: 2026-11-14
captured: 2026-11-14
---

# MCP server para Red Hat Enterprise Linux en GA (Red Hat Blog, 11 de noviembre de 2026)

Captura por extractos del post de Brian Smith.

## Del Developer Preview a GA

> System administrators and developers have long relied on a mix of specialized tools, deep knowledge, and hard-earned intuition to keep Red Hat Enterprise Linux (RHEL) environments running smoothly. But as hybrid cloud footprints grow and infrastructure becomes more complex, finding the root cause of an issue can feel like searching for a needle in a digital haystack.

> To help with this, earlier this year, we introduced the Developer Preview of Model Context Protocol (MCP) server for Red Hat Enterprise Linux — a bridge that connects large language models (LLMs) directly to your RHEL infrastructure. Today, we are thrilled to announce that the MCP server for Red Hat Enterprise Linux is now generally available (GA). Along with this milestone, we are introducing powerful new performance diagnostics capabilities backed by the Performance Co-Pilot (PCP) tool.

## Propiedades del producto

> With the GA release, administrators now have a supported, production-ready toolset, which provides read-only tools by default. The MCP server for RHEL is available as a container image in the Red Hat container registry. It is also available as an RPM package in the RHEL extensions repository for use with the `goose-redhat` or `goose` packages, which are available in the same repository. Packages in the extensions repository are provided under the Red Hat Extensions Repository Support Policy.

> The MCP server allows your AI assistant to access system logs, assess disk usage, analyze process state, and retrieve information on many other aspects of RHEL systems. This lets it help with troubleshooting issues such as a service failing, a filesystem nearing capacity, and more.

## Diagnóstico profundo con PCP

> Troubleshooting isn't just about reading static logs. It's often about understanding system performance. To give your AI assistants a deeper understanding of past system metrics, we are excited to announce the integration of Performance Co-Pilot (PCP) tools into the MCP server.

> PCP is available in RHEL and can help track system performance. Previously, the MCP server for RHEL only included tools to retrieve the current real-time performance information. Now, you can use the new PCP tools to query past performance metrics to help analyze and troubleshoot past performance issues.

> Using the goose AI agent (available in the RHEL extensions repository) connected to a locally hosted LLM, I asked for help troubleshooting a recurring performance issue on a RHEL 10 system with this initial prompt: "I'm getting reports that this system is slowing down every few minutes. Take a look and determine likely root [cause]".

## Ejecución de comandos con guardas

> You can now run the MCP server centrally, allowing multiple users to share it. [...] Earlier in the year, we introduced guarded command execution to the MCP server, allowing LLMs to dynamically generate and run commands or scripts to enable more complex use cases. You can still optionally enable this feature to test it out, under the Developer Preview scope of support.
