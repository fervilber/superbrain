---
title: "Captura: Meta Muse Ember, el modelo ligero para ejecución de agentes"
source: "https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/"
date: 2026-11-09
captured: 2026-11-09T20:05:00+01:00
---

# Meta releases Muse Ember, a new lightweight model for agent execution

Russell Brandom · 10:00 AM PST · November 9, 2026 · TechCrunch

Meta Superintelligence Lab released a new AI model on Monday called Muse Ember, the lab's lightest and most cost-efficient AI model yet. In its release, Meta said Ember was "designed for complex reasoning execution and the work agents repeat all day: tool calls, coding subtasks, routing, extraction, and long document parsing."

Meta particularly emphasized Ember's cost-per-task, using Artificial Analysis's composite benchmark score to show Ember as cheaper and smarter than competitors like Anthropic's Haiku and OpenAI's Luna.

At 10 cents per million input tokens, Ember is significantly cheaper than frontier competitors like Haiku and Luna. Not only that, it's cost-competitive with open-source competitors like DeepSeek V4.1 Flash and GLM 5.3 Flash.

Given the emphasis on low cost and accuracy at scale, Ember is designed to pair with a larger model like Meta's Muse Wonder in an agentic harness. In the case of a customer-support agent, for instance, you might see a heavier model establishing rules for how to handle a particular issue, then sending a lighter-weight model to apply the rules across tens of thousands of cases. As Meta puts it in the announcement, "Muse Wonder plans, Muse Ember handles the volume."

With volume-heavy use cases in mind, Meta also trained Ember to work well across different types of media, including text, images, and audio. The result makes the model surprisingly flexible in what kind of inputs it can handle. As Meta puts it in the announcement, "agents can read screenshots, charts, and scanned documents, or work from voice memos, meeting recordings, and video without a separate model."

Ember is the fourth model released under Meta's Muse brand, following the mid-weight Spark (released in April), Spark's open-source twin Glimmer (released in August), and the Wonder frontier model (released in October). The flagship consumer AI product, the Muse Agent, was released in September to unexpected success, with new features like Spaces and video chat rolling out earlier this month.

## Notas de estado (de búsquedas dirigidas, no del texto original)

- La marca Muse de Meta Superintelligence Lab agrupa cuatro modelos: Spark (intermedio, abril), Glimmer (gemelo open-source de Spark, agosto), Wonder (frontera, octubre) y ahora Ember (ligero/volumen, noviembre). El producto de consumo es Muse Agent (septiembre).
- La cifra de 10 céntimos por millón de tokens de entrada se compara contra Anthropic Haiku, OpenAI Luna, DeepSeek V4.1 Flash y GLM 5.3 Flash.
- El patrón recomendado es un harness agéntico de dos niveles: un modelo frontera que "planifica" (establece reglas) y Ember que "ejecuta el volumen" (aplica las reglas a decenas de miles de casos). Es la misma separación planificador/ejecutor que empujan Mistral, LangChain y OpenAI en la misma semana.
