---
title: "El Claude Agent SDK a finales de 2026: subagentes anidados con topes, SessionStore, skills y salidas estructuradas"
source: "https://www.developersdigest.tech/blog/claude-agent-sdk-whats-new-2026"
author: "Developers Digest"
date: 2026-10-17
captured: 2026-10-26
---

# Captura: el Claude Agent SDK a finales de 2026

> Extracto verbatim del artículo técnico (última actualización: 17 de octubre de 2026). Se reproduce el cuerpo principal; se omiten menús, relacionados y pie.

## Qué cambió en el Claude Agent SDK hacia octubre de 2026

El Claude Agent SDK es el bucle de agente de Claude Code, sus herramientas integradas, permisos, sesiones y hooks, empaquetados como biblioteca de TypeScript y Python que empaqueta y dirige el binario de Claude Code. Las releases actuales son `@anthropic-ai/claude-agent-sdk` **0.3.302** (16 de octubre de 2026) y `claude-agent-sdk` **0.2.168** para Python (15 de octubre de 2026); la versión de TypeScript sigue al CLI release por release.

Veredicto del autor: es la forma más completa de incrustar un agente capaz de programar en un proceso propio, siempre que se acepten tres cosas: solo corre modelos Claude; los productos que se distribuyan necesitan autenticación por clave de API y no pueden ofrecer login de claude.ai sin aprobación de Anthropic; y varios valores por defecto (modo de permisos, subagentes en segundo plano, subagentes anidados y fork) cambiaron este año, así que conviene fijar versiones y establecer esas opciones explícitamente.

## Cómo se relaciona el SDK con Claude Code

La descripción de Anthropic llama al Agent SDK "una biblioteca que ejecuta el binario de Claude Code". Ambos SDK empaquetan un binario nativo de Claude Code, así que la mayoría de instalaciones no necesitan nada más. Excepción: si pip instala el _source distribution_ de Python en lugar de una wheel de plataforma (por ejemplo ARM64 Windows), no hay binario empaquetado y el SDK busca una instalación nativa de Claude Code en el `PATH`.

Las releases recientes de TypeScript terminan con "Updated to parity with Claude Code v2.1.N", y desde 0.3.x el número de parche del SDK coincide con la versión del CLI. La 0.3.302 corresponde a Claude Code v2.1.302, y Python 0.2.168 empaqueta el CLI 2.1.301.

La carga de configuración sigue al CLI. Cuando se omite `settingSources`, `query()` lee ajustes de usuario, proyecto y locales, ficheros `CLAUDE.md`, y skills, agentes y comandos de `.claude/`, exactamente como lo hace la terminal. Pasar `settingSources: []` limita el agente a lo configurado en código. Los ajustes de política gestionada y `~/.claude.json` se leen en cualquier caso, por eso la documentación dice que no hay que fiarse de las opciones por defecto para aislamiento multiinquilino.

Comparativa de Anthropic: el Agent SDK (incrustar el agente de Claude Code en un proceso propio), el CLI de Claude Code (uso interactivo), el Client SDK (llamar a la API y escribir el bucle de herramientas uno mismo, o usar el tool runner beta) y Managed Agents (un harness alojado por Anthropic).

## Qué cambió en 2026 de un vistazo

| Área                  | Novedad                                                                                                                   | Desde                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Subagentes            | Se ejecutan en segundo plano por defecto                                                                                  | Claude Code v2.1.198    |
| Subagentes            | Pueden generar sus propios subagentes; los topes documentados de profundidad (3), concurrencia (20) y gasto aplican desde | TS 0.3.219 / Py 0.2.127 |
| Subagentes            | Subagentes _fork_ (`subagent_type: "fork"`) activados por defecto en sesiones del SDK                                     | TS 0.3.302              |
| Orquestación          | Herramienta `Workflow` para docenas a cientos de agentes                                                                  | TS 0.3.149              |
| Sesiones              | `SessionStore` refleja las transcripciones a tu propio backend (alpha en TS)                                              | TS 0.2.113 / Py 0.1.64  |
| Skills                | Opción `skills` de nivel superior                                                                                         | TS 0.2.120 / Py 0.1.62  |
| Hooks                 | `updatedToolOutput` para cualquier herramienta; decisión `defer` en Python                                                | TS 0.2.121 / Py 0.1.74  |
| Hooks                 | `updatedInput` validado como la propia entrada de Claude                                                                  | TS 0.3.300              |
| Permisos              | `permissionMode` omitido queda a Claude Code, luego se refina                                                             | TS 0.3.286, 0.3.302     |
| MCP y plugins         | `permission_policy` por herramienta en servidores MCP del SDK; `reloadPlugins({ addPlugins })`                            | TS 0.3.301              |
| Salidas estructuradas | Esquemas inválidos fallan al arrancar; `format` aceptado como anotación                                                   | Claude Code v2.1.205    |
| Arranque              | `startup()` para precalentar; `prewarm()` y `SpareProcess.claim()` (alpha)                                                | TS 0.2.89 / 0.3.282     |

## Paso 1: subagentes, ahora anidados y con topes

Los subagentes se definen en código con la opción `agents`. Cada `AgentDefinition` necesita `description` y `prompt`, y los campos opcionales han crecido este año:

- `tools` / `disallowedTools` — acotan lo que el subagente puede llamar.
- `model` — un alias (`'fable'`, `'opus'`, `'sonnet'`, `'haiku'`, `'inherit'`) o un ID de modelo completo.
- `effort` — `'low' | 'medium' | 'high' | 'xhigh' | 'max'` o un número.
- `maxTurns`, `skills`, `memory`, `mcpServers`, `initialPrompt`, `background`, `permissionMode`.
- `omitClaudeMd` (TS 0.3.271+) — arrancar sin `CLAUDE.md` de usuario, proyecto y local.
- `autoCompactWindow` (TS 0.3.296+) — compactar el subagente antes que la ventana principal.

