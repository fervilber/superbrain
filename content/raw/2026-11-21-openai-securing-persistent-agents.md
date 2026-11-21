---
title: "Securing persistent agents like OpenClaw at OpenAI (ingeniería de agentes persistentes)"
source: "https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai"
date: 2026-11-21
captured: 2026-11-21
---

# Securing persistent agents like OpenClaw at OpenAI

Extracto del artículo de ingeniería de OpenAI sobre cómo despliegan internamente un agente
persistente sobre OpenClaw. Es el documento técnico más útil publicado en esta ventana porque
describe el control que hace falta **cuando el agente ya no espera a que le hablen**.

## Disable destructive app operations by default

```
# Disable destructive app operations by default.
destructive_enabled = false

# Disable open-world app operations by default.
open_world_enabled = false
```

La primera línea de defensa es **negación por defecto**: las operaciones destructivas y las
operaciones de «mundo abierto» (cualquier app, cualquier destino) están apagadas hasta que alguien
las habilite explícitamente.

## Add model-based safeguards (Auto-review)

> All the controls we talked about so far are static in the sense that they rely on traditional
> deterministic code to prevent an agent from taking misaligned actions. As models get smarter, it's
> critical that we also have defenses that scale with compute - aka other models.
>
> With **Auto-review**, a second agent can monitor and approve the actions of a primary agent.
> Constantly requiring human review creates **review fatigue** where humans are trained to blindly
> accept all permission prompts. By using an LLM based reviewer as a filter, we reserve human
> attention for high value approvals. This is a feature that is natively supported in both OpenClaw
> and Codex.
>
> For our OpenClaw deployment, we enforce auto review on all agent actions.

Dos ideas operativas: (1) el guardrail determinista no escala con la capacidad del modelo, así que
hay que añadir un revisor basado en modelo; (2) el cuello de botella real de la aprobación humana no
es la seguridad sino la **fatiga de revisión**, que degrada la seguridad.

## Split agent identity from user identity

> When an agent takes an action, we need to be able to audit said action, give the agent access to
> resources, and distinguish whether that action was initiated by the agent or by the user. Agent
> identity gives us the means to do so. There are emerging specifications like **WAG** that give
> agents their own access to resources, and others like **XAA** that let agents act on behalf of the
> user through OAuth delegation. Note that agent identity is different from service accounts which
> provide separate API access for bots. The two should be used together - for example, your agent
> should act with its own agent identity and access third party services through service accounts
> which are linked to said identity.
>
> For our OpenClaw deployment, each agent has a unique identity that is associated with a ChatGPT
> Service Account. This gives each agent its own inference credential separate from the user's and
> allows teams to connect custom plugins to the agent. This also lets us audit agent actions and if
> needed, turn off inference.

## Observe everything

> Comprehensive observability lets operators understand the full lifecycle of agents - from how they
> were configured to what actions they took. With persistent agents, it's critical that we have this
> coverage in order to trace and detect misaligned actions.
>
> For our OpenClaw deployment, we log everything - every configuration change on the control plane
> and all turns from the agent. Because agent turns can contain sensitive information, these logs are
> locked down and only available to a select few individuals in the security team.

## Resumen operativo del documento

1. Negar por defecto lo destructivo y lo abierto.
2. Revisión automática por modelo sobre **todas** las acciones, no solo las de riesgo.
3. Identidad de agente separada de la del usuario, ligada a una cuenta de servicio para el acceso a
   terceros y con credencial de inferencia propia (permite apagar el agente sin tocar al humano).
4. Registro completo de cambios de configuración y de turnos, con acceso restringido.
