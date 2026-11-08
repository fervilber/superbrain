---
title: "Captura: CERT-In pide auditar agentes de IA por uso no autorizado de herramientas y abuso de privilegios (The Hindu)"
source: "https://www.thehindu.com/business/Industry/cert-in-calls-for-testing-ai-agents-for-unauthorised-tool-use-privilege-abuse/article71668646.ece"
date: 2026-11-08
captured: 2026-11-08T20:11:00+01:00
---

# CERT-In calls for testing AI agents for unauthorised tool use, privilege abuse

_The Hindu Bureau. Publicado 5 de noviembre de 2026. Captura del cuerpo sustantivo del artículo más el detalle del marco CERT-In publicado el 4 de noviembre de 2026._

Guidelines require checks on agents' permissions, task delegation and emergency-stop mechanisms; multi-agent systems must maintain authenticated, logged communications and records of actions.

The **Artificial Intelligence (AI) Security Auditing Guidelines: Framework for Secure, Ethical, and Auditable Artificial Intelligence Systems** identify features such as **autonomous task execution, persistent memory, and the ability to delegate work** as factors that can increase the risks associated with these systems.

Auditors are asked to test whether an agent can **exceed its permissions, skip approvals or misuse credentials**, and the framework reaches into agent memory, emergency-stop controls and, for multi-agent setups, **unique agent identities, authenticated and logged inter-agent messages and limits on runaway loops**. The report says nothing about enforcement, but the list already works as a build checklist: scoped credentials per agent, a record of every action and agent-to-agent exchange, and a suspend-and-revoke path that has actually been tested.

The guidelines call for records that allow auditors to **reconstruct what happened within a multi-agent system**. These should capture requests exchanged between agents, tasks delegated, permissions used, decisions made, software tools invoked and the external actions that followed.

For high-risk systems, the framework also specifies the ability to **suspend an individual agent or an entire workflow and revoke its access credentials**.

The guidelines also call for organisations to maintain an **inventory of the components used in production AI systems**, including models, training data, software and external tools. Where third-party model providers do not disclose internal details, organisations must **document the information gaps and their impact on audits**. Auditors using AI must **independently verify its outputs**, as AI-generated summaries cannot replace audit evidence or professional judgement.

## Estructura del marco (según difusión complementaria del 4-nov-2026)

- 107 páginas, publicadas el 4 de noviembre de 2026.
- 4 niveles de riesgo: Bajo, Moderado, Alto y Crítico.
- 9 dominios de auditoría: gobernanza de IA, privacidad de datos, riesgo de modelo, equidad, transparencia, ciberseguridad, monitorización continua, supervisión humana y aseguramiento de la cadena de suministro.
- 7 principios rectores: seguridad, responsabilidad, transparencia, equidad, privacidad, auditabilidad y resiliencia.
- 6 fases de auditoría: de iniciación y evaluación de riesgos a pruebas, informe y remediación.
- 5 niveles de madurez: de prácticas iniciales a optimización continua.
- Riesgos cubiertos: interacciones inseguras con herramientas y APIs, vulnerabilidades de RAG y bases vectoriales, y riesgos de la cadena de suministro de IA.
