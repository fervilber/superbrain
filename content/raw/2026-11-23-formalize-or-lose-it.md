---
title: "Formalize or Lose It: qué controlan de verdad las restricciones ejecutables en un enjambre de agentes"
source: "https://discuss.huggingface.co/t/research-release-formalize-or-lose-it-experimental-results-on-executable-oversight-in-agent-swarms/192381 · https://doi.org/10.5281/zenodo.24292368"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# Research Release: Formalize or Lose It — Experimental Results on Executable Oversight in Agent Swarms (Hugging Face Forums, 23 nov 2026)

We are sharing the results of our recent research project, Formalize or Lose It, along with its preprint, implementation, experimental datasets, and reproducibility materials.

## What we accomplished

### 1. A systematic audit of multi-agent supervision

- Audited 84 oversight rules.
- Found that 39 (46%) existed only as natural-language prompt instructions.
- Among 23 requirements passed from Root to Workers, 19 lacked executable checks.

### 2. Fault-injection experiments

- Replayed 19 injected faults across 29 runs.
- The existing FBS implementation blocked all 10 plan and delivery faults.
- Six additional faults passed the existing 125-case test suite (2,599 assertions) and were accepted.
- Six additional Host-level checks caught five of those six previously undetected faults, with no false positives.

### 3. Controlled requirement-relay study

- Conducted approximately 1,150 model calls, using cached results for reproducibility.
- A supervisor relying on compressed notes approved 71% of deliberately flawed plans.
- A programmatically checked requirement ledger preserved formalized requirements across handoffs at approximately one-sixth of the input-token cost.
- Requirements omitted from the ledger remained outside its protection.

## Main contribution

Our results demonstrate both the practical value and the limitations of executable oversight in multi-agent systems.

Programmatic constraints can enforce formalized requirements more consistently than relying exclusively on natural-language supervision. However, requirements that are never formalized or incorporated into executable checks can still be missed.

This is not a claim of complete safety or universal reliability. It is an experimentally grounded investigation of the boundary between natural-language supervision and executable control.

## Abstract (preprint, Zenodo, publicado 2026-11-17)

Multi-agent systems distribute execution across agents, creating more opportunities for requirements to disappear during handoffs. We study how executable constraints can preserve coordination requirements while retaining room for model planning. Drawing on design by contract and runtime verification, we distinguish requirement transmission, plan selection, and host acceptance. We examine how check coverage determines the scope of control through a supervision inventory, fault injection in the Feasibility Scheduler (FBS), and a controlled requirement-relay study.

A recorded FBS run that passed all 125 tests carried 84 supervisory rules, of which 39 were communicated only through prompts. Of 23 rules passed from Root plans to Workers, 19 had no executable check. Across 19 planted faults, FBS blocked every plan and delivery fault but accepted six violations outside the effective coverage of its checks. Six additional host checks detected five of those six survivors. In the relay study, a reviewer with full notes corrected every final violation, whereas a reviewer using compacted notes approved 71% of flawed attempts. A ledger delivered requirements directly to the executor and maintained its covered predicates at about one sixth of the supervisory input tokens used by full-note review. Violations involving omitted requirements and unprotected conditional premises still passed acceptance.

Our central conclusion is that multi-agent oversight should rest on executable requirements held by the host. Models plan within the permitted space; the host determines which plans and deliveries can be accepted. Reliability depends on whether critical coordination rules reach execution and acceptance. Test pass rates therefore need to be interpreted alongside formalization coverage.

## Nota del equipo (respuesta en el hilo)

El arquitecto de FBS explica que su operador de factibilidad evalúa cada restricción requerida individualmente (1 si se satisface, 0 si no) y las multiplica: un plan es factible solo cuando todas las restricciones formalizadas se cumplen. Esto permite descomposición de tareas por dependencias preservando las restricciones de ejecución. Las 39 reglas "solo-prompt" se descubrieron auditando registros reales de ejecución, no se seleccionaron de antemano; representan brechas de cobertura, no 39 violaciones confirmadas.

## Artefactos abiertos

- Preprint (Zenodo, v8): Formalize or Lose It: What Executable Constraints Control in an Agent Swarm — DOI 10.5281/zenodo.24292368
- Código, datos y materiales de reproducibilidad: GitHub nimayshah123/dar-executable-constraints (Apart Research Swarm Alignment Hackathon, noviembre 2026)
- Implementación FBS: GitHub zionlinne/feasibility-scheduler
