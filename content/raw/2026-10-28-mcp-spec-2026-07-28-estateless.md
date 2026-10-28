---
title: "Especificación MCP 2026-07-28: núcleo sin estado, MRTR, enrutado por cabeceras y endurecimiento de autorización"
source: "https://blog.modelcontextprotocol.io/posts/2026-07-28"
author: "David Soria Parra y Den Delimarsky (mantenedores principales de MCP)"
date: 2026-07-28
captured: 2026-10-28
---

# Captura: la especificación MCP 2026-07-28 (documento de referencia)

> Documento fundacional reutilizado como base técnica del informe del 28 de octubre de 2026. Es la revisión más grande del protocolo desde su lanzamiento y explica por qué la gobernanza de agentes de los anuncios de esta semana puede apoyarse en cabeceras HTTP y autorización por intención.

## The 2026-07-28 Specification

The 2026-07-28 Model Context Protocol specification is out, bringing a stateless protocol core, Multi Round-Trip Requests, header-based routing, cacheable list results, authorization hardening, a formal extensions framework, and updated Tier 1 SDKs.

Since our last November release MCP continued to grow at an astonishing rate. Across our Tier 1 SDKs, we're seeing close to half-a-billion downloads a month, with both TypeScript and Python SDKs crossing the 1 billion total downloads threshold. In just a few months, the protocol continued to grow as the data and interactivity substrate for agentic workflows.

Today, we're officially pushing the release button on the next version of the MCP specification, `2026-07-28`, along with the SDKs that will allow you to start building clients and servers right away.

The highlight of this release is a stateless protocol core - MCP is transforming from a bidirectional stateful protocol into a request/response stateless protocol. It was one of the most highly-requested features from developers who were eager to get better reliability and scalability for their MCP servers.

There is, of course, more to what we're introducing with this version:

- Every request is self-describing, with an optional discovery call for clients that want capabilities up front, so any request can land on any instance behind a plain round-robin load balancer.
- Method and tool names travel in the `Mcp-Method` and `Mcp-Name` HTTP headers, so gateways can route and authorize on headers directly.
- Server-to-client requests for things like sampling and elicitation are being redesigned to use Multi Round-Trip Requests (MRTR), removing the need for constantly open bidirectional streams.
- List responses carry cache hints and a deterministic order, so clients can cache tool catalogs and keep upstream prompt caches stable across reconnects.
- Formally locking in on a proper extensions framework, with Tasks joining other extensions, such as MCP Apps and Enterprise Managed Authorization (EMA).
- A set of authorization hardening changes including RFC 9207 issuer validation and a formal shift away from Dynamic Client Registration (DCR) toward client metadata documents (CIMD).
- A formal deprecation policy with a twelve-month minimum window so you can plan upgrades instead of reacting to them.

The TypeScript, Python, Go, and C# SDKs are updated to match, with detailed migration notes for the breaking bits.

### No handshake or sessions

With the new spec version, we've officially retired the `initialize`/`initialized` exchange along with the `Mcp-Session-Id` header (SEP-2575, SEP-2567). Each request now travels on its own, carrying its protocol version, client identity, and client capabilities in `_meta`. If a client wants to learn a server's capabilities before doing anything else, there's a new `server/discover` RPC for that; however, it is not required. Any request can now land on any server instance behind a plain round-robin load balancer without needing shared storage.

```
POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"search","arguments":{"q":"otters"},
 "_meta":{"io.modelcontextprotocol/clientInfo":{"name":"my-app","version":"1.0"}}}}
```

Dropping the protocol-level session doesn't force your application to be stateless. If your server needs to carry state across calls, mint an explicit handle from a tool and have the model pass it back as an argument. We found this works better than session state hidden in the transport - the model can see the handle and thread it between tools.

### Multi Round-Trip Requests (MRTR)

MRTR replaces the server-initiated `elicitation/create`, `sampling/createMessage`, and `roots/list` requests that previously required a held-open stream.

Sometimes a tool needs something from the user mid-call, such as a confirmation or a missing parameter. MRTR (SEP-2322) enables this scenario over a stateless protocol: the server returns `resultType: "input_required"` along with the requests it needs answered, and the client retries the original call with the answers attached in `inputResponses`.

### Header-based routing

Streamable HTTP requests now must include `Mcp-Method` and `Mcp-Name` (SEP-2243). Your gateway, rate limiter, or WAF can route and meter on those headers instead of parsing JSON bodies.

### List results are cacheable

Responses from `tools/list`, `prompts/list`, `resources/list`, and `resources/read` now carry `ttlMs` and `cacheScope` (SEP-2549).

### Authorization

- Authorization servers should return the `iss` parameter per RFC 9207, and clients must validate it before redeeming a code (SEP-2468). This closes an authorization-server mix-up hole.
- Clients set `application_type` during Dynamic Client Registration (DCR) so authorization servers stop rejecting `localhost` redirects for desktop and CLI apps (SEP-837).
- Client credentials are bound to the issuer that minted them. No reuse across authorization servers (SEP-2352).
- Dynamic Client Registration itself is now formally deprecated in favor of CIMD. DCR continues to work for backward compatibility, but will be removed in a future version of the MCP spec.

### Tasks

Tasks move out of the experimental core and into the `io.modelcontextprotocol/tasks` extension, with a poll-based `tasks/get` and a new `tasks/update` (SEP-2663). Change notifications move from the old HTTP GET endpoint to a single `subscriptions/listen` stream that clients opt into per notification type.

### Deprecations

Roots, Sampling, and Logging are deprecated (SEP-2577). They still work, and they'll keep working for at least twelve months. New implementations shouldn't adopt them. The legacy HTTP+SSE transport is also considered to be officially deprecated, with a year-long offramp.

### SDKs

All four Tier 1 SDKs speak `2026-07-28` as of today: TypeScript, Python, Go, C#. Beyond the Tier 1 set, the Rust SDK supports the new spec in beta.

### Notas del capturador

- El cambio de fondo: **cada petición es autodescriptiva**. Versión de protocolo, identidad del cliente y capacidades viajan en `_meta` en cada llamada, lo que elimina el estado de sesión en la capa de transporte y permite balanceo round-robin puro.
- `Mcp-Method` y `Mcp-Name` en cabeceras habilitan que un gateway o WAF **enrute, limite y autorice sin parsear el cuerpo JSON**; es la base técnica sobre la que se puede montar un plano de control de seguridad de agentes.
- La deprecación de Roots, Sampling y Logging, junto a la migración de Tasks a extensión, confirma la estrategia de núcleo mínimo más extensiones formales (Tasks, MCP Apps, Enterprise Managed Authorization).
- Ventana de deprecación mínima de doce meses: la evolución del protocolo deja de romper integraciones sin aviso, requisito para adopción empresarial.
