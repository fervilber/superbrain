---
title: "Coati: Host-Grounded Execution for Installable Mobile GUI Agents (arXiv:2611.02644)"
source: "https://arxiv.org/abs/2611.02644"
date: 2026-11-02
captured: 2026-11-03
---

# Coati: Host-Grounded Execution for Installable Mobile GUI Agents

Yudou Ying, Pu Shi, Hanlei Shi, Yuhua Zheng — arXiv:2611.02644 [cs.MA], 2 de noviembre de 2026. Captura verbatim del abstract, introducción y secciones 2–3 (texto extraído vía `https://arxiv.org/html/2611.02644v1`).

## Abstract

Mobile GUI agents can carry out tasks across apps, yet most run on a separate computer that drives a phone over the Android Debug Bridge (ADB), out of reach of ordinary users and of the apps through which most people reach Web services. We present Coati, a source-available agent that users install as an Android app. Its runtime on the phone, the host, records what a model alone cannot see: the effect of each action at its target, result screens across apps, and the progress of repeated steps. VerifyLoop checks action outcomes and completion claims against host evidence and reports a completion it cannot audit as unverified. AppMemory builds per-app procedural memory from observations that the interface supports and reuses it on later visits. A routed fast executor lets a lightweight selection model take simple, confident steps and lets the host repeat loops of simple steps that the large model plans once. On all 116 AndroidWorld tasks, with Gemini 3.8 Flash as every agent's backbone, Coati succeeds on 86.5% of the tasks over three trials, ahead of the strongest open-source agent Artemis (77.6% with the same accessibility-only access, 76.5% even when allowed ADB) and far ahead of FinalRun and Midscene (about 59%), and VerifyLoop cuts false completion claims by about a third at comparable success. In everyday use, the fast executor cuts the median time of phone tasks by 39% at comparable success and runs three of four loop tasks 2.8–5.4x faster with 6–9x fewer model tokens, while AppMemory shortens a repeated deep route in an unfamiliar app from 18.5 steps to 6–7. On an Android 16 phone, routed execution completes all 27 benchmark runs with 76% fewer Reasoning calls on the critical path. Host evidence, not model self-assessment, makes an installable agent reliable and fast.

## 1. Introduction (extracto)

Multimodal large language models can now operate graphical user interfaces (GUIs) directly: they read a screenshot or an interface tree and act through taps, swipes and text entry. On mobile devices this matters more than anywhere else, because most applications expose no programmable interface and their layouts change across versions, languages and device states.

However, most mobile GUI agents run on a separate computer that drives the phone over the Android Debug Bridge (ADB). The computer sends actions to the phone and receives observations in return. For ordinary users, installing and operating such a system can be difficult. More importantly, the agent can understand the phone only through the information returned by the bridge. Therefore, it may miss fine-grained changes after an action, making it difficult to determine whether the action succeeded and whether the task actually reached its target state.

Running an agent directly on the phone also imposes practical requirements. Each step should avoid unnecessary waiting and model calls. Since users may not continuously monitor the screen, a task reported as complete must actually reach the requested state. Repeated tasks should not require the agent to rediscover the same route each time. Existing mobile GUI agents do not fully satisfy these requirements. They typically ask a large model to make decisions step by step, rely on the model to judge whether a task is complete, and treat repeated actions as separate model decisions. These choices can increase latency and token costs, while making execution failures more difficult to detect.

A mobile agent must therefore use local evidence not only to execute actions, but also to verify their outcomes, assess task completion, and retain useful experience. This calls for a different execution principle: the model may propose an action, but the runtime on the phone should determine what actually happened from evidence recorded by the host.

We present Coati, a source-available Android agent that users install as an app. Its core principle is _host-grounded execution_: the model proposes an action, while evidence recorded by the host—the information collected by Coati's runtime on the phone—determines the outcome.

## 3.1. Host evidence (formalización)

Throughout, _host evidence_ ε_t denotes what the agent records itself rather than receives from a model: the accessibility tree at the time of the action, pixel and text changes at and around the target, the last result screen of every application the task used, and the record of a delegated loop. V, the completion audit and A are all evaluated against ε_t.

## 2.2. Verification, Reflection and Experience (extracto)

Mobile-Agent-v2 and MobileUse use reflection to detect and recover from erroneous actions; VeriSafe Agent and V-Droid verify candidate actions before execution, and BacktrackAgent and VeriGUI study error recovery. These verifiers ask a model to judge the model's own progress. VerifyLoop decides with host evidence wherever it exists (pixel and text changes at the target, result screens across apps, loop progress) and uses a model only to read that evidence.

## 3.5. VerifyLoop: Verification-Driven Mobile Execution

Traditional Observe–Think–Act agents proceed to the next reasoning step immediately after issuing an action. A successful return from the Android interface only indicates that the operation was accepted; undetected failures, unexpected pop-ups, and page drift may propagate, and repeated attempts under an unchanged interface may lead to unproductive loops. VerifyLoop extends execution to Observe–Think–Act–Verify and converts verification outcomes into control signals.

El veredicto V(ot, at, et, ot+1) toma uno de cinco valores y cada uno mapea a una decisión de control distinta:

- **SUCCESS** — la transición esperada se observa. Continuar desde el nuevo estado.
- **FAILED** — la acción es inefectiva o falta el estado esperado. Devolver feedback de fallo y replanificar.
- **DRIFTED** — la ejecución entra en un estado incompatible con la tarea. Recuperar desde el estado observado o terminar.
- **UNEXPECTED** — la interfaz cambia de forma distinta a la predicción. Continuar razonando desde el estado observado.
- **UNKNOWN** — la evidencia disponible es insuficiente. Re-observar sin asumir éxito.

Failure-aware stopping: an action that keeps failing on the same target must stop, but a loose criterion ends tasks that are still progressing. VerifyLoop counts the _consecutive_ failed attempts of the current action; waits and screenshots neither count toward nor reset the run, while any successful action resets it.

Completion assessment: when a route claims completion, VerifyLoop runs a bounded audit with a Fast model. It compares the current screen, the last result screen from every other application used, and any delegated-loop record against the values specified by the task. A rejected claim returns to execution and sends the reason to the Reasoning route; an unavailable audit ends the task with an explicit unverified status rather than plain success.

## 3.4. Routed Execution (pre-commit gate)

Because the selector treats background guidance as a hint, it may commit a form whose values are not all set. Before tapping a button whose label denotes a commit (submit, save, send, export, confirm, pay), Coati asks the Fast model once whether the screenshot shows every value the task requires; if not, the step is escalated with the missing value named.

## Case study (Appendix D.3)

Task O1 asks to choose an item in a native order form, set a painted stepper to three copies, turn on a painted toggle, fill two native text fields, and submit. In one routed phone run, the selector left the stepper at two copies, completed the rest of the form and chose _Submit order_. Before the tap, the pre-commit gate asked the Fast model whether the screen satisfied the task and received "Copies is set to 2 instead of 3". The escalated Reasoning step tapped "+" once more, its verification confirmed three copies, and the order was submitted with the requested values. Without the gate, only the completion audit could have caught the wrong order, after the fact.

## Contribuciones declaradas

1. A host-grounded execution framework for mobile GUI agents. The framework uses host evidence, rather than model self-assessment, to decide if an action succeeded, if a task was completed, and what is worth remembering.
2. Three core mechanisms: VerifyLoop, AppMemory, and a routed fast executor with loop delegation.
3. An evaluation that distinguishes benchmark capability from everyday use.
