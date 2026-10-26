---
title: "Anthropic dona Agent Skills a la Agentic AI Foundation (AAIF)"
source: "https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation | https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox | https://www.grandlinux.com/en/blogs/claude-agent-skills-agentic-ai-foundation.html | https://dev.to/max_quimby/anthropic-just-gave-away-agent-skills-4g3k | https://agentskills.io/specification"
author: "Anthropic / Linux Foundation / AgentConn"
date: 2026-10-22
captured: 2026-10-26
---

# Captura: la donación de Agent Skills al AAIF

> Captura por extractos verbatim de las fuentes primarias y de los análisis secundarios consultados. No es el texto íntegro de cada página.

## Hecho

Anthropic anunció el **22 de octubre de 2026** que dona el estándar **Agent Skills** a la **Agentic AI Foundation (AAIF)**, fundación dentro de la Linux Foundation que Anthropic cofundó con Block y OpenAI a finales de 2025. La donación cubre el nombre y el logotipo de Agent Skills, la organización de GitHub que aloja la especificación y el dominio **agentskills.io**. El anuncio coincidió con AGNTCon y MCPCon North America en San José, donde la Linux Foundation aceptó cuatro proyectos nuevos el mismo día.

Cita textual de la fuente secundaria (grandlinux):

> "On 22 October 2026 Anthropic donated the Agent Skills standard, including its name, logo, GitHub organization and the agentskills.io domain, to the Agentic AI Foundation under the Linux Foundation, which already hosts MCP. A skill written once now runs on more than 70 platforms, including ChatGPT, Cursor, GitHub Copilot and VS Code. Skills your organization has already written keep working unchanged."

## Cifras divulgadas por Anthropic

- **Más de 70** plataformas de agentes soportan Agent Skills (ChatGPT, Cursor, GitHub Copilot, VS Code, Gemini CLI y otras).
- **1.000.000** de skills publicadas.
- **~280.000.000** de instalaciones desde que el estándar se publicó en diciembre de 2025.

## Cronología

| Cuándo             | Qué pasó                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Octubre 2025       | Anthropic lanza Skills en Claude Code ("conocimiento procedimental" para tareas reales)                                               |
| 9 diciembre 2025   | La Linux Foundation forma la Agentic AI Foundation con tres proyectos fundadores: MCP (Anthropic), goose (Block) y AGENTS.md (OpenAI) |
| Diciembre 2025     | Anthropic publica Agent Skills como estándar abierto en agentskills.io                                                                |
| Principios de 2026 | Skills pasa de un solo archivo a una carpeta con scripts y referencias, cargada por _progressive disclosure_                          |
| Septiembre 2026    | Claude permite a organizaciones compartir skills con personas o grupos concretos                                                      |
| 22 octubre 2026    | Anthropic dona Agent Skills al AAIF, junto a tres proyectos nuevos de OpenAI, Hugging Face y Alibaba (total: 10)                      |

## Qué aloja el AAIF (10 proyectos)

| Proyecto                     | Aportado por        | Qué hace                                                                                                                               |
| ---------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| MCP (Model Context Protocol) | Anthropic           | Estándar para conectar IA con datos y herramientas externas                                                                            |
| goose                        | Block               | Agente open source que corre en la máquina del usuario                                                                                 |
| AGENTS.md                    | OpenAI              | Archivo que declara las reglas de un proyecto a los agentes de código                                                                  |
| A2A (Agent2Agent)            | Iniciado por Google | Protocolo para que agentes de distintos fabricantes hablen entre sí                                                                    |
| Agent Router                 | —                   | Infraestructura para enrutar peticiones entre agentes                                                                                  |
| agentgateway                 | —                   | Gateway que gobierna cómo los agentes se conectan a herramientas                                                                       |
| **Agent Skills**             | **Anthropic**       | **Formato que empaqueta instrucciones, scripts y recursos para carga bajo demanda (nuevo, 22 oct)**                                    |
| Open Responses               | OpenAI              | Especificación compartida para llamar modelos de varios proveedores con una interfaz única, basada en la Responses API (nuevo, 22 oct) |
| OpenEnv                      | Hugging Face        | Framework para construir entornos de RL con los que entrenar agentes (nuevo, 22 oct)                                                   |
| OpenSandbox                  | Alibaba             | Plataforma de sandbox para ejecutar código de agentes con seguridad, con runtimes Docker y Kubernetes (nuevo, 22 oct)                  |

Miembros Platinum en el lanzamiento: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft y OpenAI.

## La especificación SKILL.md en un minuto

Un skill es una carpeta con un archivo `SKILL.md`. El archivo arranca con una cabecera corta (mínimo `name` y `description`) seguida de instrucciones en lenguaje natural. Se pueden añadir scripts, plantillas de documento y material de referencia en subcarpetas. **El agente carga solo el nombre y la descripción al arrancar, y el contenido completo cuando una tarea encaja**: por eso puede tener docenas de skills sin llenar la ventana de contexto.

Ejemplo condensado de la fuente:

