---
title: "Top 9 AI Agent Frameworks as of October 2026 (Shakudo)"
source: "https://www.shakudo.io/blog/top-9-ai-agent-frameworks"
author: "Shakudo Team"
date: 2026-10-02
captured: 2026-10-30
---

# Captura: Top 9 AI Agent Frameworks as of October 2026 (Shakudo)

> Panorama de frameworks de agentes actualizado a octubre de 2026. Fundamenta la sección de frameworks del informe del 30 de octubre de 2026.

## Qué incluye un framework de agentes bien diseñado

- **Arquitectura de agente:** motores de decisión con gestión de memoria persistente y protocolos de interacción avanzados.
- **Capa de integración con el entorno:** APIs para integración con sistemas reales, adaptadores de entorno virtual, controles de seguridad/acceso y monitorización de rendimiento.
- **Framework de orquestación de tareas:** gestión de workflows con ejecución por prioridad y control de asignación de recursos; manejo y recuperación de errores.
- **Infraestructura de comunicación:** protocolos de interacción humano-IA, integración de APIs, intercambio de datos y canales de comunicación inter-agente.
- **Optimización de rendimiento:** aprendizaje continuo, marcos de iteración, audit trails y diagnóstico de salud del sistema.

## Los nueve frameworks

**1. LangChain.** Framework de referencia para apps LLM. Su librería compañera **LangGraph (v1.2.7)** aporta un runtime standalone basado en grafo para agentes con estado y multi-actor, y ya no requiere otros paquetes langchain-\*. Fuerte para NLP a gran escala. Contrapartida: resource-heavy y con muchas dependencias externas que hay que mantener.

**2. Kaji.** La plataforma de agente autónomo de Shakudo para entornos empresariales donde seguridad, compliance y escala son innegociables. Corre como un entorno de cómputo completo con su propio sistema de ficheros, CPU y memoria dentro de la nube privada o on-prem. Se conecta a 200+ fuentes de datos de producción out of the box. Planifica con modelos frontera, delega subtareas simples a modelos ligeros para controlar coste de tokens y se detiene a pedir aprobación humana en acciones de alto riesgo, todo gobernado por RBAC. El Shakudo AI Gateway actúa como plano de control unificado delante de Kaji, agrega cada tool interno en un único endpoint, aplica gobernanza a nivel de parámetro y elimina PII de las respuestas antes de que lleguen a modelos externos.

**3. AutoGen (AG2 / Microsoft Agent Framework).** Microsoft puso el AutoGen original en **modo mantenimiento** en octubre de 2025. El proyecto se dividió en dos: **AG2** (fork comunitario de AutoGen v0.2, mantenido por creadores originales que dejaron Microsoft) y **Microsoft Agent Framework (MAF)**, el sucesor oficial que alcanzó **v1.0 GA el 2 de abril de 2026** combinando Semantic Kernel y AutoGen.

**4. Semantic Kernel.** Framework de Microsoft que integra capacidades de IA en desarrollo de software tradicional. Absorbido en MAF como su capa de orquestación core. Los paquetes standalone siguen recibiendo actualizaciones, pero MAF es la ruta recomendada para proyectos nuevos.

**5. Google ADK 2.0 (Agent Development Kit).** Anunciado y actualizado en Google I/O 2026. Pasa de un ejecutor jerárquico a un **motor de ejecución basado en grafos** (conceptualmente similar a LangGraph). Soporta orquestación multi-agente sofisticada (agentes coordinadores, delegación a subagentes, patrones fan-out/fan-in). Incluye primitivas human-in-the-loop y persistencia de estado. `pip install google-adk`; lenguajes: Python, TypeScript, Go, Java, Kotlin. Forma parte del ecosistema Google junto con la Managed Agents API y el protocolo A2A.

**6. CrewAI (v1.15.1).** Agentes que colaboran, comparten tareas y optimizan acciones con comunicación y decisión en tiempo real. Releases recientes añadieron backends pluggables para memoria, conocimiento y RAG, junto con soporte de Snowflake Cortex.

**7. RASA (Rasa Pro 3.17.0).** Cambio arquitectónico de pipeline NLU basado en intenciones a **CALM (Conversational AI with Language Models)**, enfoque LLM-native que reemplaza la clasificación rígida de intenciones por gestión de diálogo dirigida por el modelo. Curva de aprendizaje alta; resource-intensive.

**8. smolagents (antes Hugging Face Transformers Agents), v1.26.0.** Enfoque minimalista y code-first: los agentes **escriben y ejecutan código Python directamente** para interactuar con tools, en lugar de llamadas JSON. Librería core de ~1.000 líneas, fácil de auditar. Soporta orquestación dinámica de modelos del ecosistema HF.

**9. OpenAI Agents SDK.** Sucesor oficial del experimental Swarm (archivado). Primitivas: **Agents** (LLMs con instrucciones y tools), **Handoffs** (delegación estructurada), **Guardrails** (validación de entrada/salida) y **Sandbox Agents** (entornos de ejecución de código aislados). max_turns configurable, concurrencia mejorada, soporte first-class de los últimos modelos de OpenAI.

## FAQ relevante

- **¿Qué framework es mejor para principiantes?** smolagents (menor curva por su núcleo minimalista) y Kaji (despliegue de agentes seguros sin código de integración complejo).
- **¿Cuándo LangChain vs AutoGen?** LangChain (con LangGraph) para aplicaciones complejas que requieren personalización e integraciones modulares; el AutoGen original está en mantenimiento — evaluar MAF o AG2.
