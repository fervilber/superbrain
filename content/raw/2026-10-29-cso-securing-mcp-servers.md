---
title: "Asegurar los servidores MCP antes de que el despliegue de IA supere a la seguridad"
source: "https://www.csoonline.com/article/4241763/securing-mcp-servers-before-the-ai-rollout-outpaces-security.html"
author: "Greg Neville (CSO Online, opinión)"
date: 2026-10-29
captured: 2026-10-29
---

# Captura: Securing MCP servers before the AI rollout outpaces security

> Artículo de opinión de Greg Neville (CISO, Towerwall Cyber Consulting) publicado en CSO Online el 29 de octubre de 2026.

## Resumen

El consejo aprobó el despliegue de IA sin el CISO. La tesis del autor: si no aseguras los servidores MCP ahora, luego explicarás la brecha al mismo consejo. El artículo funciona como una checklist de controles para el primer despliegue empresarial de MCP.

## What is an MCP server?

MCP servers are like the ODBC of the 1990s. Before ODBC, every application needed custom code to query databases. ODBC defined a single standard on how to talk to databases, and database vendors just developed a driver to talk to their solution.

MCP servers work in the same way: the AI app just needs to use the standardized methods to communicate with the local MCP host, and each available tool (databases, file shares, CRMs) provides an MCP server that translates the MCP transmissions into the tool's native format. So, you just need a driver on your MCP host to talk to any available endpoint.

The MCP Hosts will be in your environment, and you can control the ingress and egress traffic allowed for each MCP Host. One MCP Host can also access more than one MCP Server, allowing greater scalability, but it also adds risk.

## Top priority MCP controls

At this stage, define requirements before the MCP server implementation gets too far. Establish a list of requirements for the initial phase. Focus on the controls that deliver the most value and reduce the most risk.

### Input validation and sanitization

Inputs from any indirect external sources outside your control are untrusted and should be treated as high-risk for abuse. Identifying and removing malicious input is vital for preventing misuse of an LLM application. Input validation and sanitization include strong authentication and authorization, detection of malicious code and jailbreak attempts, and filtering sensitive or regulated data.

### Output validation and sanitization

These controls often involve enforcing a specific structure to facilitate validation, context-aware encoding and removal of unusual or unapproved data. Incorporate human oversight for higher-risk actions or other high-importance outputs, such as financial reporting.

### Network segmentation

Segmenting MCP hosts can reduce the attack surface and limit potential abuse by restricting ingress and egress traffic to authorized systems and ports.

### Server hardening

Servers should be configured following comprehensive guidelines such as the CIS Model. Hardening measures include disabling unnecessary or default accounts, closing unused ports and adjusting system settings to minimize vulnerabilities. Ideally, use infrastructure-as-code (IaaC) to make these servers ephemeral and further reduce the risk of a compromise spreading.

### Least access principle

Permissions will be key in limiting the blast radius of what an attacker can do. Multiple MCP servers can be used to reduce over-permission by grouping tools that have similar access needs. Limit access to only the users, tenants and workloads that the server needs to provide the service. Also, limit token life to as short as possible in case any token is stolen.

### Encryption

Deploy encryption at rest and in transit end-to-end, with strong key management practices.

### Tool management

Limiting the number of available tools on MCP hosts and restricting their capabilities to the minimum necessary can help reduce risks related to tool misuse and compromise.

### Third-party assessments and contracts

Ensure third-party providers implement appropriate security controls, preferably verified by independent bodies such as SOC 2, HITRUST or ISO 27001/2. Contracts should specify control requirements, and any identified high-risk gaps should be addressed through remediation agreements. A Business Associate Agreement (BAA) should be in place if protected health information (PHI) is involved.

### Audit and logging

Maintaining detailed logs of AI actions and prompts is crucial for detecting issues like hacking attempts, AI misuse and prompt abuse.

### Human-in-the-loop

Human-in-the-loop is critical for any high-risk action that an LLM application may try to take, or any highly critical data that is produced. Verify administrative actions to critical systems before allowing them to execute or be produced.

### Pre-production testing

An important, often-overlooked step is to monitor implementation and perform pre-production testing to make sure your key controls work correctly. Some potential tests would be:

- Enter fake PHI, SSNs, account numbers or whatever data is appropriate to your environment to make sure those data types are being flagged or blocked.
- Test authentication and authorization by logging in and confirming what tools you can see and access.
- Test inbound and outbound network filtering to confirm only approved systems are reachable.
- Confirm the server(s) have been hardened according to the hardening policy.
- Confirm all critical events and actions are being logged.

## The risk management approach

If you have a Risk Committee in place, it could help prioritize control requirements and timelines, so they're implemented sooner rather than later. You need to be open to prioritizing certain controls over others to avoid major roadblocks and delays in moving the product forward. A proper AI Risk Assessment will help determine the applicable threats and controls to your environment, as well as the inherent and residual risks.

For an AI threat list to build your risk assessment, I use the OWASP Top 10 for LLM Applications for my assessments and reporting. Scope the threats and rate their inherent risk in your environment.

For the Risk Committee, communicate the impacts in their language: productivity loss, downtime, loss of customer trust, regulatory fines and other industry-specific impacts, such as patient care, trading errors, bad credit decisions, unfair claims or underwriting, worker safety and service availability. Don't make it a quantitative exercise; keep it qualitative but be prepared to explain your ratings.

## Notas del capturador

- **MCP se presenta como el "ODBC de los agentes"**: un único estándar de acceso, con drivers por herramienta. La analogía es útil porque ODBC también introdujo una superficie de ataque nueva en su día.
- **El punto clave**: el _host_ MCP es controlable (ingress/egress), pero un host puede acceder a varios servidores, lo que **amplía el radio de impacto**.
- La checklist de controles coincide casi punto por punto con los marcos de seguridad agéntica de los informes del 27 y 28 de octubre: validación de entrada/salida, segmentación, hardening, mínimo privilegio, tokens de vida corta, gestión de herramientas, auditoría, human-in-the-loop y pruebas pre-producción.
- Señala explícitamente que **los inputs de fuentes externas indirectas son no confiables** — el vector de _indirect prompt injection_ (IPI) que también documenta el estudio StakeBench.
- Usa el **OWASP Top 10 for LLM Applications** como base de la evaluación de riesgos.
