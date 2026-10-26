---
title: "Microsoft Agent Framework en BUILD 2026: Agent Harness, Hosted Agents, CodeAct y más"
source: "https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce"
author: "Shawn Henry, Principal Group Product Manager, Microsoft Agent Framework"
date: 2026-06-03
captured: 2026-10-26
---

# Captura: Microsoft Agent Framework en BUILD 2026

> Extracto verbatim de la entrada oficial del equipo de Microsoft Agent Framework (BUILD 2026, 3 de junio de 2026). Se reproduce el cuerpo principal; se omite la navegación y el pie de página corporativo.

## Resumen

BUILD 2026 está en marcha, y el equipo de Microsoft Agent Framework (MAF) reúne los anuncios. MAF es el SDK y runtime de código abierto de Microsoft para construir agentes de IA y flujos de trabajo multiagente, con los mismos conceptos y APIs en .NET y Python. Ofrece un modelo de programación limpio —clientes de chat, herramientas, integraciones MCP, proveedores de contexto, middleware y flujos de trabajo de varios pasos— para centrarse en la lógica del agente en lugar de la fontanería. MAF alcanzó **GA 1.0 el 2 de abril de 2026**, con la convergencia de AutoGen y Semantic Kernel en una única plataforma soportada.

## Agent Harness: patrones de producción integrados

El _agent harness_ es la capa donde el razonamiento del modelo se encuentra con la ejecución real: acceso a shell y sistema de archivos, flujos de aprobación humana y gestión de contexto en sesiones de larga duración. Con MAF estos patrones son ahora de primera clase. Las extensiones de harness convierten cualquier cliente de chat en un Agent Harness completo con un solo método.

Bloques que trae el harness:

- **Compactación automática de contexto:** monitoriza el uso de tokens y compacta el historial de chat a mitad del bucle para evitar el desbordamiento de la ventana de contexto en cadenas largas de llamadas a herramientas.
- **Instrucciones por defecto integradas y fusión de instrucciones:** trae instrucciones de sistema con opinión para descomposición de tareas, uso de herramientas y patrones de razonamiento. Las instrucciones del harness aparecen primero, después las instrucciones personalizadas del agente.

Proveedores y herramientas integrados:

- **FileMemoryProvider:** memoria basada en ficheros con alcance de sesión para que el agente persista notas y aprendizajes entre turnos; se guarda en `agent-file-memory/{session}/`.
- **FileAccessProvider:** acceso general a ficheros.
- **TodoProvider:** permite al agente seguir elementos de trabajo (añadir, completar, eliminar, listar) en el estado de sesión.
- **AgentModeProvider:** modos "plan" frente a "execute", separando planificación de acción.
- **AgentSkillsProvider:** descubrimiento y ejecución de skills desde el sistema de archivos, habilitando inyección modular de capacidades.
- **BackgroundAgentsProvider:** delega subtareas a agentes hijos en paralelo para orquestación de tipo fan-out.
- **Búsqueda web:** herramienta de búsqueda alojada de serie (se desactiva con `DisableWebSearch`).
- **Ejecución de shell** (solo .NET): comandos vía un `ShellExecutor` en sandbox.

Middleware y personalización:

- **ToolApprovalAgent:** reglas de aprobación "no preguntar de nuevo" para llamadas sensibles.
- **OpenTelemetryAgent:** trazado automático con Semantic Conventions.
- **Backends de almacenamiento conectables:** intercambiar `FileMemoryStore` y `FileAccessStore` por cualquier implementación de `AgentFileStore` (sistema de archivos, blob storage, etc.).

Ejemplo en .NET:

```csharp
AIAgent agent = chatClient.AsHarnessAgent(
    MaxContextWindowTokens,
    MaxOutputTokens,
    new HarnessAgentOptions {
        Name = "BlogWriterAgent",
        Description = "Un asistente de redacción que investiga un tema, planifica un esquema y redacta un post.",
        FileMemoryStore = new FileSystemAgentFileStore(Path.Combine(AppContext.BaseDirectory, "artifacts")),
        ChatOptions = new ChatOptions { Instructions = instructions, Tools = [ new WebBrowsingTool(), ], },
    });
await HarnessConsole.RunAgentAsync(
    agent,
    userPrompt: "Introduce un tema de blog para empezar.",
    new HarnessConsoleOptions {
        Observers = [ new OpenAIResponsesWebSearchDisplayObserver(), new OpenAIResponsesErrorObserver() ],
        CommandHandlers = HarnessConsoleOptions.BuildDefaultCommandHandlers(agent),
    });
```

Ejemplo en Python:

```python
agent = create_harness_agent(
    client=client,
    max_context_window_tokens=128_000,
    max_output_tokens=16_384,
    name="ResearchAgent",
    description="Un asistente de investigación que planifica y ejecuta tareas.",
    agent_instructions=RESEARCH_INSTRUCTIONS,
)
```

## Foundry Hosted Agents: de local a producción

Una vez que el agente MAF corre en local, la siguiente pregunta es cómo desplegarlo, monitorizarlo, evaluarlo y versionarlo. **Hosted Agents en Foundry Agent Service** da al agente un hogar de producción con código propio, empaquetado como contenedor y desplegado en infraestructura gestionada por Foundry, con identidad integrada, escalado automático, estado de sesión gestionado, observabilidad y versionado.

