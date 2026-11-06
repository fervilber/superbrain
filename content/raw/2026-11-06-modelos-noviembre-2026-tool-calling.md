---
title: "Modelos de noviembre de 2026: GPT-6.1 Terra, Gemini 4 Carbon, Kimi K3.1 Pro y el ranking de tool calling"
source: "https://www.clone-systems.com/blog/new-ai-models-november-2026-release-guide-and-security"
date: 2026-11-06
captured: 2026-11-06T20:08:00+01:00
---

# New AI Models (November 2026): GPT-6.1 Terra, Gemini 4 Carbon, Kimi K3.1 Pro and the Security Risks of Each

By Jorja Mandy (Clone Systems). Complementado con el leaderboard de tool calling de LLM Stats (https://llm-stats.com/leaderboards/best-ai-for-tool-calling).

The major AI models released or announced in late October and November 2026 are GPT-6.1 Terra from OpenAI (released October 26), Gemini 4 Carbon from Google (announced October 28), and Kimi K3.1 Pro from Moonshot (with full open weights promised by November 4), alongside DeepSeek V4.1 Flash 1017 (October 17) and Claude Haiku 5.5 from Anthropic (October 7, just before the window). Independent scores come from the Artificial Analysis Intelligence Index, version 5.0. The security stakes are concrete: Carbon leads the index at 59 with a 0.0% attack success rate on Gray Swan's indirect prompt injection benchmark, while Moonshot says Kimi K3.1 Pro's open weights solve 81.0% of expert vulnerability discovery and exploitation tasks before its cyber-data controls.

## The Short Answer: Which New AI Model Is Best?

- **Highest independent score:** Gemini 4 Carbon, 59 on the Artificial Analysis Intelligence Index (v5.0), ahead of Claude Fable 5 (57) and GPT-6.1 Terra (56).
- **Best value near the top:** GPT-6.1 Terra at $6 per 1M input tokens and $18 per 1M output tokens, with a 25% off introductory period.
- **Cheapest useful models:** Gemini 3.6 Flash Lite at $0.50 in and $2.50 out, and Claude Haiku 5.5 at $1 in and $5 out (vendor-reported).
- **Best open-weight model:** Kimi K3.1 Pro, a 3T-class model with a 1M-token context window; full weights release by November 4, 2026 (Moonshot).
- **Most capable on cybersecurity, by the labs' own numbers:** GPT-6.1 Terra (58.5% on the HackerGPT-2 cyber benchmark, vendor-reported) and Gemini 4 Carbon (88.2% on SEC-bench Pro for vulnerability finding, vendor-reported).

## New AI Models at a Glance

| Model                    | Lab       | Released                        | API price per 1M tokens (in / out)     | Independent score            |
| ------------------------ | --------- | ------------------------------- | -------------------------------------- | ---------------------------- |
| GPT-6.1 Terra            | OpenAI    | Oct 26, 2026                    | $6 / $18 (intro, 25% off until Nov 23) | 56 (Intelligence Index v5.0) |
| GPT-6 Rosalind           | OpenAI    | Oct 30, 2026 (beta)             | See vendor page                        | Not yet ranked               |
| Gemini 4 Carbon          | Google    | Oct 28, 2026                    | $2 / $10 intro; $4 / $20 after         | 59 (Intelligence Index v5.0) |
| Kimi K3.1 Pro            | Moonshot  | Late Oct 2026; weights by Nov 4 | See vendor page                        | Not yet ranked               |
| DeepSeek V4.1 Flash 1017 | DeepSeek  | Oct 17, 2026                    | See vendor page                        | 50 (Intelligence Index v5.0) |
| Claude Haiku 5.5         | Anthropic | Oct 7, 2026                     | $1 / $5 (vendor-reported)              | 45 (Intelligence Index v5.0) |

## OpenAI: GPT-6.1 Terra and GPT-6 Rosalind

**GPT-6.1 Terra.** OpenAI's new flagship in the GPT-6 family, released October 26, 2026, replacing GPT-6 Sol and GPT-6.1 Sol as the model behind ChatGPT. OpenAI's changelog describes it as "built for long-running, multi-step work," with improved reliability, lower cost, and better performance on science and agentic tasks. A larger context window (1.15M tokens, up from 500K), a 512K max output, and a new **Ultra effort level**, which OpenAI describes as a higher reasoning effort above Max that runs a multi-agent workflow to deliver the strongest results available on the hardest problems. It supports native image and web search tool calling. Vendor-reported: 58.5% on HackerGPT-2, +9 points over GPT-6 Sol; 1.4x better accuracy and 6.8x lower cost per task on CyberGym (2.0); ~3x the rate of GPT-6 Sol and 15% cheaper than GPT-6.1 Sol at the same task outcomes. Independent ranking: 56 on the Artificial Analysis Intelligence Index (v5.0), third overall, ahead of GPT-6.1 Astra and Claude Opus 5.5 (both at 54).

**Why it matters for security.** The 9-point jump on a cyber benchmark and the 6.8x cost reduction on CyberGym mean the capability to find and exploit vulnerabilities is getting cheaper per task, not just more accurate. Terra is also the first GPT-6 generation where OpenAI explicitly positions agentic, long-running work as the headline use.

**GPT-6 Rosalind (research preview).** Announced October 30, 2026: a research preview model family for life sciences reasoning, built on GPT-6 architecture, with a new `rosalind` endpoint. Security teams should note that "GPT-6" in a procurement document is no longer one model; Terra, Astra, Luna, Terra Mini and Rosalind all ship under the same family name with different behavior profiles.

## Google: Gemini 4 Carbon

Announced October 28, 2026, two weeks after Gemini 4 Argon. Google calls it "our strongest model with state-of-the-art cybersecurity and long horizon capabilities." Carbon is built for sustained agentic workflows, with Google's teams reporting it running "for days to persist through dead ends" on multi-step engineering tasks. It builds on Argon's multi-layered safety stack and improves on alignment, honesty and prompt injection resistance. Vendor-reported: #1 on v5.0 of the Artificial Analysis Intelligence Index at 59; on cybersecurity benchmarks evaluated without guardrails, 88.2% on SEC-bench Pro for finding vulnerabilities, 54.8% on ExploitGym for exploitation, and 71.0% on Collinear's CWE-bench for patching. The Chrome team reportedly saw Carbon perform more than 10x better than another lab's large frontier model when generating high quality patches. On prompt injection, where Argon recorded a 0.7% attack success rate on Gray Swan's Indirect Prompt Injection Benchmark, Carbon achieves **0.0%**. Price: $2 / $10 intro, $4 / $20 after, cached input 95% off. Access starts with a subset of cyber defenders through the Fairwind Program.

## Moonshot: Kimi K3.1 Pro

Moonshot's first model in the K3.1 series and "our most capable 3T-class open-weight model to date," with a 1-million-token context window. A companion model, Kimi K3.1 Pro Highspeed, delivers 2 to 3x the speed. It is a post-trained version of Kimi K3 with substantially larger post-training compute, optimized for large-scale joint reinforcement learning across hundreds of downstream domains; targets coding, 3D creation, financial research and agentic work. Vendor-reported: on Terminal-Bench 4.0, 65.7%, ahead of GPT-6 Astra (58.2%) and narrowly behind Claude Opus 5.5 (66.4%); Kimi Code Bench 3.0 Long-horizon 61.2% vs 55.95% for K3; BenchCAD 92.7% with tools; OfficeQA Pro v2 state-of-the-art at 64.4; claim-level hallucination rate on an internal stress test fell from 23.4% for K3 to 8.3%. **The cyber capability disclosure:** on xdev-bench-hard, an in-house benchmark of expert-curated vulnerability discovery and exploitation tasks, the unchecked checkpoint solves 90.5% of problems at pass@3, while the final K3.1 Pro, after cyber-related data removal at both mid-training and the RL stage, reaches 81.0%. Moonshot says K3.1 Pro's cyber capability "remains behind that of frontier proprietary models that have been publicly available for at least three months."

## Ranking de tool calling (LLM Stats, noviembre 2026)

As of November 2026, GPT-6 Astra leads tool calling benchmarks with a score of 36.0, followed by Claude Sonnet 5.5 (35.9) and Gemini 4 Carbon (35.4). Rankings test function selection accuracy, parameter extraction, and multi-step tool chain orchestration from natural language instructions, across 54 benchmarks including Berkeley Function Calling Leaderboard (BFCL) and real-world API integration tests, evaluating schema adherence, parameter accuracy, and error recovery.

Modelos destacados por relación calidad/precio: Claude Sonnet 5.5 ($2.00/$10.00, contexto 1.0M), Claude Opus 5.5 ($4.00/$20.00), DeepSeek-V4.1-Flash ($0.22/$0.66, pesos abiertos, licencia MIT) y DeepSeek-V4.1-Flash-1017 ($0.30/$1.20).

Puntos clave del ranking:

- La precisión de tool calling se degrada con el número de herramientas: los modelos frontera llegan al 95-96% con una sola herramienta, bajan al 85-91% con 5 herramientas y al 65-78% con 20+.
- Los errores de parámetros (herramienta correcta, argumentos incorrectos) suponen el 60-75% de los fallos de tool calling a escala, más frecuentes que la selección errónea de herramienta.
- Los modelos de pesos abiertos (Llama 4, Qwen 3) van 5-12 puntos por detrás de las APIs frontera cerradas con una herramienta, y 10-22 puntos con 20 herramientas.
- El tool calling multi-paso (cadena de 3+ invocaciones) muestra error compuesto: una precisión del 90% por llamada da 73% a tres llamadas y 59% a cinco.
