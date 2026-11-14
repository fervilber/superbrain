---
title: "OWASP Global AppSec: la seguridad de MCP sigue siendo un desastre — ejecución arbitraria en STDIO y mercados sin validación"
source: "https://www.scworld.com/resource/owasp-global-appsec-mcp-security-still-a-mind-boggling-mess"
date: 2026-11-14
captured: 2026-11-14
---

# OWASP Global AppSec — «MCP security still a mind-boggling mess» (SC Media, 13 de noviembre de 2026)

Captura del artículo de Paul Wagenseil (SC Media). La charla se impartió en el OWASP Global AppSec de San Francisco del 5 de noviembre de 2026 por Moshe Siman Tov Bustan, jefe del equipo de investigación de seguridad de OX Security.

## El diagnóstico

> The ecosystem that's grown up around the Model Context Protocol (MCP) AI connectivity standard is a poorly governed mess, with fundamental security flaws and sloppy governance issues that are not being fixed, a security researcher said in a presentation at the OWASP Global AppSec conference in San Francisco Nov. 5.

> One issue is an unresolved vulnerability in the way MCP handles commands among MCP clients and servers on the same machine. "A year ago, we found a new attack surface that almost nobody knew about," said Bustan, referring to the flaw. "You could swap in a malicious command without anyone noticing."

> Another weakness is that there's no system to validate remote MCP servers, which can be run from anywhere, including from hostile countries or home proxy networks. A related one is that many MCP configuration marketplaces don't verify the security of what they distribute.

> Tighter controls could fix these problems, said Bustan, but neither MCP creator Anthropic nor many of the entities distributing MCP configurations, skills and tools seem interested. [...] But with millions of "vibe coders" throwing together applications quickly, Bustan worries the inherent MCP flaws may be creating problems that will never be tamed.

> "Developers are not security engineers," Bustan and his colleagues wrote in a white paper. "We cannot expect tens of thousands of implementers to independently discover and mitigate a flaw that is baked into the official SDKs [software development kits] they trust."

## La superficie

> "MCP is everywhere," said Bustan. "Every AI agent you use now is going to connect to an MCP server. And it's naturally going to attract hackers."

> The official MCP software development kit has been downloaded 150 million times, Bustan said. There are 100,000 MCP server configurations in online marketplaces. And, he added, MCP isn't just one project — instead, it's hundreds of specialized projects.

> This is quite a triumph for a standard first released just two years ago. Anthropic made MCP free and public from the start, and even rivals like OpenAI and Microsoft soon adopted it to connect their LLMs and AI agents to other applications and resources.

## El fallo concreto en STDIO

> MCP clients can connect to MCP servers in one of two ways. When the server is remote, they use HTTP or HTTPS, standard web protocols. When the client and server are on the same machine or the same local network, they use the standard input/output, or STDIO, protocol. So far, so good. But Bustan's team stumbled across something scary: They found that they could paste any command, including one that had nothing to do with MCP, in a local MCP interface to create a new local STDIO MCP server. A non-MCP command would not create a new server, and the interface would return an error message, but the command would execute anyway. "When a command is received to start a process, there's no validation that that command is allowing an arbitrary command to be executed instead of a command that explicitly starts an MCP STDIO server," notes the OX Security white paper on the topic.

> The team created a proof-of-concept MCP [server and submitted it to 11 MCP marketplaces].

## Recomendaciones de OX Security

> To mitigate against this issue in your own instances of MCP, OX security recommends running all MCP services in a sandbox, using only MCP tools and skills that come from official repositories, blocking access to sensitive data, monitoring tool invocations and treating all external MCP configuration input as untrusted.

> The flexibility, openness and simplicity of MCP are key to its success. But that's led to some well-documented security flaws, such as "tool poisoning" resulting from a lack of verification of MCP tool manifests, remote code execution from malicious servers, and authentication flaws in MCP developer tools.
