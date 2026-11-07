---
title: "Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell (arXiv 2610.07782v1)"
source: "https://arxiv.org/html/2610.07782v1"
date: 2026-11-07
captured: 2026-11-07T20:08:00+01:00
---

# Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell

**Venue:** Accepted as a poster at the Machine Learning for Systems Workshop, NeurIPS 2026 (13 pages, 1 figure). arXiv:2610.07782v1 [cs.AI].

## Abstract

Decomposing long-context inference across cooperating agents bounds the _active_ KV cache per call rather than total evidence, which matters when KV-cache memory binds. Many such systems add a persistent tier storing and recalling reasoning traces, usually validated by an ablation reporting an accuracy gain. We measure both on one three-tier agent architecture. Decomposition delivers: peak KV working set of 14.3 MiB per query against 35.5 and 35.3 MiB for single-pass and retrieval-augmented baselines. The persistent tier does not: across eight controlled dataset pairs at n=100 per arm it costs +0.368 MiB [+0.167, +0.590] of peak cache and produces no detectable accuracy change (+0.015, 95% CI [−0.011, +0.046]). We argue the null is _structural_: single-question benchmarks supply each item with its own evidence and score it independently, and correctness requires resetting stored traces between conditions, so recall has nothing informative to retrieve. Reaching it took four measurement corrections—three inflating the apparent benefit, the fourth making an effect that size look resolvable—none visible in the results table. We give the conditions an agent-memory ablation must satisfy and detection procedures that need no knowledge of the specific defect.

## Architecture (CoA-PKV)

- **L1:** ephemeral per-call KV cache.
- **L2:** key–value store of typed Communication Units, so an agent receives distilled predecessor output rather than raw context.
- **L3:** vector store whose two roles—semantic evidence filtering before anything enters a cache, and (q,k,v) trace persistence for cross-query recall—are separable in code; only the second is the persistent-memory claim.
- The full system is called **CoA-PKV** (chain of agents over a persistent key–value tier); the ablated arm with trace recall and writes disabled is **CoA-NoKV**; they differ in exactly those two operations.

## Measured results

|                         | Flat (closed-book) | RAG (retrieval-matched) | CoA-PKV (ours)    | vs Flat | vs RAG |
| ----------------------- | ------------------ | ----------------------- | ----------------- | ------- | ------ |
| peak KV per query (MiB) | 35.5 [34.0, 37.0]  | 35.3 [30.9, 39.8]       | 14.3 [13.0, 15.4] | −59.9%  | −59.7% |
| latency per query (s)   | 67                 | 52                      | 29                | −56.7%  | −44.2% |

- Peak KV is 2.5× lower and latency 1.8–2.3× lower; the CoA-PKV interval clears both baselines with no overlap, while Flat and RAG overlap each other.
- Bounded per-call working sets are bought with more calls — _cumulative_ KV traffic is ≈1.6× higher. The claim is lower peak at higher total traffic, the trade that matters when KV-cache memory binds.
- Accuracy against retrieval-matched RAG is parity, every difference smaller than the reproducibility band.

## The persistent tier's ablation

| effect                               | 95% CI     |
| ------------------------------------ | ---------- | ---------------- |
| peak KV cost of enabling recall      | +0.368 MiB | [+0.167, +0.590] |
| accuracy change from enabling recall | +0.015     | [−0.011, +0.046] |

- The cost interval excludes zero: recall prepends retrieved traces to the reasoner's prompt, so prompts grow (≈2% against per-query peaks of 13.6–21.9 MiB).
- The accuracy interval includes zero. The authors do not claim the effect is zero; they claim an effect larger than ≈0.046 is excluded, and the point estimate is not separable from noise.
- The null is argued to be **structural**: single-question benchmarks supply each item with its own evidence and score it independently, and correctness requires resetting stored traces between conditions, so recall has nothing informative to retrieve.
- Reaching it took four measurement corrections — three inflating the apparent benefit, the fourth making an effect that size look resolvable — none visible in the results table.
- The paper notes it is an intention-to-treat framing: RAG changes _which_ evidence enters a call; decomposition changes _how many calls_ it is spread across, and only the second bounds the peak KV.

## Failure-mode caveat the authors highlight

A weak scenario (their "reject" example) shows three different failure mechanisms behind one metric. Question: "Who used a Barrack buster to shoot down a British Army Lynx helicopter" (gold: IRA). All three reasoning traces independently converge on the correct entity (the IRA) before answering; the failures happen downstream and are not the same failure: CoA-PKV's Synthesiser diverges from its own correct reasoning and outputs an unrelated name (Seán Kelly); CoA-NoKV and RAG both produce the semantically right answer in a surface form that token-F1 against the gold string "IRA" scores at zero. One F1=0 collapses three distinct failure modes into the same number — the case for reading per-sample traces before trusting an aggregate.

## What the paper offers in practice

- Conditions an agent-memory ablation must satisfy (dataset matching, seed pairing, evidence scoping, endpoint matching, trace reset, live isolation probes).
- Detection procedures that need no knowledge of the specific defect (drift checks, order-confound controls, per-sample trace inspection).
