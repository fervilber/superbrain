---
title: "MCP vs A2A en 2026: la pila de tres capas, la gobernanza bajo la AAIF y la matriz de frameworks"
source: "DEV Community (pockit.tools) / NeuralCoreTech / Advantage AI Engineering / Sim"
date: 2026-11-27
captured: 2026-11-27T20:10:00+01:00
---

# MCP vs A2A: la pila de protocolos de agentes en 2026

URL: https://dev.to/pockit_tools/mcp-vs-a2a-the-complete-guide-to-ai-agent-protocols-in-2026-30li
URL: https://neuralcoretech.com/mcp-vs-a2a-agentic-ai-foundation-2026
URL: https://advantageaieng.com/blog/a2a-protocol-and-mcp-interoperable-multi-agent-enterprise-2026
URL: https://www.sim.ai/library/best-ai-agent-platforms-a2a-protocol-2026

_(Nota de captura: material de análisis/síntesis, no noticia de última hora. Se recoge como referencia técnica de la pila de protocolos.)_

## Los dos problemas distintos

Antes de MCP y A2A, cada integración de herramienta con IA era un desarrollo a medida. Eso creó dos pesadillas de integración distintas:

- **Integración de herramientas (resuelta por MCP):** cada proveedor tenía su forma de conectar con herramientas externas —function calling de OpenAI, tool use de Anthropic, function declarations de Google— con esquemas JSON, formatos de respuesta y manejo de errores diferentes.
- **Coordinación de agentes (resuelta por A2A):** no había forma estándar de que los agentes se descubrieran, negociaran capacidades o se pasaran tareas entre sí.

## MCP: vertical, agente → herramientas

MCP (Model Context Protocol), creado por Anthropic y donado a la **Agentic AI Foundation (AAIF)** de la Linux Foundation en diciembre de 2025, estandariza cómo un agente se conecta a herramientas, fuentes de datos y servicios externos. Es la interfaz entre el cerebro de IA y sus manos. Usa arquitectura cliente-servidor con **JSON-RPC 2.0** como formato de cable.

Un servidor MCP expone cuatro tipos de capacidades:

1. **Resources** — fuentes de datos de solo lectura (ficheros, registros de base de datos, respuestas de API).
2. **Tools** — acciones ejecutables (ejecutar una consulta, enviar un correo, crear un fichero).
3. **Prompts** — plantillas de prompt reutilizables con argumentos estructurados.
4. **Sampling** — capacidad de pedir completados de LLM al cliente (dirección inversa).

Transportes: **stdio** (herramientas locales, CLI, apps de escritorio; el servidor corre como subproceso), **SSE** (servidores remotos, basados en web) y **Streamable HTTP** (APIs de producción, despliegue en la nube; el más nuevo). Para producción, Streamable HTTP se está volviendo el estándar.

Ecosistema MCP en 2026: **más de 5.800 servidores MCP** en registros públicos, servidores oficiales para GitHub, Slack, PostgreSQL, Google Drive, Stripe, AWS, Jira, Linear y Notion, soporte MCP incorporado en Claude Desktop, VS Code, Cursor, Windsurf, Zed y IDEs de JetBrains, y soporte de **ejecución de código** para que los servidores MCP filtren y transformen datos antes de enviarlos al LLM, reduciendo el consumo de tokens.

## A2A: horizontal, agente ↔ agente

A2A (Agent-to-Agent), creado por Google en abril de 2025 y donado a la Linux Foundation en junio de 2025, estandariza cómo los agentes se descubren, comunican y colaboran, sin importar su framework subyacente. Es «HTTP para agentes de IA». El **ACP de IBM** se fusionó en A2A en agosto de 2025, y en diciembre de 2025 la Linux Foundation lanzó la **AAIF** —cofundada por OpenAI, Anthropic, Google, Microsoft, AWS y Block— como hogar permanente de A2A y MCP.

Conceptos centrales:

1. **Agent Card** — manifiesto JSON servido en `/.well-known/agent.json` que describe qué puede hacer un agente, sus requisitos de autenticación y capacidades soportadas.
2. **Tasks** — la unidad de trabajo entre agentes, con estados `submitted`, `working`, `input-required`, `completed`, `failed`, `canceled`.
3. **Messages** — comunicación dentro de una tarea, cada una con una o más Parts (texto, fichero, datos).
4. **Artifacts** — las salidas/entregables de una tarea completada.
5. **Streaming** — actualizaciones en tiempo real vía Server-Sent Events para tareas largas.

## La pila de tres capas

Un modelo mental útil para la arquitectura de agentes de 2026 tiene tres capas:

1. **Capa de modelo** — el LLM (Claude, GPT, Gemini o un modelo de pesos abiertos), responsable del razonamiento y la planificación.
2. **Capa de integración de herramientas (MCP)** — conectores estandarizados entre el bucle de razonamiento y recursos externos: búsqueda, bases de datos internas, ejecución de código, sistemas de ficheros, APIs SaaS.
3. **Capa de coordinación de agentes (A2A)** — descubrimiento estandarizado y traspaso de tareas entre agentes independientes, dentro de una misma empresa o entre proveedores distintos.

