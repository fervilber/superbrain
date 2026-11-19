---
title: "Introducing Computer's Multiagent effort level (Perplexity)"
source: "https://www.perplexity.ai/hub/blog/introducing-computer-multiagent"
date: 2026-11-17
captured: 2026-11-19
---

# Introducing Multiagent for the most complex work

Perplexity Computer's Multiagent effort level coordinates AI models to analyze complex tasks and cross-check their work. 17 Nov 2026.

Today we're launching Multiagent, a new effort level above Ultra for Computer's most complex work. The lead agent runs a team of agents on different frontier models that work in parallel, share findings directly with each other, and check each other's work. This lets Computer examine complex problems from multiple angles and find conflicting assumptions before bringing the findings together into a single recommendation or output.

Claude Fable 5.2 plans the task and divides it among agents running Claude Opus 5.5, GPT 6.1 Sol, and Gemini 4 Carbon. Agents share findings as they work. One agent can use evidence another has found, question an assumption, or flag a discrepancy for more investigation. The lead agent brings their inputs back into a single response with the asked-for deliverables.

Multiagent is designed for work with distinct parts that benefits from parallel analysis and cross-checking.

- **Forecasting and finance:** Agents can build different financial scenarios in parallel, compare their assumptions, and check how changes in revenue, costs, or market conditions affect the forecast.
- **Annual report review:** Agents can examine financial statements, footnotes, and management commentary separately, then compare findings to flag inconsistent figures or disclosures for an auditor's review.
- **Deep analysis:** Agents can investigate competing explanations for a business or research question, exchange evidence, and test which conclusions hold up across sources.
- **Deal data room diligence:** Agents can review financial records, contracts, and operating documents in parallel, then connect findings such as a customer contract that changes the revenue outlook.
- **Complex tax returns and year-end planning:** Agents can organize income and deduction records, research relevant tax rules, and compare year-end scenarios to prepare questions and supporting analysis for a tax professional.

When Multiagent is selected in Computer's effort slider, the lead can assign up to **16 agents**, while taking on part of the work itself. The default team combines Opus 5.5, GPT 6.1 Sol, and Gemini 4 Carbon, bringing different models to the analysis and review. Users can specify the models they want to use in their query. Fable 5.2 and GPT 6 Astra join as supporting agents only when a user requests them or when a particular part of the task calls for them. Agents communicate during the task and coordinate edits to shared files. For example, one agent might update the revenue assumptions in a financial model, then notify another agent to use those figures in its valuation analysis.

Multiagent: The same lead model as Ultra coordinates agents that share findings directly, check each other's work, and contribute to shared deliverables. Large assignments with interconnected parts that can be worked on in parallel, such as data room diligence or a financial forecast with several scenarios.
