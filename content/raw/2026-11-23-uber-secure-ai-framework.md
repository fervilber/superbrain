---
title: "El framework de seguridad de Uber gobierna los agentes autónomos a lo largo de su ciclo de vida"
source: "https://www.infoq.com/news/2026/11/uber-secure-ai-framework/"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle (InfoQ, 15 nov 2026)

En un artículo reciente, Uber Engineering destaca las limitaciones de los controles tradicionales de identidad y API a la hora de asegurar agentes de IA que razonan dinámicamente sobre contenido externo y realizan acciones en el mundo real. Para abordar este reto, Uber desarrolló un framework que determina si la acción de un agente es apropiada dados la petición del usuario, el propósito previsto del agente, sus permisos y el contexto de la interacción.

> Identity and authorization systems can determine whether a user or service has permission to access a resource, but they can't determine whether an agent's proposed action is appropriate in context.

Esto crea múltiples riesgos, incluyendo **prompt injection, envenenamiento de herramientas y memoria, secuestro de objetivos (goal hijacking), deriva conductual y acciones impulsadas por alucinaciones**, que el framework de Uber aborda a través de **tres capas** que abarcan todo el ciclo de vida del agente: desde el pre-despliegue hasta la aplicación en tiempo de ejecución y la garantía continua post-despliegue.

## Provisionamiento

En tiempo de provisionamiento, los agentes deben registrarse en el **Uber AI Registry**, estableciendo identidad, propiedad, persona, intenciones permitidas, restricciones, dependencias y clasificación de riesgo. Este proceso se automatiza con **Argus**, que analiza el código fuente del agente, prompts, configuraciones, dependencias, endpoints expuestos y rutas de invocación de herramientas para identificar debilidades de seguridad. **El mismo enfoque se aplica a los servidores MCP y las herramientas** que usan los agentes.

## Tiempo de ejecución: autorización conductual

En runtime, el framework extiende el modelo de seguridad tradicional basado en administración de políticas, decisión de políticas y aplicación de políticas para incorporar la **autorización conductual (behavioral authorization)**, que evalúa si las acciones de un agente son apropiadas en un contexto dado.

Se implementa mediante tres componentes: el **AI Registry**, los **AI Guards** y los **Agent Guard runtime hooks**. El AI Registry define y gestiona políticas, personas, intenciones y restricciones del agente; los AI Guards evalúan interacciones y acciones propuestas contra las políticas establecidas; los hooks de Agent Guard invocan a AI Guard "en puntos de control críticos y aplican su veredicto antes de permitir que una interacción o acción proceda".

## Garantía continua (post-despliegue)

Tras el despliegue, el foco pasa a la **Continuous Assurance**, que se apoya en observabilidad de extremo a extremo, auditoría, explicabilidad y replay. Esta capa comprende dos componentes principales: una **traza de ejecución unificada** que conecta acciones del agente, llamadas a herramientas y decisiones de seguridad; y **interacciones grabadas** que pueden reproducirse cuando se actualizan políticas y guardarraíles para evaluar su efectividad en el nuevo contexto.

## Retos identificados en producción

Uber también identificó varios retos al implementar controles de seguridad en producción: equilibrar lo restrictivo de las políticas para evitar tanto falsos positivos excesivos como protección insuficiente; minimizar la latencia en runtime; reducir la fricción del desarrollador durante la configuración del framework; y pasar de controles genéricos a **políticas específicas de agente**, lo que "hizo la aplicación más contextual y precisa".

Según su propio relato, **el control más fuerte fue restringir a los agentes a restricciones explícitas, es decir, mínimo privilegio en lugar de una idea nueva. El coste es la flexibilidad, y dicen que vale la pena pagarlo.**
