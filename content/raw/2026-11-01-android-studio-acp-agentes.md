---
title: "Android Studio Rabbit 2 y Bring Your Own Agent: 40+ agentes de código sobre el Agent Client Protocol — captura"
source: "https://thenewstack.io/android-agents-build-debug"
date: 2026-10-28
captured: 2026-11-01
---

# Android Studio Rabbit 2: Bring Your Own Agent sobre el Agent Client Protocol (ACP)

> Captura del análisis de The New Stack (28-oct-2026), complementado con la descripción técnica del Agent Client Protocol publicada por DEV Community y con el anuncio de Google/Android Studio. El evento es Android Dev Summit; la release estable es Android Studio Rabbit 2.

## El anuncio (verbatim de The New Stack)

> The company's Bring Your Own Agent feature now supports more than 40 coding agents that speak the open Agent Client Protocol, among them Anthropic's Claude Agent, OpenAI's Codex, and Google's own Antigravity, and Google says the feature is now stable in Wednesday's release of Android Studio Rabbit 2.

> In a Wednesday post, Adarsh Fernando, senior product manager for Android developer tools, describes the goal as giving developers and their agents "the tools and knowledge to build high-quality Android apps faster."

> The push spans Android Studio and the terminal-based Android CLI, with Google opening both to third-party agents rather than steering developers toward Gemini. Matthew McCullough, vice president of product for Android, has emphasized giving developers the freedom to choose their own models and coding agents.

## Qué obtiene el agente dentro del IDE (extracto)

> The pitch is that the agent gets the IDE's knowledge of your project. Google lists "a deep understanding of your project structure and build, symbol resolution, Compose Preview rendering, the Emulator, Logcat, and more".

> > agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results.

## El protocolo (extracto de DEV Community)

> The plumbing is the Agent Client Protocol, which "standardizes communication between code editors/IDEs and coding agents." Local agents run as subprocesses of the editor and talk "via JSON-RPC over stdio", per the ACP site. That is why one integration can cover 40 agents: Android Studio speaks the protocol, and any agent that speaks ACP, natively or through an adapter, can plug in.

> The Rabbit 2 release post names four of the 40-plus agents: Claude Agent, Codex from OpenAI, Junie and Google Antigravity, and says any "ACP compliant agent" works. The Decoder reports they can run at the same time.

## Depuración de memoria y producción (extracto)

> In one demo, Claude Code worked with LeakCanary, an open source leak-detection library, to check critical user journeys for memory leaks using a single instruction from the developer. Claude Code ran the journeys across multiple devices in parallel, analyzed heap dumps through the CLI's LeakCanary integration, and traced the leaks back to the offending code. […] Google says the tooling helped capable models complete these investigations nearly twice as fast while using up to 25% fewer tokens.

> A companion `android signals` command now pipes Android vitals and Firebase Crashlytics data into the same terminal workflow, which gives agents a direct line to production crashes, ANRs, and memory problems, but none of this retires the human in the loop.

> > autonomous bug-finding can outrun autonomous bug-fixing — an Anthropic scanner flagged some 29,000 possible vulnerabilities in open-source code while only a few hundred were ever fixed.

## Android Bench 2.0 (extracto)

> Google is also introducing Android Bench 2.0 to evaluate how models and agent harnesses perform on more complex Android development tasks. It tests whether completed apps actually run with assignments ranging from building an app from mockups to migrating an existing interface. Some tasks are modeled on work that would take an Android engineer several days, and the benchmark also measures completion time and cost.

## Flujo de adopción (verbatim del anuncio de Android Studio)

> Open the agent window or Settings > Tools > AI > Agents, select an agent, then authenticate. Access and costs depend on the provider.
