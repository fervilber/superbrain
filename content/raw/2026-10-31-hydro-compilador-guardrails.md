---
title: "AWS's Hydro team wants the compiler to catch coding agents' mistakes (The New Stack) — captura"
source: "https://thenewstack.io/ai-agents-compiler-guardrails"
date: 2026-10-29
captured: 2026-10-31
---

# AWS's Hydro team wants the compiler to catch coding agents' mistakes

> Captura por segmentos del artículo de Matthew Burns en The New Stack (29 de octubre de 2026). El extractor devolvió cabecera, cola y navegación del sitio; se reproduce el cuerpo sustantivo obtenido.

His answer is shared **correctness checks outside the agent's "zone of trust"**, such as those enforced by a compiler. Rust's borrow checker is his example: it catches race conditions before the code ever runs. Hydro does something similar for distributed systems, catching several types of bugs at compile time so an agent gets instant feedback on mistakes it introduced. The wider goal, which the team is still exploring, is **domain-specific guardrails that agents can share**.

Earlier this month, the team behind Hydro developed a new way to check that a distributed system still works correctly when it resends messages after a failure. This produced what Shadaj Laddad described to me as **"like a 5000 line PR"**. Hydro is an open-source Rust framework for distributed systems, the software that runs across many machines at once, and **agents now write most of it with humans driving**. The PR was difficult to split into smaller pieces as its components worked together.

## Por qué los tests no bastan

Según la cobertura del mismo episodio recogida por terceros (chiprook, daily.dev, podcast de The New Stack), el argumento de Laddad es que en la mayoría de los flujos agénticos **el mismo agente escribe la implementación y los tests**, por lo que los tests pueden simplemente confirmar lo que el agente construyó en lugar de detectar errores reales. Los agentes son impredecibles, lo que dificulta que un humano verifique que los tests realmente comprueban lo que el equipo pretende. La revisión humana de código no puede seguir el ritmo de pull requests de ese tamaño.

## De idempotencia a guardrail general

To find candidates, the team studies historical projects for recurring patterns. **Idempotency**, ensuring a retried request doesn't run twice, comes up repeatedly in design reviews, so the team is asking whether it can become a general-purpose guardrail. Laddad sees this as the next rung on an old ladder. C spared programmers from mangling function calls in assembly. Java took memory allocation off their plate. Agents, he argued, make the next layer more urgent.

Compilers have limits, though. As _The New Stack_ reported in August, **AI-generated Rust can compile perfectly and still be wrong**.

## Infinity, el runtime del mismo equipo

The same team also built **Infinity**, an open-source agent runtime AWS announced on October 23. It **suspends an agent while it waits on a tool call or a CI job** instead of keeping it running. Laddad cited a benchmark showing **75,000 concurrent agents on a single Raspberry Pi**. According to the AWS announcement, that figure is extrapolated from a server test in which each idle agent used about 100 KB.

Hydro itself is an early release, built for teams running high-throughput, low-latency services who are constantly worried about distributed systems bugs. Laddad noted that users should expect rough edges and a learning curve right now. The payoff is the confidence to change a system without fearing it will break a few months later.

Hydro and Infinity are open source at **hydro.run**, built jointly by AWS and UC Berkeley.
