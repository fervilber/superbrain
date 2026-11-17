---
title: "Panorama de frameworks de agentes 2026: convergencia arquitectónica y el problema que queda, la gobernanza"
source: "https://www.langchain.com/resources/ai-agent-frameworks"
date: 2026-11-17
captured: 2026-11-17
---

# Frameworks de agentes en 2026 — convergencia y gobernanza

Categoría: Comparativas de frameworks. Capturado el 2026-11-17. Fuentes: langchain.com/resources/ai-agent-frameworks, dataiku.com/blog/ai-agent-frameworks, learn.microsoft.com/en-us/agent-framework/overview, github.com/microsoft/agent-framework, domino.ai, futureagi.com, hostkey.com.

## Extractos verbatim — comparativa de LangChain (2026)

> We evaluated seven options across developer experience during prototyping, production reliability, observability and debugging support, ecosystem integrations, and pricing transparency, so you can match the right framework to your stack, not just your prototype. […] This guide compares seven frameworks: **LangChain, CrewAI, Microsoft Agent Framework, LlamaIndex Workflows, Google ADK, OpenAI Agents SDK, and Mastra.**

> Choose **OpenAI Agents SDK** if you need tightly scoped assistants and clean multi-agent delegation with minimal abstraction. Choose **Mastra** if you're a TypeScript team building production agents and want workflows, memory, and a Studio environment in one package.

## Extractos verbatim — la convergencia arquitectónica (domino.ai)

> More than **50 agentic frameworks have emerged in the past year.** What is striking is not the volume but what they share. Despite being built by different teams for different purposes, they have **converged on the same underlying architecture.** […] the architecture itself is **commoditizing**. Every framework offers these building blocks. Every major platform has shipped them. If every organization has access to the same agent skeleton, **the skeleton is not the competitive advantage.**

## Extractos verbatim — Microsoft Agent Framework (Azure Blog + GitHub)

> The **Microsoft Agent Framework**, now in public preview, is the open-source SDK and runtime that simplifies the orchestration of multi-agent systems. It **converges AutoGen** […] **and the enterprise-ready foundations of Semantic Kernel** into a unified, commercial-grade framework.

> | Use an agent when… | Use a workflow when… |
> | The task is open-ended or conversational | The process has well-defined steps |
> | You need autonomous tool use and planning | You need explicit control over execution order |
> | A single LLM call (possibly with tools) suffices | Multiple agents or functions must coordinate |
>
> **If you can write a function to handle the task, do that instead of using an AI agent.**

## Extractos verbatim — el cuello de botella es la gobernanza (dataiku.com)

> Important 2026 context: **Microsoft Agent Framework 1.0 (GA April 3, 2026)** is the consolidated successor that inherits Semantic Kernel's enterprise foundations alongside AutoGen's orchestration innovations.

> In 2026, the build problem is largely solved. […] the **production accountability problem is newer**, less discussed, and the reason enterprise AI deployments still fail at a higher rate than their pilots suggest they should. Most enterprises can build an agent. **Far fewer can scale one across the business with confidence. Frameworks aren't the bottleneck. Governance is.**

## Extractos verbatim — patrones multiagente (futureagi.com)

> Five agent architecture patterns in 2026: **ReAct, plan-then-execute, supervisor and workers, graph, event-driven.** […] This is the multi-agent orchestration pattern behind **Anthropic's research system**, where the lead agent spins up 3 to 5 subagents in parallel and each subagent uses 3 or more tools in parallel. Together, those two changes cut research time by up to **90%** for complex queries.