```
month-end-close/
├── SKILL.md
├── references/close-checklist.md
└── scripts/check-unposted.py

--- SKILL.md ---
---
name: month-end-close
description: Monthly accounting close checklist. Use when the user mentions month-end, period close or closing the books.
license: Proprietary. LICENSE.txt has complete terms
metadata:
  author: finance-team
  version: "2.3"
---
1. Run scripts/check-unposted.py to find documents not yet posted.
2. Walk through references/close-checklist.md item by item and report what fails.
3. Never report the period as closed until every item passes.
```

| Campo de SKILL.md | ¿Requerido? | Regla en la especificación                                                                           |
| ----------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| `name`            | Sí          | Hasta 64 caracteres, minúsculas, dígitos y guiones; debe coincidir con el nombre de la carpeta       |
| `description`     | Sí          | Hasta 1.024 caracteres; qué hace y cuándo usarlo, con las palabras que dice el usuario               |
| `license`         | No          | Nombre de licencia o del archivo de licencia incluido en la carpeta                                  |
| `compatibility`   | No          | Hasta 500 caracteres; solo si el skill exige software o acceso de red concretos                      |
| `metadata`        | No          | Pares clave-valor libres (autor, versión)                                                            |
| `allowed-tools`   | No          | Herramientas preaprobadas que el skill puede ejecutar. Experimental; el soporte varía por plataforma |

Validación de referencia: `skills-ref validate ./my-skill` desde la librería de referencia del proyecto en GitHub.

## Qué cambia y qué no

| Elemento                                       | Antes del 22 oct 2026                     | Después                                                                                                                                                                                |
| ---------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Propietario del nombre, logotipo y dominio     | Anthropic                                 | Agentic AI Foundation                                                                                                                                                                  |
| Quién decide la dirección de la especificación | Anthropic con aportes de la comunidad     | Maintainers de Anthropic, Google, OpenAI y otras empresas, actuando a título individual bajo la gobernanza de la fundación. Lead Maintainers: **David Soria Parra** y **Mahesh Murag** |
| Formato SKILL.md                               | Según la especificación en agentskills.io | Sin cambios; los skills existentes siguen funcionando                                                                                                                                  |
| ¿Hay que afiliarse a la fundación?             | No                                        | No; se puede usar y contribuir sin ser miembro                                                                                                                                         |
| Qué viene                                      | Sin anuncio formal                        | Releases versionados, proceso formal de propuestas y guía de seguridad para quien escribe e instala skills                                                                             |

## El patrón repetido (análisis)

Secuencia identificada por el análisis de AgentConn:

1. **Construirlo propietario.** Skills nace en octubre de 2025 como función de Claude Code.
2. **Abrir el estándar.** El 18 de diciembre de 2025 Anthropic publica la especificación con SDK de referencia en agentskills.io. OpenAI añade soporte a ChatGPT y Codex en dos meses; Cursor, GitHub Copilot, VS Code y Gemini CLI siguen.
3. **Donar la gobernanza a una fundación que cofundaste.** El AAIF es la misma fundación que ya aloja MCP desde diciembre de 2025.

Simon Willison lo predijo en diciembre de 2025: cuando Anthropic publicó skills como "estándar abierto", anticipó que terminarían en el AAIF. Diez meses después ocurrió.

## Advertencias operativas citadas

- **"A million skills is a new supply chain to screen."** Un skill no es solo texto: lleva scripts que el agente ejecutará e instrucciones en las que confiará. Instalar un skill de un desconocido es como instalar software de un desconocido. Antes de instalar: leer `SKILL.md` y cada archivo de `scripts/`, revisar qué pide `allowed-tools` y mantener los skills de la organización en un repositorio git revisado. La guía de seguridad que el AAIF dice que producirá **es un plan, no algo con lo que contar hoy**.
- **Cada skill debería tener un dueño, como un formulario** de la organización.

## Evidencia de adopción citada

Del digest de GitHub Trending del 23 de octubre de 2026, cinco de los 15 repositorios más destacados son skills o adyacentes:

| Puesto | Repositorio                     | Estrellas | Qué es                                                                                     |
| ------ | ------------------------------- | --------- | ------------------------------------------------------------------------------------------ |
| #1     | cloudflare/security-audit-skill | 41.497    | Skill de auditoría de seguridad multifase; convierte cualquier agente de código en auditor |
| #2     | Graphify-Labs/graphify          | 133.761   | Skill de grafo de conocimiento para Claude Code, Cursor, Codex, Gemini CLI                 |
| #12    | video-shotcraft                 | 13.199    | Skill de producción de vídeo con IA para Claude Code y Codex                               |
| #13    | SnailSploit/Claude-Red          | 8.255     | Librería de skills de seguridad ofensiva para Claude                                       |
| #15    | genspark-ai/genoffice           | 10.644    | Suite ofimática con IA con integración de skills                                           |

Cloudflare ejecuta su harness subyacente contra 128 repositorios internos de forma continua, con una arquitectura de seis fases donde **el agente que encuentra una vulnerabilidad nunca es el agente que la confirma**.
