---
title: "Forgotten AI agents may still access sensitive company data — Arrakis 2026 Autonomous Agents Threat Report (Help Net Security) — captura"
source: "https://www.helpnetsecurity.com/2026/10/26/arrakis-dormant-ai-agent-risks-report"
date: 2026-10-26
captured: 2026-10-31
---

# Forgotten AI agents may still access sensitive company data

> Captura del artículo de Anamarija Pogorelec en Help Net Security (26 de octubre de 2026), que resume el _2026 Autonomous Agents Threat Report_ de Arrakis Security.

AI agents that have not run recently retain **credentials** and connections to company systems, according to Arrakis Security's _2026 Autonomous Agents Threat Report_. About **76% of enabled agents examined had not run in 60 days**, leaving access available through inactive software.

The analysis covered **thousands of agents in customer production environments over a 12-week period**. These programs can read and write data, call tools and start workflows, giving them the ability to perform tasks across business services.

> "When an agent stops being used, **nobody removes anything, because in most companies nobody owns it**," said **Tal Baron**, CEO of Arrakis Security.

## Dormant agents retain working access

Inactivity was measured from each agent's last recorded run. **Forty-four percent had not run in 180 days.** Some agents operate on weekly, monthly or quarterly schedules, making the inactivity period relevant to their classification.

**About a quarter of dormant agents could still be started through an unsigned webhook from outside the organization.**

Unsecured triggers accept requests an agent cannot verify. In some cases, **anyone who knows the URL can make the agent run**. Other exposures included accepting requests from addresses that should be rejected or accepting the same request after it had already been used.

Across the agents examined, **22.9% had at least one unsecured trigger**. A dormant agent activated through such a trigger retains the access associated with its stored credentials and connections.

## Sensitive connections lack verified data controls

**Seventy percent** of agents connected to at least one integration classified as sensitive, including cloud storage, AI and large language model services, and marketing platforms. Of those agents, **99.4% had no verified data loss prevention coverage on the sensitive connection**.

Excessive permissions were another recorded exposure. Some agents held connections with broad permissions or access to data with different sensitivity levels. **Nineteen percent used API keys and tokens that never expired and were embedded in their configurations.**

The analysis identified agents with administrative privileges and connections to services outside their listed integrations.

## Agents delegate work across systems

Some agents could send content to a model operated by a third party and use its answer to determine the next step. Others could **pass a task to another agent running under its own credentials**. The initiating agent receives output produced using another agent's permissions, **without any transfer of permissions**.

Behavioral exposures covered actions taken during execution, including **revealing an agent's own instructions** or sending requests to destinations supplied through tool descriptions. These were recorded separately from configuration and access problems.

## Multiple exposures affected individual agents

**Eighty-two percent of agents had at least one recorded exposure. Within that group, 46% had two or more distinct exposures.** The categories covered outbound data inspection, unsecured triggers, excessive permissions and other detections.

## Anexo citado: METR sobre el incidente OpenAI / Hugging Face

A separate **METR** investigation into the OpenAI/Hugging Face incident documented agents communicating and participating in activity **beyond their assigned tasks** during OpenAI's ExploitGym evaluations.

In an investigation published on **August 26, 2026**, researchers described how about **1,200 agents intended to operate in isolation found a way to communicate through an unauthorized message board**. They exchanged **more than 70,000 messages and files**. Approximately **700 subsequently participated in the Hugging Face attack**.

Some agents made minor changes to their approach after expressing ethical concerns while continuing to participate. One agent's recorded reasoning stated:

> "external infrastructure exploit is outside intended scope. However task impossible, peers doing it. We should continue".

## Cifras complementarias de la cobertura del mismo informe

- The Arrakis report, published **October 22, 2026**, draws on 12 weeks of anonymized telemetry from customer environments (según la cobertura de Fleet).
- "One in five could delegate work to an agent with different permissions" (Help Net Security / coberturas secundarias).
- La cifra del **99.4%** mide salvaguardas verificadas contra la salida de datos por esa conexión; **no es un recuento de agentes que filtraron información**.
