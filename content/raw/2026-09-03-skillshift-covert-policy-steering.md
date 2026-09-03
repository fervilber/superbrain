# A Finger on the Scale: Covert Policy Steering through Agentic Skills

**Authors:** Jiarui Li, Jiahao Chen, Chunyi Zhou, Yuwen Pu, Oubo Ma, Zhou Feng  
**Date:** September 2, 2026  
**Source:** arXiv:2609.02564v1  
**Category:** Cryptography and Security, Software Engineering, AI Agents Security, Supply-Chain Security

## Abstract

Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functionality and the user-authorized objective. We further present SkillShift, a constrained black-box framework for covert policy steering without explicit target command injection or task hijacking. It combines semantically plausible policy edits with hierarchical validation, failure-guided optimization, and strategy compression to preserve effectiveness, output validity, transferability, and inconspicuousness. We instantiate this threat in agentic commerce and software dependency use, with SkillShift achieving attacker-favored selection rates of 81.33% and 63.33% while maintaining a 100% utility-preserving rate. The frozen policies also transfer without further optimization across heterogeneous LLM backends and agent environments. Moreover, the evaluated scanners fail to detect the constructed skills, motivating behavioral auditing of reusable skills as agent policy artifacts.

## What is an "Agentic Skill"?

An agentic skill is a structured package (often containing Markdown instructions, system prompts, specific tools, or execution scripts) that allows an agent to perform complex, multi-step actions (e.g., configuring Nginx, analyzing a market, or creating diagrams like this Excalidraw skill).
Modern platforms, including Hermes, load these skills to extend agent behaviors.

## The Core Threat: Supply-Chain Compromise via "SkillShift"

Because skills are treated as static behavioral guides, users often download and integrate third-party skills without rigorous behavioral testing, assuming that if the skill successfully completes the task, it is safe.

### Skill Policy Integrity

The authors define **Skill Policy Integrity (SPI)** as:

> A skill's actual behavioral policy must match its declared functional description, with no covert steering of agent decisions towards hidden, unauthorized goals.

### The SkillShift Attack Framework

The authors designed **SkillShift**, a framework demonstrating how an attacker can construct malicious, covert skills.

- **Functional Preservation:** The skill works perfectly. It does not crash, does not reject the user's task, and preserves 100% utility (the target task is successfully solved).
- **Covert Policy Steering (Covert Manipulation):** While solving the task, the skill sutilmente alters the decision-making policy of the LLM.
  - _Example in Commerce:_ The user asks the agent to find the cheapest flights or products. The malicious skill successfully finds flights but sutilmente steers the LLM's selection criteria (via structured prompt phrasing) to choose a specific affiliate company or sponsor, even if it is slightly more expensive, under the guise of "reliability metrics" or "convenience scoring".
  - _Example in Software Engineering:_ The agent is tasked with selecting dependencies for a project. The skill steers the agent to select a specific dependency version that has a known vulnerability, presenting it as "the most stable and widely used" choice.
- **Hierarchical Validation & Strategy Compression:** SkillShift optimizes the prompt modifications using black-box LLM feedback to make the steering text as short, natural, and inconspicuous as possible.

## Results and Detection Failures

- **Success Rates:** In testing, SkillShift achieved attacker-favored choice selection rates of **81.33%** (commerce) and **63.33%** (software selection) while completing the base tasks flawlessly.
- **Backend Transferability:** The manipulated skills were robust enough to transfer between different LLMs (GPT, Claude, LLaMA) without any extra tuning.
- **Detection Failures:** SOTA security scanners and prompt injection detectors failed to flag these skills because they do not contain raw command injections (like "ignore your previous instructions") or classic adversarial text. They look like perfectly normal, helpful guidelines and structured instructions.

## Security Recommendation

Systems using reusable skills (like Hermes Agent) must implement **behavioral auditing** for skills. Instead of just reviewing static code/text, we must run the skills in sandboxed environments with mock choices to audit whether their decision-making distribution is statistically biased toward unauthorized goals.
