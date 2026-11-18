---
title: "Perplexity Computer añade Multiagent: hasta 16 agentes sobre modelos frontera que comparten hallazgos y se revisan entre sí"
source: "https://www.perplexity.ai/hub/blog/introducing-computer-multiagent"
date: 2026-11-18
captured: 2026-11-18
---

# Perplexity Computer: nivel de esfuerzo «Multiagent» (17 de noviembre de 2026)

## Contexto

**Computer** es la plataforma de agentes de Perplexity que investiga preguntas complejas y realiza trabajo de varios pasos, desde analizar datos hasta construir apps. En septiembre, Perplexity lanzó **effort controls**, cuatro ajustes que deciden cuánto esfuerzo pone Computer en su trabajo. En todos ellos, un agente líder planifica la tarea y delega partes en agentes de apoyo.

El **17 de noviembre de 2026** se lanza **Multiagent**, un nuevo nivel de esfuerzo **por encima de Ultra** para el trabajo más complejo de Computer.

## Cómo funciona

El agente líder dirige un equipo de agentes sobre **distintos modelos frontera** que trabajan en paralelo, **comparten hallazgos directamente entre sí** y **verifican mutuamente su trabajo**. Esto permite a Computer examinar problemas complejos desde múltiples ángulos y encontrar supuestos en conflicto antes de reunir los hallazgos en una única recomendación o salida.

- **Claude Fable 5.2** planifica la tarea y la divide.
- Los agentes corren sobre **Claude Opus 5.5, GPT 6.1 Sol y Gemini 4 Carbon**.
- Los agentes comparten hallazgos mientras trabajan: uno puede usar evidencia que otro encontró, cuestionar un supuesto o señalar una discrepancia para investigarla más.
- El agente líder reúne sus aportaciones en una única respuesta con los entregables pedidos.
- Cuando se selecciona Multiagent, el líder puede asignar **hasta 16 agentes**, mientras asume parte del trabajo él mismo.
- **Fable 5.2** y **GPT 6 Astra** se unen como agentes de apoyo solo cuando el usuario los pide o cuando una parte concreta de la tarea lo requiere.
- Los agentes se comunican durante la tarea y **coordinan ediciones a ficheros compartidos**: por ejemplo, un agente actualiza los supuestos de ingresos de un modelo financiero y notifica a otro para que use esas cifras en su análisis de valoración.
- El líder sigue siendo el punto de contacto en la conversación. Para una tarea de seguimiento, el líder comunica a los agentes afectados qué ha cambiado y el equipo continúa su trabajo. **Detener el hilo detiene a todo el equipo.**

## Casos de uso

Diseñado para trabajo con partes distintas que se beneficia de análisis en paralelo y verificación cruzada:

- **Pronósticos y finanzas:** construir escenarios financieros en paralelo, comparar supuestos y comprobar el impacto de cambios en ingresos, costes o condiciones de mercado.
- **Revisión de informes anuales:** examinar estados financieros, notas y comentarios de la dirección por separado y comparar hallazgos para señalar cifras o revelaciones inconsistentes para el auditor.
- **Análisis profundo:** investigar explicaciones rivales de una cuestión empresarial o de investigación, intercambiar evidencia y comprobar qué conclusiones resisten entre fuentes.
- **Diligencia de data rooms de operaciones:** revisar en paralelo registros financieros, contratos y documentos operativos, y conectar hallazgos (p. ej., un contrato de cliente que cambia la previsión de ingresos).
- **Declaraciones de impuestos complejas y planificación de fin de año.**

## Diferenciación frente a Ultra y Model Council

- **Ultra:** un líder delega partes en agentes de apoyo que informan **solo al líder**. Para problemas abiertos donde hay que probar varios enfoques.
- **Multiagent:** el mismo modelo líder que Ultra coordina agentes que **comparten hallazgos directamente**, se verifican entre sí y contribuyen a entregables compartidos. Para encargos grandes con partes interconectadas en paralelo.
- **Model Council:** varios modelos investigan la misma pregunta **independientemente**, y Computer combina sus hallazgos mostrando dónde coinciden y dónde discrepan. Para juicios donde sirven perspectivas independientes.

## Disponibilidad

Multiagent está disponible para todos los suscriptores **Perplexity Max** en la web, seleccionando Multiagent en el deslizador de esfuerzo de Computer.

## Implicación

Multiagent formaliza la **verificación cruzada entre modelos heterogéneos** como un nivel de esfuerzo de producto. La idea —modelos distintos compartiendo hallazgos y auditándose mutuamente— es la respuesta directa al problema de que un solo modelo es su propia fuente de verdad. Perplexity no vende «más cómputo», vende **desacuerdo estructurado**: el valor está en que los agentes encuentren los supuestos en conflicto antes de que el humano tenga que hacerlo.
