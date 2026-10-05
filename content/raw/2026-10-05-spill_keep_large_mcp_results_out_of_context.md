---
title: "Spill — Keep large MCP results out of context"
source_url: "https://spill-ai.github.io/spill/"
date: 2026-10-05
---

# Spill — Keep large MCP results out of context

Source: https://spill-ai.github.io/spill/

Open source · Apache-2.0

# Keep large MCP results

out of context

Spill intercepts oversized MCP tool responses and stores them as local DuckDB tables. Your AI agent gets a compact descriptor and runs SQL instead of reading 50,000 tokens of raw JSON.

Install [Documentation](docs.html) [ GitHub ](https://github.com/spill-ai/spill)

GitHub MCP → 18,412 issues → Spill → DuckDB table → compact descriptor

↑

spill.query('SELECT state, COUNT(\*) GROUP BY state')

Why Spill

## Everything stays local, nothing changes in your workflow

⚡

### Automatic interception

Hook fires on every MCP PostToolUse event. Payloads under 32 KiB pass through untouched.

🗄️

### Local DuckDB storage

Rows land in `~/.spill/spill.duckdb`. No cloud account, no embeddings, no infrastructure.

🔍

### SQL over any result

Filter, aggregate, join. DuckDB runs read-only with external access disabled.

🔒

### Read-only by design

Keyword validator + connection-level read-only mode. Mutations are blocked at two layers.

🔌

### Three clients

Cursor, Codex, and Claude Code. One install command per client, fully reversible.

📦

### Homebrew tap

One-line install. No separate tap repo needed — this repo doubles as the tap.

Installation

## Up and running in two commands

Homebrew builds Spill from source with embedded DuckDB. The first build takes a few minutes; upgrades are instant.

Terminal Copy

    $ brew tap spill-ai/spill https://github.com/spill-ai/spill
    $ brew trust --formula spill-ai/spill/spill
    $ brew install spill
    $ spill install cursor   # or: codex  claude

Restart your client after install to load the MCP server and hooks. Use `spill uninstall cursor` to remove — unrelated config is never touched.

| Client      | MCP config             | Hook config               |
| ----------- | ---------------------- | ------------------------- |
| Cursor      | `~/.cursor/mcp.json`   | `~/.cursor/hooks.json`    |
| Codex       | `~/.codex/config.toml` | `~/.codex/hooks.json`     |
| Claude Code | `~/.claude.json`       | `~/.claude/settings.json` |

How it works

## What gets spilled

Serialized tool output must be at least **32 KiB** and contain a nonempty array of JSON objects. Three payload shapes are supported:

Direct JSON array

MCP text block containing a JSON array

`structuredContent` array

Errors — pass through

Binary / mixed blocks — pass through

Under 32 KiB — pass through

Columns are inferred as `BOOLEAN`, `BIGINT`, `DOUBLE`, or `VARCHAR`. Nested objects, arrays, and mixed types are stored as JSON text. Missing values become SQL NULL.

sql Query your data

    -- Agent receives a compact descriptor, then queries directly
    SELECT state, COUNT(*) AS n
    FROM  spill_list_issues_a81f32
    GROUP BY state
    ORDER BY n DESC;

## Query policy

Only `SELECT`, `WITH`, `SHOW`, `DESCRIBE`, and `EXPLAIN` are allowed. A SQL tokenizer rejects mutations, multiple statements, and semicolons mid-query. Independently, DuckDB opens in **read-only mode** with external access and extension loading disabled.

500 row cap

32 KiB output cap

No network calls at runtime

No daemon or background service

CLI Reference

## Commands

bash

    # Dataset management
    spill list
    spill describe spill_list_issues_a81f32
    spill sql 'SELECT state, count(*) FROM spill_list_issues_a81f32 GROUP BY state'

    # Hook and MCP server (normally launched by the client)
    spill hook cursor    # also: codex, claude — reads one JSON event from stdin
    spill mcp            # stdio MCP server

    # Install / uninstall
    spill install cursor
    spill uninstall cursor

The MCP server exposes `query`, `list`, and `describe`. Query responses have `columns` and `rows` in column order. [Full documentation →](docs.html)
