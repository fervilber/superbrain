---
title: "LangSmith Tool Gateway: uso de herramientas seguro y gobernado para agentes"
source: "https://www.langchain.com/blog/langsmith-tool-gateway"
date: 2026-11-19
captured: 2026-11-20
---

# LangSmith Tool Gateway: Secure, governed tool use for agents

LangChain — 19 de noviembre de 2026 — Public Beta

Agents are moving beyond the chat window to take on more proactive and ambient work. Instead of waiting for a prompt, they run on a schedule or are triggered by events, and they're handling longer tasks without someone checking every step. That makes them much more useful, but it also means teams need to **control which tools each agent can call and whose identity it acts with**, and keep a record of every action it takes.

Today, we're launching **LangSmith Tool Gateway in Public Beta**, on the LangSmith Agent Platform. Tool Gateway is a **managed tool layer that handles credentials, identity, and access for every agent tool call**, making it simple to govern the actions your agents take.

## La gobernanza de herramientas es el núcleo de la gobernanza del agente

LLM Gateway governs the model calls agents make (spend limits, model fallbacks, rate limits, PII/secret redaction). **Tool Gateway lives in LangSmith alongside LLM Gateway**, and provides governance across this lifecycle: simplifies tool lists, implements usage policies, manages identity for tool use, and provides visibility within the agent trace.

## Cómo el uso de herramientas se convierte en un problema de gobernanza

Agents in production need to serve hundreds or thousands of users, each with their own set of permissions. This means managing and refreshing a large volume of tokens, and carefully managing and recording access for security and audit requirements. Providing agents access to tools, in production, has three requirements:

- **Access:** Define which tools this agent can call and which credentials it uses.
- **Control:** Set what each user can do with it, and establish reviews when necessary.
- **Visibility:** Track which tools are being called and confirm the agent used the right credentials.

Ejemplo citado: un gran minorista estadounidense con un _store assistant_ (credenciales individuales de cada asociado) y un _inventory agent_ que corre a las 3 a.m. con sus propias credenciales de servicio; 50+ servidores MCP exponiendo >1.000 herramientas, de las que cada agente solo debe usar un subconjunto aprobado.

## Cómo funciona: Access, Control, Visibility

### Access: qué herramientas y en nombre de quién

- **Registrar las herramientas una vez**: añadir cualquier servidor MCP por URL, o activar un servidor integrado (Google, Salesforce, GitHub…).
- **Acotar cada agente a lo que necesita**: un **tool kit** es un conjunto curado de herramientas publicado en una única URL; el agente solo ve las herramientas del kit.
- **Search mode**: cuando hay cientos o miles de herramientas, el agente consulta su kit y carga solo las relevantes a la tarea.

Identidad por llamada, con dos modos:

- **Acting as the user**: usa las credenciales del propio usuario (IdP Okta/Entra ID); si no ha conectado aún, la llamada devuelve un enlace de inicio de sesión y continúa automáticamente.
- **Acting as the agent**: credenciales ligadas al agente, vía agent auth o vía un **profile** (credenciales compartidas que un admin conecta una vez para el agente).

### Control: políticas y aprobaciones

- **Deny policies**: bloquean el uso de herramientas con granularidad por usuario, clave de servicio o combinación; también para todos con excepciones. A nivel de organización o workspace.
- **Approval policies**: piden confirmación humana para una llamada sensible antes de ejecutarla (_human-in-the-loop_).

### Visibility: trazas de llamadas

Cada llamada se traza en LangSmith con contexto de la conversación del agente; se registran **herramienta, servidor, usuario, resultado y duración**, pero **no los datos de entrada/salida** de la herramienta. En planes **Enterprise**, el **audit log** captura qué herramienta corrió y _en nombre de quién_ en toda la organización.

## Servidores integrados y despliegue

Built-in servers hosted by LangSmith: Google, Microsoft, Salesforce, GitHub, Linear (sin servidor que ejecutar ni app OAuth que registrar). Compatibilidad con cualquier cliente MCP: LangChain, Deep Agents, Managed Deep Agents, Claude Code y Cursor. Beta disponible en planes **LangSmith Plus y Enterprise**; regiones GCP US/EU/APAC y AWS US (Azure US excluida). Deny policies y audit log de organización requieren Enterprise.
