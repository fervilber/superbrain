---
title: "Foundry Agent Service en Ignite 2026: agentes con cuenta de Microsoft 365 e identidad Entra"
source: "https://devblogs.microsoft.com/foundry/whats-new-in-foundry-agent-service-at-ignite-2026"
date: 2026-11-19
captured: 2026-11-20
---

# What's new in Foundry Agent Service at Ignite 2026

Microsoft Foundry Blog — Ignite 2026 (17–20 de noviembre de 2026)

Your customers don't judge agents by how well they demo. They judge them by whether the work gets done: the case resolved, the report delivered, the follow-up sent. At Ignite 2026, Foundry Agent Service delivers new capabilities across the agent lifecycle: **Build, Deploy, and Operate**.

## Deploy: agentes como miembros de Microsoft 365

### Traer agentes al trabajo cotidiano con cuentas de Microsoft 365

One powerful publishing pattern is creating **autonomous, always-on agents in Microsoft 365**. Supported hosted agents get their **own Entra Agent ID, email address, Microsoft Teams presence, and place in the org chart**, so they can start conversations, work on shared files, and follow up on action items alongside people.

Foundry is integrating with **Microsoft 365 Resources for Agents**, which equips supported agents with their own secured Microsoft 365 resources, including a **standalone mailbox, calendar, and OneDrive workspace** for file storage. These capabilities will be made available to supported agents across the Microsoft portfolio.

The result: agents that work where people already collaborate, while administrators keep control of access and availability through **Microsoft Entra and Agent 365**, subject to tenant controls.

## Build

- **Microsoft Copilot harness** (public preview): forma gestionada de construir agentes de prompt que razonan, usan herramientas y completan tareas largas. Microsoft ejecuta el bucle del agente y el sandbox.
- **Voice agents — GA**: voz en tiempo real, con interrupción, pausa y cambio de dirección; integración con telefonía y contact center.
- **Toolboxes** (endpoint MCP gestionado), **A2A tool (GA)** para conectar agentes Foundry y externos, **Web Search powered by Web IQ (GA)**, **Computer use y browser automation (GA)** con sesiones de navegador aisladas, Live View y Take control para supervisión humana.

## Deploy (controles empresariales)

- **Shared subnet IPs — GA**: sesiones comparten IP de subred con sandboxes aislados por VM; cuotas por defecto de 1.000–2.000 sesiones concurrentes por suscripción y región.
- **Memory snapshots — Public preview**: reduce _cold starts_ restaurando estado inicializado.
- **Network egress controls — GA**: define destinos accesibles por los agentes gestionados, con aplicación fuera del sandbox.
- **Private certificate authority trust — Public preview**: conexión a APIs internas, servidores MCP y gateways de modelo con certificados propios.
- **Azure Policy governance — Public preview**: exige configuraciones de egreso aprobadas entre suscripciones o grupos de recursos.
- **Long-running resiliency — GA**: recuperación de trabajos largos tras caídas/reinicios; el handler se re-ejecuta, así que hay que guardar progreso y evitar efectos duplicados. Timeout de inactividad configurable de 2 min a 4 h (15 min por defecto).
- **Deployment to customer-owned AKS — Coming soon** (public preview previsto para principios de diciembre).

## Operate: gobernar y mejorar continuamente

- **Insights — GA**: identifica problemas recurrentes en trazas de producción; se extiende a agentes construidos con LangGraph, LangChain y CrewAI.
- **Annotations on traces — Public preview** y **Evaluation datasets** para convertir revisiones en tests reutilizables.
- **Insights to Agent Optimizer — Preview** y **Skill optimization — Preview** (skills versionadas, reutilizables o reversibles).
- **Cost optimization — Public preview**.
