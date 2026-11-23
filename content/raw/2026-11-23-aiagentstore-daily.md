---
title: "AI Agent News Today — 23 de noviembre de 2026"
source: "https://aiagentstore.ai/ai-agent-news/daily/2026-11-23"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# AI Agent News Today — Monday, November 23, 2026

## Tether 0.4.0 adds deterministic test replays for recorded agent runs

**What changed:** Tether released version 0.4.0 on November 22, 2026, adding a test harness that replays recorded agent runs so developers can assert which tools were called, final file contents, and whether the agent respected step or cost limits.
**Why it matters:** Replaying traces without hitting the model makes it practical to regression-test policy changes, agent upgrades, or safety rules against known runs before deploying them in production — reducing risk from blind rollouts.
**Try/watch:** Integrate Tether into your CI to gate merges that change agent prompts, tool access, or permissions; watch for divergence when you change models or prompts, since replays only prove behaviour for the same inputs and recorded responses.

## "Formalize or Lose It" — experimental evidence that executable checks catch handoff errors in agent swarms

**What changed:** A research release published November 23, 2026, reports experiments showing that nearly half of supervisory rules in multi-agent runs lived only in natural-language prompts, and that adding executable checks (a requirement ledger and host-side acceptance tests) caught failures that prompt-only supervision missed.
**Why it matters:** For engineering teams building multi-agent pipelines or layered coding agents, the paper gives actionable evidence: formalize safety and acceptance rules into programmatic checks that execute at handoff, because human-readable prompts alone let important requirements disappear during planning and relay.

(Enlaces a los boletines: News: November 20 / 21 / 22.)
