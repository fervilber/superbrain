---
title: "El stack de protocolos de agente en 2026: MCP abajo, A2A arriba, ACP absorbido"
source: "https://zuplo.com/blog/agent-protocol-stack-mcp-a2a-acp-2026 | https://www.glukhov.org/ai-systems/comparisons/a2a-protocol-2026-adoption"
author: "Martyn Davies (Zuplo) / Rost Glukhov"
date: 2026-07-03
captured: 2026-10-26
---

# Captura: el stack de protocolos, a nivel de especificación

> Captura por extractos verbatim de dos análisis técnicos. Zuplo (3 de julio de 2026) va al nivel de formato de cable; Glukhov aporta el estado de adopción en 2026.

## Los dos protocolos que definen el exterior de un agente

Dos protocolos definen hoy cómo un agente de IA alcanza el mundo exterior:

- **MCP (Model Context Protocol)** conecta un agente **con herramientas**: una base de datos, una cuenta de Stripe, una API interna. Un cliente (Claude Desktop, Cursor, tu propio agente) se conecta a un servidor MCP que expone herramientas, recursos y prompts. **El servidor es proveedor de capacidad; el agente es el llamante.**
- **A2A (Agent2Agent)** conecta **agentes con agentes**, de modo que un agente planificador pueda entregar una tarea a un agente de facturación **sin que ninguno exponga su estado interno**.

En un sistema real se usan ambos: un orquestador usa A2A para delegar en agentes especialistas, y cada especialista usa MCP para alcanzar las herramientas que necesita.

## Dónde fue ACP

Durante buena parte de 2025 había tres protocolos en la conversación. **ACP (Agent Communication Protocol)** salió de IBM Research en marzo de 2025 para alimentar su plataforma BeeAI, con solapamiento fuerte con A2A. En **agosto de 2025**, LF AI & Data anunció que **ACP se unía a A2A** bajo el paraguas de la Linux Foundation: el equipo de ACP **cerró el desarrollo activo** y empezó a contribuir su tecnología directamente a A2A.

A2A había pasado antes a gobernanza neutral: **Google donó el protocolo, sus SDK y su tooling a la Linux Foundation el 23 de junio de 2025**, lanzando el Agent2Agent Protocol Project con AWS, Cisco, Google, Microsoft, Salesforce, SAP y ServiceNow como miembros fundadores.

Conclusión de 2026: **hay un único estándar agente-a-agente contra el que construir, A2A.**

## Dentro del AgentCard

El descubrimiento en A2A arranca con un documento público llamado **AgentCard**, servido en una ruta _well-known_. En la **especificación v1.0** esa ruta es **`/.well-known/agent-card.json`** (la antigua `/.well-known/agent.json` de los ejemplos v0.x está obsoleta).

La tarjeta anuncia quién es el agente, qué sabe hacer y cómo autenticarse contra él:

```json
{
  "name": "Billing Agent",
  "description": "Issues refunds and answers invoice questions",
  "url": "https://agents.example.com/a2a",
  "provider": { "organization": "Example Corp" },
  "capabilities": { "streaming": true, "pushNotifications": true },
  "securitySchemes": {
    "oauth": {
      "type": "oauth2",
      "flows": {
        "clientCredentials": {
          "tokenUrl": "https://auth.example.com/token",
          "scopes": { "billing:write": "Issue refunds" }
        }
      }
    }
  },
  "security": [{ "oauth": ["billing:write"] }],
  "skills": [
    {
      "id": "refund",
      "name": "Issue a refund",
      "description": "Refunds a charge by transaction ID"
    }
  ]
}
```

`capabilities` indica al llamante si el agente soporta _streaming_ y _push notifications_ (un callback a un webhook para que una tarea larga reporte sin mantener una conexión abierta). `securitySchemes` y `security` describen cómo autenticarse, **con la misma forma que los esquemas de seguridad de OpenAPI**. `skills` es el menú de lo que el agente hará. Un agente llamante obtiene la tarjeta, decide si el agente remoto encaja y arranca una tarea.

La tarjeta es **una concesión de capacidad en forma de documento**, y por eso es una superficie de seguridad: la especificación define **tarjetas firmadas** para que un llamante verifique que no ha sido manipulada antes de actuar sobre ella. **Si puedes envenenar la tarjeta de un agente, puedes redirigir o escalar todo lo que confía en él.**

## Ciclo de vida de la tarea y transportes

