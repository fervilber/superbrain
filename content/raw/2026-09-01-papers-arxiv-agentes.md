# Raw arXiv Papers Meta-Data (2026-09-01)

Este archivo contiene la información en bruto extraída de la API de arXiv el 1 de septiembre de 2026 sobre las últimas publicaciones en el área de Agentes de Inteligencia Artificial.

---

## 1. Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data

- **ID/URL:** http://arxiv.org/abs/2608.31082v1
- **Fecha de Publicación:** 2026-08-31T16:53:45Z
- **Título Original:** Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data
- **Resumen:**
  Valuable data remains embedded in unstructured sources: web pages, reports, contracts, filings, earnings calls, and PDFs. The big bet in enterprise AI is deploying LLM agents that reason over this data to answer complex questions for every knowledge worker. Agents can do this today, but at prohibitive cost. Each question repeatedly opens large documents to recover scattered evidence, consuming up to a million tokens. However, if the data were already structured, the same question would reduce to a cheap database lookup. For example, on FanOutQA benchmark, reasoning over an ideal pre-structured store is 28X cheaper, and the gap grows to orders of magnitude as questions fanning out over more documents. Yet structuring everything in advance is not viable: documents hold vastly more possible structure than any workload will use, and the useful structure and documents are unknown until queries arrive.

  We propose **agentic data cracking**, a method that structures unstructured data adaptively and speculatively as a byproduct of reasoning itself. Structuring is adaptive because observed queries decide when it happens and what matters, and speculative because it goes beyond the current question. Whenever the agent opens a document to answer, a cracking sub-agent forks from the already-loaded context at marginal cost and extracts grounded structure likely to serve related future queries. Over time, an increasing share of queries is fully covered by structured data and answered without opening a document, keeping agentic accuracy at close to RAG cost. On FanOutQA, extended with merely one related question per test question, cracking cuts cost by 53% while preserving accuracy. Agentic data cracking is a first step toward next-generation data infrastructure for agentic reasoning over unstructured data: a shared substrate beneath the model where knowledge that reasoning already paid to uncover accumulates.

---

## 2. MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

- **ID/URL:** http://arxiv.org/abs/2608.31022v1
- **Fecha de Publicación:** 2026-08-31T16:05:39Z
- **Título Original:** MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents
- **Resumen:**
  AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities.

  We address this with **MNIST-PRO**, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas.

  While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks:
  1. Perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses.
  2. Agents often stop exploring before they see the full sequence.
  3. Models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence.

  These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

---

## 3. From Prompt to Prototype: Towards a Frontier LLM Driven RF Engineering Workflow

- **ID/URL:** http://arxiv.org/abs/2608.31006v1
- **Fecha de Publicación:** 2026-08-31T15:56:14Z
- **Título Original:** From Prompt to Prototype: Towards a Frontier LLM Driven RF Engineering Workflow
- **Resumen:**
  Agentic coding environments give a frontier large language model (LLM) direct access to a workstation's terminal, file system, and software. This work demonstrates they extend to professional RF hardware design: an active GNSS L1-band antenna - a circularly polarized patch, surface acoustic wave (SAW) prefilter, and two-stage low-noise amplifier (LNA) on one printed circuit board (PCB) - was designed, optimized, and made manufacturing-ready.

  The LLM agent autonomously operated CST Studio Suite, Keysight ADS, and KiCad via scripting interfaces. Engineer input was limited to the specification, trade-off decisions, and design reviews. Workflow, results, and the RF engineer's evolving role are discussed.
