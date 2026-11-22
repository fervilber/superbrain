---
title: "Asegurar la comunicación agente-a-agente: identidad, atribución y fronteras de confianza en MCP y A2A"
source: "https://shattered.io/securing-ai-agent-to-agent-communication/"
date: 2026-11-22
captured: 2026-11-22
---

# Asegurar la comunicación agente-a-agente

Captura de _Securing AI Agent-to-Agent Communication_, Shattered, **17 de noviembre de 2026**, por
Marcus Bell.

## Dos protocolos que habilitan la interoperabilidad

Dos protocolos abiertos emergentes hacen posibles estas capacidades. El primero es **Model Context
Protocol (MCP)**, que estandariza cómo las aplicaciones de IA se conectan a herramientas y fuentes de
datos. El segundo es **Agent2Agent (A2A)**, que define cómo los agentes se comunican y se descubren
entre sí. Juntos, ambos protocolos **se complementan** y soportan sistemas multi-agente interoperables.

> "When agents communicate and carry out tasks without a human in the loop at every step, the volume of
> security questions and concerns multiplies."

Las organizaciones pueden necesitar claridad sobre **quién o qué se comunica, qué información se
intercambia y qué acciones están autorizadas**. Estas preguntas pueden dar forma a cómo evolucionan los
controles de identidad y acceso para entornos agénticos.

## Los agentes de IA crean nuevas rutas de comunicación

Un agente puede encargarse de **reunir datos**, otro de **analizarlos** y, una vez extraídas las
conclusiones, un tercero puede **actuar** sobre el resultado. Los protocolos MCP y A2A dan a estos
traspasos una estructura común.

La especificación de arquitectura de MCP provee un diseño **cliente-host-servidor**. Las aplicaciones
host crean clientes; cada cliente mantiene una **sesión 1:1** con un servidor que expone herramientas,
recursos de datos y prompts. Ambas partes **declaran las capacidades soportadas al inicio de la
sesión**. **El host impone permisos y consentimiento.**

El protocolo A2A habilita comunicación bidireccional. El cliente consulta el **Agent Card** de un
agente remoto para determinar qué servicios ofrece y dónde se puede acceder a él. Después el cliente
envía una instrucción para **crear una tarea**, y el agente remoto responde con los resultados, ya sea
mediante réplicas o enviando actualizaciones.

> "Access pathways are created on a per-connection basis. Each handoff may cross a trust boundary where
> assumptions about identity and authorization change."

Mapear estas rutas puede ayudar a los equipos de seguridad a ver **dónde puede hacer falta
supervisión**.

## Cada interacción de agente introduce una pregunta de identidad

La identidad empieza por **autenticar a cada agente** en una interacción: verificar el sistema en el que
corre el agente y la credencial que presenta (un token, un certificado o una credencial firmada).
**Autenticación** verifica la entidad que hace la petición; **autorización** determina si la petición se
permitirá.

La **atribución** complica esto aún más. Los agentes actúan en nombre de humanos o de aplicaciones, pero
trazar esas actividades hasta la fuente que les dio autoridad puede resultar difícil.

## Los equipos de seguridad necesitan visibilidad de toda la conversación

A medida que los sistemas agénticos se extienden por entornos empresariales, los responsables de
seguridad expresan preocupación por **cuánto de esa actividad pueden ver realmente**:

> "All of this power and freedom means we don't have full visibility into where our agentic systems are
> embedded and what they can do, when they could break away from our guardrails, and how far they could
> go when they do."

## Implicaciones

- Las **fronteras de confianza** se multiplican por cada traspaso entre agentes; el modelo 1:1 de MCP y
  el traspaso por tareas de A2A las hacen explícitas pero no las resuelven por sí mismos.
- **Atribución** —vincular una acción a la autoridad que la concedió— es el problema que queda sin
  resolver tras autenticar y autorizar.
- La cita final resume la brecha operativa: los sistemas agénticos son **opacos incluso para quienes
  los despliegan**, y esa opacidad crece con cada conexión nueva.
