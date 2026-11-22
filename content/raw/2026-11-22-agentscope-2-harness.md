---
title: "AgentScope 2.0: del framework de agentes al Agent Harness para tareas empresariales de horizonte largo"
source: "https://www.alibabacloud.com/blog/from-agent-framework-to-agent-harness-a-new-positioning-for-the-open-source-agentscope-project_603759"
date: 2026-11-22
captured: 2026-11-22
---

# AgentScope 2.0: del framework al Agent Harness

Captura de _From Agent Framework to Agent Harness: A New Positioning for the Open-Source AgentScope
Project_, Alibaba Cloud Native Community, publicado el **11 de noviembre de 2026**.

> "This article introduces AgentScope 2.0, an Agent Harness that orchestrates complex, long-horizon
> enterprise AI tasks."

AgentScope 2.0 es a la vez un Agent Framework profundamente personalizable y, más importante, un
**Agent Harness de propósito general para tareas empresariales**. La trayectoria de Alibaba va de
Spring AI Alibaba y AgentScope 1.0 a AgentScope 2.0, casi todos con adopción empresarial amplia.

## Cuatro puntos de partida para construir agentes en la empresa

- **Frameworks de alto código**: usan código para definir y extender el comportamiento, el contexto y
  los mecanismos de ejecución del agente.
- **Harnesses productivizados**: reutilizan capacidades maduras de planificación de tareas, espacio de
  trabajo y ejecución de herramientas mediante CLI o SDK.
- **Servicios de agentes gestionados (_Managed Agents_)**: delegan la responsabilidad del Harness y su
  infraestructura de ejecución en una plataforma, dentro de un alcance acordado.
- **Plataformas de nube de agentes**: usan recursos preconfigurados y capacidades de gestión para
  crear, configurar y publicar agentes.

Estos cuatro puntos reflejan distintas divisiones de responsabilidad y pueden combinarse. Al elegir,
la empresa debe considerar la **profundidad de personalización, los límites de datos y ejecución, y
las capacidades operativas**. Los flujos de trabajo deterministas convienen a tareas con rutas
claramente definidas; los agentes son apropiados cuando se necesita exploración dinámica; y ambos
pueden combinarse cuando los límites —como aprobaciones— están fijados pero los juicios dentro de cada
paso son complejos.

> "These practices reveal a common trend: general-purpose working mechanisms are consolidated into
> reusable Harnesses and subsequently delivered as services."

Los equipos de negocio se centran en el conocimiento de dominio, las herramientas y la aceptación de
resultados; los equipos de plataforma proveen de forma centralizada la gestión de estado, entornos
aislados, permisos y observabilidad, reduciendo la duplicación.

## La evolución del foco técnico

| Etapa                       | Foco principal                                                                          | Valor para el desarrollador                                           |
| --------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Spring AI Alibaba           | Integración de modelos, datos y herramientas con aplicaciones Java                      | Integración más rápida de capacidades de IA en sistemas empresariales |
| AgentScope 1.0              | Bucles de agente, interacción con herramientas y colaboración multi-agente              | Desarrollo más flexible de aplicaciones de agente                     |
| AgentScope 2.0 HarnessAgent | Contexto, estado, colaboración y mecanismos de ejecución para tareas de horizonte largo | Construir agentes de negocio sobre un Harness de propósito general    |

Lo descrito es una **evolución en el foco técnico**. Las capacidades de Harness se acumularon
gradualmente dentro de AgentScope; no aparecieron de repente con la versión 2.0. El cambio clave de la
2.0 es **convertir el Harness de propósito general en el punto de entrada principal de desarrollo**
para tareas complejas.

## Hacer explícitos los objetivos y el progreso como estado

> "Long-running tasks cannot rely solely on chat history to represent progress."

Cientos de mensajes pueden contener a la vez planes viejos, requisitos nuevos, resultados de tests
obsoletos y acciones canceladas. Hacer que el modelo infiera "en qué punto exactamente hemos avanzado"
de nuevo en cada ronda desperdicia contexto y puede introducir ambigüedad.

AgentScope guarda el estado de ejecución mediante **`AgentState`** y pasa información como el usuario y
la sesión de la llamada actual mediante **`RuntimeContext`**. La lista de tareas se actualiza con
**`todo_write`**, y el estado del Modo Plan (_Plan Mode_) también se guarda con `AgentState`. En cada
paso de razonamiento, el modelo puede recibir una **proyección del progreso actual**.

## Mecanismos centrales en tres capas

El artículo examina los mecanismos centrales de AgentScope 2.0 como Harness de propósito general a
través de tres capas —**tareas, información y acciones**— y explica cómo su arquitectura de
_"orquestación unificada en el lado del servicio, ejecución aislada dentro de sandboxes"_ permite a las
empresas construir plataformas de _Managed Agents_ y entregar el Harness como servicio.

## Implicaciones

- El término "harness" se consolida como categoría de producto distinta del "framework": lo que se
  vende no es la librería sino el **conjunto de mecanismos de trabajo** (estado, contexto, sandbox,
  permisos, observabilidad).
- La separación _orquestación centralizada / ejecución aislada_ replica, en el plano del software, la
  separación sustrato-aplicación que Google resuelve en el plano de la infraestructura.
- El progreso como **estado explícito** (`AgentState`, `todo_write`) responde al problema real de las
  tareas de horizonte largo: el historial de chat no es un modelo válido del avance.
