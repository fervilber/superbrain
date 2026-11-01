---
title: "Mistral Large 4 publica sus pesos (1.05T MoE, 52B activos) y apunta a la defensa — captura"
source: "https://tech-insider.org/mistral-large-4-open-weights-cybersecurity-51-percent-2026"
date: 2026-10-29
captured: 2026-11-01
---

# Mistral Large 4: pesos abiertos ("Le Chonk") — 29 de octubre de 2026

> Captura del análisis de Tech Insider (29-oct-2026), complementado con Miraflow, BenchLM (b3 Agent Security) y la ficha de Vals AI. El modelo se anunció en preview el 6 de octubre de 2026 (cubierto por el Informe-2026-10-06); el 29 de octubre se publicaron los pesos.

## Qué se publicó (verbatim)

> Mistral AI released the open weights of Mistral Large 4 on October 29, 2026, and pointed the model straight at security teams. The model, nicknamed "Le Chonk," carries 1.05 trillion total parameters with 52 billion active at a time. Mistral reports a 51% score on the Artificial Analysis Cyber Index. A public preview ran for 23 days before the full release, which began on October 6.

> Mistral is letting organisations download Large 4 and run it on their own machines, and the company calls it "the best open agentic coding model in the world." That is a vendor claim, not an independent ranking. Mistral also says the model offers "frontier AI cyber defence capabilities they can fully own and control."

## Especificaciones (tabla verbatim)

| Spec                  | Mistral Large 4 (per Mistral AI)                                   |
| --------------------- | ------------------------------------------------------------------ |
| Nickname              | "Le Chonk"                                                         |
| Architecture          | Mixture-of-Experts, natively multimodal                            |
| Total parameters      | 1.05 trillion                                                      |
| Active parameters     | 52 billion                                                         |
| Vision encoder        | 1.6 billion parameters                                             |
| Context window        | 1 million tokens                                                   |
| Public preview        | October 6, 2026                                                    |
| Open weights released | October 29, 2026                                                   |
| Cyber Index score     | 51% (Artificial Analysis Cyber Index)                              |
| API price             | $1.36 input, $4.18 output, $0.14 cached input (per million tokens) |

## Lectura de la cifra del 51% (verbatim)

> If you read the index as a pass rate on realistic security tasks, a 51% score means the model solves roughly half and fails roughly half. That is a useful tool for triage and a poor candidate for unsupervised action. A model that gets one patch in two wrong will still ship bad fixes unless a human or an automated test suite catches them. The score is strong for an open-weight model and modest as an autonomy guarantee, and both statements hold at once.

> Run Large 4 against a sample of your own closed bugs, where you already know the correct patch, before you trust any aggregate figure.

## Socio de diseño y variante ofensiva (verbatim)

> Mistral named one enterprise design partner for the security push, Orange Cyberdefense. […] Mistral says it is evaluating a specialized variant for penetration testing, vulnerability assessment, and red-teaming.

> Reports on the rollout describe a gated approach for the specialized variant, aimed at vetted and authorised environments.

> Pierre Stock acknowledged that once a model is out, it is impossible to contain access.

## Coste y autoalojamiento (verbatim)

> Caching cuts the large sweep from $355.60 to $160.40, a drop of about 55%. Output tokens dominate the remainder, since each million costs $4.18 against $0.14 for cached input.

| Weight precision | Approx. weight memory for 1.05T parameters |
| ---------------- | ------------------------------------------ |
| 16-bit           | about 2.1 TB                               |
| 8-bit            | about 1.05 TB                              |
| 4-bit            | about 0.53 TB                              |

> Open weights do not mean cheap to run. A Mixture-of-Experts model activates 52 billion parameters per step, which keeps compute per token closer to a mid-sized dense model. Memory is a different story. Every expert must be resident, so the weights of all 1.05 trillion parameters have to fit somewhere fast. […] A 1 million token context window adds a large key-value cache on top.

## Seguridad del modelo (Miraflow + BenchLM, secundario)

- Miraflow cita cifras reportadas por Mistral: **93% en Cybench**, **82% en un test de reproducir-y-parchear vulnerabilidades**, **61,7% en DeepSWE v1.1** y **93,3% de resistencia en el b3 (Lakera)**. Mistral reporta 1,691 sobre 2 en KORA, que describe como el más alto medido entre modelos de pesos abiertos.
- BenchLM (29-oct-2026) recoge el b3 Agent Security de Lakera: **Mistral Large 4 97,1%**, GLM-5.3 93,0%, Kimi K3 88,0%, Gemma 4 31B 83,0%, DeepSeek V4 Pro 59,0%. Son resultados auto-reportados por el proveedor y BenchLM los marca como _display only_ (no puntúan en su ranking global).
- Nota de contexto: la inyección indirecta de prompt (instrucción maliciosa escondida en una web, correo o salida de herramienta) está **primera en el OWASP Top 10 for LLM Applications** de 2026; una única cifra de benchmark no la cubre.
