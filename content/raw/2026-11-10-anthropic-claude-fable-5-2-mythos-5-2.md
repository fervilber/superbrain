---
title: "Captura: Claude Fable 5.2 y Claude Mythos 5.2 — Anthropic"
source: "https://www.anthropic.com/claude-fable-and-mythos-5-2"
date: 2026-11-09
captured: 2026-11-10T20:12:00+01:00
---

# Introducing Claude Fable 5.2 and Claude Mythos 5.2

Anthropic · 9 de noviembre de 2026

## Anuncio (texto verbatim)

> We've upgraded Claude Fable and Claude Mythos—models that are designed to tackle the most daunting technical challenges.
>
> Claude Fable 5.2 and Claude Mythos 5.2 show improvements in areas like coding, reasoning, and vision. During prerelease testing they've helped our engineers complete otherwise-infeasible software migrations, designed three working electronic devices from scratch, solved two open problems in the physics of black holes, made substantial progress on robotics evaluations, and formalized the proof of Fermat's Last Theorem in 30 hours—among many other applications we'll discuss below.
>
> Claude Fable and Claude Mythos are the same underlying model. Fable has strong cybersecurity and biology safeguards to guard against misuse, which allows us to make it available to all users. Organizations pursuing beneficial applications in cybersecurity or biomedical research can apply for access to Mythos through our recently expanded Life Sciences and Cyber Verification Programs.
>
> Testers have found that Fable 5.2 and Mythos 5.2 communicate more clearly than past Fable and Mythos models. They generate outputs up to 30% faster than Claude Fable 5.1 and Claude Mythos 5.1, and they're available at a lower price: $8 per million input tokens and $40 per million output tokens.
>
> Fable 5.2 and Mythos 5.2 also come with an optional fast mode, which speeds up token generation by up to 2.5 times. Fast mode is available for $16 per million input tokens and $80 per million output tokens.
>
> **Safety and alignment.** To help ensure safety and alignment keep step with growing model capabilities, we ran extensive prerelease safety testing on the model that underlies Fable 5.2 and Mythos 5.2. This included developing novel evaluations that give deeper insight into specific concerning behaviors like sandbox escapes. We believe high-stakes risks from misalignment remain low, and the model performed as well as, or better than, our recent models on most alignment measures. Fable 5.2's cyber and biology safeguards are as robust as those of Fable 5.1 but produce fewer unnecessary blocks, and we have implemented our strongest-ever protections against distillation attacks.
>
> **When to use Claude Fable 5.2 and Mythos 5.2.** Fable and Mythos are best for the most ambitious, open-ended technical work. For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5, our strongest daily driver, and then switch to a different model as required [...]—upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5. Fable 5.2 can also play the role of Advisor (where Haiku, Sonnet, or Opus models consult it to help solve harder problems) or Orchestrator (where it [...]).

## Ficha técnica (platform.claude.com/docs/en/models/fable-5-2/overview)

- Model ID: `claude-fable-5-2` · Mythos: `claude-mythos-5-2`
- Ventana de contexto: **1.000.000 de tokens** (por defecto y máximo) · Salida máxima: **128K tokens**
- Precio: **$8 / MTok entrada · $40 / MTok salida** (Fable 5.1: $10 / $50)
- Thinking adaptativo siempre activo; se controla con el parámetro `effort`
- Tokenizer: el introducido con Claude Opus 4.7
- Disponible en la Claude API, Claude Platform, Google Cloud, Microsoft Foundry, Amazon Bedrock (US Geo CRIS y Global CRIS)
- Mythos 5.2: mismas capacidades y precio, solo para organizaciones verificadas (Cyber Verification Program, Life Sciences)

### Cambios que rompen código (What's new in Claude Fable 5.2)

> Four changes from Claude Fable 5.1 can break your code:
>
> - The prefix check applies to every account.
> - Only Claude Fable 5.2 and Claude Mythos 5.2 read Claude Fable 5.2 thinking blocks.
> - The earlier `computer_20251124` computer use tool returns an error on every platform except Amazon Bedrock.
> - With the advisor tool, a Claude Fable 5.2 executor needs a Claude Fable 5.2 or Claude Mythos 5.2 advisor.
>
> [...] On Claude Fable 5.2 and Claude Mythos 5.2, a request that sends back an invalid thinking block and leaves `prefix_mismatch_behavior` unset gets a 400 error, whatever the account's age [...] When the check fails, the request returns a 400 error whose message says `The block is bound to a different conversation`. To drop the affected blocks and continue instead, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`.

## Benchmarks y contexto (the-decoder.com, Matthias Bastian, 9 nov 2026)

