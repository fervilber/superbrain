---
title: "Microsoft Entra Agent ID y Agent 365: identidad gestionada para cada agente"
source: "https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753"
date: 2026-11-18
captured: 2026-11-20
---

# What's new in Microsoft Agent 365: Ignite 2026

Microsoft Community Hub — 18 de noviembre de 2026

As organizations adopt more cloud agents, admins need a consistent way to manage agent identity and access across services.

## Microsoft Entra Agent ID se extiende

**Microsoft Entra Agent ID now extends to Microsoft Autopilot**, building on existing support for agents built with Copilot Studio and Microsoft Foundry. This gives admins a consistent way to identify, authenticate, and govern these agents (preview).

Connected agents now **automatically receive a Microsoft Entra Agent ID**, which brings them under identity management and helps IT and security **tell agents apart from people in a shared identity inventory**. With that identity, organizations can:

- govern each agent's lifecycle,
- apply supported Conditional Access and security policies,
- assess identity risk, and
- revoke access when needed.

**Entra Agent ID automatically assigns an identity to supported local agents** discovered by Microsoft Defender on managed devices and by Microsoft Entra Global Secure Access on the network, starting with **GitHub Copilot CLI and Claude Code**. With a distinct identity for each local agent, organizations can tell agent activity apart from human activity and apply supported access controls (preview).

## Otros puntos

- **Export Agent Activity**.
- **Agent 365** es el plano de control que reúne Entra Agent ID, gobernanza de Foundry y protecciones de Defender para equipos de IT y seguridad (GA prevista para el 1 de mayo de 2026, 15 USD por usuario/mes).
- **Entra automated lifecycle for agent identities — GA**: políticas que comprueban patrocinio y actividad reciente y actúan según la política.
- **MCP Firewall — Preview**.
- Al crear un agente en Foundry se aprovisiona automáticamente un **Agent Identity Blueprint** y un **Agent Identity** en el tenant de Entra; la autenticación fluye por las credenciales del Blueprint con flujos OAuth 2.0 optimizados para cargas de IA.
