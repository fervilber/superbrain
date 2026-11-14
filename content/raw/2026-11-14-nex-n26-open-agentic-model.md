---
title: "Nex-AGI publica Nex-N2.6, un modelo agéntico multimodal de 321B sobre GLM-5.3-Flash"
source: "https://aiweekly.co/alerts/nex-agi-releases-nex-n26-321b-agentic-model-on-glm-53-flash"
date: 2026-11-14
captured: 2026-11-14
---

# Nex-AGI — Nex-N2.6, modelo agéntico de 321B bajo Apache 2.0 (14 de noviembre de 2026)

Captura del análisis de AI Weekly (Alexis Dufresne, publicado el 14 de noviembre de 2026 a las 06:12 UTC, actualizado a las 06:45 UTC).

## TL;DR del medio

> - Nex-AGI has published Nex-N2.6, a roughly 321B-parameter multimodal agentic model built on GLM-5.3-Flash under an Apache 2.0 license.
> - The model card reports 83.0 on OSWorld versus 78.0 for the base GLM-5.3-Flash, and 84.1 on Terminal-Bench 2.1.
> - Nex-AGI says reasoning repetition dropped from 16.0% to 1.6% versus Nex-N2.5-Pro on an internal checkpoint-replay evaluation.

## Cuerpo del artículo

> Nex-AGI has released Nex-N2.6, a roughly 321-billion-parameter multimodal agentic model built on GLM-5.3-Flash and shipped under an Apache 2.0 license.

> The model card reports a score of 83.0 on OSWorld, up from 82.2 for Nex-N2.5-Pro and 78.0 for the base GLM-5.3-Flash, alongside 84.1 on Terminal-Bench 2.1. On internal reliability tests, the card states that "Reasoning repetition fell from 16.0% to 1.6% compared with Nex-N2.5-Pro in our internal checkpoint-replay evaluation," which it describes as a 90% relative reduction.

> Weights ship as FP8-quantized tensors; the Hugging Face page records 410 downloads in the past month, and two researchers we track posted the link. On tool use, Nex-AGI reports "100% tool-list adherence among responses making tool calls in our internal evaluation," a number drawn from the company's own benchmark set, not an external audit.

> An Apache-2.0 agentic model at 321B carrying a 100% tool-adherence claim is a credible open option for agent teams, but that number is Nex-AGI's own internal measurement and needs replication before anyone wires it into production.