> - Fable 5.2 ranks first with 65 points on the Artificial Analysis Intelligence Index v5, five points ahead of Gemini 4 Carbon and 15 ahead of its predecessor, Fable 5.1. Peak quality averages $26.50 per task, about 2.6 times as much as Opus 5.5.
> - At lower compute tiers, Fable 5.2 still outperforms every other model at every tier with 62 points while consuming far fewer tokens.
>
> Claude Fable 5.2 and Mythos 5.2 reclaim the AI performance lead shortly before the company's IPO [...] Anthropic positions the new models for the most demanding technical work and continues to recommend Claude Opus 5.5 for everyday use.
>
> Fable 5.2 scores best in five of nine individual tests according to Artificial Analysis, including 80 percent on HLE-Diamond and 73 percent on Terminal-Bench-Science. In agentic knowledge work and terminal-based coding, Fable 5.2 falls behind some competitors.

Tabla citada por the-decoder (Artificial Analysis):

| Prueba                                                 | Fable 5.2                 | comparativas                                   |
| ------------------------------------------------------ | ------------------------- | ---------------------------------------------- |
| Agentic coding FrontierCode 2.0                        | 49,1% (Xhigh effort)      | 32,4% (Xhigh) · 45,5% · 42,8% · 41,1% (Medium) |
| Agentic coding FrontierSWE v2                          | 69,9%                     | 56,3% · 62,3% · 65,5% · 61,2%                  |
| Business Workflows AutomationBench                     | 51,4%                     | 31,4% · 42,5% · 41,4% · 53,9%                  |
| Agentic scientific research Terminal-Bench Science 0.1 | 74,6% (Mythos 5.2: 75,3%) | 52,6% · 58,7% · 68,1% · 64,8%                  |

## Hilos de X de @claudeai (9 nov 2026)

> Fable 5.2 and Mythos 5.2 are a step above Opus 5.5 in almost all the capabilities we evaluated. Testers have found that they communicate more clearly than past Fable and Mythos models. They generate outputs up to 30% faster than Fable 5.1 and Mythos 5.1.
>
> In early testing on FrontierCode 2.0, Fable 5.2 at High effort scored about level with Opus 5.5 at Max effort, for roughly half the cost per task. At Xhigh effort, it scored the highest of any released model tested. Medium is the default in Claude apps and Claude Code.
>
> Gene therapies can be delivered in a protein shell called a capsid. Mythos 5.2 found a new way to predict a whole capsid's structure. In our tests, it accurately modeled 28 of the 34 capsids it attempted.
>
> A team of 1,000 Fable 5.2 agents fully formalized Fermat's Last Theorem in 30 hours, translating the proof into a language a computer can check step by step. With the same setup, Opus 5.5 completed only 26% in 18 hours, and barely made any more progress after 30 hours.
>
> Claude Fable 5.2 is available today on all paid plans, on the Claude Platform, and on all major cloud platforms. It's $8 per million input tokens and $40 per million output tokens, down from $10 and $50.
>
> Fable 5.2 and Mythos 5.2 performed as well as, or better than, our recent models on most alignment measures. The model was also tested before release by external evaluators, including the @AISecurityInst, @FrontierDesign2, and @METR_Evals.

## Bloomberg (9 nov 2026)

> Anthropic said Fable 5.2, set to be released Monday, can tackle more difficult software engineering work, take on more hardware-related tasks like controlling robots and handle long-running projects. It's also designed to coordinate over 1,000 AI agents at a time. Mythos 5.2, the same model but with fewer safeguards for cybersecurity and life sciences work, is being rolled out to select organizations through a previously announced verification program.

## System Card (assets.claude.com, 9 nov 2026)

> Claude Fable 5.2 and Claude Mythos 5.2 are two configurations of a new large language model from Anthropic [...] Claude Fable 5.2 is available for general use and has additional safeguards that prevent it from performing certain tasks in high-risk, dual-use domains, such as biology and cybersecurity. Claude Mythos 5.2 has more permissive safeguards in these domains. Direct access to Claude Mythos 5.2 is limited to vetted individuals and organizations through our trusted access programs.
>
> [...] Before releasing Claude Mythos 5.2, we ran largely the same agentic safety evaluation suite that we used for Claude Fable 5.1 and Claude Mythos 5.1. These evaluations cover the malicious use of coding and computer use agents, autonomous execution of influence operations, and robustness to prompt injection.
>
> The first focuses on graphical interaction with a simple Linux desktop system. The second focuses on complex agentic harnesses (including the Claude Code harness). Agentic sessions can optionally include copies of Anthropic's internal codebases, and can be pre-seeded with actual sessions from internal usage.

## AWS (aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-2-on-aws/)

> In Anthropic's alignment testing, Mythos 5.2 hallucinates less, completes tasks more reliably, surfaces important information more consistently, and self-reports issues more honestly than Opus 5.5, Sonnet 5.5, and Mythos 5.1 [...] If a cyber security query is declined, you can retry it on Opus 4.8, and if a biology query is declined, you can retry it on Opus 5.
>
> Where Fable 5.2 fits: 1. Agentic coding across large, multi-repository codebases. 2. Long-running agents for coordinating many subagents on multi-day work.
>
> It is open source at anthropics/skills on GitHub, so any coding agent can integrate it.
