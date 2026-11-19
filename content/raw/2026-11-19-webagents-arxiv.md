---
title: "WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web"
source: "https://arxiv.org/abs/2611.21978"
date: 2026-11-16
captured: 2026-11-19
---

# WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web

Dario Fenoglio (USI/MIT), Martin Gjoreski, Marc Langheinrich, Pradyumna Chari, Ramesh Raskar. arXiv:2611.21978, 16 nov 2026.

## Abstract

Large language models are moving from isolated assistants toward autonomous agents that can plan, use tools, and coordinate with others, motivating an emerging Agentic Web of independently developed agents and services. Realizing this vision requires agent behavior to move across creators, hosts, and runtimes without coupling publication to a particular execution environment or transferring authority over user resources. We introduce WebAgents, which unbundles these roles through a signed `agent.pkg` that carries portable workflows, skills, schemas, and resource requirements. An OpenClaw-based agent-native browser/runtime verifies the package, obtains authorization, and binds it at run time to user-controlled models, tools, permissions, and budgets, while hosts distribute the public program and may retain private services server-side. We demonstrate this contract with three unrelated workflows executed unchanged under local and API-backed models, including literature review with live services and a website-published travel agent using semantic tools and user-selected personal resources. In a controlled suite, WebAgents explicitly blocks all 716 injected contract violations while accepting all 295 matched benign controls, with median automated pre-execution processing below 0.5 s for all three packages. We conclude by outlining a path toward NANDA-based discovery and interoperable package ecosystems while retaining execution authority in the user's runtime.

## Introduction (extracto)

Large Language Models (LLMs) are increasingly moving beyond passive content generation toward autonomous agents that can plan, invoke tools, maintain state, and coordinate with others. These capabilities are already being explored across domains ranging from scientific discovery to enterprise automation, suggesting a shift from isolated AI applications toward ecosystems of interacting agents. As these systems mature, the Web can become a substrate not only for humans accessing pages and services, but also for agents discovering capabilities, delegating tasks, and acting across organizational boundaries. We refer to this emerging setting as the **Agentic Web**: an open environment where independently developed agents, tools, and services can be discovered, composed, and executed. Realizing this vision, however, requires more than increasing model capability: it requires separating the roles of _creator_, _host_, and _runtime_ so that publication is not coupled to a particular execution environment and authority over user resources is never transferred away from the user.

Nota de captura: el abstract se obtuvo por búsqueda; la página `/abs/` de arXiv no renderiza el abstract en el HTML (lo inyecta en cliente), por lo que se usa `arxiv.org/html/2611.21978v1`.
