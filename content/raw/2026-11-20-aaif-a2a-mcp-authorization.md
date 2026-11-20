---
title: "Diseño de autorización segura a través de A2A y MCP"
source: "https://aaif.io/blog/designing-secure-authorization-across-a2a-and-mcp"
date: 2026-11-19
captured: 2026-11-20
---

# Designing secure authorization across A2A and MCP

Yasutaka Mitsumoto & Yoshiyuki Tabata — Agentic AI Foundation (AAIF) — 19 de noviembre de 2026

As AI agents become more widely adopted, the Agent2Agent (A2A) and Model Context Protocol (MCP) specifications continue to evolve, alongside a growing ecosystem of services that implement them. As agents take on more business processes and access more data, establishing secure communication becomes increasingly important.

AI agents do not always complete their work in isolation. Within a single task, an agent may delegate work to a specialized agent through A2A or access tools and data through an MCP server. The official A2A documentation describes A2A as complementary to MCP: the two protocols address distinct but related aspects of agent interactions. The A2A and MCP documentation explains this relationship in _A2A ❤️ MCP: Complementary Protocols for Agentic Systems_ and illustrates their combined use in _Example Scenario: The Auto Repair Shop_. In systems that combine A2A and MCP communication, differences in the protocols' security requirements can introduce vulnerabilities.

When authorization is implemented for a remote MCP server using an HTTP-based transport, MCP recommends following its OAuth 2.1-based authorization specification. By contrast, when OAuth is used to protect A2A, PKCE is recommended but not mandatory (A2A §4.5.8), and does not mandate compliance with OAuth 2.1. If the A2A implementation permits less secure authorization flows, access tokens may be stolen and used by third parties. Inadequate token audience validation or downstream delegation can further allow unauthorized access to other MCP servers or API servers. OAuth is only one example: A2A also permits API keys, which can make these security concerns even more pronounced.

This article draws on MCP's authorization security considerations to examine vulnerabilities and mitigations in systems that combine A2A and MCP. It then proposes an OAuth security baseline for A2A implementations.

## Protocol versions

| Protocol  | Referenced version or document |
| --------- | ------------------------------ |
| A2A       | v1.0.1                         |
| MCP       | 2026-07-28                     |
| OAuth 2.1 | draft-ietf-oauth-v2-1-13       |

OAuth 2.1 references and section numbers follow draft-13, which is referenced by the MCP 2026-07-28 authorization specification. The article's core recommendations remain unchanged under OAuth 2.1 draft-17, the latest revision as of November 2026.

## Security risks and mitigations

### MCP's security baseline

The MCP authorization specification recommends implementing OAuth 2.1 to authorize access to protected resources over HTTP. Its security baseline draws on the following standards and specifications:

- OAuth 2.1 IETF Draft (draft-ietf-oauth-v2-1-13)
- OAuth 2.0 Bearer Token Usage (RFC 6750)
- OAuth 2.0 Authorization Server Metadata (RFC 8414)
- OAuth 2.0 Dynamic Client Registration Protocol (RFC 7591)
- OAuth 2.0 Protected Resource Metadata (RFC 9728)

### Risks in A2A + MCP combined systems

- Flujos de autorización débiles en A2A: PKCE recomendado pero no obligatorio, sin exigencia de OAuth 2.1 → robo de tokens de acceso y uso por terceros.
- Validación insuficiente de la audiencia (_audience_) del token → delegación descendente que permite acceso no autorizado a otros servidores MCP o API.
- Uso de claves de API (API keys) en A2A, en lugar de OAuth, agrava los riesgos anteriores.

### Recomendación central

Aplicar a las implementaciones de A2A un perfil de seguridad equivalente al de la autorización de MCP, incluyendo OAuth 2.1 y validación de audiencia, de modo que la autorización se diseñe de forma consistente a lo largo de todo el camino de comunicación —A2A y MCP— y no solo en un extremo.
