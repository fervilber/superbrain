---
title: "HKUDS publica AutoSwarm: orquestador de hasta 11 agentes de código en paralelo"
source: "https://www.thenextgentechinsider.com/pulse/hkuds-unveils-autoswarm-to-orchestrate-multiple-ai-coding-agents-in-parallel"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# HKUDS Releases AutoSwarm: An Open-Source Orchestrator for Multi-Agent Coding Workflows

El HKU Data Intelligence Lab (HKUDS) ha publicado **AutoSwarm**, un framework de orquestación de código abierto que coordina una única tarea entre **hasta 11 agentes de código soportados** y fusiona sus salidas en un resultado unificado. **Publicado el 16 de noviembre de 2026**, la herramienta ataca el creciente problema de fragmentación en el desarrollo asistido por IA, donde los ingenieros hacen malabares con múltiples agentes —Claude Code, Cursor, Codex y otros— sin contexto compartido ni ejecución coordinada.

AutoSwarm actúa como una **capa de coordinación central**. El usuario delega una tarea compleja al orquestador, que reparte el trabajo **en paralelo** entre múltiples agentes especializados, gestiona el **contexto y la memoria compartidos** entre ellos y sintetiza las salidas individuales en un único resultado verificado. El sistema gestiona enrutado inteligente de agentes, verificación automatizada de las salidas y ejecución paralela de tareas para reducir el tiempo de reloj en proyectos multi-paso.

## Detalles técnicos — componentes clave

- **Coordinación unificada de agentes:** un solo prompt despacha trabajo a agentes heterogéneos (Claude Code, Cursor, Codex y otros) sin pasar contexto manualmente entre herramientas.
- **Gestión de contexto y memoria compartidos:** evita silos de información manteniendo un estado común entre todos los agentes activos.
- **Ejecución paralela:** las tareas se distribuyen simultáneamente en lugar de secuencialmente, reduciendo el tiempo total de finalización.
- **Síntesis y verificación automatizadas de resultados:** las salidas de los agentes se fusionan y validan antes de devolverse al usuario.

Las opciones de despliegue incluyen una aplicación de escritorio dedicada para Windows y macOS, una interfaz CLI e integraciones con IDE.

## Por qué importa

El panorama multi-agente de código se ha expandido rápidamente, pero la mayoría de los flujos de trabajo siguen siendo secuenciales y fragmentados en cuanto a contexto. AutoSwarm lo aborda tratando la flota de agentes como **una única unidad computacional** en lugar de una colección de herramientas aisladas. El proyecto es gratuito y de código abierto, con el código fuente disponible en GitHub.
