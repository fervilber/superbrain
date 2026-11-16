---
title: "Oakgen: AI Agent News, November 5 to 12, 2026 — MCP, Agent Standards, New Models and Security"
source: "https://oakgen.ai/blog/ai-agent-news-week-of-2026-11-09"
date: 2026-11-16
captured: 2026-11-16
---

# AI Agent News, November 5 to 12, 2026: MCP, Agent Standards, New Models and Security (Oakgen, 12 de noviembre de 2026)

Autor: Oakgen Team. Capturado el 2026-11-16.

## Summary (verbatim)

> A verified roundup of AI agent, MCP, standards, model and security news from November 5 to 12, 2026, ranked by importance, with a table of what to act on this week.

> The AI agent news of November 5 to 12, 2026 was dominated by security, not launches. The week's most important item is a real breach that started in an MCP server, at the German hosting company Mittwald. Two research and release items followed from the same theme, Corelight's finding that "pinned" MCP servers keep changing underneath you, and a six-vulnerability fix across the official reference servers. Next in importance came Anthropic's Claude Fable 5.2 and Mythos 5.2 on November 9, the MCP project's new six-month release schedule on November 11, and an open identity standard, Agent Name Service, landing at the Linux Foundation on November 10.

## The week at a glance (verbatim)

| Rank | Item                                               | Date   | Publisher        | Evidence               |
| ---- | -------------------------------------------------- | ------ | ---------------- | ---------------------- |
| 1    | MCP server used to breach a hosting provider       | Nov 7  | Mittwald         | Company's own account  |
| 2    | Pinned MCP servers re-resolve dependencies         | Nov 10 | Corelight        | Vendor lab observation |
| 3    | Six vulnerabilities fixed in reference MCP servers | Nov 11 | MCP servers repo | Release notes          |
| 4    | Claude Fable 5.2 and Mythos 5.2                    | Nov 9  | Anthropic        | Vendor claims          |
| 5    | MCP moves to six-month releases                    | Nov 11 | MCP project      | Official post          |
| 6    | GPT-6 Cyber                                        | Nov 5  | OpenAI           | Vendor claims          |
| 7    | Agent Name Service joins the Linux Foundation      | Nov 10 | Linux Foundation | Press release          |

## Items (verbatim, extractos)

> **5. MCP moves to a six-month release schedule (Nov 11, 2026).** The MCP blog says specification releases move to a regular six-month schedule, generally the last Tuesday of March and September. The next target is March 30, 2027, version `2027-03-30`. Soft freeze is two and a half months before release and Tier 1 SDK betas arrive one and a half months before. Luca Chang joins Den Delimarsky and David Soria Parra as a release manager. The process is written up in SEP-3398. Why it matters: Maintainers get a calendar they can plan against, and a proposal that is not ready now waits for the next release instead of delaying everyone.

> **7. Agent Name Service joins the Linux Foundation (Nov 10, 2026).** The Linux Foundation announced that Agent Name Service, an open standard for agent identity, registration and discovery built on DNS, has launched as a Linux Foundation project. The specification has seven documents. It names 11 organizations that contributed to or adopted it, including Cisco, Cloudflare, DigiCert, GoDaddy and Salesforce. Why it matters: It is a credible candidate for the identity layer that MCP and A2A do not supply, though a press release counts supporters, not production use.

> **11. Nvidia's OpenShell joins the CNCF (Nov 10, 2026).** The CNCF welcomed OpenShell as a Sandbox project. It is an open source runtime for securing and governing autonomous agents, adopting Cedar as its policy language. Repositories move to a neutral `ai-openshell` organization, and the post names core contributors from NVIDIA, Red Hat, Docker and Canonical. Why it matters: Sandbox is the CNCF's earliest stage, so treat it as promising, not proven.

> **12. Durable Task extension for Microsoft Agent Framework is GA (Nov 9, 2026).** Microsoft's announcement says durable agents keep session state across worker restarts, and durable workflows resume without repeating saved steps and can wait for approvals without holding a worker. It runs in Azure Functions or self-hosted .NET and Python apps. Why it matters: Human approval steps are where long agent jobs break.

## Notas de síntesis

- La semana (5–12 nov) estuvo dominada por **seguridad, no por lanzamientos**: una brecha real que empezó en un servidor MCP (Mittwald), el hallazgo de Corelight de que los servidores MCP "pinned" siguen cambiando bajo tus pies (re-resuelven dependencias), y un parche de seis vulnerabilidades en los servidores de referencia oficiales.
- **MCP pasa a ciclo de release semestral** (último martes de marzo y septiembre); próximo objetivo 30-mar-2027, versión `2027-03-30`; proceso documentado en SEP-3398.
- **Agent Name Service (ANS)** entra en la Linux Foundation (10-nov): identidad de agente basada en DNS, 7 documentos, 11 organizaciones (Cisco, Cloudflare, DigiCert, GoDaddy, Salesforce). Candidato creíble a la capa de identidad que MCP y A2A no dan.
- **OpenShell** (NVIDIA) entra en el CNCF como proyecto Sandbox: runtime open-source para asegurar y gobernar agentes autónomos, con Cedar como lenguaje de políticas.
- **Durable Task** de Microsoft Agent Framework en GA: agentes durables que conservan estado entre reinicios de worker y flujos que esperan aprobaciones sin retener un worker.
