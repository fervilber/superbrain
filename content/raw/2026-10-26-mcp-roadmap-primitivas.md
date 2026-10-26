---
title: "Roadmap de MCP: primitivas de mensajería agéntica, identidad de agente y transporte HTTP nativo"
source: "https://modelcontextprotocol.io/development/roadmap"
author: "Core Maintainers, Model Context Protocol"
date: 2026-08-22
captured: 2026-10-26
---

# Captura: el roadmap de MCP (última actualización: 2026-08-22)

> Texto completo extraído de la página oficial de roadmap del Model Context Protocol. Se reproduce íntegro salvo la navegación.

## Introducción

El roadmap cubre las áreas prioritarias que los Core Maintainers y los Working Groups están impulsando para la próxima release de la especificación y cómo dan forma a la revisión de los SEP (_Specification Enhancement Proposals_).

Los SEP que caen dentro de las áreas prioritarias reciben revisión acelerada y tienen la mejor probabilidad de aceptación. Los SEP fuera de ellas no se rechazan automáticamente, pero se enfrentan a una cola más larga y un listón más alto de justificación.

## Áreas prioritarias

### 1. Primitivas de mensajería agéntica

Core Maintainers: Caitie McCaffrey, Clare Liguori, Peter Alexander.

Las cargas agénticas necesitan **patrones de mensajería más allá de petición y respuesta**: trabajo que dura minutos, servidores que empujan, resultados que se transmiten en streaming y una forma de **pilotar el trabajo en vuelo** (_steer work mid-flight_). MCP ha acumulado conceptos para esto, incluidos **Tasks**, `subscriptions/listen` y **notificaciones de progreso**, repartidos entre varios Working Groups. El riesgo es tener **tres respuestas distintas a "el servidor aún no ha terminado" que no comparten ciclo de vida, modelo de cancelación ni superficie de error**. Quieren que compongan.

Para este periodo:

- **Eventos iniciados por el servidor** (Triggers & Events WG): canales y suscripciones para entrega push, incluidos webhooks. Al asumir cargas asíncronas vía Tasks y otros eventos, hacen falta extensiones que permitan al servidor decir al cliente que el trabajo terminó, sin depender solo de polling caro del lado del cliente.
- **Una revisión de composición** (Agents, Transports y Triggers & Events WGs): primitivas en construcción, como Tasks y Triggers, deben componer limpiamente entre sí y encajar en casos de uso concretos.

Más allá de esto, se espera trabajo continuado en Tasks (SEP-2663) hacia su eventual inclusión en el protocolo core.

### 2. Unificación y endurecimiento del transporte HTTP nativo

Core Maintainers: Kurtis Van Gent, Nick Cooper.

La release **2026-07-28** convirtió un servidor MCP remoto en **una carga de trabajo HTTP normal**, y cada vez más se apoyan en particularidades de HTTP (cabeceras, códigos de estado) para transportar información de nivel de transporte. Cada función nativa HTTP necesita un segundo diseño específico de stdio o no funciona localmente. Los SDK mantienen **dos pipelines de transporte**, y los metadatos del protocolo se duplican entre cabeceras HTTP y campos de mensaje que los servidores deben validar cruzadamente. Quieren **un solo modelo de transporte**, con práctica HTTP estándar encima.

Para este periodo:

- **HTTP sobre stdio** (Transports WG): _streamable HTTP_ como binding único, hablado sobre stdin/stdout para servidores locales. Creen posible usar **HTTP/2 sobre stdio** para obtener transporte HTTP multiplexado conservando las garantías de seguridad y ciclo de vida de un subproceso.
- **Caché** (Transports WG): la revisión más reciente del protocolo añadió `ttlMs` y `cacheScope` a los resultados de listado y lecturas de recursos (SEP-2549). Quieren extender el enfoque de caché para soportar **ETags**, lo que permitiría versionar los resultados de primitivas, en particular las llamadas a herramientas.

Además: manejo estandarizado de errores en todas las superficies, alcance de capacidades para listas de herramientas tras SEP-2575 (_stateless MCP_) y provisión de opciones de configuración a los servidores de forma segura.

### 3. Identidad de agente y seguridad lista para empresa

Core Maintainers: Paul Carleton, Den Delimarsky.

La autorización de MCP asume **una persona con navegador en el momento del consentimiento**. Cada vez más, el llamante es un agente: **una carga de trabajo en la nube con identidad propia**, que actúa por un usuario que no está presente, o que genera subagentes que deberían recibir **autoridad más estrecha que su padre**. Los servidores MCP existentes se apoyan en claves de API pegadas y refresh tokens de larga vida. Hace falta una forma estandarizada de que los servidores MCP manejen identidades de agente.

