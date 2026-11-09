---
title: "Captura: CrowdStrike — AI Kill Switch y detección de la amenaza interna del agente"
source: "https://www.crowdstrike.com/en-us/press-releases/crowdstrike-extends-agentic-soc-detect-stop-agent-insider-threat/"
date: 2026-11-04
captured: 2026-11-09T20:13:00+01:00
---

# CrowdStrike Extends the Agentic SOC to Detect and Stop the Agent Insider Threat

CrowdStrike · Press Release · November 4, 2026 · Fal.Con Europe 2026, Barcelona

New Agent Insider Threat Detection recognizes abnormal agent behavior even when no rule is broken; coordinated multi-agent investigations now generally available.

CrowdStrike (NASDAQ: CRWD) today introduced agentic SOC innovations to detect the new insider threat: enterprise AI agents that act faster than any human can respond. Agent Insider Threat Detection exposes abnormal agent behavior and routes deviations into coordinated, multi-agent investigations that run across every domain at the same time. The verdict lands in seconds, and the new Falcon Guardian AI Kill Switch terminates the agent immediately.

> "AI agents can be both an insider threat and an adversary," said Michael Sentonas, president of CrowdStrike. "One acts without authorization from inside your walls. The other is weaponized against you from outside. Stopping the insider means knowing the moment an agent turns, investigating across every domain, and shutting it down at machine speed. That's the next evolution of the agentic SOC."

## The Threat on Your Payroll

Organizations are deploying thousands of AI agents, each with system-level access to sensitive data and the autonomy to act on it. You pay this insider in tokens.

Policy and log-based tools miss it because there is no violation to catch, and they can't tell a rogue agent from the person running it. **Agent Insider Threat Detection** in Falcon Next-Gen SIEM learns the normal behavior of every AI agent and the person who runs it and flags deviations even when no policy is violated.

## Roadmap anunciado

- **Agent Insider Threat Detection (Q4):** aprende el comportamiento normal de cada agente y su dueño, marca desviaciones aunque no se viole ninguna política, y alimenta ese riesgo al score de Falcon.
- **AI Ecosystem Detections (Q4):** detecta ataques en el patrimonio de IA, incluido abuso de API de LLM, claves de API robadas y compromiso de asistentes de código, servidores MCP y frameworks de agentes.
- **Expanded Triage Coverage (Q4):** los agentes de triaje se extienden a Falcon Guardian, Cloud, Shield (SaaS), Data Security y detecciones personalizadas.
- **Agent and Workflow Approvals (Q4):** las compuertas de aprobación se extienden más allá de llamadas individuales a herramientas, a agentes, apps y flujos enteros.
- **Policy-Drift Agent Guardrails (FY28, Q1):** Falcon Guardian inspecciona cada interacción de Charlotte AI y AgentWorks en busca de deriva de política, llamadas a herramientas no autorizadas y acceso a datos fuera de límites.
- **AI Credit Visibility and Control (Q4):** los administradores ven los créditos que consume cada agente y flujo del SOC en tiempo real, pueden detener el consumo a mitad de ejecución y subir límites.

## AI Kill Switch (3 de noviembre, disponible hoy)

- **Terminate the Running Agent:** el sensor de Falcon detiene la ejecución del agente, primero en el Gateway y pronto en el endpoint.
- **Block it from Running Again:** la política de Falcon Guardian impide que el agente se relance en el host o grupo de hosts objetivo.
- **Cut Off its Network Access:** el agente pierde su acceso a la red corporativa.
- **Human in Control, Fully Logged:** un administrador autorizado dispara la acción y cada acción queda registrada en el rastro de auditoría.

## Adquisiciones y Claude Cowork (3 de noviembre)

- CrowdStrike anunció su intención de adquirir **Fiddler AI** (observabilidad de agentes; se reportó ~400 M USD) y **Dreadnode** (testing automatizado de seguridad de IA), para añadir observabilidad y evaluación de agentes a la plataforma Falcon.
- Falcon Guardian se integra nativamente en **Claude Cowork** de Anthropic: el sensor de Falcon corre dentro de la máquina virtual donde los agentes de Cowork ejecutan código. Beta en macOS, Windows previsto para más tarde en noviembre.
