---
title: "Claude Managed Agents autoalojado (beta privada): el plano de control del agente dentro del perímetro del cliente"
source: "https://claude.com/es/resources/articles/self-hosted-claude-managed-agents ; https://platform.claude.com/docs/en/managed-agents/self-hosted ; https://www.helpnetsecurity.com/2026/11/12/anthropic-self-hosted-claude-managed-agents/ ; https://aifrontierpost.com/articles/anthropic-self-hosted-claude-managed-agents-private-beta/"
date: 2026-11-13
captured: 2026-11-13
---

# Anthropic — Claude Managed Agents autoalojado (beta privada, 12 de noviembre de 2026)

Captura por extractos del artículo oficial de Anthropic, de la documentación de plataforma, de Help Net Security y de AI Frontier Post. Fecha de captura: 2026-11-13.

## Artículo oficial (claude.com)

> Introducing self-hosted Claude Managed Agents. Now you can run agents in your own environment, whether that's in your own cloud or on-premise. You host the agents, credentials, and session history, and choose where requests to Claude are sent. Self-hosted Claude Managed Agents is now available in private beta.

> With self-hosted Managed Agents, every part of the service runs in your own cloud or on-premise, including the harness, sandboxes, credentials, and session history. You operate the Managed Agents server, its database, and the workers where agents run their shell and file tools. Model requests go where you choose, whether that's Anthropic directly, your cloud provider (Amazon Bedrock, Google's Agent Platform, or Microsoft Foundry), or your own gateway.

### Los cuatro principios de seguridad

> **The brain and the hands are split** — The harness (the brain) calls Claude, and the sandbox (the hands) is where the agent's code runs. They are kept separate by design. The agent's code runs in the sandbox, while the agent loop, session history, and vault secrets stay outside it.

> **Credentials stay out of the sandbox** — Vaults are designed to keep credentials out of the sandbox. For MCP tools and supported API calls, a proxy outside the sandbox adds the credential to the request. With self-hosted Managed Agents, you can also store credentials in your own secrets manager.

> **Network access can be limited** — You can limit each environment to a list of allowed hosts, and requests to any other host are blocked.

> **Every session leaves a full record** — Managed Agents keeps a record of every step an agent took, including the tool calls it made and what came back. The record exports over OpenTelemetry.

## Documentación de plataforma

> | Option                     | Sandboxes | Service   | Model                                    |
> | -------------------------- | --------- | --------- | ---------------------------------------- |
> | Cloud sandboxes (default)  | Anthropic | Anthropic | Anthropic                                |
> | Self-hosted sandboxes      | You       | Anthropic | Anthropic                                |
> | Self-hosted Managed Agents | You       | You       | Anthropic, or a provider that you choose |

> - Server (`cma-server`): Serves the API, runs the agent loop, and stores agents, sessions, and each session's history. It calls your inference provider whenever the agent needs the model. The server never runs an agent's shell or file tools.
> - Database: PostgreSQL 16 or later. Without a database, the server keeps its data in memory, and a restart erases it.
> - Workers: Programs that take work from the server and run the agent's shell and file tools in your sandboxes. A worker is an `ant beta:worker` command or an SDK worker.

> The agent's `bash` tool is a real shell with the worker process's permissions and network access. The worker doesn't isolate that shell. Isolation comes from what the worker runs in. [...] If you start a worker yourself, run it in a disposable container or VM that holds nothing you need to protect.

> | Credential           | Who holds it                                        | What it authenticates                                         |
> | -------------------- | --------------------------------------------------- | ------------------------------------------------------------- |
> | Server API key       | Your applications, the `ant` CLI, and the admin CLI | Requests to your server.                                      |
> | Inference credential | The server                                          | The server's model calls to your inference provider.          |
> | Environment key      | Your workers that poll the server                   | One environment's work queue and that environment's sessions. |

## Help Net Security (12 de noviembre de 2026)

> The change matters for agents that already work unattended inside corporate systems, fixing broken builds, testing releases, triaging alerts, and working through bug backlogs. Until now, customers could host the sandbox themselves. [...] Anthropic ran everything else, including the credential handling and the record of what each agent did.

> Anthropic limits that protection to MCP tools and "supported API calls," so any other service an agent reaches is worth checking before the agent goes live.

## AI Frontier Post — carencias de la beta

> Model requests can go to Anthropic, Amazon Bedrock, Google's Agent Platform, Microsoft Foundry or the customer's own gateway — but Claude still runs outside the customer's network, so this is self-hosted orchestration, not an on-premises model. Scheduled runs and webhooks are missing, nothing migrates from the hosted service, and access is limited to eligible organizations through their Anthropic account team.

> The gaps: scheduled deployments and webhooks are unavailable in the beta, and nothing migrates from the hosted service — agents, skills, vault credentials, memory stores and session history must be rebuilt. No pricing or general-availability date has been published.
