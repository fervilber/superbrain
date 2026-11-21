---
title: "La pila de protocolos agénticos en noviembre de 2026: MCP endurecido, A2A v1.0 y un gateway común"
source: "https://zuplo.com/blog/agent-protocol-stack-mcp-a2a-acp-2026"
date: 2026-11-21
captured: 2026-11-21
---

# La pila de protocolos agénticos: MCP para herramientas, A2A para agentes

Captura compuesta de `zuplo.com/blog/agent-protocol-stack-mcp-a2a-acp-2026`,
`dev.to/pockit_tools/mcp-vs-a2a-the-complete-guide-to-ai-agent-protocols-in-2026-30li` y
`masaischool.com/blog/a2a-vs-mcp-agent2agent-protocol-explained`.

## 1. Estado a nivel de especificación

- **A2A**: última versión publicada **1.0.0** (12 de marzo de 2026), seguida de la corrección de
  errores **v1.0.1** (28 de mayo de 2026). A2A pasó de 0.3 a 1.0 cambiando el nombre de operaciones y
  los valores de enumeración a SCREAMING_SNAKE_CASE. Existe un **v1.1 RC** en despliegue en redes
  air-gapped.
- **MCP**: revisión estable actual fechada **2025-11-25**; la siguiente revisión (**2026-07-28**)
  estaba en release candidate, y en noviembre de 2026 ya se cita como revisión vigente. La revisión
  2026-07-28 **elimina el handshake `initialize`** que usaban las revisiones anteriores (MCP sin
  estado). El transporte HTTP+SSE antiguo está deprecado a favor de Streamable HTTP.

> Both protocols have changed names and message formats between versions, so tutorials should be
> matched to the version they target.

## 2. Gobernanza: dos protocolos, una fundación

- **MCP** fue donado por Anthropic a la **Agentic AI Foundation** (AAIF), un fondo dirigido de la
  Linux Foundation cofundado con Block y OpenAI, en diciembre de 2025. Ya no es un proyecto de
  Anthropic consumido por el resto de la industria: es gobernado por la comunidad, con grupos de
  trabajo y un proceso formal de propuestas.
- **A2A** fue donado por Google el **23 de junio de 2025**, lanzando el Agent2Agent Protocol Project
  con AWS, Cisco, Google, Microsoft, Salesforce, SAP y ServiceNow como miembros fundadores.
- **ACP** (Agent Communication Protocol, de IBM Research, marzo de 2025, para su plataforma BeeAI)
  se fusionó en A2A: en agosto de 2025 LF AI & Data anunció que ACP se unía a A2A bajo el paraguas de
  la Linux Foundation. «"Merger" undersells it: the ACP team wound down active development and began
  contributing its technology directly to A2A.»

> So in 2026 there is **one agent-to-agent standard worth building against: A2A**.

## 3. AgentCard y ciclo de vida de la tarea (A2A v1.0)

Documento público de descubrimiento en una ruta conocida: en la especificación v1.0 la ruta es
`/.well-known/agent-card.json` (la antigua `/.well-known/agent.json` de los ejemplos v0.x está
desactualizada). El card declara `capabilities` (streaming, notificaciones push por webhook),
`securitySchemes` y `security` (reutilizando la forma de los esquemas de seguridad de OpenAPI) y
`skills` (el menú de lo que el agente hará).

**El card es una concesión de capacidad en forma de documento**: por eso es una superficie de
seguridad. La especificación define **agent cards firmados** para que quien llama pueda verificar que
el card no ha sido manipulado antes de actuar: «If you can poison an agent's card, you can redirect or
escalate everything that trusts it.»

Estados de tarea: `submitted`, `working`, `input-required`, `auth-required`, `completed`, `failed`,
`canceled`, `rejected`. Los estados `input-required` y `auth-required` son lo que convierte A2A en un
protocolo de coordinación y no en una API de petición/respuesta: una tarea puede pausarse a mitad,
pedir más al llamante y reanudarse. Transportes v1.0: **JSON-RPC 2.0 sobre HTTP, gRPC y HTTP+JSON/REST**;
las actualizaciones en streaming van por Server-Sent Events.

A2A no inventa un esquema de autenticación: el `securitySchemes` del AgentCard reutiliza el vocabulario
de OpenAPI (API keys, HTTP auth, OAuth 2, OpenID Connect, mTLS).

