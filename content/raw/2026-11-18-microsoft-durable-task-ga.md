---
title: "Durable Task GA para Microsoft Agent Framework: sesiones persistentes y orquestación multiagente que sobrevive a fallos"
source: "https://mc.merill.net/message/AZ578829"
date: 2026-11-18
captured: 2026-11-18
---

# Durable Task extension para Microsoft Agent Framework — GA (17 de noviembre de 2026)

## Qué se anuncia

La **extensión Durable Task para Microsoft Agent Framework** está ya disponible con carácter general (GA) para **C# y Python**. Permite construir agentes, orquestaciones multiagente y flujos de trabajo de Microsoft Agent Framework que corren de forma fiable **durante minutos, días o semanas**.

- Estado: _Launched_.
- Cronología: GA en noviembre de 2026.
- Producto: Azure Functions.
- Categoría: Containers, Internet of Things.

## Qué resuelve

La extensión **persiste las sesiones de agente**, hace _checkpoint_ del progreso de la orquestación y del flujo de trabajo, y **reanuda automáticamente el trabajo** tras límites de tasa del LLM (_rate limits_), timeouts de red, reinicios de proceso, eventos de escalado o fallos de infraestructura, **sin requerir lógica de recuperación personalizada**.

## Modelos de hospedaje

1. **Azure Functions:** hospedaje serverless gestionado, con escalado automático y endpoints HTTP generados.
2. **Trae tu propio cómputo:** contenedores, Kubernetes, servicios o infraestructura de aplicación existente.

El trabajo completado se preserva y puede reanudarse **en otro worker** sin perder el contexto de la conversación ni repetir pasos ya hechos.

## Capacidades clave

- Historial de conversación persistente.
- Orquestación multiagente **determinista**.
- Flujos de trabajo de grafo durables de Agent Framework.
- Esperas con el humano en el bucle (human-in-the-loop).
- Eventos externos.
- Limpieza de sesiones por _time-to-live_ (TTL).
- _Streaming_ fiable.
- Visibilidad a través del panel del **Durable Task Scheduler**.

## Implicación

Es la misma respuesta que dan eve 1.0 y Hermes Agent: la **durabilidad** deja de ser un parche y se convierte en requisito de arquitectura. Un agente que pierde su estado ante un reinicio o un _rate limit_ no es auditable ni operable. La GA de Durable Task cierra el círculo en el ecosistema Microsoft —Agent Framework + Azure Functions + Durable Task Scheduler— y confirma que «sesión persistente y reanudable» es ya una casilla obligatoria del _checklist_ de cualquier plataforma de agentes empresarial.
