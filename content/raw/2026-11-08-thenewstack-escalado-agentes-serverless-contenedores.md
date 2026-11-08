---
title: "Captura: Scaling an autonomous agent from one team to fifty — a serverless-to-container decision framework (The New Stack)"
source: "https://thenewstack.io/scaling-autonomous-agents-framework/"
date: 2026-11-08
captured: 2026-11-08T20:07:00+01:00
---

# Scaling an autonomous agent from one team to fifty: A serverless-to-container decision framework

_Captura (texto limpio; el artículo completo queda en el fichero cache de `web_extract`). Autor: Rashmi Erande (Senior QA Engineer en Amazon), 8 de noviembre de 2026. Extracto con la parte sustantiva del marco de decisión._

I built a system to eliminate this entirely. Not a dashboard. Not a notification bot. An autonomous agent that observes test results, makes judgment calls – is this a new bug, a duplicate, or a regression? And takes action without human intervention. It files structured bugs, attaches screenshots, calculates repro rates, detects regressions build-over-build, and notifies the right people. The team just marks FAIL and moves on.

## The decision framework

This led me to build a simple decision rubric – not Lambda vs. containers, but which characteristics does your workload actually exhibit?

| Workload characteristic                        | Lambda (+ Managed Instances, Durable Functions) | Auto Mode                                  |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| Event-driven, short-lived                      | Optimal                                         | Overengineered                             |
| Single-tenant, low complexity                  | Optimal                                         | Unnecessary                                |
| Multi-tenant with isolation needs              | Possible (Tenant Isolation)                     | Native (namespaces, RBAC, NetworkPolicies) |
| Long-running with persistent state             | Possible (Durable Functions)                    | Native (pods, persistent connections)      |
| Cross-tenant analysis requiring shared memory  | Complex (custom orchestration)                  | Natural (shared services namespace)        |
| GPU-burst inference                            | Possible (Lambda GPU – if available)            | Native (GPU NodePools, scale-to-zero)      |
| Centralized rate limiting + connection pooling | Custom build (SQS + Step Functions)             | Shared platform service                    |

The next frontier isn't single agents doing single tasks faster. It's agents coordinating with other agents. An auto-filer agent detects a failure pattern and hands context to a root-cause agent, which traces the dependency chain across services, identifies the offending commit, and drafts a fix recommendation – all before a human sees the bug ticket. Agent-to-agent delegation, where one agent's output becomes another's input without human routing in between.

## Key takeaways (verbatim)

- **Design for portability from day one:** Structure your Lambda function as a pure decision engine with external state. Containerizing it means wrapping it in an async loop and adding a health endpoint. If you build Lambda functions as self-contained decision engines rather than tightly coupled to the invocation model, the transition is a one-day exercise whenever you need it.
- **The decision trigger isn't scale – it's workload characteristics:** Don't move because you hit 50 teams. Move when you need capabilities that benefit from persistent, shared infrastructure: cross-team correlation, centralized rate limiting, GPU inference, streaming connections.
- **Multi-tenancy is an isolation problem, not a compute problem:** Both Lambda (Tenant Isolation) and Kubernetes (namespaces) solve this. Choose based on what other characteristics your workload needs alongside isolation.
- **EKS Auto Mode closes the operational gap:** Before Auto Mode, choosing EKS meant accepting node management overhead. Auto Mode removes that tradeoff. You get container-native execution with serverless-like operations.

## The cost math

Single team on Lambda today: $3-5/month. 8-10 hours/week saved. 67x ROI. Fifty teams on EKS Auto Mode would cost approximately $200-250/month total – roughly $4-5 per team per month. Same per-team economics as Lambda, but with namespace isolation, persistent connections, GPU-ready infrastructure, centralized observability, and built-in organizational governance.

The cost-per-team barely changes. What changes is what you get for it!

## What comes next?

The agentic pattern – 'observe, decide, act' is infrastructure-agnostic. The decision logic doesn't care about its deployment target. What changes is what becomes possible when agents stop operating in isolation.

> "The next frontier isn't single agents doing single tasks faster. It's agents coordinating with other agents."

Beyond that: agents that build their own decision models. Today, I hand-code the dedup logic and regression detection rules. Tomorrow, the agent observes which of its filed bugs humans close as duplicates, learns from those corrections, and tightens its own classification boundaries. The system improves not because I ship better code, but because it accumulates organizational judgment over time.
