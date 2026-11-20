---
title: "MCP sin estado: una nueva era para la integración empresarial de IA"
source: "https://www.techtarget.com/news/stateless-mcp-a-new-era-for-enterprise-ai-integration/874933/"
date: 2026-11-17
captured: 2026-11-20
---

# Stateless MCP: A new era for enterprise AI integration

Abhishek Jadhav — TechTarget — 17 de noviembre de 2026

When an enterprise AI agent sends a request to an enterprise system, the operation may succeed even if the connection drops before the response reaches the agent. However, the agent cannot determine whether to retry the request because doing so could repeat an action that has already been completed. This is one of the reliability challenges organizations face when using the **Model Context Protocol (MCP)**. Recent changes to the MCP specification **remove protocol-level sessions**, making it easier to distribute requests across servers.

## Stateless MCP cambia el despliegue del servidor

In earlier versions of MCP, servers typically issued a **session identifier** and used it to recognize subsequent requests. Deployments that maintained state in memory had to route subsequent calls to the same instance or share that state across servers. A server failure could then interrupt an ongoing interaction. The protocol changes remove this session mechanism. **Each request includes the information needed to process it**, so traffic can move to another server instance — más fácil añadir capacidad, reemplazar servidores caídos y usar infraestructura _serverless_.

Business processes still need to remember what happened between calls (por ejemplo, un _draft_ de orden de compra guardado en el ERP y referenciado por número). La pregunta práctica es **dónde almacenar ese estado**: almacenamiento compartido para hacer los registros disponibles entre instancias.

## Controles de acceso en MCP sin estado

MCP usa un **modelo de autorización basado en OAuth** para conexiones HTTP protegidas: cada petición incluye un _access token_ que el servidor valida para confirmar la identidad del llamante, el servicio pretendido y los permisos concedidos. La información aportada por el cliente (por ejemplo, sus datos de software) **no prueba identidad ni permiso**. Si un agente pide acceso a un registro de cliente, el servicio debe verificar que el usuario o la carga de trabajo que hace la petición tiene permiso para verlo o modificarlo.

Las **gateways** pueden aplicar reglas comunes antes de que las peticiones lleguen a servidores MCP individuales. El nuevo protocolo tiene **cabeceras que dicen cuál es la operación**, lo que permite aplicar políticas de enrutado y límites a funciones sensibles o de alto volumen sin ver la petición completa. Pero esas comprobaciones **no sustituyen** a los controles en la aplicación subyacente.

## Manejo de fallos: idempotencia

Better routing can improve availability, but it does not ensure that a business operation is completed successfully. If an MCP instance fails, the next request can reach another instance; the second server needs a reliable way to determine whether earlier work was completed. El ejemplo de la orden de compra: el ERP puede crear la orden antes de que se pierda la respuesta; si la aplicación no sabe que es un repetido, reintentar en otro servidor puede **crear una orden duplicada**. Salvaguarda: **idempotencia** con un identificador único por operación y su resultado guardado. **Multi Round-Trip Requests (MRTR)** y la función opcional **Tasks** cubren interacciones que requieren entrada adicional y operaciones largas.

## Monitorización

Cuando los agentes dependen de múltiples servicios, cada componente puede reportar que está operativo **incluso cuando la transacción falla**. La solución es **trazado distribuido** (MCP soporta pasar información de traza estándar con las peticiones). Los _dashboards_ deben distinguir entre "respuesta MCP correcta" y "operación de negocio completada"; los registros de auditoría deben identificar quién pidió acciones sensibles, qué recurso se vio afectado y el resultado.