El trabajo en A2A se modela como **Task**. Un llamante envía un **Message** (compuesto de **Parts**: texto, archivos, datos estructurados), el agente remoto hace el trabajo y **transmite de vuelta Messages y Artifacts**. Estados:

| Estado           | Significado                                    |
| ---------------- | ---------------------------------------------- |
| `submitted`      | La tarea ha sido aceptada pero no arrancada    |
| `working`        | El agente está procesando activamente          |
| `input-required` | El agente está bloqueado esperando al llamante |
| `auth-required`  | El agente necesita autenticación adicional     |
| `completed`      | La tarea terminó con éxito                     |
| `failed`         | La tarea dio error                             |
| `canceled`       | El llamante o el agente detuvieron la tarea    |
| `rejected`       | El agente declinó la tarea                     |

**`input-required` y `auth-required` son lo que convierte A2A en un protocolo de coordinación y no en una API petición/respuesta**: una tarea puede pausarse a mitad, pedir más al llamante y reanudarse.

A2A v1.0 define **tres bindings de transporte**: **JSON-RPC 2.0 sobre HTTP, gRPC y HTTP+JSON/REST**. Las actualizaciones de streaming viajan sobre **Server-Sent Events**. Sobre el binding JSON-RPC, delegar una tarea es un único POST a la URL del agente:

```http
POST /a2a HTTP/1.1
Host: agents.example.com
Authorization: Bearer <token>
Content-Type: application/json

{ "jsonrpc": "2.0", "id": "1", "method": "message/send",
  "params": { "message": { "role": "user",
    "parts": [{ "kind": "text", "text": "Refund charge ch_3Nk for $40" }] } } }
```

El agente responde con un objeto Task con `id` y `status.state` de `submitted` o `working`, y luego transmite actualizaciones por SSE conforme avanza el estado. **Para un operador de gateway, el titular es: el tráfico A2A es HTTP más JSON más SSE, sin transporte exótico que aprender.**

## Cómo autentica A2A

A2A **no inventa un esquema de autenticación**: `securitySchemes` reutiliza el vocabulario de OpenAPI, así que un agente puede declarar claves de API, autenticación HTTP, OAuth 2, OpenID Connect o mTLS. Un agente llamante lee el esquema, obtiene la credencial correspondiente (normalmente autenticándose como él mismo con una **identidad de máquina**, aunque un esquema puede llevar un **token delegado de usuario**) y la presenta en cada petición de tarea.

## Amenazas cuando los agentes llaman a agentes

- **Envenenamiento de herramientas (_tool poisoning_).** Una herramienta maliciosa o comprometida devuelve contenido fabricado para manipular al modelo llamante. Es el ítem **#3 del OWASP MCP Top 10** (proyecto incubadora), junto a _rug pulls_ y _tool shadowing_.
- **Inyección de prompt.** Contenido no confiable llega al modelo como instrucciones. Es **LLM01 del OWASP Top 10 para aplicaciones LLM**. **Fluye hacia atrás a través de las respuestas de herramientas y agentes**, así que la frontera tiene que inspeccionar lo que vuelve, no solo lo que sale.
- **Agencia excesiva.** Se concede a un agente más capacidad de la que la tarea necesita y actúa en consecuencia. Es **LLM06** de la misma lista; el modo de fallo que hace **no negociable el privilegio mínimo**.
- **Ataques de tarjeta de agente y de diputado confundido.** Una AgentCard envenenada o un token reenviado al servidor equivocado permiten a un componente comprometido actuar con la autoridad de otro. La especificación de autorización de MCP nombra el ataque de diputado confundido explícitamente en sus consideraciones de seguridad.

OWASP publica ya un **Top 10 dedicado a Aplicaciones Agénticas 2026**, la lista contra la que diseñar si tu sistema tiene agentes llamando a agentes. El hilo común: **la capa de modelo no puede ser el único punto de aplicación. Los guardrails del lado del modelo ayudan, pero son probabilísticos y nunca lo capturan todo, así que hace falta una frontera determinista entre el agente y lo que está alcanzando.**

## Gobernar la frontera (patrón de gateway)

Cada upstream al que se pone frontera se publica como _virtual server_, su propia ruta de gateway con su propio recurso OAuth. Con **PKCE** y un parámetro **`resource`** obligatorio (**RFC 8707**), un token emitido para un virtual server se rechaza en otro, cerrando el hueco de diputado confundido: un token acuñado para `/mcp/linear-v1` no puede reenviarse contra `/mcp/stripe-v1`.

Dos controles más:

