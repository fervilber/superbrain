---
title: "De MCP a A2A: conectar cualquier asistente de IA a tu broker de agentes"
source: "https://blogs.mulesoft.com/artificial-intelligence/mcp-to-a2a-connect-any-ai-assistant-to-your-agent-broker/"
date: 2026-11-18
captured: 2026-11-20
---

# MCP to A2A: Connect Any AI Assistant to Your Agent Broker

Harish Subramanian — MuleSoft Blog — 18 de noviembre de 2026

Your teams have built an agent network that answers real business questions. Now your employees want to ask those questions from the AI assistant they already use every day. There's just one problem: **the assistant speaks only MCP, your agent network understands only A2A**. One side asks a question the other can't understand, and the answer never arrives.

## El puente MCP ↔ A2A

Agent brokers in **MuleSoft Agent Fabric** speak the **A2A protocol** (tasks, messages, y un _conversation ID_ compartido). La **MCP A2A bridge policy** es una política personalizada para **MuleSoft Omni Gateway (Flex Gateway)** que hace que tu broker de agentes **parezca un servidor MCP**, sin cambiar el broker.

To an AI assistant, the broker now offers **one simple tool**, such as "ask the HR agent". The assistant calls that tool with a plain-language question. **The policy turns the call into an A2A message, sends it to the broker, and turns the answer back into a tool result.** Because the translation happens in the gateway, it sits next to the policies you already trust: **the same authentication, logging, rate limiting, and analytics**. No new service to deploy or run.

## Modos de despliegue

- **Dos proxies**: el broker mantiene su proxy A2A existente para tráfico de agentes; se crea un segundo API proxy de tipo **MCP** que apunta al mismo broker y se aplica la bridge policy solo al proxy MCP. Los clientes A2A siguen usando la URL A2A; asistentes como ChatGPT usan la nueva URL MCP. Cada proxy reenvía peticiones al broker a través de su propio conjunto de políticas.
- **Pass-through / un solo URL**: se aplica la política directamente y se activa el modo pass-through. Una sola URL sirve a ambos tipos de cliente: si llega una petición MCP, la política la responde o la traduce; si llega una petición A2A nativa, la política la pasa al broker sin cambios.

**Implicación**: la traducción entre protocolos se convierte en una **función de gateway**, donde ya viven la autenticación y la observabilidad, en lugar de exigir un servicio nuevo o cambiar el broker.
