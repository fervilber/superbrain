---
title: "DeepSeek Super-Agent: prototipo abierto de agente de codificación que no espera al prompt"
source: "https://www.digitaltrends.com/computing/deepseek-wants-to-steal-claude-code-and-codexs-lunch-with-an-ai-agent-that-does-not-wait-around"
date: 2026-11-02
captured: 2026-11-02
---

# DeepSeek wants to steal Claude Code and Codex's lunch with an AI Super Agent that does not wait around

Autor: Moinak Pal — Digital Trends (1 de noviembre de 2026). Captura verbatim de los párrafos sustantivos del artículo.

The AI coding race is moving beyond chatbots that write code when developers prompt them to. DeepSeek wants its next agent to be a little more aggressive. The Chinese AI company has released a prototype called Super-Agent, an open-source coding tool that listens in on developer group chats, identifies coding problems, and suggests solutions without waiting to be called.

The move puts DeepSeek in more direct competition with Anthropic's Claude Code and OpenAI's Codex, two prominent names in the rapidly-growing market for AI-powered software development. The bigger goal is clear: to design AI agents to be less assistants waiting for instructions, and more members of a development team who can take initiative.

## DeepSeek's coding agents are going to stop waiting for prompts

DeepSeek's Harness team has launched Super-Agent, which is designed to scan developer discussions for feedback on coding problems and recommend possible solutions. The company says its goal is to provide the maximum value with the minimum human attention.

That's a significant departure from the familiar chatbot workflow. Typically, developers describe a problem, provide some context, and then ask the AI tool to write or fix code. DeepSeek's approach attempts to bring the agent closer to the conversations where those problems originate in the first place.

The technology behind this is called the agent harness, a software scaffolding that wraps around a large language model and equips it with the tools to take on more complex tasks. DeepSeek set up its Harness team earlier this year to build agents that can provide the coding services of leading US AI firms.

But this is a prototype, not proof that DeepSeek has already surpassed established rivals. The announcement doesn't set the bar for how reliable Super-Agent is for complex development work, or how ready it is for deployment at scale.

## Claude Code and OpenAI Codex have serious competition to keep an eye on

Anthropic's Claude Code is already helping developers navigate codebases, debug issues, write code, run tests, and make pull requests. And not just code, but agent-based workflows across software development, including parallel tasks and tools for reviewing code, have been demonstrated by Codex at OpenAI.

Now DeepSeek is moving into similar territory, but Super-Agent gets an interesting angle by focusing on proactively monitoring developer conversations. Rather than simply answering a developer's question, it tries to figure out when a developer might need help.

This is important because the next phase of AI competition is increasingly about agents that can automate entire chunks of work, not just generate impressive answers. OpenAI, Anthropic and DeepSeek are all pursuing that opportunity.

DeepSeek is also getting ready for a big financial push. In its latest fundraising round ahead of a planned initial public offering, the company has raised about 100 billion yuan ($15 billion), Bloomberg reported.

More competition could eventually lead to more capable and affordable coding tools for developers. But for now, Super-Agent is an early sign of the direction the industry is going – not a reason to uninstall Claude Code or Codex just yet.

---

# DeepSeek launches Super-agent coding tool to rival Anthropic

The Straits Times / Bloomberg (1 de noviembre de 2026, 12:55 PM). Captura verbatim de los párrafos sustantivos.

DeepSeek has released a prototype of a more autonomous coding agent as it seeks to challenge Anthropic PBC's popular Claude Code.

The new open-source offering, dubbed "Super-agent" can proactively monitor group chats among developers for feedback on coding issues and suggest solutions without being summoned, the DeepSeek Harness team said in a post on WeChat on Oct 31.

The new agent aims to "take as little human attention as possible, and give as much value as possible", DeepSeek said in a user manual on GitHub.

Earlier in 2026, DeepSeek created the Harness team to focus on helping build AI agents that can take on coding services offered by leading US labs including Anthropic.

The term harness refers to the software scaffolding that wraps around a large language model which enables AI agents to manage more complex tasks. Anthropic and other developers have designed harnesses to make their software better at streamlining coding and other work.

Chinese firms are locked in a heated rivalry with US developers to build more advanced – and affordable – AI tools. While OpenAI's ChatGPT chatbot helped kick off the global AI race, many companies have since focused more on the lucrative emerging market for AI agents that can help automate work for developers and business professionals.

To bulk up its war chest and compete with Anthropic and OpenAI, DeepSeek has raised about 100 billion yuan (S$19.2 billion) in its latest fundraising round, one of China's largest-ever, ahead of its initial public offering. BLOOMBERG

---

# Notas de verificación (repo y cobertura secundaria)

- Repositorio: github.com/deepseek-ai/dsh-superagent-prototype — publicado el 2026-10-31 como un único commit aplastado (216 ficheros, +37.068 líneas), v0.1.0, licencia MIT. Aproximadamente 6.600 estrellas y 653 forks en día y medio (6.635 estrellas el 1 de noviembre de 2026 a las 18:08 UTC).
- El propio README lo describe como prototipo de investigación, no producto oficial, con "mucha de la ingeniería hecha por agentes de codificación".
- Arquitectura descrita: un "router" recoge información de chat y correo y asigna tareas a "workers" (3 por defecto, rango 1–16, más 1 slot reservado a un mensaje humano) que cubren revisión de código y desarrollo de funcionalidades; el agente vigila un repositorio de GitHub y responde a peticiones permitidas con pull requests.
- Ensayo de diseño de DeepSeek: una persona puede seguir solo "3 a 5 sesiones activas a la vez"; algunas partes del diseño "no están implementadas en este prototipo".
- No se han publicado modelo, precios ni benchmarks; la tarifa de lista más barata de DeepSeek citada es de ~$0,15 por 1M tokens de entrada con fallo de caché en horario valle (precio de lista, no coste medido).
- Cobertura: Bloomberg (1 nov), South China Morning Post, The Edge Malaysia, Digital Today (anuncio por WeChat), Startup Fortune.
