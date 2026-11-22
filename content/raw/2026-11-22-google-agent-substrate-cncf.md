---
title: "Google dona Agent Substrate y gVisor al CNCF: aislar agentes no confiables a escala"
source: "https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html"
date: 2026-11-22
captured: 2026-11-22
---

# Google dona Agent Substrate y gVisor al CNCF: aislar agentes no confiables a escala

Captura del artículo _Sandboxing Untrusted AI Agents at Scale: Google Donates Agent Substrate and
gVisor to the CNCF_, Google Open Source Blog, publicado el **5 de noviembre de 2026** por Mofi Rahman
(Developer Relations Engineer) y Brandon Royal (Product Manager, Google Cloud). Anunciado en KubeCon
North America, Salt Lake City.

## Tesis del artículo

Cuando Google introdujo Kubernetes hace doce años, el Pod se convirtió en la unidad por defecto de
cómputo en la nube. El diseño asumía un ciclo de vida sencillo: un programa arranca, se ata a un
puerto, sirve tráfico y corre hasta que lo paras.

> "AI agents work fundamentally differently."

Un agente que corre en una máquina **ejecuta código no confiable, comandos y llamadas a herramientas**,
y debe estar aislado de su host y de sus recursos de red. Al mismo tiempo, estos agentes —ya sea un
asistente de programación interactivo, un resolutor de incidentes SRE o un bucle de evaluación
multi-turno— **no se ejecutan de forma continua**: ejecutan un paso, llaman a un modelo de lenguaje y
esperan. La mayor parte del tiempo el agente no hace absolutamente nada mientras espera a que el
modelo emita tokens o a que un humano revise un pull request.

De la misma manera que Kubernetes se creó para atender las necesidades de las aplicaciones
contenedorizadas, Google introdujo **Agent Substrate** como un nuevo orquestador para las aplicaciones
agénticas emergentes: seguro por defecto, altamente eficiente y construido para escala de millones de
agentes.

Agent Substrate se diseñó desde cero para **seguridad y densidad de agentes de IA**, y combina lo mejor
de Kubernetes con un nuevo plano de control y de datos para cómputo y almacenamiento en sandbox
totalmente aislados y de latencia ultrabaja. La comunidad creciente de Agent Substrate ha estado
construyendo capacidades centrales y estabilizando APIs, culminando en la **versión 1.0**.

En KubeCon North America, Google Cloud donó **Agent Substrate y gVisor a la Cloud Native Computing
Foundation (CNCF)** en estado _Sandbox_, junto con **OpenRL**.

## Los dos cuellos de botella de infraestructura

Los agentes de IA introducen dos cuellos de botella que el Kubernetes estándar nunca fue construido
para manejar: **desperdicio de recursos en reposo** y **sobrecarga del plano de control**.

### 1. El problema del recurso en reposo

Durante una sesión interactiva típica, un agente puede pasar **entre el 90 % y el 95 % de su tiempo
esperando** inferencia del modelo, APIs externas o revisiones humanas. Durante esa espera, el agente
consume **cero CPU**. Sin embargo, no puedes simplemente matar el contenedor: el agente mantiene estado
crítico en memoria y en disco —runtimes de lenguaje activos, repositorios Git locales, ediciones de
ficheros sin commitear y sesiones de herramientas.

Con Kubernetes estándar, los ingenieros de plataforma se enfrentan a dos opciones malas:

1. **Mantener un Pod dedicado corriendo todo el día**: el agente responde rápido porque ya está
   caliente, pero pagas por cómputo ocioso las 24 horas. A diez mil usuarios activos, los costes del
   clúster se vuelven insostenibles.
2. **Escalar a cero con contenedores serverless**: ahorras cómputo mientras el agente está ocioso,
   pero reanudar desde almacenamiento frío obliga al contenedor a clonar repositorios, reinstalar
   paquetes y reconstruir memoria. La latencia de despertar sube **por encima de 20 segundos**,
   rompiendo la experiencia interactiva.

> Platform teams need agents that wake up in under 500 milliseconds with full memory and disk state
> intact—without paying for running Pods while the agent sits idle.

### 2. La sobrecarga del plano de control

El problema opuesto ocurre al entrenar o evaluar agentes. Los bucles de aprendizaje por refuerzo y las
suites de benchmark necesitan ejecutar **código de agente no confiable a través de miles de tareas al
mismo tiempo**.

## La arquitectura de Agent Substrate

Diagrama de arquitectura: las peticiones entrantes se enrutan vía `atenet-router`, el controlador
`ateapi` hace la colocación de _actors_, hay almacenamiento por niveles (_tiered storage_) y un pool
compartido de _workers_.

### El ciclo de vida de un turno de agente

1. **Aparcado de la petición (_request parking_)**: una llamada entrante llega al proxy L7
   `atenet-router`. Si el Actor objetivo está suspendido, el proxy retiene la petición en memoria y
   alerta al controlador de Substrate.
2. **Colocación rápida (_fast placement_)**: el controlador asigna el Actor a una ranura disponible en
   el pool de Workers calientes.
3. **Restauración sub-segundo**: la memoria y el estado en disco del Actor se restauran desde el
   almacenamiento por niveles, el proceso despierta y el proxy entrega la petición. **El agente se
   reanuda en menos de 500 milisegundos justo donde se pausó.**

## Cita textual de encuadre

> "In the same way that Kubernetes was created to address the needs of containerized applications, we
> introduced Agent Substrate as a new orchestrator for the emerging agentic applications. Secure by
> default, highly efficient and built for multi-million agent scale."

## Implicaciones

- El andamiaje de agentes deja de ser un problema de aplicación y pasa a ser un problema de
  **infraestructura nativa de la nube**, con una unidad de cómputo nueva (el Actor stateful) que
  reemplaza al Pod stateless como abstracción dominante.
- La latencia de reanudación (<500 ms) y el coste en reposo se convierten en métricas de primer orden
  de la plataforma, no detalles de implementación.
- La donación a la CNCF (Agent Substrate, gVisor, OpenRL en estado Sandbox) institucionaliza el
  aislamiento de agentes como infraestructura neutral, igual que pasó con los contenedores.
