---
title: "AgentRun: plataforma abierta para agentes auto-mejorables que reutilizan lo aprendido para gastar menos tokens"
source: "https://operatorsguidetoai.substack.com/p/run-smarter-agents-use-fewer-tokens"
date: 2026-11-13
captured: 2026-11-15
---

# Run smarter agents. Use fewer tokens. Introducing AgentRun, an open-source platform for self-improving agents

Fuente: The Operator's Guide to AI (substack), AJ Asver y Miguel Rios Berrios, 13 de noviembre de 2026.

## Contenido (verbatim, selección)

> Earlier this year, I added up what we were spending on AI across Anthropic, Open AI and the coding tools our team used. It came to nearly $80,000 for the month.

> Some of that went into building Grep AI. The rest went into running it. We were spending more on tokens than we were bringing in as revenue. At that rate, the annual bill would approach $1 million.

> Miguel, my co-founder, began experimenting with a smaller harness for lower-effort research. Within a week, he had a prototype that cost roughly one-fifth as much to run. It gave cheaper models narrower jobs, kept their progress in a workspace and routed different stages to different models.

> AgentRun brings the pieces we've been building at Grep into an open-source platform: learning between runs, reusable workflows, computers for doing the work, recovery when something breaks, and a console for running it all.

> We first released parts of this as extensions to pi, our default agent harness. [...] An agent that already works shouldn't need rewriting to get a better operating environment. AgentRun supports pi, Claude Code, Codex and OpenCode. The harness runs the model's loop and calls its tools. AgentRun supplies the learning, execution history and controls around it.

## Learning from previous runs (verbatim)

> With learning enabled in AgentRun, an agent reviews a completed run and proposes what to keep: a useful fact, a correction, a skill describing the procedure, or a workflow. AgentRun checks and grades those proposals before saving them. The Learning tab shows what was accepted and which run produced it; you can retire something that turns out to be wrong.

> This changes the instructions and procedures available to the agent, rather than retraining the model. Reflection and grading also cost tokens. The payoff comes when later runs reuse something useful, and it depends on the job.

## Workflows (verbatim)

> A workflow can fetch a document, extract information, ask Jev, a decision model, a defined question, and choose what happens next. It can classify, score, branch, run another workflow or call an agent for a step that needs investigation. Parallel's web-grounded Decisions API can also handle questions that require checking the web.

## Durabilidad (verbatim)

> AgentRun persists the conversation, files and execution state of each run so it can recover unfinished work when the server restarts with its data intact. Workflows recover too. We built on pi-durable and Vercel's durable-harness so teams can use the same recovery layer across harnesses.

> AgentRun is an open-source alpha, available on GitHub. On a Mac or Linux machine with a supported Node version, start with: `npx @parcha/agentrun`

## Lectura técnica

- **Premisa económica**: gastar ~80.000 $/mes en tokens (≈1 M$/año) para un producto que aún no cubría ese coste. El prototipo que redujo el gasto a ~1/5 daba **trabajos más estrechos a modelos más baratos**, guardaba el progreso en un workspace y **enrutaba distintas etapas a distintos modelos**.
- **Independencia del harness**: AgentRun **no exige cambiar de harness** —soporta pi, Claude Code, Codex y OpenCode—; el harness corre el bucle del modelo y llama a sus tools, AgentRun aporta **aprendizaje, historial de ejecución y controles** alrededor.
- **Aprendizaje como artefacto revisable**: tras cada run, el agente **propone** qué conservar (un hecho útil, una corrección, una **skill** que describe el procedimiento, o un **workflow**); AgentRun **verifica y califica** esas propuestas antes de guardarlas; el panel de Learning muestra qué se aceptó y qué run lo produjo, y permite retirar lo que resulte erróneo. No es reentrenar el modelo: es cambiar las instrucciones y procedimientos disponibles.
- **Coste del aprendizaje**: la reflexión y la calificación también cuestan tokens; el beneficio llega cuando runs posteriores reutilizan algo útil, y depende del trabajo.
- **Durabilidad**: persiste conversación, ficheros y estado de ejecución para reanudar trabajo inacabado tras un reinicio; construido sobre pi-durable y durable-harness de Vercel.
- Licencia: **Apache-2.0**; estado: **alpha**.
