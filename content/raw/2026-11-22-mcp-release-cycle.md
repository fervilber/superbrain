---
title: "Un ciclo de publicación más predecible para MCP: semestral, con gestores de release y SEP-3398"
source: "https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/"
date: 2026-11-22
captured: 2026-11-22
---

# Un ciclo de publicación más predecible para MCP

Captura de _A More Predictable Release Cycle for MCP_, blog oficial del Model Context Protocol, **11
de noviembre de 2026**, por Den Delimarsky y David Soria Parra (Lead Maintainers). Luca Chang se une
a ellos como gestor de release para el siguiente ciclo de especificación.

## Dos releases al año

Los mantenedores principales trabajaron estas cuestiones juntos en **MCPCon Europe**, y Kurtis Van Gent
escribió el proceso en **SEP-3398: Release Cycle Updates** —la guía de release _de facto_ en adelante.

Como resultado, MCP pasa a un **calendario regular de seis meses**:

> "We'll generally publish specification releases on the **last Tuesday of March and September**."

Junto a cada fecha de publicación se compartirán las fechas límite de propuestas y las fechas beta de
los SDK, de modo que puedas planificar hacia atrás para tu propia implementación y pruebas.

Para el siguiente release, el objetivo es el **30 de marzo de 2027**: se espera que llegue entonces la
versión **`2027-03-30`**.

Para mantener el calendario predecible, **una propuesta que no esté lista se mueve a un release
posterior** en lugar de retrasar toda la especificación. Sus autores pueden seguir trabajando sin
prisa, y el resto puede seguir preparando el release que planificaron.

> **Nota:** esto cambia cómo se prepara un release, no los mensajes MCP ni la negociación de versión,
> así que no hay nada que cambiar en un cliente o servidor existente por este anuncio. Las versiones de
> especificación seguirán usando fechas.

## El nuevo rol de Release Manager

Preparar un release de especificación implica autores de propuestas, Grupos de Trabajo y los
mantenedores de varios SDK, cada uno con su propio trabajo por terminar. Se necesitan personas que
sigan ese trabajo a lo largo del proyecto, detecten cuándo un equipo espera a otro y ayuden a resolver
problemas antes de una fecha límite. Ese es el trabajo que se formaliza con el rol de **Release
Manager**.

## Qué ocurre entre releases

Los autores de propuestas necesitan tiempo para desarrollar sus ideas y responder a revisiones, mientras
que los mantenedores de SDK necesitan tiempo para implementar y probar los cambios aceptados. Por eso
**la planificación comienza ocho meses naturales antes de un release regular**. Se publica cada seis
meses, así que la planificación del siguiente release se solapa con los **dos últimos meses** de trabajo
del release actual.

Cronología para objetivos `2027-03-30` y `2027-09-28`: planificación a 8 meses, betas de SDK de Nivel
1, congelaciones suaves y duras, y la cadencia de seis meses.

El próximo release de marzo es algo distinto, ya que parte de la planificación ya concluyó en agosto de
este año. Para los ciclos regulares siguientes, el calendario se desglosa así:

- **Ocho meses antes del release**: comienza la planificación. Se recoge retroalimentación de
  mantenedores y Grupos de Trabajo sobre qué trabajar y qué depende de qué.

## Implicaciones

- MCP trata su especificación como un **producto con cadencia de release**, no como un flujo continuo de
  propuestas: fechas fijas, ventanas de propuesta, betas de SDK y un rol dedicado a coordinar.
- La regla de "propuesta no lista → release siguiente" desacopla la ambición individual de la
  puntualidad del conjunto, el mismo principio que aplican las plataformas maduras a sus trenes de
  release.
- Es un cambio **de proceso, no de protocolo**: ningún cliente o servidor existente debe cambiar por
  este anuncio.
