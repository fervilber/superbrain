import os

title = "Spending on AI Is Becoming Almost Impossible for Businesses to Budget"
url = "https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a"
date_str = "2026-10-05"
filepath = "/home/vilber/proyectos/superbrain/content/raw/2026-10-05-spending_on_ai_is_becoming_almost_impossible_for_businesses_to_budget.md"

content = f"""---
title: "{title}"
source_url: "{url}"
date: {date_str}
---

# {title}

Source: {url}

## Context and Key Findings

Budgeting for artificial intelligence (AI) in corporate environments has become a massive financial challenge. Unlike traditional SaaS software with fixed per-user pricing, generative AI usage is billed by **tokens**—the basic units of text processed by models. Because LLM workflows are inherently dynamic, non-deterministic, and prone to loops, predicting how many tokens a model will consume for a given task is nearly impossible.

### Statistical Highlights
- A recent survey of **400 businesses** revealed that **only 11%** were capable of accurately forecasting their AI spending.
- Google's token volume skyrocketed from **9.7 trillion tokens per month** to over **480 trillion tokens per month** in a single year—an almost 50-fold increase.
- Many companies report that AI is now the fastest-growing technology expense, in some cases representing up to **50% of total IT budgets**.
- Consequently, cloud computing bills for enterprises incorporating generative AI rose by **19%** year-over-year.

### Real-World Anecdotes
- Engineers using advanced agentic tools like Claude Code report massive unexpected usage: **"Burned 16.7M tokens on one glossary audit in Claude Code on Saturday. No way anyone puts that in a budget upfront!"**
- This dynamic has triggered a wave of corporate caution, with companies shifting from "unlimited experimentation" to rationing AI, implementing hard API budget caps, and shopping *a la carte* for cheaper, smaller models (including local models or open models) to perform mundane tasks.

"""

os.makedirs(os.path.dirname(filepath), exist_ok=True)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Created {filepath}")
