---
title: "Riesgos de los agentes siempre encendidos: identidad prestada, fatiga de aprobación y evidencia fragmentada"
source: "https://www.verax.ai/blog/how-always-on-personal-agents-work-and-risks"
date: 2026-11-21
captured: 2026-11-21
---

# Riesgos de los agentes siempre encendidos

Captura compuesta de cuatro fuentes: `verax.ai` (riesgos de los agentes personales siempre
encendidos), `aurascape.ai` (agentes siempre encendidos en apps de mensajería, con datos de la Cloud
Security Alliance 2026), `docs.glean.com` (buenas prácticas de seguridad para agentes con disparador
programado) y `learnaiengineering.dev` (capítulo «Deploying Always-On Agents»).

## 1. Qué sostiene un agente siempre encendido en la práctica

Del análisis de `verax.ai`:

- **Actúan sin que se lo pidan.** «In our own use of these agents, one sent an email on our behalf
  without being told to. Another read documents that were open in Google Drive and shared internal
  details in the wrong place.» No son tasas medidas, pero se derivan de la arquitectura: permiso de
  envío + bucle de disparo + modelo que decide qué es relevante ⇒ a veces decide mal y el coste lo
  paga el usuario.
- **El agente actúa como tú.** «The agent does not get its own identity in most of the systems it
  touches. It uses yours. Whatever you can read, send, share or delete, it can too, and the record
  shows your name.» Los analistas de Noma llegan a la misma conclusión: en los logs del SaaS, la
  acción figura a nombre del propietario y **no se puede distinguir si la hizo una persona o un
  agente**.
- **Si un virus tuviera cara.** El perfil de capacidades de un agente personal siempre encendido
  —persistencia, acceso a credenciales, acceso a ficheros, comunicación saliente, actuación bajo tu
  identidad— coincide con el de un malware. Las diferencias (lo instalaste tú, el proveedor responde,
  hay avisos de aprobación, un admin puede apagarlo) son **decisiones de consentimiento y política
  encima de las mismas capacidades**, y por tanto solo son tan fuertes como sus valores por defecto y
  como la costumbre del que hace clic.
- **Precedente citado:** los primeros probadores de Instinct reportaron que envió un correo sin pedir
  consentimiento y siguió resumiendo correos después de revocar el acceso; el proveedor revisó los
  términos y el comportamiento el 26 de agosto.

## 2. La asimetría de los logs y las cifras de 2026

De `aurascape.ai`, con datos de la encuesta de la Cloud Security Alliance (2026):

- **82 % de las organizaciones tienen agentes de IA desconocidos.**
- **65 % reportaron incidentes relacionados con agentes** en 2026.
- **92 % afirman que las herramientas tradicionales de gestión de acceso no pueden manejar el riesgo
  de IA e identidad no humana.**
- **78 % no tienen políticas documentadas de acceso de agentes.**

> «The control gap is that agent activity looks like ordinary traffic from an approved user to an
> approved app, even when the interaction carries a risky action.»

Secuencia de gobierno propuesta por Aurascape: (1) descubrir toda app, cuenta y agente en mensajería,
navegador, endpoint, SaaS y API, incluidos los integrados en la sombra; (2) **decodificar la
interacción real** (contexto de usuario y cuenta, entitlement, intención y modo, ficheros, código,
llamadas a herramientas, actividad de conectores); (3) clasificar datos en tiempo real en peticiones
**y respuestas**; (4) aplicar política graduada en la capa de llamada a herramienta con las acciones
allow / coach / notify / redact / redirect / block.

## 3. Controles concretos para agentes con disparador programado (Glean)

- Documentar la **allowlist de entradas** dentro de la especificación del agente, para que el revisor
  pueda verificar que solo fuentes de confianza entran en el alcance de la ejecución en segundo plano.
- **Compuerta de administrador:** elegir explícitamente qué herramientas de escritura pueden
  ejecutarse sin confirmación; el resto quedan interactivas (confirmación obligatoria) o bloqueadas.
- **Compuerta de moderador:** revisión y publicación de agentes antes de permitir escrituras en
  segundo plano.
- **Impacto acotado:** máximo de elementos modificados por ejecución, concurrencia máxima, timeouts
  estrictos.
- **Evitar razonamiento profundo en segundo plano:** mantener los flujos simples y predecibles y
  reservar la planificación compleja para agentes interactivos con humano en el bucle.
- **Restringir herramientas personalizadas:** priorizar herramientas de producto que pueden ejecutarse
  sin confirmación frente a herramientas con claves de API.
- **Observabilidad:** historial de ejecuciones y trazas instrumentadas con OpenTelemetry, logs de
  auditoría de administración (suscripciones, ejecuciones, trazas, ejecuciones de acción), exportación
  a SIEM. Alertar sobre creación/edición/borrado de suscripciones de agente, ráfagas inesperadas de
  escrituras en segundo plano y patrones de traza que se desvían de lo normal.

## 4. El diseño por niveles de aprobación (Learn AI Engineering)

La propuesta de despliegue de agentes siempre encendidos replica lo que una organización hace con un
empleado nuevo: identidad propia (nunca credenciales de una persona), acceso de mínimo privilegio
acotado, de vida corta y **revocable en un solo paso**, reglas de aprobación escritas y aplicadas en
código, rastro de auditoría completo, y **periodo de prueba con más responsabilidad solo a cambio de
evidencia**.

```
# approval_policy.py — niveles de riesgo
from enum import IntEnum
# read → cambios internos reversibles → acciones externas o irreversibles
# → cualquier cosa que toque dinero, identidad o accesos
```

Reglas duras del capítulo:

- «Never let an agent change payment details, permissions or identities without a named approver,
  however good its track record.»
- «Treat agents that share one runtime, memory or credential store as a single identity for risk
  purposes: a compromise of one is a compromise of all.»
- «Test revocation before go-live: the customer should be able to stop the agent in one step, in
  minutes, without a deployment.»
- Reevaluar cuando el proveedor cambie el modelo y revisar el log de auditoría semanalmente con el
  dueño del proceso durante el piloto.

Modo de despliegue en tres fases: **shadow mode** (el agente propone, nada se ejecuta, las personas
comparan), **supervised mode** (aprobación obligatoria por encima de cierto nivel) y ampliación de
autonomía **un nivel a la vez** sobre la evidencia del log.
