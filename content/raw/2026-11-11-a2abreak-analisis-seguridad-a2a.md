---
title: "A2ABreak: Systematic Security Analysis of the A2A Protocol (arXiv 2609.10871)"
source: "https://arxiv.org/abs/2609.10871"
date: 2026-10-24
captured: 2026-11-11
---

# A2ABreak: Systematic Security Analysis of the A2A Protocol

Autores: Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim, Elisa Bertino. Publicado 2026-10-24.

## Abstract

The Agent2Agent (A2A) protocol, now governed by the Linux Foundation, is an open standard that enables autonomous AI agents to discover, authenticate with, and delegate tasks to one another across organizational boundaries. Designed to complement the Model Context Protocol (MCP) for tool integration, A2A is rapidly emerging as the horizontal communication layer of the multi-agent ecosystem. Yet the protocol's security has received no systematic analysis.

This paper presents A2ABreak, the first rigorous systematic security analysis of the A2A protocol. We introduce a novel framework that utilizes an LLM-assisted extraction of a verified finite-state machine directly from the natural-language specification, producing a unified model of 37 states and 76 transitions from 929 formalized statements, and then systematically reasons over this model to discover protocol-level vulnerabilities through adversarial verification, under a full-compliance assumption.

Our analysis uncovers 11 new vulnerabilities, each exploitable by a specification-compliant adversary without requiring any implementation flaw. Among the findings are cross-client context injection through unprotected context identifiers, credential harvesting via multi-hop identity loss in delegation chains, and data exfiltration through rogue agents advertising unattested capability claims.

A2ABreak achieves 73.3% precision and 84.6% F1 against manual expert review, while a zero-shot LLM baseline operating over the same specification produces zero confirmed findings, demonstrating that explicit formal grounding is essential for sound protocol security analysis.

## Contexto complementario (agenticcyber.co, 9 nov 2026 — A2A Protocol Security)

Key takeaways:

1. Gap: A2A standardises the handoff between agents but leaves identity of the person, trust in replies and delegation limits to the implementer.
2. Core insight: A signed Agent Card proves origin and integrity, not honesty, so approve remote agents like vendors instead of trusting what discovery finds.
3. Evidence: The A2A project's enterprise guidance and its specification. No dependable data on attacks against A2A in the field, so none is claimed, and no SDK was run.

Whose request is it? Transport authentication names the calling client. It does not name the person or system that client acts for, or confirm that anyone approved this task. When the remote agent works on a user's data, send the user's context explicitly and verify it. RFC 8693 token exchange can say a party is acting for another through an actor claim, leaving the chain readable; the patterns appear in OAuth for AI agents.

Recomendaciones: HTTPS y certificados validados; verificar credenciales en cada petición; cada agente con su propia identidad; autorizar habilidad por habilidad con mínimo privilegio; para tareas delegadas, llevar y verificar el contexto del usuario; tratar lo que devuelve un agente remoto como entrada no confiable; limitar la profundidad de delegación; almacenar logs fuera del alcance de los agentes; registrar cada agente externo y conservar un medio para cortarlo.

Agent Card signing is a useful control and also an easy one to over-read. A valid signature tells a client the card was issued by the claimed provider and has not been altered (A2A specification). It tells you nothing about whether that provider's agent is honest, competent or safe with your data. Production A2A flows should not trust agents they discover at run time: treat a new remote agent the way you treat a new vendor.
