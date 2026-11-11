---
title: "Google Antigravity lanza /swarm: colaboración multiagente en el IDE"
source: "https://help.apiyi.com/en/google-antigravity-swarm-multi-agent-collaboration-en.html"
date: 2026-11-11
captured: 2026-11-11
---

# Google Antigravity Launches /swarm: How AI Coding Shifts from Single-Agent Execution to Multi-Agent Team Collaboration, Explained Through 4 Types of Roles

Por Fourteen, 11 nov 2026. El artículo se apoya en el blog oficial y la documentación de Google Antigravity.

On November 10, 2026, Gemini 4 Carbon became generally available. The same day, the Google Antigravity team launched the /swarm multi-agent collaboration feature (Preview). With one command, a single conversation turns into a small AI engineering team: one agent breaks down the task, others write the code, another runs checks, and another notices when progress stalls.

The feature is well documented. Antigravity's official blog and Swarm documentation are both live, and Google says its own engineers have been using it internally for about five weeks. /swarm isn't just a way to open several chat windows at once. It's an attempt at a collaboration system that can break down tasks on its own, run work in parallel, share progress, cross-check results, and keep fixing problems.

## Key terms

| Term         | Explanation                                                           | Role in /swarm                                                                         |
| ------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Agent        | An agent that can use tools to carry out tasks                        | Every member of the team is an independent Agent                                       |
| Swarm        | A preview feature that coordinates multiple agents working together   | Launched with the `/swarm ` command                                                    |
| Coordinator  | The agent that splits up the task and coordinates the members         | Created from the current conversation; handles task assignment and summarizing results |
| Worker       | An agent that takes on an assigned subtask                            | Has its own independent context; modifies code or investigates issues                  |
| Verifier     | An agent that checks other members' output or test results            | Reads diffs, runs tests, and reports problems back to the Worker                       |
| Monitor      | A member that watches the team's overall progress                     | Wakes up the relevant members when the team stalls before the task is done             |
| Working copy | A separate workspace used to isolate parallel changes                 | Allocated on demand when multiple Workers edit code or run builds at the same time     |
| Quota        | The resource limit a service places on model invocation or task usage | Consumed separately by each Worker; a Worker pauses once its quota runs out            |

## Mecánica y contexto

When you run `/swarm`, your current conversation becomes the Coordinator. It splits the task up, spins up multiple Workers to run in parallel, then hands things off to a Verifier that checks and tests the output. Human teams handle this by having someone else do the code review, and `/swarm` moves that division of labor into the AI coding workflow.

La nota del traductor del propio artículo advierte que no puede verificar de forma independiente la fecha de lanzamiento de noviembre de 2026, el nombre del modelo "Gemini 4 Carbon" ni el comando `/swarm` contra las fuentes oficiales; conviene contrastarlo con la documentación de Antigravity antes de publicar.

## Implicación señalada por el artículo

Multi-model collaboration becomes a deployment pattern: strong models handle planning and review while fast models handle bulk execution — a division of labor more and more Agent frameworks will borrow. That makes it easy to test whether the "strong model plans, fast model executes, heterogeneous model reviews" combination fits your project.

## Contexto relacionado (dealroom.co)

On November 4, 2026, OpenAI announced plans to acquire developer tools company Pierre Computer Company, Inc. Codex's competitive scope is expanding.
