---
title: "Bedrock + Spring AI: agentes autónomos en Java con tool calling, memoria y orquestación multiagente"
source: "https://aws.amazon.com/blogs/machine-learning/build-autonomous-ai-agents-with-amazon-bedrock-and-spring-ai/"
date: 2026-11-13
captured: 2026-11-13
---

# AWS — Construir agentes autónomos con Amazon Bedrock y Spring AI (11 de noviembre de 2026)

Captura por extractos del blog técnico de AWS Machine Learning. Fecha de captura: 2026-11-13.

> Java teams have established JVM tooling, continuous integration and continuous delivery (CI/CD) pipelines, and operational patterns, yet taking AI agents from prototype to production is hard: agent frameworks do not solve scalability, governance, security, and operational concerns by default. Amazon Bedrock and Spring AI close those gaps, so Java teams can build autonomous AI agents that plan, call tools and APIs, and maintain context across multi-turn conversations.

> Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. [...] It is framework-agnostic and model-agnostic: you bring your preferred agent framework and foundation model (FM). With AgentCore, you can access the production infrastructure you need: managed runtime, memory, browser automation, code execution, and identity management.

> In this post, we show you how to build autonomous AI agents in Java using Spring AI and Amazon Bedrock with spring-ai-agentcore. We explore the key implementation patterns for two systems. The first is a single-agent travel assistant that demonstrates tool calling and memory. The second is a multi-agent intelligent document processing (IDP) system that shows how specialist agents, a rules engine, and alerting work together.

> ## What makes a system an agent
>
> A chat completion call can generate text, but it can't decide what to do next, reach into external systems, or remember what happened yesterday. An agent can, because it unites three capabilities:
>
> - **Planning** – Given a goal, the model breaks it into steps, prioritizes them, and revises the plan as new information arrives.
> - **Tool use** – Beyond generating text, the model calls external systems.
> - **Memory** – The agent retains context across turns.

> Prerequisites: Java – JDK 21 (required); Spring Boot – 4.1 (with Spring AI 2.0 and spring-ai-agentcore 2.0); Maven – 3.9+; Node.js – 18+ (for the React frontend); Terraform – 1.5+; Docker – with Buildx for multi-architecture builds; AWS CLI v2, configured with credentials.
