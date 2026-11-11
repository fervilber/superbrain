---
title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth (DeepMind)"
source: "https://deepmind.google/blog/introducing-alphaproof-code/"
date: 2026-11-10
captured: 2026-11-11
---

# Introducing AlphaProof Code: a breakthrough in verifying complex software at depth

Autores: Pushmeet Kohli y Swarat Chaudhuri. Publicado el 10 de noviembre de 2026 (Research).

How Google DeepMind researchers built a new agentic framework that formally verified the code of Signal's cryptographic protocol — long considered to be a grand security challenge.

Today, we're sharing a milestone in software security long considered to be a grand challenge: Google DeepMind researchers guided AI agents to mathematically prove key security properties of the actual code underlying the Signal protocol, the technology that protects billions of private conversations in apps like Signal and Google Messages.

This breakthrough discovery was made using AlphaProof Code, a novel agentic framework for formal verification at unprecedented depth that combines human expertise with AI agents. Formal verification—mathematically proving code runs correctly without flaws—is the highest standard of security assurance; however, it is difficult and often labor-intensive.

Our work marks the first time AI has been used to formally verify a widely deployed cryptographic protocol at this depth. It's also the first time the implementation of a widely deployed protocol like this has been formally verified by any method, with or without AI.

## How we verified Signal

AlphaProof Code is a multi-LLM agentic framework that splits the work of formal verification the way a research team would: human experts work with AI to decide what to prove, and a group of AI agents does it.

First, our researchers collaborated with a mix of models to translate Signal's security goals into formal mathematical specifications, with human experts reviewing every one. From there, agents powered by Gemini Carbon did the proofs, generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code.

Next, the agents audited the proof and highlighted areas that needed a second look by a human – just one percent of the codebase, a massive time savings. Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most.

Cryptographic protocols underpin nearly all digital communication, from online banking to web browsing, and a single flaw can expose millions of people at once. That's why experts have spent decades formally analyzing them.

But most protocol verification stops at the design level. Our agents went further, proving that the compiled code fulfills the key security properties – such as keeping messages protected before and after a device is temporarily compromised – down to the exact code running on devices. Because real-world vulnerabilities often hide in the gap between design and implementation, bridging this gap makes these proofs vastly more complex.

Even at this complexity, our verification process took just four weeks – a task that historically takes expert teams years – proving that Signal's core cryptographic code delivers the security protections our experts specified.

To confirm that AlphaProof Code can tell correct code from buggy code, we reintroduced two real, previously fixed bugs into an isolated version of Signal's code. In both cases, the system produced a machine-checked proof that the buggy version was insecure.

In AlphaProof Code, AI agents help users write a specification, then autonomously prove that the implementation meets it. Every proof is checked by Lean to verify the agents' work.

## Fragmentos del paper (Formal Verification of Signal 4.pdf)

We introduce AlphaProof Code, a multi-agent AI framework for formal software specification and verification that we used to prove key security properties of libsignal, the Signal protocol's reference implementation, at the machine-code level. AlphaProof Code consists of a human-guided agent for writing Lean specifications of code, a formal semantics of AArch64 machine code, and a team of autonomous prover agents whose proofs are accepted only if Lean's kernel checks them against the approved specification.

Applied to libsignal, our agents generated about 6.5 million lines of machine checked Lean proof code, resting on about 26,000 lines of trusted specifications and AArch64 semantics. The proofs cover Signal's post-quantum PQXDH handshake and Triple Ratchet, establishing forward secrecy, authentication, post-compromise security, and handshake secrecy. They are the first proofs connecting protocol-level security guarantees to the unmodified code of a widely used cryptographic protocol implementation.

AlphaProof Code is a framework for human–AI collaboration on the formal specification and verification of real-world software. The framework is based on a simple principle: The majority of human effort in software verification now lies in engineering the specification, the formal statement that is proved and its assumptions about how the machine code executes. Previously, the expertise and labor required to write proofs was a bottleneck to large-scale formal verification, but this is no longer the case. As we demonstrate, even large proofs about software can be written by teams of AI agents once a specification is fixed, and the proof agents can work autonomously: since the proof is ultimately checked by the Lean kernel, the reliability of the results does not depend on the reliability of these proving agents.

Componentes (Figura 1):

1. Specification writing: a specification-writer agent drafts trusted theorems and definitions under close guidance from the user. A pool of reviewer agents checks that a draft is faithful to its sources and to the implementation. The user reviews, revises, and approves the specification before any proofs are written, and its git commit becomes the baseline that the gatekeeper later checks proofs against.
2. Machine-Code Semantics: the theorems are stated over a formal semantics of user-mode AArch64 Linux, written in Lean. The semantics takes an executable (an ELF binary) as a list of bytes and describes all of its possible runs as a relation between inputs and outcomes.
3. Proof Synthesis: proofs are produced autonomously by a team of agents with distinct roles, each defined by a skill. An orchestrator divides up the work and schedules agents but never edits Lean files itself. Each subtask is assigned to a proof worker. The orchestrator groups workers under team leads; an architect designs the high-level decomposition; an integrator merges verified proofs into library modules. In our proof campaigns, a team typically had 40 to 80 agents and ran on a single machine for 24 to 72 hours.
4. Gatekeeping: a proof is accepted only if it proves exactly the statements the user approved. The gatekeeper is an agent used during development to check recorded approvals for specification amendments and to call the standard comparator tool to check the proof.

## Cobertura (The Register, 10 nov 2026)

Google DeepMind researchers have completed a formal verification of Signal's messaging security, marking what they claim is the first time AI has helped devise a proof that links protocol-level security guarantees to a widely used cryptographic implementation. In this instance, AlphaProof Code verified Signal's post-quantum PQXDH handshake and Triple Ratchet, thereby validating the design of libsignal's forward secrecy, authentication, post-compromise security, and handshake secrecy. The result is theoretical in that it assumes perfect cryptography and doesn't guarantee the computational secrecy of bytes. But it's still a meaningful assertion of correctness.

## Limitaciones (Piotr Sobolewski, sysnote.net)

- Alcance: la mensajería de grupo, el estado multi-dispositivo y los ataques de canal lateral quedan fuera; la app Signal es mucho más que libsignal.
- Supuestos: las rutinas criptográficas de bajo nivel no se verifican, sólo se describen mediante contratos que hay que confiar, igual que la semántica de AArch64 y las propias especificaciones.
- Computación cuántica: la parte computacional de la prueba no da garantías frente a un atacante cuántico. El secreto del acuerdo de claves frente a un futuro ordenador cuántico sólo se mostró en el modelo simbólico, que asume criptografía perfecta.

Repositorio público: https://github.com/google-deepmind/code-verification (Lean 4 v4.34.0, Rust 1.98.1, verificación con leanprover/comparator).