Un desglose más amplio añade **WebMCP** por debajo de MCP (acceso de la web al agente), dando la pila **WebMCP → MCP → A2A**. Un reto señalado en producción: depurar fallos a través de las tres capas exige instrumentarlas por separado, y las herramientas actuales no las unifican bien. Cuando falla una tarea A2A, ¿fue enrutado de delegación, fallo de herramienta MCP o error de acceso WebMCP? Hoy eso significa leer tres flujos de registro distintos; una capa de observabilidad que tratara toda la pila como una sola unidad de traza sería un desbloqueo significativo.

## Gobernanza: la AAIF como casa neutral

El 20 de agosto de 2026, A2A se unió formalmente a la AAIF de la Linux Foundation, el mismo hogar neutral que MCP. La membresía de la AAIF pasó de menos de 40 organizaciones en su lanzamiento a **más de 250 a mediados de agosto de 2026**, con AWS, Microsoft, Google, Anthropic, OpenAI y Bloomberg entre ellas.

**Mantener A2A y MCP separados pero alineados es el punto:** MCP es vertical (agente → herramientas), A2A es horizontal (agente ↔ par). Poner ambos bajo gobernanza AAIF no colapsa la distinción, la protege. La gobernanza fragmentada arriesgaba que los dos protocolos se separaran, obligando a cada framework a construir puentes a medida. Una casa compartida significa un conjunto de procesos de revisión de seguridad, una vía de conformidad y un lugar donde resolver solapamientos conforme evolucionan ambas especificaciones.

**Cifras (reportadas por la industria, no auditadas de forma independiente):** MCP había superado los **110 millones de descargas mensuales de SDK** y **10.000 servidores públicos activos** en abril de 2026; la adopción de A2A se reportaba en **más de 150 organizaciones** a mediados de 2026. La hoja de ruta de la AAIF lista la finalización de un RFC para una especificación formal de gobernanza de A2A como objetivo para el tercer trimestre de 2026 —un objetivo declarado, no un resultado confirmado—.

## Matriz de frameworks (Q3 2026)

| Framework                     | MCP nativo                 | A2A nativo          | Encaje                                                                                            |
| ----------------------------- | -------------------------- | ------------------- | ------------------------------------------------------------------------------------------------- |
| Microsoft Agent Framework 1.0 | Sí                         | Sí                  | Empresas .NET/Python que necesitan GA estable y soporte LTS; sucesor de Semantic Kernel y AutoGen |
| CrewAI                        | Sí                         | Sí (creciendo)      | Equipos multiagente por roles, tiempo mínimo hasta el primer agente                               |
| Pydantic AI                   | Sí                         | Sí                  | Equipos Python que quieren tipado estricto y validación con poca sobrecarga                       |
| Google ADK                    | Soporte cliente            | Sí                  | Equipos estandarizados en Vertex AI y Gemini                                                      |
| LangGraph                     | Basado en adaptador        | Basado en adaptador | Flujos stateful complejos con ciclos, ramas y checkpoints human-in-the-loop                       |
| OpenAI Agents SDK             | Sí                         | Vía AGENTS.md/shim  | Equipos estandarizados en modelos OpenAI                                                          |
| Claude Agent SDK              | Sí (nativo)                | Vía shim            | Despliegues safety-first, sesiones de código autónomas largas                                     |
| goose (Block)                 | Sí (MCP nativo por diseño) | Emergente           | Framework local-first de código abierto; proyecto ancla de la AAIF                                |

Nota específica sobre **AutoGen**: Microsoft lo ha movido a **modo mantenimiento** —sigue recibiendo parches de seguridad pero no nuevas funciones— y su propia documentación apunta a nuevos usuarios hacia Microsoft Agent Framework. Un despliegue existente de AutoGen no se romperá de la noche a la mañana, pero los nuevos desarrollos deben apuntar a otro sitio.

## Regulación: el Digital Omnibus

Ninguna de las labores de gobernanza y certificación de seguridad de la AAIF es un mandato legal. El **Digital Omnibus** de la UE sobre IA, en vigor desde el 27 de julio de 2026, movió las obligaciones de sistemas de alto riesgo del Anexo III del AI Act del 2 de agosto de 2026 al **2 de diciembre de 2027**, y las del Anexo I al 2 de agosto de 2028. El programa de conformidad de seguridad de protocolos de la AAIF es un esfuerzo voluntario de la industria que corre en paralelo a esa línea temporal regulatoria.

## Puesta en marcha

1. **Auditar las integraciones actuales** — listar cada conector a medida; cada uno es candidato a reemplazarse por un servidor MCP estándar.
2. **Levantar o conectar un servidor MCP por dominio de herramienta.**
3. **Decidir si se necesita A2A** — si todos los agentes viven en un framework y un equipo, puede que no; A2A se gana su complejidad cuando hay agentes de distintos proveedores, equipos o frameworks que necesitan traspasarse tareas.
4. **Exponer un Agent Card** para descubrimiento entre frameworks.
5. **Añadir trazado antes de escalar** — un camino de trazado compatible con OpenTelemetry (LangSmith, Application Insights o Logfire).
6. **Seguir la hoja de ruta de la AAIF** — cuatro líneas activas hasta 2027: especificación MCP v2 con streaming y flujos de autenticación mejorados, spec de gobernanza A2A con objetivo RFC en Q3 2026, release estable de AGENTS.md v1.0 y programa de conformidad de seguridad para certificar plataformas de agentes.

## Eventos próximos

AGNTCon + MCPCon Europe (Ámsterdam, 17-18 de septiembre de 2026) y AGNTCon + MCPCon North America (San José, 22-23 de octubre de 2026).
