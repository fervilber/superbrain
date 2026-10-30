---
title: "agentgateway 1.4: soporte de la especificación MCP 2026-07-28 y el papel del gateway en sistemas agénticos"
source: "https://agentgateway.dev/blog/2026-08-03-new-mcp-spec-revision"
author: "Eitan Suez (agentgateway)"
date: 2026-08-03
captured: 2026-10-30
---

# Captura: Agentgateway out the gate with support for the 2026-07-28 MCP specification (v1.4)

> Post de agentgateway anunciando soporte de la revisión `2026-07-28` de MCP en su versión 1.4. Fundamenta la sección de gateways del informe del 30 de octubre de 2026.

## La nueva especificación, en breve

- El protocolo deja de ser stateful: se acaban los problemas de dirigir clientes a instancias sticky para mantener estado.
- Desaparecen los MCP session IDs y la llamada de apertura `initialize`.
- Nuevo endpoint `server/discover` para intercambiar versión de protocolo y capacidades. Los servidores "dual era" manejan con gracia clientes legacy y de nueva era.
- Los clientes pueden cachear listas de tools, prompts y resources gracias a las pistas de caché "time to live" (`ttlMs`) que los servidores pueden aportar en sus respuestas.
- Se repite la metadata de MCP (versión de protocolo, método y nombre) en las cabeceras de petición para facilitar a los intermediarios de enrutado que, de otro modo, tendrían que parsear los cuerpos.
- Se formalizan las **extensiones** (MCP Apps, Tasks y Enterprise Managed Authorization).
- En seguridad: Dynamic Client Registration queda deprecado y se recomienda CIMD. Para empresas que acceden a múltiples servidores MCP fuera de su control directo, se añade la extensión **Enterprise Managed Authorization** (EMA), que incorpora la especificación OAuth ID-JAG, también conocida como "Cross App Access", para dar una experiencia de single sign-on entre dominios de identidad.
- Sale la versión 2 del **MCP Inspector**, con soporte para configurar múltiples servidores y pre-configurarlos con el flag `--catalog`. Permite ver detalles de la comunicación cliente-servidor, cuerpos de petición y respuesta, información de conexión y tokens de auth (decodificables in-app).

## El papel de los gateways en sistemas agénticos

Los gateways son componentes de infraestructura necesarios que aportan observabilidad, auditoría, seguridad y control sobre el flujo de comunicación en un sistema agéntico. Median la comunicación entre agentes, LLMs y servidores MCP; recogen telemetría para logging, tracing y auditoría; actúan como puntos de aplicación de política (conceder/denegar acceso a backends); aplican rate-limiting a los LLMs para mitigar costes; y controlan el enrutado de peticiones a modelos seleccionados. Respecto a MCP, dan autorización y control sobre quién accede a tools y resources concretos, pueden federar múltiples servidores de herramientas e implementar la autenticación MCP de forma desacoplada del servidor backend.

Un gateway nativo de MCP actúa como servidor MCP frente a los agentes y, del otro lado, como cliente MCP frente a los servidores MCP backend.

## agentgateway v1.4

agentgateway v1.4 salió el 27 de julio, un día antes de la release de la revisión `2026-07-28`. Uno de sus grandes temas es el soporte de la nueva revisión. La v1.4.1 salió dos días después, con mayor compatibilidad.

Ejemplos destacados del repositorio:

- `mcp-basic`: proxy de un servidor MCP que cumple la nueva revisión, usando el servidor canónico "everything" como backend.
- `mcp-multiplex`: gateway que multiplexa/federa varios servidores MCP, útil mezclando servidores legacy y de "nueva era".
- `mcp-apps`: la extensión MCP Apps, ya graduada, con un proxy entre cliente y servidor MCP.
- `mcp-telemetry`: visualización de trazas para llamadas MCP.
- `mcp-authentication` y `mcp-authorization`: ejemplos para implementar authn/authz MCP como preocupación transversal.
- `traffic-cross-app-access`: tres ejemplos distintos de Cross App Access.

## Resumen

El ritmo de avance del ecosistema agéntico continúa. La comunidad avanza hacia la adopción de la nueva especificación MCP. agentgateway soporta ese esfuerzo para construir soluciones observables, seguras, rentables y bajo control del operador.
