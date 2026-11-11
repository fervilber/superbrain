---
title: "SAP: negocio autónomo con Joule Work, Joule Assistants y la Business AI Platform"
source: "https://e3mag.com/en/autonomous-business-joule-work-joule-assistants-und-die-sap-business-ai-platform"
date: 2026-11-11
captured: 2026-11-11
---

# Autonomous Business: Joule Work, Joule Assistants, and the SAP Business AI Platform

Por Peter M. Färbinger, E3 Magazine, 11 nov 2026.

At the SAP Connect in-house exhibition, Executive Board Spokesperson Christian Klein proclaimed a supposedly groundbreaking turning point for the world of enterprise software.

Under the theme of the "autonomous enterprise," SAP showcased the integration of the new AI user interface, Joule Work, domain-specific Joule Assistants, and the integrated SAP Autonomous Suite. The consolidated SAP Business AI Platform now includes the following components: the cloud portfolio, the Business Technology Platform (SAP BTP), the Business Data Cloud (SAP BDC), and the AI Core Framework. To underscore its capabilities, SAP cites internal experience: With approximately 110,000 of its own employees, Joule Work is already in productive use and has led to demonstrable productivity gains averaging 20 percent in key administrative and logistics areas.

The transition from ad hoc assistance systems to autonomously acting AI agents is by no means merely a technical upgrade, but rather a fundamental shift in responsibility and cost structures. While SAP markets the Autonomous Suite as a way to free users from repetitive routine tasks, in operational reality, existing SAP customers face the challenge of reconciling probabilistic language models with the precision and audit-proof nature of a deterministic general ledger.

The technical core of the announced ecosystem is the Joule Work interaction layer, which allows users to initiate and execute cross-system tasks using natural language—both on mobile devices and on the desktop. To suppress stochastic hallucinations in business-critical operations, the assistant relies on the SAP Knowledge Graph. This knowledge graph maps over seven million data fields and relationship networks within the S/4 universe and provides the AI models with the necessary business context. When simple voice commands are not sufficient, specialized Joule Assistants step in to execute multi-step workflows directly within the system, based on established role and authorization models.

## Low-Code and Pro-Code

To customize and expand this agent landscape, SAP provides Joule Studio, a low-code and pro-code development environment. Business users and developers can choose from more than 70 language and AI models and design complex multi-agent workflows using the visual orchestration platform from SAP's integrated partner, n8n. To address the pressing threat of uncontrolled agent installations, SAP is relying on an open interoperability concept: The Agent2Agent (A2A) protocol and the integration of the Model Context Protocol (MCP) are designed to ensure that even third-party AI agents can be integrated into the system in a controlled manner.

The AI Agent Hub serves as the central control mechanism within the SAP LeanIX enterprise architecture solution, providing a centralized directory of all agents active within the company.

## Governance and the EU AI Act

An autonomous agent that makes erroneous procurement or payment decisions due to "hallucinations" or insufficient master data quality triggers chain reactions in the core ERP system, for which the user company is ultimately and without exception liable under the European Union's AI Act. SAP Business Data Cloud and the SAP Knowledge Graph provide these agents with trustworthy business data and business context.

The Business Data Cloud's data foundation is derided by the community as "Business Data Complexity" due to confusing license clauses and restrictions on OData data transfer. The situation is exacerbated by the restrictive SAP API Policy (Version 4.2026), which acts as a digital customs barrier by regulating direct bulk data extraction for external AI agents and forces customers to route their agent workloads through the fee-based BTP infrastructure.
