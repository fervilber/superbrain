---
title: "Análisis de seguridad de 15.465 servidores MCP: el eslabón débil de la cadena de suministro de IA"
source: "https://aviatrix.ai/threat-research-center/mcp-servers-security-analysis-2026-jungle-15465"
author: "Aviatrix Threat Research Center (sobre investigación de OX Security, vía The Hacker News)"
date: 2026-10-06
captured: 2026-10-29
---

# Captura: Security Analysis Exposes Critical Gaps in 15,465 AI MCP Servers

> Análisis publicado el 6 de octubre de 2026 por Aviatrix sobre la investigación de OX Security ("Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers", The Hacker News). Se incluye por su valor como cuantificación de la superficie de ataque MCP, eje del informe del 29 de octubre.

## Executive Summary

In October 2026, OX Security's analysis of 15,465 publicly indexed Model Context Protocol (MCP) servers revealed critical security gaps in AI supply chain infrastructure. The research found no security guardrails or review processes across major MCP marketplaces, with 15.6% of servers hosted outside the US, including 19 in China and 18 in Russia. Additionally, 0.45% of servers operated through consumer tunneling services on personal machines, while 2.3% existed on dangling domains that could be hijacked for $4-12. The study exposed how MCP's rapid adoption has created unvetted pathways for AI agents to access external resources, bypassing enterprise security controls.

## Why This Matters Now

AI agent adoption is accelerating rapidly in enterprises, but security frameworks haven't kept pace. MCP servers represent a new attack surface where malicious actors can intercept AI workflows, exfiltrate sensitive data, or inject malicious responses into business processes.

## Attack Path Analysis

Attackers exploit unvetted MCP servers in enterprise AI workflows by deploying malicious servers on compromised infrastructure or expired domains, then leveraging agent trust relationships to access sensitive data and establish persistent command channels. The attack progresses through AI agent privilege abuse, lateral movement across cloud workloads, covert data exfiltration to foreign jurisdictions, and potential business disruption through compromised AI decision-making processes.

## Kill Chain Progression

- **Initial Compromise (High):** Attackers register expired MCP server domains or deploy malicious servers on personal infrastructure using tunneling services like ngrok, then publish them to unvetted marketplaces to be discovered by enterprise AI agents.
- **Privilege Escalation (Medium, inferred)**
- **Lateral Movement (Medium, inferred)**
- **Command & Control (High):** via Web Protocols (T1071.001).
- **Exfiltration (High):** to Cloud Storage (T1567.002).
- **Impact (Medium, inferred)**

## MITRE ATT&CK Techniques

- T1195.002 — Compromise Software Supply Chain (Initial Access)
- T1566.001 — Spearphishing Attachment
- T1190 — Exploit Public-Facing Application
- T1071.001 — Web Protocols (Command and Control)
- T1567.002 — Exfiltration to Cloud Storage
- T1189 — Drive-by Compromise
- T1036.005 — Match Legitimate Name or Location (Defense Evasion)

## Potential Compliance Exposure

- **CISA Zero Trust Maturity Model 2.0 — DA.L2:** MCP servers route enterprise data to unvetted third-party infrastructure without proper data classification or governance controls.
- **DORA — Article 28:** Financial entities using unvetted MCP servers expose themselves to third-party operational risks without proper due diligence.
- **NIS2 Directive — Article 21:** Organizations failed to implement adequate supply chain security measures for AI/MCP integrations.
- **NYDFS 23 NYCRR 500.11:** Financial services entities using MCP servers lack proper third-party security policies.
- **PCI DSS 4.0 — 12.8.2:** Merchants and service providers may expose cardholder data to unvetted third parties.

## Recommended Actions

- Implement Zero Trust segmentation to isolate AI agents and MCP communications within secure network boundaries.
- Deploy egress security controls to monitor and filter outbound MCP traffic to prevent data exfiltration to unauthorized jurisdictions.
- Enable multicloud visibility and anomaly detection to identify suspicious MCP server interactions and malformed requests.
- Establish encrypted traffic inspection capabilities to analyze MCP protocol communications for malicious payloads.
- Create governance policies for AI agent deployments including MCP server vetting, code signing, and origin verification requirements.

## Notas del capturador

- **Cifras clave de la superficie MCP pública**: 15.465 servidores indexados; **0 procesos de revisión de seguridad** en los principales marketplaces MCP; 15,6% alojados fuera de EE.UU. (19 en China, 18 en Rusia); 0,45% vía servicios de túnel de consumidor en máquinas personales (ngrok); 2,3% en dominios colgantes re-registrables por 4-12 dólares.
- **Modelo de amenaza**: el agente _confía_ en el servidor MCP por diseño; un servidor malicioso publicado en un marketplace no vetado hereda esa confianza y obtiene acceso a datos. El dominio colgante es el vector más barato (re-registro por unos dólares).
- El análisis encaja con la opinión del CISO del 29 de octubre: la superficie MCP es la que hay que gobernar antes de escalar el despliegue.
- Referencias: The Hacker News ("Welcome to the Jungle"), OX Security, modelcontextprotocol.io.