Para este periodo:

- **DPoP** (Agent Identity WG, en formación): finalizar la especificación de _Demonstrating Proof of Possession_ y centrarse en lograr adopción amplia.
- **Identidad de agente y delegación** (Agent Identity WG): una forma opinada de que los servidores MCP sean alcanzados por agentes mediante **su propia identidad o una identidad delegada por el usuario**. El trabajo se centrará en **Workload Identity Federation** (SEP-1933), el **Identity Assertion JWT Authorization Grant (ID-JAG)** usado por _Enterprise-Managed Authorization_ y el **intercambio de tokens RFC 8693**, coordinado con los grupos de trabajo IETF OAuth y WIMSE.

Además, bajo discusión y posible entrada en alcance cuando se forme el WG: **atestación de presencia humana**, para distinguir clientes interactivos de agentes sin cabeza (_headless_), y otras cuestiones de identidad de agente.

### 4. Primitivas mejoradas

Core Maintainers: Kurtis Van Gent, Peter Alexander, Den Delimarsky.

La interfaz de llamada a herramientas de MCP ha servido bien. Sin embargo, `tools/call` permite devolver **`content` y `structuredContent` al mismo tiempo**, lo que ha confundido tanto a autores de servidores como de clientes y ha producido implementaciones divergentes. Quieren mejorar la forma de la interfaz `tools/call` para una semántica más consistente. La comunidad repite que los servidores necesitan más opciones para guiar a los clientes por **conjuntos grandes de herramientas y recursos**, así que arrancan un esfuerzo dedicado de **descubrimiento progresivo** (_progressive discovery_).

Para este periodo:

- **Forma del resultado de herramienta** (Core Primitives WG, en formación): rediseñar `tools/call` para resolver disparidades de fidelidad entre tipos de retorno y simplificar el manejo de salida estructurada y no estructurada.
- **Descubrimiento progresivo** (Core Primitives WG): los clientes aprenden las herramientas y recursos de un servidor **a medida que los necesitan** en lugar de ingerir el catálogo completo de entrada, con una interacción definida con el trabajo de caché del área 2.
- **Anotaciones de primitiva** (Core Primitives WG): las anotaciones de contenido en la especificación declaran la audiencia y prioridad previstas de un contenido. Aplicarlas a resultados de herramienta y recursos podría resolver la confusión de visibilidad descrita en SEP-2200, pero la mayoría de los implementadores no las han adoptado y puede que no conozcan su propósito. Si no resultan útiles, consideran deprecarlas.

Además, el File Uploads WG continúa con operaciones de archivo con alcance definido y semántica de recursos tipo sistema de archivos (lecturas por rango, listado jerárquico).

### 5. Mejor experiencia de desarrollo en los SDK

Core Maintainers: Den Delimarsky, David Soria Parra.

Los SDK, servidores de referencia y quickstarts se mantienen a mano. Creen que la especificación y una **suite de tests de conformidad revisada por humanos** pueden servir como fuente de verdad de la que derivar más artefactos, de modo que SDKs y ejemplos se regeneren y revaliden en cada release en vez de repararse después.

Para este periodo:

- **El contrato de extensión** (SDK WG con los Core Maintainers): qué rol ata una extensión (host, cliente, servidor, agente) y qué hace cada uno cuando se declara la capacidad; qué deben soportar los SDK nativamente; cómo se empaquetan las extensiones; adiciones de capacidad como cambios versionados de la extensión; y autenticación tratada como área propia.
- **El experimento de artefactos generados** (SDK WG): generar un SDK Tier 1 candidato y sus quickstarts desde la especificación, validar ambos contra la suite de conformidad y publicar hallazgos con recomendación para el siguiente ciclo, incluyendo qué capas deberían ser _codegen_ determinista y cuáles asistidas por modelo.

Además: revisar propiedad y frescura esperadas de los repositorios de servidores de referencia y quickstarts, y tratar los problemas de claridad de la especificación destapados por fallos de generación como bugs de documentación.

## Cómo participar

Cada área prioritaria tiene un Working Group detrás o formándose. Vías: unirse a un WG o Interest Group, proponer o comentar un SEP, arrancar una extensión experimental (SEP-2133 permite a cualquier WG/IG experimentar en un repositorio `experimental-ext-` antes de un SEP formal), o contribuir directamente.

## Nota de contexto

La página advierte: "Este roadmap refleja el pensamiento actual más que compromisos firmes. Las prioridades pueden cambiar, algunos elementos pueden entregarse de forma distinta a la descrita o aplazarse, y trabajo no listado aquí puede aún incluirse en la release."
