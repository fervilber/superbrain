---
title: "Salesforce Agentforce: el runtime de horizonte largo llega a GA con Hunter"
source: "salesforce.com (blog y notas de prensa) / PPC Land"
date: 2026-11-26
captured: 2026-11-26T20:07:00+01:00
---

# Tu agente puede esprintar, pero ¿aguanta la distancia?

URL: https://www.salesforce.com/blog/long-horizon-agents/
URL: https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/
URL: https://www.salesforce.com/blog/dreamforce-2026-announcements/

## El anuncio

El nuevo **runtime de horizonte largo (long-horizon) de Agentforce** alcanza disponibilidad general en noviembre de 2026. Extiende el horizonte de un agente de un chat a **días y semanas**, preservando memoria entre sesiones, manteniendo un plan en ejecución duradera y permitiendo la dirección (steering) sobre la marcha a partir del feedback humano. **Hunter**, el agente de ventas outbound, es el primer inquilino de producción del runtime.

Los agentes de horizonte largo aparecen donde trabaja el empleado: Agentforce Coworker, Slack o incluso aplicaciones de terceros.

## Las tres capacidades

- **Memoria**: preserva el contexto y el progreso entre sesiones, de modo que el trabajo no se detiene cuando termina la interacción.
- **Ejecución duradera (durable execution)**: mantiene los planes en ejecución a lo largo del tiempo y permite al agente reanudar o corregir el rumbo cuando cambian las circunstancias.
- **Dirección dinámica (dynamic steering)**: adapta el comportamiento del agente en función del feedback y la dirección de un usuario concreto, actualizando la configuración del agente sobre la marcha.

## Cómo trabaja Hunter, paso a paso

1. Se le da un objetivo: «reactiva mis oportunidades en riesgo». Hunter analiza las oportunidades abiertas y extrae señales de engagement de **Data 360** y **Slack**.
2. **Refina el objetivo** a una meta medible y acotada en el tiempo: «reactiva 340 000 USD de pipeline en riesgo antes de fin de trimestre».
3. **Formula un plan** que abarca días, semanas o incluso meses, con su memoria asegurando que se mantiene en curso. El plan incluye las tareas que realizará, el calendario que seguirá y los **guardarraíles** que gobiernan cuándo pide aprobación humana.
4. **Dirección conversacional**: el usuario puede dar guía adicional (por ejemplo, dirigirse a VPs en tono más formal). El agente actualiza el plan en consecuencia. El usuario previsualiza el plan en un panel lateral, hace ajustes y pulsa «activate».
5. **Ejecución con corrección de rumbo**: en el ejemplo, un correo rebota porque el destinatario está de baja. Gracias a la ejecución duradera, Hunter no se rinde: busca en datos internos y externos, identifica un destinatario alternativo y redacta un mensaje. Como eso se desvía del plan originalmente aprobado, **pide aprobación al usuario antes de enviar**. Además, aprende del incidente y sugiere actualizaciones de plan para futuras respuestas de fuera de oficina.

## Implicaciones operativas

El patrón que equipos de RevOps necesitarán rodear de **stop-rules y topes de presupuesto**: un agente que persigue un objetivo durante semanas puede acumular coste y acciones mientras nadie mira. La ejecución duradera y la memoria convierten al agente en algo más parecido a un empleado que a una función, y trasladan la pregunta de diseño de «¿qué puede hacer?» a «¿cuándo debe parar y pedir permiso?».

A lo largo del tiempo, más agentes del portfolio correrán sobre este runtime, y los clientes podrán construir sus propios agentes de horizonte largo con Agentforce y **Agent Script** (el lenguaje de código abierto de Salesforce para el comportamiento del agente, que combina razonamiento de IA con reglas deterministas).
