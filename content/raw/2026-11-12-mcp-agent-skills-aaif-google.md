---
title: "Scaling AI agents with open standards: Kurtis Van Gent on MCP and Agent Skills joining the AAIF"
source: "https://opensource.googleblog.com/2026/11/scaling-ai-agents-open-standards-mcp-aaif.html"
date: 2026-11-11
captured: 2026-11-12
---

# Scaling AI agents with open standards: Kurtis Van Gent on MCP and Agent Skills joining the AAIF

Google Open Source Blog, 11 de noviembre de 2026. Por Kurtis Van Gent (Google Cloud) y Daryl Ducharme (Google Open Source Programs Office). Captura en bruto (entrevista).

## Extractos verbatim

> Building production AI agents requires more than a capable reasoning model. Agents need a reliable way to connect to external systems and data, and they need procedural domain knowledge so they know how to use those tools safely without exhausting their context window.

> Over the past year, open source communities have rallied around two complementary open standards to solve these challenges: the Model Context Protocol (MCP) for connecting agents to live tools, and Agent Skills for loading procedural instructions and scripts on demand. Following Anthropic's donation of the Agent Skills specification to the Linux Foundation's Agentic AI Foundation (AAIF) alongside MCP, engineers from Google, Anthropic, OpenAI, and the wider ecosystem are now co-maintaining the standard under vendor-neutral governance.

### Del problema N-por-M de bases de datos a la colaboración open source

> When I started my current role around three years ago, it was early in the generative AI cycle. [...] As model reasoning improved, context and data were clearly the keys to making effective use of it [...] At the time, most database conversations focused on retrieval-augmented generation (RAG) using vector search. However, our team believed that agents and tools held the most interesting potential for large language models (LLMs) going forward. We immediately hit two scaling challenges: Google Cloud supports more than 15 different databases across its portfolio, and new open source agent frameworks (starting with LangChain and LlamaIndex) were emerging every week. That created a classic N-by-M integration problem between many clients and many data hosts.

> When Anthropic announced MCP, it was exciting validation that the broader ecosystem was arriving at the same architectural conclusions we were seeing across our database integrations. Rather than insisting on a homegrown protocol or spinning off a competing specification, we reached out to the MCP co-creators, Justin Spahr-Summers and David Soria Parra, and began meeting regularly. [...] We evolved our project into MCP Toolbox for Databases so it worked out of the box with any MCP client, and I focused on contributing capabilities from our original protocol back into the upstream MCP specification.

### Liderando la transición a una especificación MCP sin estado

> One of my primary upstream focuses was transport scalability. I began leading the MCP Transports Working Group with the goal of evolving the specification toward a stateless, horizontally scalable architecture. At first, it wasn't a crowded room. Our early working group meetings had around five participants, three of whom were from Google. As MCP adoption accelerated across the industry, however, it became clear that early stateful assumptions around persistent sessions and initialization were holding MCP back at production scale. That effort culminated in a two-day Transports Summit where Google and fellow working group members hosted the MCP core maintainers at our San Francisco offices [...] Shortly afterward, I was invited to become an MCP core maintainer [...] The result of that collaboration was the July 28, 2026 MCP specification, which transitioned MCP to a stateless model.

> That experience as an MCP core maintainer naturally positioned me to help co-maintain Agent Skills. Having already built working relationships with contributors across Google, Anthropic, and OpenAI, stepping in to help steward Agent Skills inside the AAIF felt like a natural continuation of the same collaborative model.

### Por qué importa la gobernanza neutral en la AAIF

> We've seen open source technologies like Kubernetes achieve widespread adoption and sustained cross-company contributions, but organizations are understandably hesitant to build critical workflows on a specification controlled by a single vendor. Just as the Cloud Native Computing Foundation (CNCF) provided a vendor-neutral home for container orchestration, the AAIF provides a neutral forum where organizations and independent maintainers can collaborate on shared agent standards.

> For developers, this means you can author a skill once and trust that it will remain portable across different agents, IDEs, and harnesses without vendor lock-in.

### Resolviendo el «tool bloat» con divulgación progresiva

> One of the most impactful things MCP accomplished was commoditizing tools: it became straightforward for anyone to wrap a set of actions in an MCP server and share it. The unintended consequence was tool and context bloat. As agents grew more capable and connected to dozens of MCP servers, deciding which tool schemas and operational instructions to load into the context window became a major bottleneck.

> Agent Skills introduced a remarkably simple, effective pattern for solving that problem through progressive disclosure. By loading only a lightweight YAML frontmatter name and description at startup, and pulling the full `SKILL.md` instructions, reference files, or scripts into context only when a task requires them, Agent Skills commoditized context the same way MCP commoditized tools.

> While some observers initially viewed MCP and Agent Skills as competing approaches, they have always been complementary: Agent Skills package domain expertise into modular chunks that teach an agent how to approach a problem, while MCP provides the live execution interface to carry it out. Today, the broader ecosystem has converged on combining them, including efforts around Agent Plugins and proposals for serving Agent Skills over MCP so platform maintainers can distribute domain instructions and live tools together.

> In our agent workflow benchmarks, we see developers complete complex database tasks much more quickly and reliably when MCP tools are paired with targeted Agent Skills.

### Qué viene después para la especificación Agent Skills

> Two major areas I'm focused on evolving next are packaging and discovery. Today, the Agent Skills specification defines how an individual skill is structured, but it doesn't yet standardize how collections of skills are bundled, how harnesses discover them, or how to resolve naming conflicts across skill sets. Closing those gaps will help address conformance differences across harnesses. Versioning is another priority. As the Agent Skills specification matures under the AAIF, we need a clear, portable way for skill authors and agent harnesses to declare which version of the specification they support.

> If you want to start authoring portable skills today, the documentation at agentskills.io walks through creating your first `SKILL.md` package in just a few minutes, and you can explore Google's open source catalog of developer skills at github.com/google/skills.

## Notas de captura

- Extraído con `web_extract` el 2026-11-12. La página completa (16.651 caracteres limpios) quedó guardada en `/home/vilber/.hermes/cache/web/opensource.googleblog.com-37fa3130a1.md`; aquí se reproduce la parte sustantiva (se omite el tramo intermedio sobre benchmarks de workflow de bases de datos y los módulos de pie de página).
