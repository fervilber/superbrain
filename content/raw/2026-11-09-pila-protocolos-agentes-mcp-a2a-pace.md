---
title: "Captura: la pila de protocolos de agentes — MCP, A2A y el borrador IETF PACE"
source: "https://www.truefoundry.com/blog/mcp-vs-a2a"
date: 2026-11-07
captured: 2026-11-09T20:14:00+01:00
---

# MCP vs A2A: la pila de protocolos de agentes en 2026

Síntesis de búsquedas dirigidas (toolsground.io, truefoundry.com, akoode.com, SAP Architecture Center, IETF draft-nandakumar-agentproto-pace-00).

## La separación por capas

- **MCP (Model Context Protocol):** conecta una aplicación de IA con sus **capacidades** —herramientas, recursos, prompts—. El modelo nunca habla con el servidor directamente; el cliente media, y por eso el cliente es el lugar correcto para imponer aprobaciones y permisos. Es la capa `aplicación de IA ↔ capacidades`.
- **A2A (Agent2Agent):** conecta un agente con **otros agentes**. Trata al agente remoto como opaco: un cliente pide trabajo y recibe resultados sin ver la memoria, prompts o herramientas internas del agente remoto. Es la capa `agente ↔ agente`. Google lo anunció en abril de 2025 y lo donó a la Linux Foundation en junio de 2025; la Linux Foundation reportó en abril de 2026, al año del protocolo, más de 150 organizaciones de apoyo.

## Estado normativo

- La revisión **MCP 2026-07-28** es el mayor cambio desde el lanzamiento: cambió de golpe cómo se registran los clientes (DCR deprecado en favor de CIMD), cómo hablan con los servidores (Streamable HTTP reemplaza HTTP+SSE), cómo se enrutan las peticiones (cabeceras `Mcp-Method`/`Mcp-Name`) y cómo piden entrada a mitad de llamada (elicitation pasa a Multi-Round-Trip Requests). Los SDK de Python pasaron los mil millones de descargas totales. MCP se movió a la Agentic AI Foundation de la Linux Foundation en diciembre de 2025.
- **A2A v1.0** incluye negociación de versión, múltiples bindings de protocolo y **Agent Cards firmadas** que ayudan a verificar la identidad y los metadatos anunciados de un agente. Descubrimiento vía `/.well-known/agent-card.json`. Clientes consumen actualizaciones de tareas por polling, streaming o webhooks.
- **PACE (Protocol for Agent Communication Exchange)**, borrador IETF `draft-nandakumar-agentproto-pace-00` (noviembre 2026): no reemplaza a A2A, MCP o AutoGen; se sitúa **por debajo**, como capa de transporte/sesión sobre MOQT (Media over QUIC Transport), y permite que varios protocolos de aplicación coexistan dentro de un mismo diálogo usando campos de espacio de nombres por protocolo (`a2a`, `ext`). Su tesis es que los protocolos de aplicación mantienen sus formatos nativos y llevan el contexto del diálogo por sus propios puntos de extensión.

## Advertencias de seguridad

- Ambos protocolos cambiaron de forma en 2026; construir contra una especificación obsoleta es un error frecuente.
- Un acceso amplio y permanente es lo que convierte una instrucción inyectada en un incidente de "confused deputy".
- Al evaluar proveedores, pedir implementaciones documentadas entre proveedores, guías de migración claras y evidencia de manejo de fallos (timeouts, respuestas contradictorias, actualizaciones duplicadas de tareas) en lugar de contar logos de socios.
