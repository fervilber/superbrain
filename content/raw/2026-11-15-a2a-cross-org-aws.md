---
title: "AWS publica una arquitectura de referencia A2A entre organizaciones: orquestador LangChain contra agente Strands SaaS"
source: "https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/"
date: 2026-11-12
captured: 2026-11-15
---

# Build composable, interoperable multi-agent systems with A2A on AWS

Fuente: AWS Machine Learning Blog, Amit Chaudhary, 12 de noviembre de 2026 (nivel Advanced/300, Technical How-to).

## Contenido (verbatim, selección)

> Agents in multi-agent systems that span organizational boundaries often need to collaborate in a composable, interoperable way, with agents that other organizations build and run. They need a way to discover each other, communicate, and exchange tasks without exposing internals or requiring the same framework on both sides.

> The Agent-to-Agent (A2A) protocol addresses this constraint. Without A2A, building composable multi-agent systems across organizational boundaries requires custom integration code for each customer and framework. Independent software vendors (ISVs) can instead build composable, interoperable agents that work with the A2A-compatible frameworks their customers already use.

> In this post, we walk through a deployed reference architecture on AWS. A LangChain-based enterprise orchestrator communicates with a Strands Agents-based software as a service (SaaS) agent across organizational boundaries using A2A, with the enterprise and the SaaS provider in separate AWS accounts. Neither side depends on the other's framework or SDK, and the two sides share no secrets. We cover the architecture and implementation patterns, then deploy the system from three Jupyter notebooks and run an end-to-end test.

> The A2A protocol is now a Linux Foundation project, and AWS is among the organizations that support it. With A2A, agents can discover each other, negotiate tasks, and collaborate across organizational boundaries through a standardized protocol. The protocol uses existing authentication standards such as OAuth 2.0 and OpenID Connect (OIDC) for cross-boundary security, and is designed to work across A2A-compatible frameworks.

> Three agents run in two AWS accounts, one for the enterprise and one for the SaaS provider. The A2A protocol connects them, with OAuth authentication in both directions. Each account has its own Amazon Cognito user pool, so each side authenticates with its own identity provider.

## Separación de responsabilidades (verbatim, del listado de noticias)

> A2A and the Model Context Protocol (MCP) solve different problems in this architecture. MCP connects an agent to its own tools and data sources in a client-server model. A2A connects agents to other agents as peers, where neither side exposes its internals. In production, the SaaS agent could use MCP internally to connect to its compliance scanning tools while exposing itself externally through A2A. The external interface stays the same regardless of how the agent connects to its internal tools.

## Lectura técnica

- **Patrón de referencia desplegable**: orquestador empresarial en **LangChain** ↔ agente SaaS en **Strands Agents**, en **cuentas AWS separadas**, comunicados por **A2A**, sin dependencia mutua de framework/SDK y **sin secretos compartidos**.
- **Autenticación en ambos sentidos** con **OAuth 2.0 / OIDC**, cada lado con su propio **Amazon Cognito user pool** (su propio IdP).
- **Extensibilidad por registro**: a medida que el sistema crece, se añaden capacidades **registrando Agent Cards** en el orquestador, sin tocar los agentes ya en marcha.
- **MCP y A2A son capas distintas**: MCP conecta el agente con **sus** herramientas y datos (cliente-servidor); A2A conecta **agentes con agentes** como pares, sin exponer interioridades. Un agente SaaS puede usar MCP internamente y exponerse externamente por A2A sin cambiar su interfaz externa.
- A2A es ya proyecto de la **Linux Foundation**; el despliegue se hace desde **tres notebooks Jupyter** con prueba end-to-end.
