---
title: "Salesforce SFR-AutoR&D: agentes de I+D que mejoran modelos de IA en producción"
source: "https://www.salesforce.com/news/stories/agents-that-improve-ai-models/"
date: 2026-11-11
captured: 2026-11-11
---

# Salesforce Releases R&D Agents That Improve Its AI Models

November 11, 2026, 5 min read.

SFR-AutoR&D, a new self-improving system from Salesforce, trains and improves the embedding models in deployment-grade enterprise AI.

Salesforce AI Research recently published SFR-AutoR&D, a set of agents built to run the research loop end-to-end, autonomously improving codebases and training AI models. Given one goal, a system to work on, and a compute budget, SFR-AutoR&D agents formulate hypotheses, implement methods, and run controlled experiments against baselines. They retain improvements to the codebase only when supported by evidence and proven accurate and safe.

SFR-AutoR&D is now being used to train and improve production AI models. The system autonomously improved SFR-Embedding V3, the model Salesforce uses for retrieval in Data Cloud. Next, the Salesforce AI Research team pointed SFR-AutoR&D at the open source model EmbeddingGemma 2, and it produced a measurably better model in both quality and latency, SFR-Embedding v4. These are early examples of something larger: AI systems that improve the software and models an enterprise already runs on.

The system had already built a track record on improving public codebases. The first published results came from open source software that enterprise data teams rely on every day: pandas, the Python library most data scientists use to manipulate large tables of data. Other codebases SFR-AutoR&D has improved include hnswlib and USearch, two libraries that power the kind of similarity search behind AI retrieval. These are heavily optimized projects with years of expert tuning in them, and yet the agents found further gains in all three, each packaged with the benchmark evidence.

Embedding models are the workhorses of enterprise AI. They convert text into numerical representations so that a system can find the right record, document, or case history out of millions. When an Agentforce agent answers a question grounded in a customer's own data, it reaches through Data Cloud, and an embedding model decides what comes back. Retrieval quality determines everything the agent says next.

## From weeks to hours

Improving an embedding model has historically been a human process. Research scientists propose an approach, build the experiment, run it, read the results, and decide what to try next, often over a period of several weeks. With SFR-AutoR&D, the system did all of that work itself, completing the cycle in about 80 hours; just a little over three days.

"For most of the history of machine learning, progress has moved at the speed of human experimentation," said Silvio Savarese, EVP and chief scientist at Salesforce. "What we are seeing now is a research system that forms a hypothesis, tests it, and holds itself to the evidence, applied to a model our customers depend on. The scientific method still governs, and the loop runs faster. This is self-improvement engineered for trusted enterprise deployment."

## Arquitectura y resultados

The team built two agents to deliver this kind of improvement. AutoR&D-Engineer searches for algorithmic and systems improvements inside existing code. TrainForge explores new training methods, runs them, and evaluates candidates against held-out benchmarks that the system never trains on. Both agents run on AutoInfra, the training backbone that carries their experiments across shared GPU capacity.

Evaluated against 10 public retrieval tasks in MTEB, SFR-AutoR&D improved the model's ability to place relevant results near the top, raising its nDCG@10 score by 6.13 points. The system then ran a second session on its own, roughly nine hours, this time aimed at how fast and cheaply the model runs. It came back with 36% more throughput and 17% lower latency, with almost no loss in quality.

An important aspect of training any model at Salesforce is trust. The models trained for product use draw only on datasets that have cleared ethical and legal review, a constraint the research team treats as part of the problem definition rather than a step after the fact.