De serie:

- **Escala a cero**, sin coste mientras el agente está inactivo; escala de vuelta en la siguiente petición.
- **Reanudación con el sistema de archivos intacto**, ficheros, estado de disco e identidad de sesión persisten a través del escalado a cero.
- **Aislamiento por sesión**, cada sesión recibe su propio sandbox aislado por VM con estado persistente.
- **Observabilidad integrada**, las trazas OpenTelemetry de MAF fluyen a Application Insights sin cableado extra.

Convertir un agente local en alojado son unas pocas líneas. En .NET:

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);
var app = builder.Build();
app.MapFoundryResponses();
app.Run();
```

En Python:

```python
server = ResponsesHostServer(agent)
server.run()
```

## CodeAct: agentes más rápidos con menos turnos de modelo

Muchos agentes no están limitados por la calidad del modelo, sino por la sobrecarga de orquestación. Cuando un agente encadena muchas llamadas pequeñas a herramientas, cada paso es un turno de modelo separado, disparando latencia y uso de tokens.

**CodeAct** colapsa ese bucle. En lugar de elegir una herramienta, esperar y elegir la siguiente, el modelo escribe un único programa corto en Python que llama a tus herramientas vía `call_tool(…)`, lo ejecuta una vez en un sandbox y devuelve un resultado consolidado. CodeAct viene en el nuevo paquete `agent-framework-hyperlight` (alpha), que ejecuta el código generado por el modelo en una micro-VM aislada de **Hyperlight** por llamada, de modo que el aislamiento fuerte es prácticamente gratis a la granularidad de una sola llamada a herramienta.

Cablearlo es un cambio de una línea en cómo se registran las herramientas:

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Devuelve el tiempo actual para una ciudad."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(tools=[get_weather], approval_mode="never_require")

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="Eres un asistente útil.",
    context_providers=[codeact],
)

result = await agent.run("Obtén el tiempo de Seattle y Ámsterdam y compáralos.")
```

Sobre una carga representativa de varios pasos (cálculo de totales de pedidos entre muchos usuarios, docenas de llamadas a herramientas), la diferencia es significativa:

| Cableado    | Tiempo     | Tokens     |
| ----------- | ---------- | ---------- |
| Tradicional | 27.81 s    | 6.890      |
| CodeAct     | 13.23 s    | 2.489      |
| **Mejora**  | **52,4 %** | **63,9 %** |

## También alcanzando 1.0

### Integración del GitHub Copilot SDK

MAF ahora soporta construir agentes sobre el [GitHub Copilot SDK](https://github.com/github/copilot-sdk) como backend, trayendo las capacidades orientadas a código de Copilot (ejecución de shell, operaciones de ficheros, obtención de URL e integración de servidores MCP) al modelo de programación estándar de MAF.

Python:

```python
import asyncio
from agent_framework.github import GitHubCopilotAgent

async def basic_example():
    agent = GitHubCopilotAgent(
        default_options={"instructions": "Eres un asistente útil."},
    )
    async with agent:
        result = await agent.run("¿Qué es Microsoft Agent Framework?")
        print(result)
```

.NET:

```csharp
using GitHub.Copilot.SDK;
using Microsoft.Agents.AI;

await using CopilotClient copilotClient = new();
await copilotClient.StartAsync();
AIAgent agent = copilotClient.AsAIAgent();
Console.WriteLine(await agent.RunAsync("¿Qué es Microsoft Agent Framework?"));
```

El agente Copilot es un agente MAF estándar, así que soporta herramientas, instrucciones, streaming, sesiones, servidores MCP y observabilidad OpenTelemetry integrada.

## Notas sobre orquestación multiagente (de la documentación relacionada)

- Los sistemas multiagente a menudo empiezan como un router que reenvía a un especialista, y se rompen la primera vez que un agente necesita una pregunta de seguimiento, más contexto de un par, o se da cuenta a mitad de turno de que la petición pertenece a otro. La orquestación de _handoff_ está hecha exactamente para eso: se declaran los agentes y las aristas dirigidas entre ellos, y el framework inyecta las herramientas de handoff que cada agente usa para transferir el control. La topología y los guardarraíles se quedan con el desarrollador; las decisiones de enrutado con los agentes.
- MAF 1.0 estandariza cómo los agentes hablan entre sí (A2A), descubren herramientas (MCP) y procesan información (middleware).

## Fuente original

- Microsoft Agent Framework Blog — Shawn Henry, _Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more_ (3 jun 2026): https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce
- Microsoft Community Hub — _The Future of Agentic AI: Inside Microsoft Agent Framework 1.0_: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/the-future-of-agentic-ai-inside-microsoft-agent-framework-1-0/4510698

## Nota de captura

Captura por extracto verbatim del cuerpo principal de la entrada, con navegación y pie corporativo eliminados. El texto completo limpio está en la caché de `web_extract` (`/home/vilber/.hermes/cache/web/devblogs.microsoft.com-5c877ec454.md`).
