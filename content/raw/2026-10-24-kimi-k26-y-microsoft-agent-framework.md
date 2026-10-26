---
title: "Kimi K2.6 (Agent Swarm) y Microsoft Agent Framework 1.23.0 (MCP 2.x)"
captured: 2026-10-24
sources:
  - https://huggingface.co/moonshotai/Kimi-K2.6
  - https://www.kimi.ai/help/agent/agent-swarm
  - https://dropagentic.com/microsoft-agent-framework-python-release-mcp/
  - https://releasebot.io/updates/microsoft/agent-framework
---

# Kimi K2.6 — modelo agéntico multimodal nativo con Agent Swarm

Kimi K2.6 is an open-source, native multimodal agentic model that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.

## Key Features

- **Long-Horizon Coding**: K2.6 achieves significant improvements on complex, end-to-end coding tasks, generalizing robustly across programming languages (Rust, Go, Python) and domains spanning front-end, DevOps, and performance optimization.
- **Coding-Driven Design**: K2.6 is capable of transforming simple prompts and visual inputs into production-ready interfaces and lightweight full-stack workflows, generating structured layouts, interactive elements, and rich animations with deliberate aesthetic precision.
- **Elevated Agent Swarm**: Scaling horizontally to 300 sub-agents executing 4,000 coordinated steps, K2.6 can dynamically decompose tasks into parallel, domain-specialized subtasks, delivering end-to-end outputs from documents to websites to spreadsheets in a single autonomous run.
- **Proactive & Open Orchestration**: For autonomous tasks, K2.6 demonstrates strong performance in powering persistent, 24/7 background agents that proactively manage schedules, execute code, and orchestrate cross-platform operations without human oversight.

## Arquitectura

| Campo                              | Valor                                         |
| ---------------------------------- | --------------------------------------------- |
| Tipo                               | Mixture-of-Experts (MoE)                      |
| Parámetros totales                 | 1T                                            |
| Parámetros activados               | 32B                                           |
| Capas                              | 61 (1 densa)                                  |
| Dimensión de atención              | 7168                                          |
| Dimensión oculta MoE (por experto) | 2048                                          |
| Cabezas de atención                | 64                                            |
| Expertos                           | 384 (8 seleccionados por token, 1 compartido) |
| Vocabulario                        | 160K                                          |
| Longitud de contexto               | 256K                                          |
| Atención                           | MLA                                           |
| Activación                         | SwiGLU                                        |
| Codificador de visión              | MoonViT (400M parámetros)                     |
| Licencia                           | Modified MIT                                  |

Motores recomendados: vLLM, SGLang, KTransformers. API OpenAI/Anthropic-compatible en platform.moonshot.ai.

## Agent Swarm (documentación de producto)

Agent Swarm is a "horizontal scaling" architecture that coordinates up to 300 sub-agents working in parallel — no predefined roles or hand-crafted workflows required. It completes tasks approximately 4.5× faster than single-agent execution.

- 27 de enero de 2026: Kimi K2.5 introduce Agent Swarm.
- 20 de abril de 2026: se lanza y open-sourcea Kimi K2.6 con mejoras mayores de Agent Swarm.
- Entrenamiento con PARL (Parallel-Agent Reinforcement Learning). Reduce los pasos críticos 3×–4.5× en escenarios de búsqueda a gran escala.
- El agente principal (orquestador) supervisa ~15 pasos y delega hasta 300 subagentes y 4.000 pasos de flujo de trabajo.
- Caso de uso: analizar 100 nichos de YouTube creando 100 especialistas de búsqueda independientes y consolidando resultados.
- K2.6 puede programar de forma continua durante 13 horas, escribir o modificar más de 4.000 líneas de código.
- Soporta hasta 5 días de operación autónoma continua en frameworks proactivos como OpenClaw y Hermes Agent.

Nota: la documentación de Kimi indica que Agent Swarm está actualmente impulsado por Kimi K3 (K3 Swarm). Cifras de "1.000 agentes" que circulan en prensa secundaria no aparecen en la documentación oficial, que fija el límite en 300 subagentes.

---

# Microsoft Agent Framework python-1.23.0 (22 de octubre de 2026)

Microsoft has released a new Python version of its Agent Framework, a library for building AI agents, that adds MCP 2.x compatibility groundwork as a breaking change. Microsoft's release notes list the update as version 1.23.0, dated October 22, 2026.

MCP, the Model Context Protocol, is a standard that lets AI agents connect to tools and data. Microsoft says the update adds a compatibility foundation for MCP 2.x and migrates MCP transports, errors, schemas and lifecycle handling. The change is marked breaking and touches several packages, including core, declarative, hosting-mcp and AG-UI.

The release also adds allowlisted forwarding of function-invocation and client arguments from A2A request metadata. A2A is a protocol for agents to communicate with one another. Only arguments on the allowlist are passed along.

A third addition is an opt-in synthetic trailing user turn in the core and orchestrations packages. It targets providers that return empty text after a prompt that ends with an assistant message. Developers must switch it on, since it is not the default.

## Otras versiones de la serie (contexto)

- **1.22.0 (15 oct 2026)**: soporte de Python 3.15 donde esté disponible, URLs de servicio de chat configurables, respuestas de consentimiento OAuth mejoradas y soporte del proveedor de memoria Cosmos. Cambios de ruptura en semántica de contenido y streaming.
- **1.21.0 (8 oct 2026)**: controles de razonamiento, conector de vector-store nativo de Oracle (alpha), evaluación de políticas Purview sobre respuestas en streaming, guía permanente de resultados de herramientas, opción de máximo esfuerzo de razonamiento en `agent-framework-openai`.
- **dotnet-1.26.0 (23 oct 2026)**: mejoras en flujos de trabajo, integraciones MCP y AG-UI, manejo de herramientas, streaming y gestión de sesiones; capacidades de hosting A2A y file search.
