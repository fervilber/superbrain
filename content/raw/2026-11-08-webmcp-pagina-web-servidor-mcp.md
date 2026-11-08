---
title: "Captura: WebMCP — la página web como servidor MCP en el cliente (W3C Community Group, Draft)"
source: "https://webmachinelearning.github.io/webmcp"
date: 2026-11-08
captured: 2026-11-08T20:10:00+01:00
---

# WebMCP

Draft Community Group Report. Editors: Brandon Walderman (Microsoft), Khushal Sagar (Google), Dominic Farolino (Google).

## Abstract

The WebMCP API enables web applications to provide JavaScript-based tools to AI agents.

## Status of this document

This specification was published by the Web Machine Learning Community Group. It is not a W3C Standard nor is it on the W3C Standards Track.

## 1. Introduction

WebMCP API is a new JavaScript interface that allows web developers to expose their web application functionality as "tools" - JavaScript functions with natural language descriptions and structured schemas that can be invoked by agents, browser's agents, and assistive technologies. Web pages that use WebMCP can be thought of as Model Context Protocol [MCP] servers that implement tools in client-side script instead of on the backend. WebMCP enables collaborative workflows where users and agents work together within the same web interface, leveraging existing application logic while maintaining shared context and user control.

## 2. Terminology

An **agent** is an autonomous assistant that can understand a user's goals and take actions on the user's behalf to achieve them. Today, these are typically implemented by large language model (LLM) based AI platforms, interacting with users via text-based chat interfaces.

A **browser's agent** is an agent provided by or through the browser that could be built directly into the browser or hosted by it, for example, via an extension or plug-in.

An **AI platform** is a provider of agentic assistants such as OpenAI's ChatGPT, Anthropic's Claude, or Google's Gemini.

## 3. Supporting concepts / API surface

- `document.modelContext.registerTool(tool, options)` — Registers a tool that agents can invoke. Returns a rejected promise if a tool with the same name is already registered, if the given `name` or `description` are empty strings, or if the `inputSchema` is invalid.
- `document.modelContext.getTools(options)` — returns the registered tools.
- `document.modelContext.executeTool(tool, inputObject, options)` — Executes a tool on the document it was registered on. Returns a promise that resolves to the stringified result of the tool's execution.

A **tool definition** struct carries: `name` (1–128 chars, ASCII alphanumeric plus `_`, `-`, `.`), `title` (nullable human-readable), `description`, `input schema` (stringified JSON Schema), execute steps, `annotations`, and `exposed origins`.

An **annotations** struct carries three booleans: `read-only hint` (initially false), `untrusted content hint` (initially false) and `consequential hint` (initially false).

### Notas de estado (de búsquedas dirigidas, no del texto normativo)

- La spec vive en `document.modelContext`; una versión anterior usaba `navigator.modelContext`, que Chrome deprecó en Chrome 150. Ya no existen los helpers `provideContext()`, `clearContext()` ni `unregisterTool()`: un tool vive hasta que se dispara su `AbortSignal`.
- Origin trial pública en Chrome 149–156 (Chrome 149 desde junio); origin trial también en Edge 150, soporte experimental en Brave Leo, y soporte en ChatGPT Desktop. WebKit se opone; Mozilla es neutral.
- Repositorio e issues: github.com/webmachinelearning/webmcp (issues #146, #224, #227 abiertos sobre eventos `toolcanceled`/`toolactivated`, valores por defecto y ejecución entre documentos del mismo browsing context group).
