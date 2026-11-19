---
title: "Meet Shepherd, the Meta-Agent Keeping Rogue AI In Check (IEEE Spectrum)"
source: "https://spectrum.ieee.org/ai-agent-manager"
date: 2026-11-19
captured: 2026-11-19
---

# Meet Shepherd, the Meta-Agent Keeping Rogue AI In Check

Rina Diane Caballar — IEEE Spectrum, 19 de noviembre de 2026. _The tool uses version control and sandboxing to recover from AI missteps and "manage" agents._

AI agents are running amok on the internet, armed with commands to accomplish certain tasks but often acting in undesirable or unexpected ways. These rogue incidents run the gamut from deleting an entire email inbox to hacking websites and even launching cyberattacks.

Much like human workers need managers, Weiyan Shi, an assistant professor at Northeastern University, believes AI agents require oversight. "They are running potentially for a long time. However, the longer they run, they may have some errors, and they may make some dangerous, unsafe actions. We feel like there should be a middle layer," she says.

This middle layer comes in the form of meta-agents that oversee behavior, provide quality control, and kick issues up the chain of command to a human when appropriate. "Worker agents are like the sheep wandering around, and the meta agent is like this shepherd trying to get them back on track," Shi says.

As such, Shi and her colleagues at Northeastern University and Stanford University named their framework Shepherd, an intelligent guide for agentic sheep. To arm meta-agents with power, the team borrowed a concept from software development: version control. The accompanying paper will be presented at the 2026 NeurIPS conference to be held in December.

## Version control for AI agents

Version control systems, such as the popular GitHub, track and manage changes to source code over time. These tools allow software engineers to collaborate on the same codebase without losing work. They can "fork" or create a copy of the codebase that they develop independently, "commit" to save a new version with changes, review revisions, and roll back to a previous version when an error or failure occurs.

Similarly, Shepherd serves as a version control system for AI agents. It's built using the Python programming language and rooted in functional programming principles. Each agent action, along with the AI agent's state and its relevant environment (such as an email inbox, a file system, or other) is stored as a commit, with a commit graph consisting of a series of actions. Meta-agents traverse the graph to navigate to any commit, enabling them to observe worker agents, intercept a buggy action, revert the worker to its previous step, and fork it to try another direction.

"There's a subtlety because it looks to [worker] agents like they're in the regular world where they can do things like send emails. But in actuality, the action of sending the email has been caught by a Shepherd sandbox, so a meta-agent or a human can come in and decide to actually send it," says Derek Chong, a researcher at Stanford University's Natural Language Processing Group who's part of the Shepherd team. This sandboxing, he adds, functions as a guardrail or governance component.

Shepherd is available as an open-source project, but Chong notes that the team is still in the process of building it from alpha to full production readiness. The Shepherd framework is part of the broader Agent Sciences Research Initiative (ASRI) cofounded by Chong and Shi. This collaboration of researchers from Northeastern, Stanford, and UC Berkeley aims to explore how to make AI agents more reliable and robust, how to evaluate them better, and how to ensure they're safer.
