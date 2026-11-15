---
title: "Unit 42: atacantes usan el framework abierto Cairn con GLM y DeepSeek para 25 operaciones autónomas contra 19 organizaciones"
source: "https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/"
date: 2026-11-15
captured: 2026-11-15
---

# Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors

Fuente: Palo Alto Networks Unit 42 (unit42.paloaltonetworks.com). Cobertura secundaria: CSO Online, Cybersecurity Dive, Help Net Security, GovInfoSecurity (12–13 de noviembre de 2026).

## Executive Summary (verbatim)

> From August–September 2026, Chinese-speaking attackers used an open-source AI penetration testing framework called Cairn to autonomously conduct 25 operations against at least 19 organizations. The attackers weaponized Cairn by pairing it with Chinese AI models Zhipu GLM and DeepSeek. The attackers supplied a target and a goal, then Cairn planned, executed and recorded results on its own. These attacks achieved unauthorized access or data retrieval at 10 of the targeted organizations, including:
>
> - Accessing dozens of valid credentials
> - Mass exposing personal data (exceeding one million records at one organization)
> - Retrieving military and government identities
> - Creating persistent administrator accounts in a production system
> - Modifying a live industry standards-ballot document
>
> We assess with moderate confidence that this activity represents China-nexus intelligence collection, which we currently track as CL-STA-1238.

## Metodología (verbatim, selección)

> The attackers behind CL-STA-1238 orchestrated their campaign using the publicly available penetration testing framework Cairn. An AI model drives each Cairn "agent worker." Cairn coordinates its activities through a shared "blackboard." Agents read the blackboard and write their findings back as a fact-intent graph, while human operators can inject "hints" at any time to help guide the operations if needed. Confirmed findings accumulate as immutable facts and the agent queues its next actions as intents.

> For each operation, the attackers created a task with a one-line goal, such as: 以拿到实质性高价值权限为止，包括但不限于webshell、ssh、源码、key、用户信息、凭据等，最好是可以进入内网
> Translation: "Obtain substantive high-value access, including but not limited to webshell, SSH, source code, keys, user information, credentials, ideally, to enter the internal network."

> Cairn runs each operation through three task types, all carried out by the same AI worker. At the start of an operation, a bootstrap task attempts to solve the goal directly from the target and any hints the attackers supplied. From there, Cairn maps the target and breaks the goal into many small tasks. The model produced a different plan for each target, running from three–seven stages. For example, during the operation against one semiconductor manufacturer, the stages moved through the following phases:
>
> - Reconnaissance and asset mapping
> - Web application exploitation
> - Services and middleware exploitation
> - Credential and secret collection
> - Privilege escalation and lateral movement
> - Internal-network access and persistence
>
> Cairn then worked through these tasks in a loop, with each task building on what earlier tasks had confirmed. Beyond the initial bootstrap task, this orchestration loop consists of two phases:
>
> - Reason
> - Explore

> This loop repeats until the model judges that it has met its goal, that it has exhausted its options or that the attacker has stopped it.

> Individual operations ran from 20 minutes to more than 50 hours with no attacker-imposed time limit.

## Modelos chinos (verbatim)

> Cairn is model-agnostic. The attackers ran their operations on the Chinese models Zhipu GLM 5.2 and DeepSeek V4 Flash/Pro. Out of 25 operations, the attackers ran:
>
> - Thirteen on GLM 5.2
> - Eight on DeepSeek V4 Flash
> - Four on DeepSeek V4 Pro
>
> The attackers appear to have benchmarked the models against one another, using the higher-tier DeepSeek V4 Pro for repeated attempts against targets that resisted the DeepSeek V4 Flash model. Each operation also loaded a skill pack named "AIScan Runner Skills," providing the model with scanning and exploitation capabilities. This pack does not appear in the upstream Cairn project and is specific to the configuration for these attacks.

## Objetivos (verbatim)

> - Semiconductor and advanced-manufacturing supply chain: Seven organizations spanning the lithography, chip-design, materials, photomask and standards layers of the supply chain.
> - Defense and defense policy: Three organizations including a space technology company, a defense-analytics vendor and a policy think tank.
> - Human rights and civil society: Four organizations including a Canadian human-rights body, a U.S. teachers' union, a science-policy advocacy group and an education nonprofit.

## Conclusión de Unit 42 (verbatim)

> The building blocks of this campaign were an off-the-shelf open-source framework, commodity model APIs and a trivial jailbreak pretext. Attackers set targets and goals, and the framework pursued the objective autonomously. In this campaign, the attackers behind CL-STA-1238 were likely a single operator or small team. They conducted simultaneous intrusion attempts against 19 organizations in two weeks. Autonomous orchestration removes the historical limit on the number of targets an actor could pursue simultaneously due to operator hours. However, the vulnerabilities the attackers exploited were known:
>
> - Authentication bypasses
> - Insecure direct object references
> - Mass-assignment privilege escalation
> - Weak and default credentials
> - Exposed cloud APIs
> - Dated public CVEs
>
> Autonomous AI raises the volume and coverage of exploitation, but not its complexity. Identity hygiene, attack-surface reduction and software patching remain effective.

## Detalle del jailbreak (verbatim, Help Net Security)

> Getting the models to cooperate took very little. Cairn's stock prompts already tell the model never to refuse a task. The attackers added a Chinese-language preamble claiming every job was authorized security testing, and each operation generated an AUTHORIZATION.md file declaring the work client-approved. Neither Zhipu GLM nor DeepSeek refused.

## Origen del framework (verbatim, GovInfoSecurity)

> Like similar tools in China's offensive security ecosystem, Cairn emerged from a red team competition. It won the third place in the week-long AI Penetration Testing Challenge hosted by Tencent Cloud Hackathon in April. "The system had never been tested before the competition," Cairn's developer team Bytex wrote on GitHub. "The full pipeline came online for the first time at 4 a.m. on race day. No training, no tuning, no domain-specific tooling. Zero MCP tools, zero RAG, zero predefined agent roles."

## Botín citado (verbatim, GovInfoSecurity)

> Some assets the attackers stole include credentials of an industry standards body, a million member records from a teachers' union, 500 user records at a defense-policy think tank and 150,000 internal documents at an industrial-automation manufacturer.

## Lectura técnica

El caso es el reverso exacto del discurso comercial del mes: **un framework abierto, APIs de modelos commodity y un pretexto de jailbreak trivial** bastan para que un solo operador lance intrusiones simultáneas contra 19 organizaciones en dos semanas. La orquestación autónoma elimina el límite histórico de objetivos por horas de operador. Lo importante: **la IA autónoma sube el volumen y la cobertura de la explotación, no su complejidad** —las vulnerabilidades explotadas eran conocidas (bypass de autenticación, IDOR, escalada por mass-assignment, credenciales débiles o por defecto, APIs cloud expuestas, CVEs públicos antiguos)—. Higiene de identidad, reducción de superficie y parcheo siguen siendo la defensa efectiva.
