---
title: "Captura: OpenAI Responses API multiagente — spawn_agent, send_message, wait_agent, interrupt_agent"
source: "https://developers.openai.com/api/docs/guides/responses-multi-agent"
date: 2026-11-08
captured: 2026-11-09T20:12:00+01:00
---

# Multi-agent | OpenAI API

developers.openai.com

## Overview

Multi-agent lets a model spin up and coordinate subagents in parallel, synthesizing their work to provide a final response. This is especially effective for applications with complex tasks that benefit from parallel work delegation, such as codebase exploration, documentation, and implementation.

Multi-agent is available as a beta feature with GPT-6.1 Sol and all GPT-5.6 models. Check the model page before enabling Multi-agent in your application.

## When to use Multi-agent

Multi-agent orchestration is most useful when a task can be divided into concrete, independent workstreams, such as:

- Exploring separate parts of a large codebase
- Comparing multiple proposals, documents, or hypotheses
- Researching several sources in parallel
- Implementing independent components or writing independent test suites
- Investigating different possible causes of a failure in parallel
- Exploring separate approaches to a problem concurrently

Note that adding subagents can increase token usage.

## Quickstart

The Python and JavaScript examples use the beta Responses SDK. For HTTP requests, use `client.beta.responses` and pass `responses_multi_agent=v1` in the betas argument.

## New Multi-agent output items

Multi-agent responses can include three additional output item types:

- `multi_agent_call`: records a hosted Multi-agent action, such as `spawn_agent`.
- `multi_agent_call_output`: contains the result from execution of a hosted action.
- `agent_message`: carries an encrypted message from one agent to another.

Your application should not execute these `multi_agent_call` items or submit outputs for them.

## Actions

| Action          | Purpose                                               |
| --------------- | ----------------------------------------------------- |
| `spawn_agent`   | Create a subagent and assign its initial task.        |
| `followup_task` | Give an existing agent a new task and trigger a turn. |
| `send_message`  | Pass a message to a running agent.                    |

## Transport

- HTTP streaming: `client.beta.responses.create` with `betas` argument `responses_multi_agent=v1`; this enables beta types and autocomplete.
- WebSocket: the Python beta SDK exposes it through `client.beta.responses.connect`; the TypeScript beta SDK through `ResponsesWS`. Pass `OpenAI-Beta: responses_multi_agent=v1` in the connection headers; unlike HTTP streaming, the WebSocket connectors do not yet accept the betas argument in the `response.create` call. Over WebSocket, your application injects the function output into the active response.

## Notas de estado (de búsquedas dirigidas)

- La documentación de la API Responses para multiagente clarifica cómo un agente raíz lanza y coordina subagentes (`spawn_agent`, `send_message`, `wait_agent`, `interrupt_agent`) y cómo habilitar ejecuciones multiagente (flag beta `responses_multi_agent=v1`). Los valores por defecto y límites incluyen `max_concurrent_subagents = 3` por defecto. La guía recomienda WebSockets para flujos con muchas herramientas y señala que la compactación de contexto y la semántica de tool-calling son restricciones prácticas.
- El OpenAI Agents SDK v0.24.0-alpha.7 (8 de noviembre) añadió sesiones raíz durables, herramientas alojadas y presupuestos de uso observados al runtime nativo; la alpha cambia varios defaults y nombres.