Los dos últimos son solo de TypeScript; el `AgentDefinition` de Python no los tiene.

Tres cambios de comportamiento que conviene conocer antes de desplegar:

1. **El segundo plano es el defecto.** Una llamada a Agent que omite `run_in_background` lanza un subagente en segundo plano, y Claude pone `run_in_background: false` cuando necesita el resultado primero. Antes de Claude Code v2.1.198 este defecto seguía desplegándose. Poner `background: true` en una definición lo fuerza.
2. **Los subagentes anidan.** Un subagente puede generar sus propios subagentes. La documentación describe tres topes para TS 0.3.219+ y Python 0.2.127+: `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (por defecto 3 capas; `1` desactiva el anidamiento), `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (por defecto 20; devuelve `Concurrent subagent limit reached`) y `maxBudgetUsd` / `max_budget_usd` (sin defecto; cuenta el gasto de subagentes y termina la ejecución con `error_max_budget_usd`).
3. **Los subagentes fork están activados.** Desde TS 0.3.302, los subagentes fork (que heredan la conversación del padre en lugar de empezar de cero) están activados por defecto en sesiones del SDK. `CLAUDE_CODE_FORK_SUBAGENT=0` los desactiva.

Dos detalles más que tropiezan a la gente: la opción `env` de TypeScript **reemplaza** el entorno del subproceso, así que hay que esparcir `process.env` o se pierde `PATH`; el SDK de Python **fusiona** `env` en el entorno heredado. Y la herencia de permisos: un subagente corre en el modo del padre salvo que su `permissionMode` esté fijado y el padre esté en `default`, `dontAsk` o `plan`. Aun así, Claude Code nunca aplica un `bypassPermissions` de subagente (Claude Code v2.1.267+). Un subagente solo evita permisos cuando el padre lo hace.

La elección de modelo afecta a la delegación. La documentación señala que Claude Opus 5 delega a subagentes con más facilidad. Con el preset de system prompt `claude_code` sobre Opus 5, Claude Code añade una línea diciendo a Claude que no llame a la herramienta Agent salvo que se le pida; un system prompt propio, o ninguno (el defecto del SDK), no recibe esa línea, así que conviene añadir instrucción propia y fijar los topes de todos modos.

Núcleo de un agente de revisión con un subagente acotado y los tres topes (TypeScript):

```ts
import { query } from "@anthropic-ai/claude-agent-sdk"

for await (const msg of query({
  prompt: "Usa el agente security-reviewer para revisar el diff en src/auth.",
  options: {
    permissionMode: "dontAsk", // fíjalo tú; el defecto omitido cambió en 0.3.286
    allowedTools: ["Read", "Grep", "Glob", "Agent"],
    agents: {
      "security-reviewer": {
        description: "Revisa cambios de código en busca de bugs de auth e inyección.",
        prompt: "Eres un revisor de seguridad. Reporta hallazgos concretos con fichero y línea.",
        tools: ["Read", "Grep", "Glob"],
        model: "sonnet",
        effort: "high",
        maxTurns: 20,
        omitClaudeMd: true, // TS 0.3.271+
      },
    },
    // La opción env de TS REEMPLAZA el entorno del subproceso: esparce process.env
    env: {
      ...process.env,
      CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH: "2",
      CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS: "5",
    },
    maxBudgetUsd: 2, // incluye el gasto de subagentes
  },
})) {
  if (msg.type === "result") {
    if (msg.subtype === "success") console.log(msg.result)
    else console.error(msg.subtype) // p. ej. error_max_budget_usd
  }
}
```

### Cuándo subir a la herramienta Workflow

La herramienta `Workflow` (TS 0.3.149) está pensada para orquestar docenas o cientos de agentes, donde las llamadas individuales a Agent se quedan cortas.

## Skills: control, no sandbox

Las skills son ficheros `SKILL.md` en disco. No hay API de registro programático; el SDK las descubre a través de las _setting sources_, igual que el CLI. Lo que cambió es el control: la opción `skills` (TS 0.2.120, Python 0.1.62) toma una lista de nombres, `'all'` o `[]`. Los nombres coinciden con el campo `name` de la skill o el nombre de directorio, y las skills de plugin usan la forma `plugin:skill`. Las skills fuera de la lista se ocultan al modelo y la herramienta Skill las rechaza, pero **la lista no es un sandbox**.

## Permisos y sesiones

- **Permisos:** el orden de evaluación, los seis modos y el comportamiento del modo omitido; el defecto de `permissionMode` cambió en TS 0.3.286 y se refinó en 0.3.302.
- **Sesiones:** `continue`/`resume`/`fork`, y el contrato `SessionStore` que refleja las transcripciones JSONL locales a tu propio backend (alpha en TypeScript).

## Salidas estructuradas

La validación sigue draft-07; los esquemas inválidos fallan al arrancar y hay reintentos. `format` se acepta como anotación (Claude Code v2.1.205).

## Fuente original

- Developers Digest — _Claude Agent SDK in Late 2026: What Is New and How to Use It_ (17 oct 2026): https://www.developersdigest.tech/blog/claude-agent-sdk-whats-new-2026
- Documentación oficial: https://code.claude.com/docs/en/agent-sdk/overview

## Nota de captura

Captura por extracto verbatim del cuerpo principal. El texto completo limpio está en la caché de `web_extract` (`/home/vilber/.hermes/cache/web/www.developersdigest.tech-fef067b40c.md`).
