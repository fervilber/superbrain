---
title: "Agent Collaboration Weekly: Agent Host Protocol, OpenAI Multi-agent y compromiso de agent-framework"
source: "aiagentstore.ai"
date: 2026-11-23
captured: 2026-11-25T20:05:00+01:00
---

# Agent Collaboration Agentic AI News - Week Ending 2026-11-24

URL: https://aiagentstore.ai/ai-agent-news/topic/agent-collaboration

## Agent Collaboration Weekly AI News — November 16 - November 24, 2026

### Weekly signal

This briefing covers agent-collaboration developments during 2026-11-16 → 2026-11-24. The week saw three platform-level moves that change how agents coordinate across clients and providers, one ecosystem security incident that directly targets agent runtimes, and a set of runtime/library patches that affect message delivery and provider interoperability.

### What changed

1. GitHub published the Agent Host Protocol (AHP), an open protocol that lets Copilot/agent sessions persist and be shared across VS Code, the Copilot app and cloud hosts (designed around URI-identified "channels" and reducer-based server state). This makes multi-client agent collaboration (concurrent clients, reconnect, replay) a supported interoperability surface for agent UIs and hosts.

2. OpenAI expanded Responses API documentation and examples for Multi-agent (beta): root agents can spawn parallel subagents, exchange encrypted agent messages, and use hosted collaboration actions like spawn_agent, wait_agent, and interrupt_agent. The docs spell out required header flags (responses_multi_agent) and new output item types your app must handle.

3. Open-source runtimes shipped compatibility and provider updates: open-multi-agent released v1.25.0 with a new Venice provider and fixes mapping provider refusal/content_filter responses; LangChain's LangGraph pushed 1.2.23/1.2.24 fixes addressing message-delta, streaming and Send-dispatched tool state parity — important for consistent multi-agent messaging and streaming UI behaviour.

4. Critical supply-chain compromise: two malicious versions (1.26.1/1.26.2) of Microsoft's agent-framework PyPI package were uploaded and contained a Python .pth startup hook credential-stealer before PyPI quarantined them. The incident directly targets agent runtimes and CI/build machines. If you install agent-framework via PyPI, check your lockfiles and runners now.

### What to do with it

- If you run agent UIs or multi-client workflows, evaluate AHP for session continuity (clients, hosts and language bindings are published). Start small: run an AHP host locally and test session handoff flows.
- If you use OpenAI Responses multi-agent, audit code paths for the new item types (multi_agent_call, agent_message) and add the required betas header and server-side orchestration handling. Test max_concurrent_subagents in dev.
- Upgrade agent runtimes: pin open-multi-agent to 1.25.0 if you need Venice model support and check content_filter handling; upgrade LangGraph to 1.2.24 to avoid message-delta bugs in streaming subagents. Run your integration tests.
- Urgent: scan for agent-framework==1.26.1/1.26.2 in build images, rotate any credentials that may have been exposed, and follow JFrog/DependencyWatch IoCs and mitigation guidance. Block those PyPI versions in your CI and agents.

---

## Agent Brief — November 2026 (issue Tue Nov 24)

URL: https://news.agentcommunity.org/issues/month/2026-11

### Loops, Local Weights, Agent Harnesses

- Looping Into Capability — Z.ai's GLM-5.4 runs 28 middle layers twice per token, but the open weights stay held pending safety hardening, no date given.
- Meta's 30B Bet — Muse Glimmer ships Apache 2.0, benchmarked by Meta against Gemma4-31B and Qwen3.6-27B — not frontier models.
- Delivery Gap — A SWE-CoWork benchmark found leading coding agents pass ~63% of tests yet finish under 8% of assignments.

### Harness Wars and Env Standards (issue Mon Nov 23)

- Harness Over Model — Anthropic's experimental Code Mode has Claude write runnable code for multi-step tool calls, while Thinking Machines' open-weight Inkling 2 Mini reportedly runs agent tasks locally.
- Environments, Not Rewards — Hugging Face's OpenEnv moves to nine-organization committee governance with a deliberately narrow API that leaves reward design outside the socket.
- Price Per Task — H Company reports Holo4 27B at 61.7% on OSWorld 2.0 versus 81.8% for Opus 5.5 — at $1.22 per task against $8.48.

### Cheap Models, Costly Failures (issue Fri Nov 20)

- Cheap Frontier Claims — Cognition's evaluation reportedly puts Gemini 4 Neon within one point of Opus 5.5 at roughly a third the cost.
- Benchmarks Don't Hold — MAST attributes 41.77% of multi-agent failures to specification issues; no frontier model tops 50% on ITBench-AA.
- Architecture Is Risk — HF's July intrusion post-mortem points to sandbox breakouts and shared credentials, not model capability.