## 4. MCP en 2026: el modelo de autorización se endureció

- Los servidores MCP **DEBEN** implementar **OAuth 2.0 Protected Resource Metadata (RFC 9728)**.
- Los clientes MCP **DEBEN** implementar **Resource Indicators (RFC 8707)**, atando cada token al
  servidor concreto para el que se emitió.
- El **registro dinámico de clientes**, antaño el camino esperado, ahora es **opcional**.

> Common mistake: If you implemented MCP auth in early 2025, do not assume it still conforms. The
> token-binding and Resource Indicator requirements became **MUST** since, and dynamic client
> registration is no longer the expected path.

Incidente citado: una vulnerabilidad crítica de inyección de comandos divulgada en abril de 2026
(**CVE-2026-30623**) permitía que la función de creación de servidores MCP de LiteLLM ejecutase
comandos de configuración sin validación. «A maturing protocol needs a governed path, not blind trust
in every server you connect to. Ungoverned servers are exactly the **shadow MCP** problem.»

## 5. Un gateway para ambos (Zuplo)

| Aspecto             | MCP                                                        | A2A                                                   |
| ------------------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| Trabajo del gateway | Emite tokens (servidor de autorización OAuth 2.1 completo) | Valida tokens (cada agente trae el suyo)              |
| Handler dedicado    | Sí, el MCP Gateway                                         | No, se pone delante como cualquier API HTTP           |
| Transporte          | HTTP, JSON-RPC, SSE, stdio                                 | HTTP, JSON-RPC, SSE                                   |
| Controles extra     | Filtrado de capacidades, sin passthrough de token          | Limitación de tasa por agente, registro de peticiones |

Para MCP, cada upstream se publica como **servidor virtual**, con su propia ruta de gateway y su propio
recurso OAuth; con PKCE y el parámetro `resource` obligatorio (RFC 8707), un token emitido para un
servidor virtual se rechaza en otro, cerrando el hueco del confused deputy: un token emitido para
`/mcp/linear-v1` no puede reproducirse contra `/mcp/stripe-v1`. Dos controles adicionales: **sin
passthrough de token** (las cabeceras de autenticación entrantes nunca se filtran al upstream; el
gateway resuelve la credencial del usuario del lado servidor y la adjunta, guardando los tokens
upstream cifrados en reposo) y **filtrado de capacidades** (una política filtra `tools/list`,
`prompts/list` y `resources/list` y bloquea llamadas a lo oculto devolviendo `MethodNotFound`, incluso
a un agente que ya conozca o adivine el nombre de la herramienta).

## 6. Los ataques que añade encadenar agentes

- **Tool poisoning** — ítem #3 del OWASP MCP Top 10, junto a _rug pulls_ y _tool shadowing_.
- **Prompt injection** — LLM01 en el OWASP Top 10 for LLM Applications; fluye hacia atrás a través de
  las respuestas de herramientas y agentes, «so the boundary has to inspect what comes back, not only
  what goes out».
- **Excessive agency** — LLM06; es el modo de fallo que hace **no negociable** el reparto de privilegio
  mínimo.
- **Ataques de agent-card y confused deputy** — un AgentCard envenenado o un token reproducido en el
  servidor equivocado permite que un componente comprometido actúe con la autoridad de otro.

> The common thread: **the model layer cannot be the sole enforcement point**. Model-side guardrails
> help, but they are probabilistic and never catch everything, so a deterministic boundary has to sit
> between the agent and whatever it is reaching.

## 7. La pila de tres capas y la instrumentación pendiente

Del análisis en dev.to (HK Lee): la pila de protocolos de IA en tres capas —**WebMCP para el acceso
web, MCP para herramientas, A2A para agentes**— se está convirtiendo en la arquitectura de consenso.
Datos de adopción citados: MCP cruzó **97 millones de descargas mensuales de SDK** (Python + TypeScript)
en febrero de 2026, con más de **5.800 servidores MCP** en registros públicos a marzo de 2026; A2A
superó los **100 apoyos empresariales**.

La advertencia útil es de observabilidad: «debugging failures across all three layers requires
instrumenting all three separately, and today's tooling doesn't unify them well. When an A2A task
fails, was it a delegation routing issue, an MCP tool failure, or a WebMCP access error? Right now
that usually means reading three separate log streams.»
