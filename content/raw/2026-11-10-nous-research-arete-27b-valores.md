---
title: "Captura: Nous Research publica Arete-27B, Qwen3.8-27B reentrenado con valores occidentales"
source: "https://nousresearch.com/arete"
date: 2026-11-07
captured: 2026-11-10T20:26:00+01:00
---

# Introducing Arete-27B: Qwen3.8-27B Post-Trained To Reinforce Western Values

Nous Research · 7 de noviembre de 2026 · licencia Apache 2.0

## Anuncio (X de @NousResearch)

> Introducing Arete-27B: Qwen3.8-27B, post-trained to reinforce Western values. Chinese open models are currently the strongest available, but they ship with state-aligned behavior in the weights. We built an 803-prompt eval across seven value categories, including freedom of expression, democracy, and privacy, and measured how often a model adopts China's party line. After fine-tuning on roughly 53 million tokens, Arete-27B's propaganda rate fell from 22% to 1%, in line with the Western models we tested. Its Hermes Bench score shows no significant performance tradeoffs. **The values in an open model are one fine-tune away.** Our eval, weights, [...]

## Página del proyecto (nousresearch.com/arete)

> On our evaluation, Arete-27B raised its fact score from 2.32 to 2.98 out of 5 and cut answers containing propaganda from 22% to 1%, in line with the Western models we tested. The number of answers scoring 0 fell from 359 to 216 of 803. Results were stable across runs (±0.03), and the improvement held in all seven categories. The largest change was in freedom of expression, where the fact score rose from 0.89 to 2.44 and the propaganda rate fell from 60% to 1%.

Tabla de la evaluación (803 prompts, 5 ejecuciones cada uno, tope de 32k tokens):

| Modelo                             | Fact mean (0–5) | Cualquier propaganda |
| ---------------------------------- | --------------- | -------------------- |
| Inkling (teacher)                  | 3,96 ± 0,07     | 0,3%                 |
| Mistral Large 4                    | 3,65 ± 0,04     | 0,3%                 |
| Muse Glimmer 30B                   | 3,02 ± 0,05     | 0,5%                 |
| Gemma 4 31B                        | 2,58 ± 0,05     | 0,5%                 |
| Nemotron 3 Ultra                   | 3,22 ± 0,02     | 0,6%                 |
| **Arete-27B (thinking on)**        | **3,07 ± 0,03** | **0,6%**             |
| **Arete-27B (thinking off)**       | **2,98 ± 0,03** | **0,9%**             |
| GLM 5.3 (thinking off)             | 3,10 ± 0,06     | 15%                  |
| DeepSeek V4.1 Flash (thinking off) | 2,39 ± 0,05     | 16%                  |
| Qwen3.8-27B (base)                 | 2,24–2,32       | 22%                  |

## Detalles de entrenamiento (MarkTechPost, 7 nov 2026)

> - Size: 27B dense parameters (all active). Trained at 64k context. Base Qwen3.8-27B supports 262,144 tokens natively.
> - Runs on: BF16 weights are 53.81 GB. A community Q4_K_M quant is 17.20 GB, sized for 24 GB consumer GPUs.
> - Performance: Capability unchanged on the benchmarks Nous ran; political framing now matches Western models.
> - Best: Propaganda rate 0.9%, down from 22% for base Qwen3.8-27B.
> - Worst: Fact score 2.98 of 5; 216 of 803 answers still score 0.
>
> Arete-27B is Qwen3.8-27B after supervised fine-tuning only. Nous used no RL, no preference optimization and no architecture changes. The license is Apache 2.0, matching the base model.
>
> Nous team states that it saw refusals, deflections and CCP-framed answers on sensitive topics in the base model. It picked Qwen3.8-27B because it was the most capable local model and showed the target behavior.

## Detalles adicionales (AI Weekly, 7 nov 2026)

> Training used about 52.8 million tokens at 64k context, 2 epochs, and 1,202 steps. 'We used supervised fine-tuning only. No RL, no preference optimization, and no architectural modification.' **The teacher was an open-source model called Inkling**, which generated 20,000 prompts across seven value categories: freedom of expression, state ideology, [...]
>
> Capability benchmarks moved little. **Hermes Bench went from 65.77% to 65.60%**, which Nous calls noise. **Terminal-Bench-2.1 climbed from 67% to 70%.**
>
> 'The users of a model deserve optionality in which values they work with,' Nous writes.

## Análisis (The Decoder, 7 nov 2026)

> State propaganda in some Chinese AI models is only "a thin layer" that fine-tuning can strip away. [...] According to Nous, the Arete-27B project shows that the political bias in Chinese open-weight models is only superficial; the model and training data have been released publicly.
>
> Table listing ten AI models with their factuality score from 0 to 5 and their share of propagandistic responses, ranging from Inkling at 0.3 percent to Qwen3.8-27B at 22 percent.
