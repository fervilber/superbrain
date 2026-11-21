---
title: "OpenAI Dots: agentes siempre encendidos que ya no esperan a que se los pida"
source: "https://aiagentstore.ai/ai-agent-news/daily/2026-11-21"
date: 2026-11-21
captured: 2026-11-21
---

# OpenAI Dots: agentes siempre encendidos que ya no esperan a que se los pida

Captura del boletín diario de AI Agent Store (21 de noviembre de 2026), complementada con
`https://learn.chatgpt.com/docs/dots`, `https://www.aicentralresources.com/news/openai-dots-agent-chatgpt-plus-background-execution`
y `https://puppyip.com/en/resources/openai-dots-agent-access-permissions-guide`.

## Titular del día: OpenAI inicia la prueba limitada de Dots (agentes siempre encendidos)

**What changed:** OpenAI is testing Dots — persistent, always‑on agents that run between conversations
and can connect to apps — with a small group of ChatGPT Plus users and is rolling availability to
eligible Business Standard workspaces.

**Why it matters:** Dots move agent capabilities from experiment to product for a broader paying user
base, which means startups and operators should assume more end users will expect agents that run
background workflows, keep state, and take multi‑step actions on their behalf.

**Try/watch:** If you sell agent integrations or widgets, map which features require persistent agent
context (background tasks, callbacks, event triggers) and prioritize hardened permission controls,
rate limits, and audit logs to handle always‑on behavior.

## Detalles de producto recuperados de la documentación oficial

- Los Dots se describen como agentes persistentes que **se ejecutan entre conversaciones** y que
  pueden **conectarse a aplicaciones** (cuentas, ficheros, calendarios, herramientas externas).
- Existe una fase explícita de **review** antes de que una acción afecte a las cuentas del usuario o
  comparta información: la revisión decide si el Dot puede proceder, **necesita aprobación** o debe
  **entregar el paso al humano**.
- El usuario puede añadir instrucciones de comportamiento («muéstrame los borradores antes de
  enviarlos»); las reglas personalizadas se aplican de forma persistente.
- Hay documentación específica de **tareas y memoria** del Dot, y de «controlar tu Dot».
- El modelo subyacente referenciado en la cobertura de prensa es de la familia GPT-6 Astra.
- La elegibilidad y la facturación se revisan por plan: la cobertura del 20 de noviembre de 2026
  describe la expansión a suscriptores de ChatGPT Plus de 20 $/mes, con acceso previo en el nivel Pro.
- OpenAI ha publicado un system card del sistema de Dots, donde se afirma que los Dots pueden
  «hacer seguimiento» de tareas por iniciativa propia.

## Contexto comparado (qué hace cada uno en la práctica)

| Producto      | Proveedor | Modelo de ejecución                                     | Disponibilidad                           |
| ------------- | --------- | ------------------------------------------------------- | ---------------------------------------- |
| ChatGPT dots  | OpenAI    | Siempre encendido, con su propio «ordenador» en la nube | Pro (desde 100 $/mes) y ahora Plus       |
| Gemini Spark  | Google    | Siempre encendido, en segundo plano                     | Google AI Ultra (99,99 $/mes en EE. UU.) |
| Claude Cowork | Anthropic | Trabajo de oficina en varios pasos                      | Por niveles                              |

## Por qué el titular importa técnicamente

1. **Cambia el disparador del agente.** Un chatbot se despierta con una pregunta y olvida; un Dot se
   despierta con un evento (correo, cambio en un fichero, temporizador) y **decide** que hay trabajo.
   El vector de entrada deja de ser el prompt del usuario y pasa a ser cualquier contenido que el
   agente lea: es exactamente el escenario donde la inyección de prompt deja de ser teórica.
2. **Cambia el modelo de estado.** El Dot mantiene contexto entre conversaciones; la memoria deja de
   ser un extra y pasa a ser el sustrato del producto.
3. **Cambia el modelo de permiso.** La aprobación ya no es un «sí» puntual delante de una acción,
   sino una política persistente que hay que diseñar por adelantado.