- **Sin paso de tokens (_no token passthrough_).** El paso está prohibido por la especificación MCP y el gateway lo aplica: las cabeceras de autenticación entrantes nunca se filtran al upstream; el gateway resuelve la credencial del usuario en el servidor y la adjunta, guardando los tokens upstream cifrados en reposo.
- **Filtrado de capacidades.** Una política filtra las respuestas `tools/list`, `prompts/list` y `resources/list` del upstream y bloquea llamadas a lo oculto, devolviendo `MethodNotFound` incluso a un agente que ya conoce o adivina el nombre de la herramienta. Se publica un subconjunto de solo lectura o escogido a mano, en vez de entregar al agente todo.

Para A2A no hay manejador dedicado y no hace falta: **cada agente presenta su propia credencial**, así que el gateway **valida en vez de emitir** tokens, la tarea más ligera. A2A es HTTP más JSON-RPC más SSE, así que se pone frontera como a cualquier API: validación de JWT u OpenID Connect, _rate limiting_ por agente y logging completo de peticiones.

## Estado de adopción de A2A en 2026 (Glukhov)

> "A2A is not dead. It is just not universal."

- Cuando Google anunció A2A en abril de 2025, la reacción fue tibia: parecía solaparse con MCP, venía de Google (dudas sobre compromiso a largo plazo) y llegó antes de que la mayoría hubiera resuelto acceso a herramientas, inyección de prompt, observabilidad, control de coste y seguridad de sistemas monoagente. Muchos demos de 2025 no necesitaban A2A: necesitaban mejores prompts, mejores herramientas, mejores permisos, mejor lógica de reintentos y mejores logs.
- **Hacia abril de 2026, la Linux Foundation reportaba que el proyecto A2A había superado las 150 organizaciones de soporte**, ganado integraciones de plataformas cloud mayores y alcanzado despliegues en producción en múltiples industrias.
- Advertencia del autor: **"supported by" no es lo mismo que "usado en profundidad en producción por la mayoría de desarrolladores"**. Los ecosistemas de protocolo a menudo parecen más grandes en las notas de prensa de lo que se sienten en el trabajo de ingeniería diario.
- La crítica más defendible no es que A2A esté muerto, sino que **está vivo pero con un alcance útil más estrecho que el hype**.

### La ambigüedad con MCP

Un servidor MCP puede exponer algo muy agéntico: una herramienta MCP llamada `research_company` que internamente corre búsqueda, recuperación, resumen, ranking y redacción de informe. Desde el punto de vista del host MCP es **una herramienta**; desde la arquitectura, **esconde un flujo tipo agente detrás de una frontera de llamada a función**. De ahí que algunos argumentaran que A2A era innecesario.

La respuesta: A2A da estructura de primera clase a cosas que MCP trata con más torpeza — descubrimiento de agente, capacidades, ciclo de vida de tarea, trabajo de larga duración, estado multi-turno, mensajería agente-a-agente, artefactos, colaboración entre agentes opacos y delegación a través de fronteras organizativas. **Envolverlo todo como herramienta acaba siendo una mala abstracción**: en algún punto un sistema especialista tiene suficiente estado, política, ciclo de vida y autoridad de decisión propios como para que modelarlo como herramienta **oscurezca la arquitectura en lugar de simplificarla**.

### El modelo mental correcto: MCP abajo, A2A arriba

```
Usuario / aplicación
        │
        ▼
Asistente primario / orquestador
   │  (A2A)          │  (A2A)
   ▼                 ▼
Agente A          Agente B
   │  (MCP)          │  (MCP)
   ▼                 ▼
Herramientas/APIs  Herramientas/APIs
```

- A2A es la capa de colaboración entre agentes.
- MCP es la capa de integración de herramientas.

El encuadre "guerra de protocolos" es, en palabras del autor, "análisis perezoso que da buenos titulares mientras no ayuda a nadie a diseñar mejores sistemas".

### Recomendación práctica

A2A no es el protocolo por el que debería empezar la mayoría: **MCP resuelve un problema más inmediato y aplicable** (conectar agentes a herramientas y contexto útiles). A2A resuelve un problema de etapa posterior: conectar agentes independientes entre sí a través de fronteras reales de despliegue y propiedad. Recomendación: **empezar con MCP, diseñar fronteras de agente limpias desde el principio, y añadir A2A solo cuando esas fronteras se conviertan en restricciones reales de despliegue, propiedad o interoperabilidad. No adoptar A2A por vibraciones. Adoptarlo cuando la arquitectura lo exija.**
