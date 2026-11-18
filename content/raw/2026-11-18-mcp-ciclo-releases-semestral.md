---
title: "MCP adopta un ciclo de releases semestral: objetivo 2027-03-30 y el rol de Release Manager"
source: "https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/"
date: 2026-11-18
captured: 2026-11-18
---

# Un ciclo de releases más predecible para MCP (11 de noviembre de 2026)

## Qué cambia

Los Core Maintainers de MCP trabajaron el proceso en **MCPCon Europe**, y **Kurtis Van Gent** lo escribió en **SEP-3398: Release Cycle Updates**, que pasa a ser la guía de facto de releases. Como resultado, MCP mueve sus releases de especificación a un **calendario regular de seis meses**.

## Dos releases al año

- Las releases de especificación se publican en general el **último martes de marzo y de septiembre**.
- Junto a cada fecha se comparten las fechas límite de propuestas y las fechas beta de los SDK, para que se pueda planificar hacia atrás.
- Para la próxima release, el objetivo es **30 de marzo de 2027**: la versión MCP `2027-03-30`.
- Para mantener el calendario predecible, una propuesta que no esté lista **se mueve a una release posterior** en lugar de retrasar toda la especificación.
- Esto **no cambia** los mensajes de MCP ni la negociación de versión, así que no hay nada que cambiar en un cliente o servidor existente. Las versiones de especificación siguen usando fechas.

## El rol de Release Manager

Preparar una release implica autores de propuestas, Grupos de Trabajo y los mantenedores de varios SDK. Se formaliza el rol de **Release Manager**: seguir el trabajo entre el proyecto, detectar cuándo un equipo espera a otro y resolver problemas antes de una fecha límite. **Luca Chang** se une a David Soria Parra y Den Delimarsky como Release Manager para el próximo ciclo. Luca coescribió la propuesta original de _Tasks_ (soporte experimental para trabajo de larga duración en la especificación de noviembre de 2025), trabajó con Caitie McCaffrey en la _Tasks extension_, y co-lidera el Grupo de Trabajo de Tasks and Events y facilita el Grupo de Interés de Agents.

## Qué pasa entre releases

La planificación arranca **ocho meses** antes de una release regular; como se publica cada seis meses, la planificación de la siguiente se solapa con los dos últimos meses de trabajo de la actual.

- **Ocho meses antes:** empieza la planificación; se recoge _feedback_ de mantenedores y Grupos de Trabajo sobre qué hacer y qué depende de qué.
- **Seis meses antes:** empiezan las revisiones de los Core Maintainers y duran hasta el _soft freeze_.
- **Dos meses y medio antes:** _soft freeze_. Toda propuesta que vaya a la release debe estar marcada _Final_ y fusionada. Hasta el _hard freeze_ se aceptan correcciones, pulido y aclaraciones dentro de su alcance; no se aceptan nuevas funcionalidades ni rediseños sustanciales.
- **Un mes y medio antes:** llegan las betas de los SDK de Tier 1 con soporte de la especificación congelada.
- **Un mes antes:** _hard freeze_. Solo correcciones críticas de seguridad o de corrección/interoperabilidad bloqueantes entran, con aprobación por voto completo de los Core Maintainers.
- **Día de la release:** salen la especificación y las notas, con guía de implementación. Los SDK de Tier 1 deben tener soporte estable disponible de antemano; si un SDK llega tarde, se documenta el hueco sin mover la fecha.

## Implicación

MCP pasa de «spec viva, cuando esté» a **producto con calendario**. Para los equipos que construyen sobre MCP, la consecuencia práctica es que las decisiones de arquitectura se pueden anclar a fechas: la propuesta que no llegue a marzo espera a septiembre. Es la misma señal que ya se veía en la v1.0 de A2A y en el ciclo de Agent Skills: los protocolos de agentes se están **industrializando** y adoptando prácticas de gobernanza de proyectos de infraestructura maduros.
