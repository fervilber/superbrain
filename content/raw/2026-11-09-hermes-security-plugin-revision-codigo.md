---
title: "Captura: hermes-security — el plugin oficial de revisión de seguridad de Hermes Agent"
source: "https://hermes-ai.net/news/nous-research-s-hermes-agent-now-traces-real-attack-paths-in-your-code/"
date: 2026-11-08
captured: 2026-11-09T20:09:00+01:00
---

# Nous Research's Hermes Agent Now Traces Real Attack Paths in Your Code

Hermes AI News · Nous Research · Nov 8, 2026, 6:47 PM

## Takeaways

- Nous Research released `hermes-security`, an official Hermes Agent plugin for local repo security review.
- Parallel subagents build a threat model, chunk the code, and trace attacker reachability before reporting.
- Optional test confirmation writes exploit reproductions and runs them in a temporary copy of the repo.
- Standard, deep, and diff modes; invoke via chat, `/security`, or `hermes security-review` CLI.
- Exports to Markdown, JSON, CSV, and SARIF, with findings, rejected candidates, and coverage gaps preserved.
- Apache-2.0, needs Hermes 0.21.5+ and Python 3.11+; source on GitHub.

Nous Research has released `hermes-security`, an official plugin that turns Hermes Agent into a repository-level security reviewer. It reads the code, builds a threat model, traces attacker-controlled input to candidate vulnerabilities, and can write and run a reproduction.

Static application security testing, or SAST, analyzes source code without requiring a running application. Many scans still surface risky patterns that lack an attacker-reachable path. Hermes centers its review on that reachability question, which can reduce false positives and provide stronger evidence for findings that survive verification.

## How Hermes maps the attack surface

Once pointed at a local repository, Hermes identifies entry points and trust boundaries, then assigns parallel subagents to inspect the code. Those reviewers find candidates, compare them with the surrounding implementation, and trace whether untrusted input can reach the flagged operation.

Hermes divides folders into chunks of about 4,000 lines, sized as one reviewer's working set. Up to 10 chunk reviewers run concurrently, while an additional reviewer examines the broader scope for cross-cutting entry points and trust boundaries.

## Three modes set the review budget

| Mode     | Scope and behavior                                                                                                                                                                                                                      |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard | Reads all production code when the scope fits within 90 chunks, or about 360,000 lines. Larger repositories prioritize files associated with routes, request input, shell commands, SQL, deserialization, authentication, and webhooks. |
| Deep     | Removes the standard scan's skip list and makes independent passes over the entire repository. The default is three passes.                                                                                                             |
| Diff     | Reviews uncommitted work or compares the current branch with the default branch.                                                                                                                                                        |

## A finding needs a reachable path

Each candidate proceeds through code-level and reachability checks before Hermes reports it with a severity.

## Reports retain the audit trail

Every report records supporting evidence, rejected candidates, and coverage gaps. Results can be exported as Markdown, JSON, CSV, or SARIF, and Hermes Desktop provides a dedicated Security page for reviewing them. Checkpointed state allows interrupted or crashed scans to resume from a new message or the Continue scan button. Unreviewed code and reviewers that failed to return results remain visible as coverage gaps. A report with zero findings and partial coverage leaves those paths unresolved.

The Apache-2.0-licensed plugin lives in the official plugin repository and requires Hermes 0.21.5 or later with Python 3.11 or later. Installation uses one command:

- Chat: Ask Hermes to `scan this repo for security issues`.
- Slash command: Run `/security`.
- CLI: Run `hermes security-review`.

## Where Hermes fits in the stack

Hermes packages threat modeling, parallel review, reachability analysis, optional exploit execution, and SARIF export into the first official Nous plugin aimed at SAST workflows. Its staged pipeline gives model-generated findings explicit checkpoints before they reach a triage system. Teams already using Snyk, Semgrep, or human diff review can add Hermes as another reviewer that traces exploitability and, when permitted, attempts a reproduction. SARIF output allows confirmed and unconfirmed findings to enter existing security workflows.

## Detalles de privacidad y límites (del marketplace oficial)

- El primer escaneo descarga una release fijada de `osv-scanner` (~55 MB, rechazada si su SHA-256 no coincide) en la carpeta de datos del plugin; los nombres y versiones de paquetes se envían a api.osv.dev y api.deps.dev, y las versiones declaradas de runtime a endoflife.date (`HERMES_SECURITY_DEPENDENCY_CHECK=off` lo desactiva).
- La confirmación por tests ejecuta código del repositorio como tu usuario en una copia temporal con las variables de entorno que parecen credenciales eliminadas; **eso no es un sandbox**.
- Probar una app en ejecución exige un permiso por escaneo (un origen, una hora, 200 peticiones) que las herramientas del agente no pueden emitir.
- Con `plugins.entries.hermes-security.allow_gateway_injection` activado (por defecto off), el plugin encola un mensaje "Continue security scan" cuando un escaneo se atasca, como máximo 3 veces sin progreso. Sin dependencias de Python.
