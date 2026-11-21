---
title: "Leaderboards agénticos de noviembre de 2026: BenchLM, LiveBench 2.0 y el nacimiento del Hermes Index"
source: "https://benchlm.ai/agentic"
date: 2026-11-21
captured: 2026-11-21
---

# Leaderboards agénticos de noviembre de 2026

Captura compuesta de `benchlm.ai/agentic` (datos refrescados el 13 de noviembre de 2026),
`livebench.ai` (release 2026-11-06), `whatllm.org/best-agentic-models`, `scale.com/labs`
(ToolComp-Enterprise) y `mindstudio.ai` (Nanbeige4.3-33B).

## 1. BenchLM: BenchAlign agentic v5.8

> As of November 2026, the top agentic model on the BenchLM leaderboard is **Claude Fable 5.2** with a
> BenchAlign agentic score of **91**.

Cobertura: 1.033 modelos rastreados, 831 benchmarks, **52 benchmarks de la categoría agéntica**
soportados, 135 modelos rankeados. 73 «Supported» (respaldados por evidencia independiente suficiente)
frente a 62 «Estimated» (rankeados con incertidumbre mayor).

> Decision lens: the score sets the order, except in close calls: an **Estimated** model with fewer than
> two independent sources ranks below any model scoring within 2 points of it.

Top-10 de la tabla publicada (score agéntico BenchAlign, contexto, precio por millón de tokens de
entrada/salida):

1. Claude Fable 5.2 (Anthropic, Estimated) — 91,0 · 1M · $8/$40
2. Claude Opus 5.5 (Anthropic, Supported) — 86,64 · 1M · $4/$20
3. Gemini 4 Carbon (Google, Estimated) — 89,19 · 1M · $2/$10
4. Claude Fable 5.1 (Anthropic, Supported) — 79,22 · 1M · $10/$50
5. Claude Opus 5 (Anthropic, Supported) — 76,07 · $5/$25
6. Gemini 4 Argon (Google, Supported) — 79,06 · 1M · $2/$10
7. GPT-6 Astra (OpenAI, Supported) — 85,68 · 1,05M · $10/$50
8. GPT-6.1 Terra (OpenAI, Estimated) — 79,65 · 1,05M · $1/$5
9. Claude Sonnet 5.5 (Anthropic, Supported) — 83,07 · 1M · $2/$10
10. Claude Fable 5 (Anthropic, Supported) — 76,29 · 1M+ · $10/$50

Selecciones destacadas: mejor peso abierto = **Kimi K3.1 Pro** de Moonshot AI (70,37 global, «[Self-host]»),
mejor relación calidad/precio agéntica = **Gemini 4 Carbon**, más rápido medido = **Gemini 3.5 Flash-Lite**
(461 tokens/s), mayor contexto útil = **GPT-6 Astra** (1,05M).

## 2. Benchmarks agénticos rastreados (selección con su descripción)

- **Terminal-Bench 2.0** — tareas de terminal; **Terminal-Bench-Science 0.1** (ejecutado por Google con
  timeout del verificador multiplicado por seis para resolver los timeouts de verificación).
- **BrowseComp / BrowseComp-VL / DeepSearchQA / WebVoyager** — investigación y navegación web.
- **OSWorld-Verified / OSWorld 2.0 / AndroidWorld** — uso de ordenador.
- **CyberGym / CWE-Bench / CWE-bench v1 / Cybench / ExploitGym** — ciberseguridad; CWE-bench v1 es
  parcheo defensivo de vulnerabilidades sobre 120 tareas reservadas que cubren 73 tipos de debilidad.
- **JobBench / GDPval-AA / Finance Agent v2 / ApprenticeBench / YC-bench / Tau3-Bench /**
  **EnterpriseOps-Gym / Automation Bench / Claw-Eval / Toolathlon(-Verified)** — trabajo de oficina y
  negocio simulado.
- **MCP Atlas** — el benchmark específico de MCP.
- **MM-ClawBench** — derivado de OpenClaw: entrega de documentos de oficina, investigación,
  planificación y mantenimiento de código.
- **MazeBench** — ¿puede un agente de código explorar un mundo de puzles 3D de 256 salas y recoger 100
  gemas escondidas, con empuje de cajas, rotación de cámara y planificación de horizonte largo?
- **ApprenticeBench** — ¿puede un agente de uso de ordenador aprender un trabajo real de cuentas a
  pagar sobre la marcha, procesando 100 facturas de proveedor en un ERP con solo el manual, registros
  históricos y retroalimentación de un mentor?
- **ReviewBench** — ¿identifica un agente revisor problemas útiles en PRs reales sin falsos positivos?
- **AI4AI-Bench / MLE-Bench Lite** — ¿puede un agente de código mejorar el algoritmo de entrenamiento
  dentro de un código de investigación y sobrevivir a una ejecución de entrenamiento sellada?

## 3. El Hermes Index y el Hermes Bench (aparición en el catálogo de BenchLM)

> **Hermes Index** — Mean pass@1 score across four agentic suites (**Hermes Bench, TerminalBench 4,
> TerminalBench Science and SkillsBench**), run inside the **Hermes Agent harness** and reported with
> mean cost per task.
>
> **Hermes Bench** — 150 tasks across 25 categories covering Hermes skills, research, diagrams and
> art, memory, tool use and safety. Each agent starts in a workspace with real files and the grader
> checks what it leaves behind.

Esto es significativo por dos razones: (1) un benchmark mide ahora el **harness**, no solo el modelo,
y publica el **coste medio por tarea** junto al pass@1; (2) el grader comprueba **el estado del
workspace que el agente deja detrás**, no solo la respuesta final — el mismo giro hacia la evidencia
que aparece en los papers de memoria de esta misma ventana.

## 4. LiveBench 2.0 (Abacus AI, release 2026-11-06)

> We give models real work (decks, research reports, bug fixes, apps that run for hours) and grade what
> they hand back.

Categorías: Agentic, Design, Coding, Browser Use, Data Analysis, Research, Reasoning, con **coste por
tarea exitosa**. Cabecera de la tabla: Claude Fable 5.2 (xhigh) 84,9 global / 82,9 agéntico / $9.850;
GPT-6.2 Astra 84,9 / 70,8 / **$1,941**; GPT-6 Astra 84,5 / 75,6 / $5.318. La lectura práctica: dos
modelos empatados en calidad global con una diferencia de **5× en coste por tarea exitosa**.

## 5. Otras referencias de la ventana

- **whatllm.org** ordena por índice agéntico y por coste por tarea, con Terminal-Bench, τ-Bench y
  GDPval-AA: Claude Fable 5.1 ($7,63/tarea), Claude Opus 5 ($5,86), Qwen3.8 Max ($5,41). Destaca
  Claude Fable 5 con **99,0 % en τ²-Bench Telecom** como el candidato de tool-use con esa cifra exacta.
- **Scale Labs** mantiene un leaderboard de uso de herramientas empresarial con **ToolComp**
  (485 prompts, 11 herramientas en la variante Enterprise, cadenas de respuesta doradas y etiquetas de
  supervisión de proceso).
- **Nanbeige4.3-33B** (Apache 2.0, contexto de 512K): el artículo de MindStudio argumenta que «the
  differentiation among these ~30B models shows up mainly in how well they execute long, tool-using
  workflows, not in raw math or knowledge-style reasoning» — en razonamiento los cuatro modelos quedan
  en una banda estrecha (AIME 2026 de 89,2 a 95,2).
