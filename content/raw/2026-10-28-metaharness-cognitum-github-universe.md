---
title: "Cognitum One MetaHarness: fábrica open source de harness de agentes (GitHub Universe 2026)"
source: "https://finance.yahoo.com/technology/ai/articles/cognitum-one-unveils-metaharness-open-134700301.html"
author: "Cognitum One (ACCESS Newswire) vía Yahoo Finance"
date: 2026-10-28
captured: 2026-10-28
---

# Captura: MetaHarness, fábrica de harness de agentes gobernados

> Texto completo del comunicado de Cognitum One publicado el 28 de octubre de 2026 en coincidencia con GitHub Universe 2026 (Fort Mason Center, San Francisco, 28-29 de octubre).

## Cognitum One Unveils MetaHarness, the Open-Source Factory for Branded, Governed AI Agent Harnesses

**_With over 100 Million downloads and over 196,000 GitHub stars, MetaHarness arrives as the next open-source project of the prolific creator, Reuven "rUv" Cohen._**

**SAN FRANCISCO, CA / ACCESS Newswire / October 28, 2026 /** Every team building AI agents ends up rebuilding the same plumbing: the command-line tool, the tool connections, memory, safety rules and release checks that sit around a model. Cognitum One™, Inc. (cognitum.one), the sovereign agentic control plane company, today announced MetaHarness™, in conjunction with GitHub Universe 2026, which takes place October 28 and 29 at Fort Mason Center in San Francisco. MetaHarness is an open-source factory for agent frameworks. Starting from a GitHub repository or a blank page, it generates a branded agent harness that a team owns and can publish under its own name. Each harness comes with its own npx command-line tool, Model Context Protocol (MCP) server, scoped memory, governance policy and witness-signed releases. The model can be swapped out. The harness is what the team builds and keeps.

MetaHarness doesn't stop at the first attempt. It tests different ways for an AI agent to work, builds on changes that perform better and pass safety checks, and uses those results to guide the next round - all without changing the AI model itself. These capabilities support Cognitum One's vision for AI that businesses can control: the company sets the rules, the system checks tool actions against those rules, and records them for review.

MetaHarness comes from the developer behind some of the most widely used open-source AI infrastructure on GitHub. Cohen's ruvnet projects, including RuView™, Ruflo™ and RuVector™, have passed 100 million downloads across npm and crates.io and earned more than 196,000 GitHub stars from a community of more than 12,000 GitHub followers. MetaHarness is also ranked #2 on the OpenEnv Arena leaderboard, a new benchmark in which AI agents design the reinforcement-learning environments used to train and test a model.

> "Most teams treat the model as the product and the harness as an afterthought. We think it is the other way around," said Reuven "rUv" Cohen, Founder and Chief AI Officer of Cognitum One and creator of MetaHarness. "The model changes every few months. The harness holds your tools, your memory, your safety rules and your release history. MetaHarness lets a team mint that harness in minutes and put its own name on it. Then it builds many versions, races them against each other on real work, and keeps the one that wins, without touching the model."

Explore MetaHarness: https://github.com/ruvnet/metaharness
Get started: `npx metaharness --wizard`

### What MetaHarness Does

- **Generates a harness from your repository.** `harness analyze-repo` reads a repository's structure and recommends a harness before anything is built. Analysis is read-only and never runs repository code. Inferred build and test commands stay disabled until someone explicitly trusts them.
- **Runs on the hosts teams already use.** Generated harnesses target ten hosts: Claude Code, Codex, GitHub Copilot, OpenCode, pi.dev, Hermes, OpenClaw, RVM, Prime Agent and GitHub Actions. Nineteen quick-start templates cover verticals including coding, DevOps, research, trading, legal, support, sales and education.
- **One shared Rust kernel.** Every harness uses `@metaharness/kernel`, a Rust core shipped as WebAssembly (WASM) and native bindings. It provides governance, memory, routing and witness signing. Host-specific behavior stays in thin adapters.
- **Tools with a policy boundary.** MCP tool access is denied by default. Teams then choose one of three modes: MCP turned off entirely, local connections only, or authenticated remote connections. `harness mcp-scan` checks tool configurations for risky grants and missing audit or timeout settings without running the tools.
- **Routes against a quality bar.** `@metaharness/router` predicts each candidate model's quality on a team's labeled examples and picks the cheapest one expected to clear the team's threshold.
- **Builds many versions and keeps the best.** Darwin Mode generates competing variants of a harness, runs each one in a sandbox against the same tasks and keeps only those that measurably beat the current version and pass its safety gates. The underlying model stays frozen, and the defaults need no network and no API keys.
- **The flywheel: run, measure, mutate, verify, promote.** `@metaharness/flywheel` turns that search into a compounding loop. Each generation starts from the last proven winner, and a candidate is promoted only if it clears a frozen gate, including held-out tasks it was never tuned on. Every promotion is signed with Ed25519, so an outside reviewer can replay the full lineage and confirm each gain was real.
- **Reviewable releases.** Ed25519 witness signing, SPDX-2.3 software bills of materials and release gates record what was generated and what shipped. Publishing stays an explicit maintainer action.
- **Red-team and blue-team testing.** `@metaharness/redblue` attacks an agent a team owns with adversarial models, covering prompt injection, tool misuse, data leakage, jailbreaks and runaway costs. It then patches the vulnerable areas with declarative rules, retests and produces a board-readable report. Real credentials, shell access and live external targets are blocked in code.

### Proven on Public Benchmarks

MetaHarness's published benchmarks show that the right harness can let lower-cost models match or beat frontier models on specific workloads, at a fraction of the cost:

- **Research (DRACO).** Claude Haiku 4.5 scored higher than Claude Opus 4, 0.7566 versus 0.7143, at about one-tenth the calculated token cost, delivering 10.6 times more quality per dollar.
- **Function calling (BFCL).** MetaHarness's DeepSeek-V4-Pro configuration reached 96% accuracy versus 83.3% for GPT-5.2 across the same 150 tasks, at about 54% lower cost.
- **Research and assistant questions (FRAMES).** DeepSeek-V4-Pro matched GPT-5.2's 42.7% observed accuracy on the same 150 questions while costing about 79.5% less per question.
- **Software engineering (SWE-bench Verified).** A GLM-to-Opus cascade resolved 278 of 500 issues, or 55.6%, at an estimated $0.15 per issue.

### Leading on OpenEnv Arena

Most AI benchmarks measure how well a model answers questions that people wrote. OpenEnv Arena flips that. AI agents design and code the reinforcement-learning environments, then the arena trains an open model on those environments and scores the result on held-out tasks across eight domains: cybersecurity, finance and economics, industrial and physical systems, math and formal reasoning, media and content production, natural science, office and white-collar work, and software engineering. It is designed to be hard. Every task is held out, and the agent never sees the test it is training a model for. As of October 26, 2026, no entrant had solved more than a quarter of the 40 tasks.

As of October 26, 2026, MetaHarness ranks #2 on the leaderboard with a 22.5% average, solving 9 of 40 held-out tasks. Its strongest domain is office and white-collar work, where it solved 3 of 5 tasks, followed by industrial and physical systems at 2 of 5. The leaderboard keeps each entrant's best result in each domain across submissions. Earlier this month, MetaHarness was tied for the top score at 15%.

### Why It Matters

AI agents are capable, but regulated enterprises cannot deploy what they cannot govern. Auditors want to know what an agent did, where it ran and whether that can be proven. Evaluation has become a market of its own: on October 8, 2026, Arena, formerly LMArena, announced a $200 million Series B at a $3.1 billion valuation. MetaHarness brings that discipline into the agent itself. Every harness it generates ships with policy boundaries, adversarial testing, quality-gated model routing and a signed record of each release.

Enterprises do not want another framework to babysit. They want an agent they own, with their name on it, that they can prove is safe before it reaches production. MetaHarness delivers that in a single command. Teams can start with one harness on one repository and grow into governed agents across the business, running under Cognitum One's control plane alongside Ruflo and ruOS on infrastructure they control.

### Getting Started

- **Guided setup:** run `npx metaharness --wizard` and pick a template and host.
- **Claude Code:** run `npx metaharness my-bot --template vertical:coding --host claude-code`. For Codex, use `--host codex`.
- **From an existing repository:** run `harness analyze-repo . --scaffold my-bot`, then validate it and publish under your own package name.
- **Security testing:** run `npm i @metaharness/redblue` and point it at a local copy of the agent you own.

### Availability

MetaHarness is available today. It is open source under the MIT license at github.com/ruvnet/metaharness, with the metaharness command-line tool and the `@metaharness/*` packages on npm. Model provider subscription or usage costs still apply. Experimental modules, including AVO governed variation, field memory, the ARC-AGI-3 harness and Weight-EFT, are clearly labeled and carry their own requirements. Cognitum One offers commercial licensing, enterprise support and deployment with Ruflo and ruOS™ on infrastructure the customer controls.

### Notas del capturador

- Hermes figura explícitamente entre los diez hosts soportados por los harness generados (`--host hermes`), junto a Claude Code, Codex, Copilot, OpenCode, OpenClaw y GitHub Actions.
- La tesis «el harness es el producto, el modelo es un componente intercambiable» ya apareció en el informe del 26 de octubre; aquí se materializa en herramienta instalable y con gates de promoción firmados (Ed25519).
- Los números de benchmark son autoinformados por Cognitum One y provienen de corridas publicadas en el propio repositorio; el comunicado advierte que las cifras de FRAMES no son comparables con el leaderboard externo y que el coste de SWE-bench Verified es una estimación.
- OpenEnv Arena invierte el modelo de evaluación: el agente diseña los entornos de RL con los que se entrena un modelo abierto; ninguna entidad superaba el 25% de las 40 tareas al 26 de octubre de 2026.
