---
title: "Mistral Studio añade agentes gestionados, constructor de workflows, conectores HTTP y evaluaciones"
source: "https://mistral.ai/news/build-with-studio"
date: 2026-11-05
captured: 2026-11-05
---

# Build Enterprise Agents, Workflows & Apps in Mistral Studio

Mistral AI, 5 de noviembre de 2026. Captura verbatim (extractos). Extraído vía `web_extract` y `web_search`.

## Agents, workflows and apps for your business processes

Agents, workflows and apps serve different parts of a business process. An agent investigates and acts, a workflow coordinates execution and approvals, and an app gives employees a way to use these systems.

Studio brings all three together on shared infrastructure. You start with a model like Le Chonk and connect it to your enterprise data and systems through connectors and MCP servers. That foundation lets you easily build agents, workflows and apps with access to the context they need. Studio manages how they run and lets teams inspect what happened.

Through the new Mistral MCP server, developers can build with Mistral Vibe or the coding agent they already use, test locally and deploy to their Studio environment with one command. Studio handles hosting and execution, so teams can build on that foundation to get each new use case into production faster.

Today, we're expanding Studio with managed agents and apps, alongside new capabilities for workflows, enterprise context, agent observability and evaluations.

Customers and partners including ABANCA, Accenture, Alten, BNP Paribas, Capgemini, CMA CGM and Tata Consultancy Services already use Studio in production.

## Detalle técnico (AICoder, 5 de noviembre de 2026)

On November 5 Mistral expanded Mistral Studio. Managed Agents, built with the Agents SDK (mistralai-agents), run the same code in-process, self-hosted (`agents serve`) or Mistral-managed (`agents deploy`), with durable execution for hours or days, crash resume and human approvals. Mistral also shipped a Vibe-powered workflow builder, the `mistral apps` CLI, HTTP API connectors, webhooks and triggers, a managed search index, and offline and online evaluations, mostly in Public Preview.

- One agent codebase, three run modes: in-process, self-hosted `agents serve`, or managed `agents deploy`.
- Deployed agents run durably in the background, can wait for human approval and resume, and support per-session sandboxes, MCP and connectors, skills, secrets, guardrails and custom hooks.
- The workflow builder has Vibe write, test and deploy code from a description; the `mistral apps` CLI offers init, dev and deploy; connectors add HTTP APIs; a managed search index removes ops work.

Studio can run in Mistral's cloud, a customer VPC or on-premises. Mistral says one internal workflow built on it saves its product operations team about 35 hours a week.

## Fuentes complementarias

- https://aicoder.com/news/news-20261105-mistral-studio-managed-agents-apps-workflow-builder-http-connectors-online-evals
- https://docs.mistral.ai/resources/release-notes
- https://docs.mistral.ai/studio/workflows/getting-started/overview
