---
title: "Bielik 11B v3.1, DFlash y la familia Bielik-One: 56 idiomas y capacidad agéntica en un modelo abierto europeo"
source: "https://www.bielik.ai/en/blog/launching-bielik-11b-v31-dflash-and-the-bielik-one-family"
date: 2026-11-14
captured: 2026-11-14
---

# Bielik 11B v3.1, DFlash y Bielik-One (10-12 de noviembre de 2026)

Captura del blog oficial de Bielik.ai (SpeakLeash Foundation / ACK Cyfronet AGH, 10 de noviembre de 2026).

## Tres lanzamientos en tres días

> This week belongs to Bielik. Together with ACK Cyfronet AGH, we are releasing Bielik 11B v3.1: it speaks 56 languages (including languages from outside Europe), can call external tools and handles tasks made up of many steps. It comes with two new companion models: Bielik-One, the first decision models in the Bielik family, and Bielik DFlash, an accelerator. Three launches in three days.

| Fecha                   | Lanzamiento                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| 10 de noviembre de 2026 | Bielik 11B v3.1 (nuevo modelo insignia)                            |
| 11 de noviembre de 2026 | Bielik 11B v3.1 DFlash (modelo borrador que acelera la generación) |
| 12 de noviembre de 2026 | Bielik-One (familia de cuatro modelos de decisión)                 |

> The models will be available on Hugging Face: https://huggingface.co/speakleash

## 56 idiomas manteniendo el carácter polaco

> We trained Bielik 11B v3.1 on an additional 500 billion tokens. This raised the number of supported languages from 32 in version 3.0 to 56, without the model losing its Polish identity.

> In practice, you can now talk to Bielik in every official language of the European Union. For the first time, it also supports languages from outside Europe, including Arabic and Asian languages such as Chinese, Japanese and Korean. Caucasian languages have been added too: Armenian, Azerbaijani and Georgian.

> The benchmarks show it:
>
> - Belebele (reading comprehension): +8 percentage points,
> - INCLUDE (knowledge and reasoning in 44 languages, including regional knowledge): +5 percentage points.

> "We are not building Bielik just so that Poland has its own language model. We are building it because we believe Polish technology can set standards rather than merely follow them. (…) We want Bielik to become the model of first choice in Europe, and in time beyond it as well." — Sebastian Kondracki, President of the Board, SpeakLeash Foundation

## El modelo no solo responde, actúa

> The biggest new feature in version 3.1 is its agentic capabilities. Bielik now combines three mechanisms that work together:
>
> - function calling: it calls external functions and tools,
> - structured output: it returns answers in a strictly defined structure,
> - reasoning: for harder tasks, it switches to an explicit reasoning mode.

> Together, they make Bielik a good fit for agentic systems: systems that don't stop at generating an answer, but carry out multi-step tasks using the tools available to them.

> One of the benchmarks we used to test this is τ²-bench. It simulates realistic customer service scenarios, for example at airlines, in retail and in telecoms. The model has to understand the problem, use the right tools (for example, check a booking or charge a card) and reach the correct outcome.

## Bielik-One: modelos de decisión

> On 12 November, we launch the Bielik-One family: four decision models. They are not built to generate text. Instead, they analyse information and assess it against criteria you set in advance. For example, they can assign a ticket to the right category, check whether it meets the requirements, or point to the most likely of the available answers.
