# EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction

**Authors:** Yuling Shi, Zhensu Sun, Junsen Dong, Chengcheng Wan, David Lo, Xiaodong Gu  
**Date:** September 2, 2026  
**Source:** arXiv:2609.02783v1  
**Category:** Language Models, AI Agents, Software Engineering Benchmarks

## Abstract

Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles. Prior efforts, centered on benchmark distillation, reduce the number of evaluation tasks but leave the cost of executing each retained task untouched. In this work, we introduce early outcome prediction, a complementary axis of efficiency that instead cuts cost within each task. Our key insight is that an agent's final outcome is often evident from its intermediate behavior well before execution completes. We instantiate this idea in EarlyEval, a lightweight framework that trains a pair of LightGBM success and failure classifiers over behavioral, textual, and reference-solution features, and halts an agent run the moment either classifier crosses a calibrated confidence threshold, adding negligible per-step overhead. Across three benchmarks, SWE-bench Verified, TerminalBench, and Toolathlon, EarlyEval can eliminate 13%-26% of agent steps and up to 44.1% input tokens and 29.4% output tokens at 89%-97% prediction accuracy, while perturbing per-agent resolve rates by only one to two percentage points on average.

## Core Problem: The Prohibitive Cost of Agent Evaluation

Modern agentic evaluation relies on running large frontier models through long, multi-step execution loops. Unlike static QA benchmarks, evaluating an agent involves executing tools, parsing logs, and handling complex environment loops. This process is extremely expensive:

- Running an agent over SWE-bench or other terminal/coding benchmarks can take dozens of turns.
- Each turn appends history, inflating the context window and resulting in massive token ingestion costs.
- Iterative cycles of agent development require running these evaluations repeatedly, multiplying the financial barrier for smaller labs and open-source developers.

## The EarlyEval Approach

Instead of filtering tasks (like distillation methods) or using cheaper, less-capable models, **EarlyEval** introduces **Early Outcome Prediction**.

### Fundamental Insight

An agent’s success or failure is often predictable from its intermediate steps before the episode officially ends.

- **Signs of Success:** Early generation of correct syntactic constructs, consistent tool matching, progressive reduction of error distances.
- **Signs of Failure:** Infinite loops, repeating identical terminal commands, recurrent JSON parser errors, stalling, or navigating away from relevant directory structures.

### Framework Architecture

EarlyEval operates as a lightweight wrapper that runs alongside the agent's environment loop.

1. **Feature Extraction (per step):**
   - **Behavioral Features:** Number of steps, tool invocations, repeat counts, rate of unique command executions.
   - **Textual Semantic Features:** Context similarity, output confidence, error logs.
   - **Reference-Solution Features:** Proximity to known solution files or expected API responses.
2. **LightGBM Dual Classifiers:**
   - Instead of a single model, EarlyEval trains two separate gradient-boosting classifiers (LightGBM): one optimized for **Success Prediction** and one for **Failure Prediction**.
   - These classifiers have negligible CPU inference overhead compared to LLM calls.
3. **Calibrated Halting Threshold:**
   - At each step $t$, the classifiers output confidence scores. If either score exceeds a pre-calibrated threshold, the evaluator forces a halt.
   - If halting occurs early:
     - **Predicted Success:** The task is logged as solved.
     - **Predicted Failure:** The task is logged as failed, saving subsequent expensive LLM generation steps.

## Empirical Performance and Cost Savings

The authors evaluated EarlyEval across three representative agentic benchmarks:

- **SWE-bench Verified:** Software engineering tasks.
- **TerminalBench:** Terminal-based bash navigation and file manipulation.
- **Toolathlon:** Intensive tool-calling environment.

### Key Metrics

- **Steps Eliminated:** 13% to 26% of all execution steps across the benchmarks.
- **Token Reductions:** Saves up to **44.1% of input tokens** and **29.4% of output tokens**.
- **Accuracy:** Maintains **89% to 97%** prediction accuracy in determining final outcomes.
- **Resolve Rate Fidelity:** The predicted resolve rate varies by only 1 to 2 percentage points compared to the ground truth of running every step to completion, preserving the benchmark's utility as a compass for model capabilities.
