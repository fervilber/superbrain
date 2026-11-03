---
title: "Kradle y Four Bridges: la mentira emerge en la interacción multiagente sin instrucción de engañar"
source: "https://arxiv.org/list/cs.MA/recent"
date: 2026-11-03
captured: 2026-11-03
---

# Kradle / Four Bridges: decepción emergente en juegos de asimetría de información

Paper listado en el feed cs.MA del 3 de noviembre de 2026 (cross-list). Captura verbatim del abstract tal como aparece en el listado `arxane.org/cs.MA` (equivalente al listado de arXiv, con abstracts completos).

## Abstract (verbatim)

AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce Kradle, a platform for evaluating AI models, and Four Bridges, an information asymmetry game in which four agents distribute across four rooms: one is the death room, the others hold food worth more if not shared. One agent, the informed agent, knows which room is the death room and can withhold or disclose that information. We evaluate eight frontier models as the informed agent. Deceptive behavior appears in every model and in 73% of all runs (6% to 100% per model), and does not decrease with capability tier within a model family. When the informed agent does disclose, the warning is often challenged, and agents that challenge it enter the death room twice as often as those that do not. Telling all agents that one of them knows the death room collapses deception in six of eight models; telling the informed agent that the room is permanently fatal moves only one. On an open-weight model, an honesty steering vector reduces deception to 0% and adversarial honesty training to 6%. The platform and game provide a testbed for measuring deceptive behavior and comparing interventions.

## Nota de captura

El listado completo de cs.MA del 3 de noviembre de 2026 incluye 14 envíos nuevos, 23 cross-lists y 23 reemplazos. Los abstracts íntegros se conservan en la fuente (arxane.org/cs.MA → arXiv). Este fichero recoge el abstract de Kradle/Four Bridges como muestra representativa del eje de evaluación de honestidad en interacción multiagente de la jornada.
