# An Expert Analysis Pattern Library for Financial Report Generation

**Source URL:** https://arxiv.org/html/2609.00818v1

##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

# AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation

###### Abstract

We argue that financial report generation should operate at the analytical rather than structural level, composing content from data-derived insights rather than high-level topics or sections. To this end, we propose AnalysisBank, which distills expert reports into a reusable library of _Analyses_, each pairing a data signal, an analytical move, and the expert span it was derived from. At inference time, AnalysisBank matches input signals to library entries and applies the retrieved moves to compose the report. A study of _Analyses_ distilled from 550 expert reports reveals a heavy-tailed distribution of 47–52 signal types spanning 13 move types. On two financial benchmarks across four LLM backbones, AnalysisBank increases the proportion of novel, data-grounded insights by 1.7–3.7×\times over structural-level baselines. Transfer to scientific writing suggests that the distinction generalizes beyond finance. Code and the distilled _Analysis_ library are available at <https://github.com/yajingyang/AnalysisBank>.

## 1 Introduction

In finance, analytical reports support decisions by producing _insights_: claims derived from analyzing source data rather than paraphrasing it [Asquith et al. (2005)](#bib.bib37); [Huang et al. (2014)](#bib.bib38). Each insight is the output of an _analytical move_: a comparison, an attribution, a derivation, a projection, a gap-detection. Which analytical moves to make depends on what the data contains: the same earnings transcript, read by different analysts, yields different insights because each analyst recognizes different conditions in the data and responds with different analytical moves [Huang et al. (2018)](#bib.bib39). This distinguishes the task from summarization ([Lewis et al., 2020](#bib.bib27)) and data-to-text generation ([Wiseman et al., 2017](#bib.bib20)), where the output paraphrases or restates the input; analytical report generation produces content the input does not state.

![Refer to caption](2609.00818v1/task.png)

Existing methods operate at what we term the _structural level_: they prescribe what the report should cover, such as topics, viewpoints, or analytical categories, but leave the reasoning within each section to the language model’s default behavior [Goldsack et al. (2025)](#bib.bib24); [Koshkin et al. (2025)](#bib.bib25); [Yang et al. (2022)](#bib.bib22); [Shao et al. (2024)](#bib.bib46) (Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"), top). In every case the skeleton varies but the analytical substance does not: sections are filled with generic analyses such as trend description and standard ratio computation, regardless of what the input data specifically warrants.
We argue that the task requires operating at the _analytical level_: the report should be composed of analytical moves driven by the specific signals in the source data (Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"), bottom). For example, a revenue decline smaller than peers’ calls for a relative-outperformance inference; a downward guidance revision calls for a margin-implication derivation. These are not generic trend descriptions but signal-specific insights.

Operating at the analytical level is non-trivial for two reasons. First, the space of pairings between data signals and the analytical moves they call for is large and heavy-tailed: our corpus analysis identifies 47–52 signal types spanning 13 analytical move types, yet over a third appear in three or fewer instances, each pairing with only one to two moves (§[3.3](#S3.SS3 "3.3 Coverage and Distribution ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")). These tail patterns
reflect the diverse ways experts respond to uncommon data conditions ([Huang et al., 2018](#bib.bib39)) and are too sparse for LLMs to learn from prompting or fine-tuning alone.
Second, even given comprehensive pairings, selecting the right one for a given input is challenging:
as autoregressive models, LLMs are biased toward high-probability outputs ([McCoy et al., 2024](#bib.bib45)) and default to generic analytical moves rather than the rare, signal-specific move the data calls for.
Our ablation confirms that alternate selection mechanisms yield 19% less insightful content (§[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

To close this gap, we propose AnalysisBank. The core idea is that expert reports already embody analytical-level reasoning: each insight is derived from a specific data signal with the analytical move it calls for. AnalysisBank distills these pairings into a reusable library, where each entry, an _Analysis_, tuples a data signal, an analytical move, and the expert span it was distilled from, with the signal and move abstracted to making each _Analysis_ reusable across inputs sharing the same pattern. Our study shows that _Analyses_ distilled from 550 expert reports cover the heavy-tailed distribution (§[3.3](#S3.SS3 "3.3 Coverage and Distribution ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).
The same abstraction addresses the selection challenge: by disentangling the underlying analytical pattern from surface specifics, the data signal field makes the link between a stored pattern and the input signal it should match explicit, enabling direct retrieval at inference time.
On two benchmarks covering structured market data and unstructured earnings transcripts, AnalysisBank increases the proportion of novel, data-grounded insights by 1.7–3.7×\times across four LLM backbones.

Our contributions are threefold: (i) we distinguish _structural_ and _analytical_ levels of report generation and argue existing methods address only the former; (ii) we propose AnalysisBank, a library of expert-distilled _Analyses_ and a pipeline to apply them at inference; (iii) on two benchmarks across four backbones, AnalysisBank increases novel, data-grounded insight by 1.7–3.7×\times, while structural-level methods converge well below it.

## 2 Related Work

We break down relevant prior work into three areas: long-form and report generation (the task), reusable reasoning patterns (the method), and financial NLP (the domain).

#### Long-form and report generation.

Data-to-text generation maps tables and records to fluent prose [Wiseman et al. (2017)](#bib.bib20); [Parikh et al. (2020)](#bib.bib21), but the output restates the input rather than analyzing it.
Report-generation methods go further by introducing organizational structure:
multi-agent frameworks assign predefined analytical roles [Goldsack et al. (2025)](#bib.bib24); [Koshkin et al. (2025)](#bib.bib25),
plan-then-write approaches decompose output into sections [Yang et al. (2022)](#bib.bib22); [Puduppully et al. (2019)](#bib.bib23); [Hu et al. (2022)](#bib.bib47),
and retrieve-organize-write systems research a topic through retrieval and generate from the resulting outline [Shao et al. (2024)](#bib.bib46).
All three control what the report covers but not what analysis to apply to the data.

#### Reusable reasoning patterns.

A natural approach is to retrieve reusable reasoning patterns at inference time. Self-discovered reasoning modules [Zhou et al. (2024)](#bib.bib12) and thought templates [Yang et al. (2024a)](#bib.bib11); [Jeong et al. (2025)](#bib.bib13) provide abstract reasoning strategies not grounded in specific data patterns. Agent workflows [Wang et al. (2025)](#bib.bib10); [Wang et al. (2024a)](#bib.bib5) and induced functions [Wang et al. (2024b)](#bib.bib7) learn concrete routines from task-solving trajectories but capture full procedures, not individual analytical moves. Case-based methods [Yasunaga et al. (2024)](#bib.bib28); [Wiratunga et al. (2024)](#bib.bib29) and experience memories [Park et al. (2023)](#bib.bib30); [Zhong et al. (2024)](#bib.bib31) operate at the instance level but store complete cases tied to specific inputs, not abstracted into reusable patterns. Analytical report generation requires patterns that are grounded in data, decomposed at the analytical-move level, and abstracted for reuse across the heavy-tailed distribution found in expert reports.

#### Financial NLP.

Domain-pretrained models [Wu et al. (2023)](#bib.bib1); [Yang et al. (2023)](#bib.bib2); [Xie et al. (2023)](#bib.bib14) adapt language
models to financial text but do not explicitly model
signal-to-move reasoning. Signal-mining pipelines extract salient content within it [Ju et al. (2023)](#bib.bib43); [Lu et al. (2025)](#bib.bib44) but do not prescribe what analysis a signal calls for. Downstream reasoning work targets question answering [Chen et al. (2021)](#bib.bib15); [Zhu et al. (2021)](#bib.bib16); [Islam et al. (2023)](#bib.bib3); [Choi et al. (2025)](#bib.bib6), injecting expert structure through hand-authored workflows ([Nitarach et al., 2025](#bib.bib4)) or historical scaffolds ([Singhal, 2025](#bib.bib17); [Le, 2024](#bib.bib19)), but produces closed-form answers, not open-ended reports. For report generation, bullet-point earnings-call summarization [Mukherjee et al. (2022)](#bib.bib18) remains structural, while hierarchical data narration ([Yang et al., 2025](#bib.bib26)) reaches the analytical level but leaves the choice of analysis to the model, which defaults to the most common ones.

## 3 AnalysisBank

We first define the representation of each _Analysis_, designed to be reusable across inputs while preserving actionability (§[3.1](#S3.SS1 "3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")), then the extraction pipeline that populates the library from a corpus of expert reports (§[3.2](#S3.SS2 "3.2 Extraction Pipeline ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")), and finally characterize the resulting library (§[3.3](#S3.SS3 "3.3 Coverage and Distribution ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

### 3.1 _Analysis_ Representation

| data_signal: A key revenue or fee line shows a large decline versus the prior period, but the decline is smaller than what was broadly expected and also smaller than the decline reported by a comparable peer facing similar conditions.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analytical_move: When a major revenue or fee category declines sharply, compare the actual change to pre-report expectations and to the change reported by close peers; if the decline is less severe than both, explicitly assess and quantify whether this indicates relative outperformance and potential share gains in that activity.                                                                                                                                                                                                                                                                                                                                                     |
| reference_text: “Even investment banking, widely expected to be a sore thumb for all banks this quarter, may have contributed to this Friday’s bullish reaction. To be clear, revenues of $1.7 billion were small as fees sank by a whopping 47% YOY. But keep the following in mind: (1) expectations were highly de-risked ahead of the print, with Seeking Alpha contributor Cavenagh Research bracing for a fee drop greater than 50%, and (2) JPMorgan, the top Wall Street player in investment banking, may have stolen some market share away from its competitors once again. Citi (C), for example, reported Q3 investment banking revenues that were an astonishing 64% lower YOY.” |

![Refer to caption](2609.00818v1/extraction_pipeline.png)

Each entry in the AnalysisBank library, an _Analysis_, is a tuple of (data_signal, analytical_move,
reference_text), as illustrated in
Table [1](#S3.T1 "Table 1 ‣ 3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

The reference_text is a verbatim span from the source expert report that demonstrates the analytical move applied to real data (e.g., “revenues of $1.7 billion were small as fees sank by a whopping 47% YOY”). It provides a generation anchor and a faithfulness check, but contains specific entities, figures, and time references that prevent it from transferring to new inputs.

The analytical_move abstracts the reasoning in the reference text into a reusable instruction specifying what analysis to perform on the matched signal (e.g., “compare the actual change to expectations and to peers; if less severe than both, assess whether this indicates relative outperformance and potential share gains”). This transfers across inputs, but its specificity hinders fuzzy retrieval when used as the matching key.

The data_signal resolves this by serving as a separate retrieval key, stating triggering conditions in entity-free, number-free language (e.g., “a key revenue line declines sharply, but less than broadly expected and less than a comparable peer”). Retrieval matches on structural patterns while generation follows the specific instruction in the analytical move.

This three-field decomposition is a design hypothesis; we evaluate it against alternative designs in §[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"), finding that removing or merging any field degrades either retrieval precision or generation quality.

![Refer to caption](2609.00818v1/bank_signal_move_heatmap_compact.png)

### 3.2 Extraction Pipeline

Prior pattern libraries induce entries from problem-solving traces with observable success signals (cf §[2](#S2 "2 Related Work ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")); expert reports offer no such structure, requiring the pipeline to reverse-engineer the three fields from finished prose. We design a four-pass pipeline to convert the corpus into a static library (Figure [2](#S3.F2 "Figure 2 ‣ 3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

Induce identifies candidate _Analysis_ content in each report. Analytical moves are implicit in expert prose; this stage makes them explicit by locating text spans where the analyst performed a specific reasoning operation. These spans become the reference*text of each \_Analysis*.

Generalize extracts the data*signal and analytical_move from each identified span, producing the full three-field \_Analysis* of §[3.1](#S3.SS1 "3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"). The data signal is abstracted by stripping entity names, specific figures, and time references while preserving the conditional structure. The analytical move is similarly abstracted into a specific instruction that applies to any instance of the signal. A self-check enforces that each _Analysis_ would apply to the same pattern across different industries.

Deduplicate drops redundant _Analyses_ across reports, since multiple expert reports often apply the same analytical move to similar signals. Candidates with data*signal embeddings above a cosine similarity threshold are grouped together and merged into a single \_Analysis*, retaining the most general data signal and the most complete analytical move. This prevents duplicate entries from consuming retrieval budget and biasing toward head patterns.

Quality-filter validates each _Analysis_ against three criteria aligned with the three fields: transferability (does the data signal generalize across industries?), actionability (would two analysts following the analytical move independently produce similar outputs?), and grounding (does the reference text show a real instance of the pattern?). Grounding failures are discarded; transferability or actionability failures are routed back to Generalize with a targeted rewrite instruction. The resulting _Analyses_ are industry-agnostic, executable, and empirically grounded.

The pipeline runs offline once, allowing a stronger model than the inference backbone to maximize _Analysis_ quality. The resulting library is reused across all generation runs.

![Refer to caption](2609.00818v1/generation_pipeline.png)

### 3.3 Coverage and Distribution

We instantiate AnalysisBank on two corpora spanning the dominant input modalities: 550 daily market-analysis reports written from structured price data (_DataTales_; [Yang et al., 2024b](#bib.bib8)) and 550 equity-research reports written from filings and earnings-call transcripts (*Earnings*11
1
The Earnings _Analysis_ library is distilled from Seeking Alpha (<https://seekingalpha.com/>) analyst reports, which we cannot redistribute.). The extraction pipeline of §[3.2](#S3.SS2 "3.2 Extraction Pipeline ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") yields 1,422 _Analyses_ from DataTales and 3,889 from Earnings. We characterize each library by labeling every _Analysis_ with a signal type and a move type using two hand-built keyword taxonomies (Appendix [B](#A2 "Appendix B Bank Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).
The move taxonomy has 13 types (e.g., compare/contrast), all populated in both corpora. The signal taxonomy has 55 types (e.g., outlook direction), of which 47 signal types are populated in DataTales and 52 in Earnings. The two axes are not independent: each signal type triggers a median of 4 distinct move types in DataTales and 6 in Earnings, and the move mix varies across signals (e.g., outlook direction spreads across compare/contrast, assess durability, contextualize historically, and articulate implication, while volatility observed concentrates on articulate implication alone; Figure [3](#S3.F3 "Figure 3 ‣ 3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

This breadth coexists with a heavy long tail. The top-5 signals account for only 55% and 51% of _Analyses_ in DataTales and Earnings respectively; reaching 90% coverage requires 19 and 22 signal types. The remaining tail is not residual noise: 17 of 47 signal types in DataTales (36%) and 10 of 52 in Earnings (19%) appear in ≤3{\leq}3 _Analyses_, yet unlike head signals that spread across many moves, each tail signal concentrates on 1–2 moves (Figure [3](#S3.F3 "Figure 3 ‣ 3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"), below the dotted line), reflecting the narrow, decisive way an expert responds to an uncommon situation such as a trend reversal or a structural advantage assessment. These are precisely the patterns too rare for prompting or fine-tuning to internalize, preserved in reusable form by the abstraction of §[3.1](#S3.SS1 "3.1 Analysis Representation ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

## 4 Narrative Generation with AnalysisBank

The library built in §[3](#S3 "3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") provides coverage and the field structure needed for effective retrieval; the generation pipeline selects and applies the right _Analyses_ for a given input (Figure [4](#S3.F4 "Figure 4 ‣ 3.2 Extraction Pipeline ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

#### Stage 1: Signal extraction.

Raw financial input is too broad to match effectively against the abstracted data*signal field. This stage reduces it to a list of typed \_signals*, each consisting of a signal type (e.g., margin delta, volatility regime), a signal description summarizing the condition, and supporting source spans. For textual input (e.g., earnings-call transcripts), an LLM extracts the signals, each verified by a fact-checking pass ([Penman, 2013](#bib.bib40)). For structured input (e.g., market data), a Python program computes them deterministically from price and volume series ([Murphy, 1999](#bib.bib41)) and formats the results into the signal description for retrieval.

#### Stage 2: Per-type retrieval.

Signal descriptions query AnalysisBank by cosine similarity against data*signal field of each library entry. To ensure the retrieved \_Analyses* cover diverse signal types rather than concentrating on one, each signal type contributes its best matching _Analysis_, and remaining slots are filled by global top-kk.

#### Stage 3: Per-_Analysis_ execution.

Each retrieved _Analysis_ is applied independently: an LLM call executes the analytical_move on the triggering signal descriptions and their supporting spans, producing one analytical finding. The reference_text is included as a demonstration of how the same type of analytical move has been applied before.
Independence across calls ensures that Stage 4 receives findings with distinct analytical content.

#### Stage 4: Composition.

A single LLM call composes the findings into a report. Rather than following a fixed section template, the model organizes around investment-relevant themes inferred from the findings themselves, consistent with the analytical-level principle that report structure should be driven by the data.
The extracted signals from Stage 1 are included to fill factual gaps the findings do not cover, grounding the report in the source data.

The pipeline uses the same backbone model at every stage. Prompts and hyperparameters are in Appendix [C](#A3 "Appendix C Narration Pipeline Configuration ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"). The contribution of each design choice across all stages is isolated in §[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

|                    |        |           |      |       |       |      |                   |      |       |       |       |
| ------------------ | ------ | --------- | ---- | ----- | ----- | ---- | ----------------- | ---- | ----- | ----- | ----- |
|                    |        | DataTales |      |       |       |      | Earnings2Insights |      |       |       |       |
| Model              | Method | %ins      | %ana | depth | %fact | %win | %ins              | %ana | depth | %fact | %win  |
| Qwen3-8B           | Direct | 3.8       | 36.1 | 1.92  | 88.7  | 25.3 | 6.6               | 38.8 | 2.04  | 94.9  | 88.6  |
| CoT                | 7.2    | 48.8      | 2.16 | 92.8  | 26.5  | 4.2  | 38.3              | 2.15 | 94.5  | 58.8  |
| RAG                | 3.9    | 36.5      | 1.92 | 89.5  | 29.9  | 4.4  | 34.0              | 1.95 | 96.1  | 87.8  |
| BoT                | 9.2    | 48.2      | 2.18 | 88.9  | 40.9  | 5.2  | 31.3              | 1.55 | 91.8  | 86.3  |
| AWM                | 6.5    | 40.8      | 1.98 | 92.5  | 29.5  | 5.0  | 39.9              | 1.99 | 93.1  | 80.2  |
| AnalysisBank       | 22.5   | 71.2      | 2.59 | 92.1  | 60.0  | 18.0 | 57.4              | 2.52 | 89.8  | 96.6  |
| Qwen3.5-9B         | Direct | 5.2       | 31.1 | 1.79  | 93.6  | 54.9 | 3.7               | 27.8 | 1.82  | 98.5  | 95.0  |
| CoT                | 5.7    | 35.5      | 1.84 | 95.2  | 51.6  | 6.4  | 34.0              | 1.93 | 97.6  | 88.2  |
| RAG                | 8.5    | 44.7      | 2.04 | 94.2  | 70.2  | 4.5  | 25.4              | 1.49 | 98.4  | 98.1  |
| BoT                | 14.0   | 50.4      | 2.19 | 95.8  | 88.2  | 3.2  | 19.1              | 1.66 | 98.8  | 74.6  |
| AWM                | 11.4   | 48.5      | 2.19 | 96.7  | 70.0  | 6.4  | 37.7              | 2.05 | 98.9  | 97.3  |
| AnalysisBank       | 26.1   | 67.1      | 2.50 | 89.8  | 81.9  | 23.8 | 63.1              | 2.61 | 97.2  | 99.6  |
| DeepSeek -V4-Flash | Direct | 5.5       | 36.7 | 1.79  | 94.0  | 75.6 | 5.7               | 34.6 | 1.92  | 98.9  | 97.7  |
| CoT                | 6.6    | 43.7      | 1.98 | 95.0  | 83.1  | 5.8  | 36.7              | 2.09 | 98.2  | 91.2  |
| RAG                | 7.9    | 46.9      | 2.10 | 92.4  | 85.4  | 7.5  | 39.5              | 2.12 | 98.5  | 98.1  |
| BoT                | 12.7   | 55.6      | 2.27 | 90.8  | 88.3  | 7.0  | 38.5              | 2.07 | 98.6  | 95.4  |
| AWM                | 10.5   | 52.4      | 2.25 | 96.1  | 96.3  | 7.7  | 42.7              | 2.07 | 97.0  | 98.5  |
| AnalysisBank       | 21.1   | 67.6      | 2.48 | 90.9  | 99.3  | 18.1 | 55.5              | 2.36 | 97.7  | 100.0 |
| GPT-5.1            | Direct | 9.8       | 54.6 | 2.17  | 94.8  | 71.1 | 15.7              | 45.6 | 2.22  | 99.3  | 100.0 |
| CoT                | 4.0    | 28.8      | 1.57 | 94.8  | 43.3  | 14.2 | 42.2              | 2.30 | 99.3  | 100.0 |
| RAG                | 10.5   | 60.1      | 2.34 | 95.9  | 90.1  | 7.3  | 38.4              | 2.04 | 99.0  | 99.2  |
| AnalysisBank       | 22.3   | 64.9      | 2.43 | 95.5  | 99.6  | 16.9 | 53.5              | 2.34 | 98.5  | 99.2  |

## 5 Experiments

#### Benchmarks.

We evaluate on the two analytical report generation benchmarks. DataTales [Yang et al. (2024b)](#bib.bib8) pairs structured market data with expert daily reports (460 instances). Earnings2Insights [Takayanagi et al. (2025)](#bib.bib9) provides earnings call transcripts for analytical report generation (132 instances, extended from the original 64).

#### Models.

We test four backbones spanning scale and capability: Qwen3-8B and Qwen3.5-9B (small open-source), DeepSeek-V4-Flash (reasoning model), and GPT-5.1 (proprietary), each in identical configurations across all conditions.

#### Baselines.

We compare against two families. The prompting family consists Direct, CoT, and RAG. The structural-level pattern family consists of Buffer of Thoughts (BoT) [Yang et al. (2024a)](#bib.bib11) and Agent Workflow Memory (AWM) [Wang et al. (2025)](#bib.bib10), which are close to
AnalysisBank in approach: BoT retrieves thought templates and AWM
retrieves task-level workflows, both from a library at inference
time. Both are adapted to distill from the same 550-report corpus that AnalysisBank consumes (adaptation details in Appendix [D](#A4 "Appendix D Structure-Level Baseline Adaptation ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

#### Metrics.

We evaluate along five dimensions measuring the quality of analytical-level report generation. Insight rate, the fraction of claims that surface insights beyond what careful reading of the source data would yield (e.g., connecting a revenue decline to a peer’s steeper decline to infer market share gain), is the headline metric. Analysis rate, the fraction of claims containing insights or standard expert analysis (e.g., decomposing that same revenue decline into volume and price components), measures the overall expert-level analytical content in the report. Reasoning depth, the mean analytical hops per claim, measures whether the gain comes from deeper inference chains. Factual precision, the fraction of numerical values correct against the source, ensuring analytical depth does not trade off correctness. Win rate, the rate at which the generated report is preferred over or tied with the expert reference, judged by two LLM personas (analyst, investor) under order-swapped trials. Judgments use Gemini-3-Flash; protocol details
and reliability checks are in Appendix [E](#A5 "Appendix E Metric ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation"), where the LLM judge’s claim labels agree with human annotators at a level comparable to inter-annotator agreement, and human and judge insight rates correlate at the report level.

|                  |                         |              |              |              |             |              |
| ---------------- | ----------------------- | ------------ | ------------ | ------------ | ----------- | ------------ |
|                  | Configuration           | %insight     | %analysis    | depth        | %factual    | %win         |
| Axis             | Full pipeline (default) | 23.8         | 63.1         | 2.61         | 97.2        | 99.6         |
| Representation   | Single-field            | 20.3 (+3.5)  | 58.1 (+5.0)  | 2.50 (+0.11) | 98.2 (-1.0) | 99.2 (+0.4)  |
| Two-field        | 23.9 (-0.1)             | 62.1 (+1.0)  | 2.57 (+0.04) | 96.6 (+0.6)  | 97.6 (+2.0) |
| Retrieval target | Reference text          | 19.3 (+4.5)  | 56.8 (+6.3)  | 2.48 (+0.13) | 96.4 (+0.8) | 100.0 (-0.4) |
| Integration      | Skip per-Analysis gen.  | 19.2 (+4.6)  | 57.9 (+5.2)  | 2.52 (+0.09) | 98.1 (-0.9) | 99.6 (0.0)   |
| Composition      | Transcript only         | 13.0 (+10.8) | 49.1 (+14.0) | 2.39 (+0.22) | 98.6 (-1.4) | 97.7 (+1.9)  |
| Signals only     | 11.1 (+12.7)            | 45.4 (+17.7) | 2.21 (+0.40) | 98.8 (-1.6)  | 96.6 (+3.0) |
| Findings only    | 25.1 (-1.3)             | 65.9 (-2.8)  | 2.70 (-0.09) | 94.1 (+3.1)  | 96.5 (+3.1) |

## 6 Results and Discussions

#### Main Results.

Table [2](#S4.T2 "Table 2 ‣ Stage 4: Composition. ‣ 4 Narrative Generation with AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") reports results across all conditions. AnalysisBank lifts insight rate by 1.7–3.7×\times over all baselines. AnalysisBank consistently outperforms all baselines:

On DataTales, insight rate (first column) rises from a best-baseline range of 9.2–14.0% to 21.1–26.1%; on Earnings2Insights, from 6.4–7.7% to 18.0–23.8% for the three non-GPT backbones. Baselines cluster in a narrow band regardless of prompting strategy: on DataTales with Qwen3-8B, insight rate rises by 2.4–5.9×\times, analysis rate by 1.3–2.1×\times, and reasoning depth by 0.4–0.7 hops, while factual precision remains comparable (89–97% across conditions) and win rate reaches 60–100%.
Baselines cluster in a narrow band regardless of method: across all backbones, prompting methods fall within 4–16% insight rate of each other, and the structural-level methods (BoT, AWM) do not escape this band despite distilling from the same 550-report corpus, indicating a ceiling on insight for methods operating at the structural level.

To verify that insight gains stem from the library mechanism rather than prompting effects, we analyze 30 instances with the largest insight-rate gap between AnalysisBank and direct prompting. First, 80.4% of AnalysisBank’s novel claims trace to a retrieved _Analysis_ (44% strongly, 37% partially), confirming the library as the primary driver of novel content. Second, for 58% of these claims, the baseline either omits the same signal entirely (25%) or mentions it only generically (34%). The remaining 42% cite the same data but do not draw the analytical inference AnalysisBank makes, illustrating the selection challenge: the data is available but the right analytical move is not applied. Table [4](#S6.T4 "Table 4 ‣ Main Results. ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") shows a representative traced claim alongside the baseline’s treatment of the same input. Third, AnalysisBank covers 4.6 distinct signal types per instance vs. 0.83 for the baseline, a 5.5×\times gap. AnalysisBank produces novel insights across a wider range of data signals rather than concentrating on the most prominent one.

|                                   |                                                                                                                                                                                                                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Retrieved _Analysis_              |                                                                                                                                                                                                                                                                               |
| _signal_                          | A company reports a very large amount of cash generated after necessary investments, and this amount is growing rapidly, while another well-known company with a much larger overall valuation generates only moderately more of this same type of cash flow.                 |
| _move_                            | Compare the company’s cash generation level and growth to that of a significantly larger peer by relating each company’s cash flow to its overall valuation, and use this comparison to assess how efficiently the company converts its value into cash relative to the peer. |
| Report generated for PARA_q1_2022 |                                                                                                                                                                                                                                                                               |
| Ours                              | “Operating cash flow grew 34% YoY to $347M, but it represents only 31.5% of the peer’s $1.1B, suggesting lower cash flow efficiency.”                                                                                                                                         |
| Direct                            | Does not cite operating cash flow figures or any peer comparison.                                                                                                                                                                                                             |

The gain is smallest for GPT-5.1 on Earnings2Insights, where Direct and CoT already reach 14–16% insight rate natively, leaving less headroom for the library. On DataTales, where no analysis is stated in the raw price and volume input, GPT-5.1 still gains 2.1×\times (22.3% vs. 10.5%), matching the lift on weaker backbones.

#### Human Evaluation.

We perform two human evaluations to check that LLM-based metrics reflect genuine quality. To validate insight quality, two human annotators independently ranked 30 report triplets (AnalysisBank, best prompting baseline, BoT) by insight quality, blind to method identity. AnalysisBank is preferred in 96.7–100% of pairwise comparisons on Earnings2Insights and 63.3–86.7% on DataTales, confirming that AnalysisBank produces more insightful reports across both benchmarks. Annotators agree on which report ranks first in 66.7% of sets, with most disagreements concerning the ordering of the two baselines, which independently confirm the structural-level ceiling observed in the automated metrics.

To validate factuality, a human audit of sampled claims checks the content beyond the numerical values covered by %factual: AnalysisBank contradicts the source in 4.7% of claims on the stronger backbone, below the pooled baseline, with the higher rate on Qwen3-8B tracking the reasoning capability that valid inference requires. Protocols and full results for both evaluations are in Appendix [F](#A6 "Appendix F Human Evaluation Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

### 6.1 Ablation Study

Table [3](#S5.T3 "Table 3 ‣ Metrics. ‣ 5 Experiments ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") isolates the contribution of each design choice by changing one axis at a time from the full pipeline (Qwen3.5-9B, Earnings2Insights).

#### Representation.

Reducing to a single field (raw reference text only) drops insight rate by 3.5 points. Two analyses reveal why. First, at a cosine threshold of 0.85, the abstracted data_signal index retrieves 20×\times more library entries than reference_text, whose concrete prose produces a sparse embedding space with few retrievable neighbors. Second, 90% of entries retrieved via data_signal come from a different sector than the input, compared to 44% for reference_text, which clusters within the source domain. Abstraction makes the library globally reusable rather than locally bound. The two-field variant (fusing data_signal and analytical_move into one field) recovers most of the insight rate with a small drop on win rate (2 points), suggesting that separating the retrieval key from the generation instruction may further improves output quality.

#### Retrieval target.

Retrieving on reference_text instead of data_signal drops insight rate by 4.5 points. Because reference_texts are concrete prose, similarity is driven by surface wording rather than by whether the stored pattern fits the input. For example, the input “E&I delivered a 6% volume increase” retrieves an entry whose reference span cites “a growth rate of 6% annually”. The two share wording but not pattern: the analytical move retrieved converts forward expectations into an implied growth rate, while the input reports an actual change, so the move is not executable. Across reports, only 36.4% of the moves retrieved on reference_text are executed, against 52.8% for data_signal, which selects the more applicable move on 80% of reports.

#### Integration strategy.

Skipping Stage 3 (per-_Analysis_ generation) and passing retrieved _Analyses_ directly to composition drops insight rate by 4.6 points. The analysis_move is an imperative that must be executed against the input’s signals, not merely supplied as context; without this execution step, the composer defaults to the generic analytical moves that characterize the baseline ceiling.

#### Composition input.

Removing findings (the Stage 3 outputs produced by executing
each retrieved analytical move) from Stage 4 halves insight rate to 11–13%, while the findings-only condition preserves it at 25.1%. This confirms that executed analytical moves, not raw input or the data signal extracted, derive insight content. The full pipeline adds signals and transcript for factual grounding: precision recovers from 94.1% to 97.2% and win rate from 96.5% to 99.6%, a deliberate trade-off for a modest 1.3-point insight cost.

### 6.2 Cross-Domain Transferability

The extraction pipeline and _Analysis_ representation are designed to be domain-agnostic: the move typology, abstraction procedure, and quality filter make no assumptions specific to finance. To test this, we apply AnalysisBank to SciGen [Moosavi et al. (2021)](#bib.bib32), a scientific paper generation benchmark, extracting _Analyses_ from its training set and evaluating with Qwen3-8B against BoT and AWM on the same corpus (Figure [5](#S6.F5 "Figure 5 ‣ 6.2 Cross-Domain Transferability ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

The pattern partially replicates. AnalysisBank achieves the highest analysis rate (65.7% vs. 61.2% for BoT and 48.5% for AWM) and win rate (65.1%), confirming that the three-field decomposition transfers without architectural changes. On insight rate, BoT slightly edges AnalysisBank (17.9% vs. 16.7%), a reversal from the financial benchmarks where AnalysisBank leads by 1.7–3.7×\times. We attribute this to the nature of scientific writing: the dominant analytical moves (methodology comparison, result interpretation, limitation identification) are fewer and more predictable than in financial analysis, reducing the long-tail advantage that drives AnalysisBank’s gains on DataTales and Earnings2Insights. BoT’s full-report templates are better matched to this more uniform move distribution, while AnalysisBank’s per-_Analysis_ decomposition adds coverage in the tail that SciGen’s narrower move vocabulary does not reward as strongly. The key result is nonetheless positive: the extraction pipeline produces a functional library from a non-financial corpus, and the resulting reports achieve the highest overall quality without domain-specific adaptation.

## 7 Conclusion

Analytical report generation requires more than deciding what a report should cover: it requires determining what analyses the data warrants. Existing methods largely leave this reasoning to model defaults, leading to generic analytical behavior despite differences in report structure. AnalysisBank addresses this gap by retrieving and applying distilled expert _Analyses_ at inference time, substantially increasing the proportion of novel, data-grounded insights across benchmarks and model backbones. Its transfer to scientific writing further suggests that operating at the analytical level may generalize beyond finance to other forms of expert, data-grounded reasoning.

Two directions extend this work. First, the current pipeline applies each _Analysis_ independently in a single pass, but expert analysis is both iterative and compositional: one finding may trigger further Analyses, and some insights require chaining multiple moves into a compound finding. Iterative retrieval-generation ([Shao et al., 2023](#bib.bib33); [Trivedi et al., 2023](#bib.bib34)) and analysis composition ([Press et al., 2023](#bib.bib36)) offer natural mechanisms but remain unexplored for analytical generation. Second, expert reports pair analysis with visualizations, yet the current pipeline produces text only. Extending the _Analysis_ representation with visualization specifications ([Yang et al., 2026](#bib.bib35)) would enable multi-modal reports.

## Limitations

The quality of the _Analysis_ library is bounded by the expert reports it is distilled from. If the source reports are formulaic or lack deep analytical reasoning, the resulting _Analyses_ will reflect those limitations. While our quality filter mitigates some of this risk, the pipeline cannot produce analytical patterns richer than what the source corpus contains. Our experiments are conducted exclusively on English corpora. The extraction pipeline relies on LLM-based abstraction and generalization, and its effectiveness on other languages has not been tested. AnalysisBank is designed for reports requiring data-specific analytical reasoning. For domains where a standard, fixed set of analyses suffices, the analytical-level approach offers limited advantage over structural-level methods, as the long-tail coverage that drives AnalysisBank’s gains would not be needed.

## Ethical Considerations

The expert reports used for _Analysis_ extraction are publicly available financial documents. We release only the distilled _Analyses_ and extraction code, not the source reports themselves, to respect the intellectual property of the original authors and publishers.

Our automated evaluation relies on LLM-based judgment. Human evaluation involved two voluntary annotators from the authors’ professional network who ranked system-generated reports without compensation; no personal data was collected.

Generated reports may contain analytical errors or unsupported inferences. We strongly recommend human review before any investment decision is based on system-generated content, and advocate for human-AI collaboration where the system augments rather than replaces expert judgment. Any deployment of this technology should clearly disclose that reports are AI-generated to ensure transparency for readers and stakeholders.

## References

## Appendix A Extraction Pipeline Configuration

This appendix details the hyperparameters, prompts, and implementation choices for the four-pass extraction pipeline (§[3.2](#S3.SS2 "3.2 Extraction Pipeline ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")). The pipeline takes a CSV of expert analyst reports with columns sector, symbol, company, author, date, url, cleaned*text and writes a SQLite-backed \_Analysis* library.

### A.1 Hyperparameters

Pass A tags each identified move with one of seven seed types (attribution, derivation, flagging, comparison, projection, gap detection, and stress test) to steer extraction,
together with three accompanying fields (what_analyst_did, what_triggered_it, result_text).

|                         |                             |                       |
| ----------------------- | --------------------------- | --------------------- |
| Pass                    | Parameter                   | Value                 |
| Pass A (Induce)         | temperature                 | 0.3                   |
|                         | move types                  | 7                     |
| Pass B (Generalize)     | temperature                 | 0.3                   |
|                         | retry budget                | 1                     |
| Pass C (Deduplicate)    | temperature                 | 0.2                   |
|                         | cluster threshold (cosine)  | 0.88                  |
|                         | max cluster size            | 30                    |
|                         | cross-batch dedup threshold | 0.85                  |
|                         | embedding batch             | 100                   |
|                         | clustering algorithm        | greedy single-linkage |
| Pass D (Quality-filter) | temperature                 | 0.1                   |
|                         | criteria                    | 3 (transferable,      |
|                         |                             | actionable, grounded) |
|                         | retry budget                | 1                     |

### A.2 Pass A: Induce

Pass A issues one LLM call per report. The system prompt frames the task around three properties of an analytical move (active reasoning, non-trivial output, transferability) and requests a JSON list of moves. Malformed items missing any of the four required keys are silently dropped. The output is a per-report list of candidate moves; reports yielding no moves are skipped.

### A.3 Pass B: Generalize

Pass B issues one LLM call per candidate. The system prompt requires a JSON object with exactly the three fields used by the rest of the pipeline (data*signal, analytical_move, reference_text) and includes an explicit transferability test (“would this description match the same situation in a hospital, a retailer, and a defense contractor?”). The pass is callable with a retry_instruction that is appended to the system prompt; this slot is used by Pass D to request targeted re-generation when a \_Analysis* fails the transferability or actionability check.

Source metadata is attached deterministically after Pass B completes: sector, symbol, company, date, url, and author are copied from the CSV row, and the reference_text is wrapped with a trailing source label “— <company> <date>” before being stored as the first element of the reference_texts list.

#### Retry instructions used by Pass D.

### A.4 Pass C: Deduplicate

Pass C has two stages: a deterministic clustering step on embeddings and an LLM merge step per cluster. Candidates are embedded by their data_signal using text-embedding-ada-002 in batches of 100. Clustering is greedy single-linkage on the unit-normalized embeddings: each candidate is assigned to the first existing cluster whose centroid has cosine similarity ≥0.88\geq 0.88 with the candidate; otherwise a new cluster is opened. Centroids are running means re-normalized after each addition. Clusters larger than 30 candidates are split into chunks of 30 before being sent to the LLM merge step, to keep prompts within context.

The LLM merge step receives the cluster as a JSON payload of (data*signal, analytical_move, reference_texts) triples and is asked to return a merged \_Analysis* per cluster. Reference texts are taken verbatim from the originating candidates rather than from the LLM output, since the LLM was observed to occasionally paraphrase what the prompt required to be verbatim spans. Provenance for a merged _Analysis_ is reconstructed by matching the merged data_signal back to the originating candidates and aggregating per-field via a scalar-or-list rule (single distinct value →\to scalar; multiple →\to list).

For incremental updates against an existing library, Pass C runs a cross-batch deduplication step before clustering: each new candidate is compared by cosine similarity against existing _Analysis_ embeddings, and candidates above the cross-batch threshold of 0.85 are paired with their nearest existing _Analysis_ and sent through Pass C as a targeted merge that preserves the existing _Analysis_’s ID (so downstream stores update rather than insert).

### A.5 Pass D: Quality-filter

Pass D issues one LLM call per _Analysis_ asking for a pass/fail verdict on each of three criteria. The criteria are evaluated independently, but the routing of failures is asymmetric:

Grounded fail →\to discard. A _Analysis_ whose reference span does not show the pattern executed cannot be repaired by re-generation, so it is removed from the library.

Transferable fail →\to retry Pass B with the transferability retry instruction (above). The originating moves are re-sent through Pass B with the appended instruction, re-merged via Pass C, and re-evaluated. If the retry passes all three criteria, the resulting _Analysis_ enters the library with the original ID preserved; otherwise it is discarded.

Actionable fail →\to retry Pass B with the actionability retry instruction. Same loop as above.

Parse failures on the Pass D response are treated conservatively as pass-all rather than discard-all, on the principle that an inability to judge a _Analysis_ is not evidence against it; this affects <1%<1\% of _Analyses_ in practice.

### A.6 Concurrency and Caching

The pipeline parallelizes at two levels: rows of the input CSV are processed in parallel (one thread per row), and within each row Pass B calls are issued in parallel across the moves Pass A identified. All LLM-call results, embeddings, and intermediate candidates are written to a SQLite store keyed by _Analysis_ ID and embedding model identifier, so re-runs of the pipeline skip already-extracted _Analyses_ and already-embedded items. Embeddings for clustering and for cross-batch dedup share the same cache.

## Appendix B Bank Details

![Refer to caption](2609.00818v1/bank_signal_move_heatmap_datatales.png)
![Refer to caption](2609.00818v1/bank_signal_move_heatmap_earnings.png)

We characterize each library along two axes, using one keyword taxonomy per axis, since signals are noun-phrase data conditions and moves are verb-phrase operations. Each taxonomy is a hand-built, ordered list of categories defined by keyword patterns over the data*signal and analytical_move fields, refined against the libraries until coverage stabilized; we assign each \_Analysis* to the first matching category (single-label) and collect non-matches as _other_.
Figures [6](#A2.F6 "Figure 6 ‣ Appendix B Bank Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") and [7](#A2.F7 "Figure 7 ‣ Appendix B Bank Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") show the full signal-by-move distribution for both corpora.

## Appendix C Narration Pipeline Configuration

This appendix details the hyperparameters (Table [6](#A3.T6 "Table 6 ‣ Appendix C Narration Pipeline Configuration ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")), prompts, and implementation choices for the four-stage narration pipeline (§[4](#S4 "4 Narrative Generation with AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")). The pipeline takes a source input (an earnings call transcript with sector tag, or a structured OHLCV DataFrame with a report date and market tag) and produces an analyst-style report.

|                                   |                        |                                                                                                                                                                                                                                                      |
| --------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stage                             | Parameter              | Value                                                                                                                                                                                                                                                |
| Stage 1 (signal extraction)       |                        |                                                                                                                                                                                                                                                      |
| Earnings (LLM)                    | temperature            | 0.2                                                                                                                                                                                                                                                  |
|                                   | mode                   | hierarchical (default)                                                                                                                                                                                                                               |
|                                   | signal types           | 17 (14 presence + 3 absence)                                                                                                                                                                                                                         |
|                                   | per-type cap           | 6–12 (see Table [7](#A3.T7 "Table 7 ‣ Per-type caps and numeric prioritization. ‣ C.1 Stage 1: Signal extraction ‣ Appendix C Narration Pipeline Configuration ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")) |
| Earnings (validation)             | temperature            | 0.1                                                                                                                                                                                                                                                  |
|                                   | error classes          | 6                                                                                                                                                                                                                                                    |
| DataTales (pandas)                | lookback windows       | 1d, 5d, 20d                                                                                                                                                                                                                                          |
|                                   | momentum threshold     | 0.5%                                                                                                                                                                                                                                                 |
|                                   | vol spike / collapse   | 1.5×\times / 0.5×\times hist                                                                                                                                                                                                                         |
|                                   | volume spike threshold | 2.0×\times 20d avg                                                                                                                                                                                                                                   |
|                                   | MA threshold           | 0.5% from 20d MA                                                                                                                                                                                                                                     |
| Stage 2 (retrieval)               |                        |                                                                                                                                                                                                                                                      |
| Top-kk                            | per input              | 5                                                                                                                                                                                                                                                    |
| Retrieval mode                    | default                | per-type                                                                                                                                                                                                                                             |
| Retrieval backend                 | default                | text-embedding-ada-002                                                                                                                                                                                                                               |
| Sector boost                      | multiplicative         | 1.2×\times on match                                                                                                                                                                                                                                  |
| Similarity threshold              |                        | 0.0 (no floor)                                                                                                                                                                                                                                       |
| Triggers per _Analysis_           |                        | up to 2                                                                                                                                                                                                                                              |
| Stage 3 (per-_Analysis_ analysis) |                        |                                                                                                                                                                                                                                                      |
| Temperature                       |                        | 0.4                                                                                                                                                                                                                                                  |
| Mode                              | default                | pattern                                                                                                                                                                                                                                              |
| Parallelism                       |                        | one thread per _Analysis_                                                                                                                                                                                                                            |
| Stage 4 (composition)             |                        |                                                                                                                                                                                                                                                      |
| Temperature                       |                        | 0.5                                                                                                                                                                                                                                                  |
| Mode                              | default (Earnings)     | signals (transcript-free)                                                                                                                                                                                                                            |
|                                   | default (DataTales)    | findings + signals + summary                                                                                                                                                                                                                         |
| Validate-and-retry                |                        |                                                                                                                                                                                                                                                      |
| Temperature                       |                        | 0.1                                                                                                                                                                                                                                                  |
| Quality verdicts                  |                        | high / partial / missing                                                                                                                                                                                                                             |
| Retry trigger                     |                        | quality = missing                                                                                                                                                                                                                                    |
| Retry budget                      |                        | 1                                                                                                                                                                                                                                                    |

### C.1 Stage 1: Signal extraction

The pipeline supports two signal-extraction backends, selected by input modality. Both produce the same output type: a list of (type, fields, span) tuples that drive Stage 2 retrieval.

#### Earnings transcripts (LLM-based).

For transcripts, an LLM extracts 17 signal types: 14 _presence_ signals (margin delta, incremental margin, guidance revision, volume trend, market share, pricing realization, FX impact, forward signal, cash flow, capital allocation, earnings quality, balance sheet, segment mix, management tone) and 3 _absence_ signals (absent mechanism, absent estimate, absent conversion). The hierarchical mode (default) issues one focused LLM call per signal type and runs them in parallel; each call is gated by a keyword-evidence check (e.g. the MARGIN_DELTA call fires only if "margin", "basis point", "bps", or "profitability" appears in the transcript), with absence types having empty keyword lists so they always fire.

#### Per-type caps and numeric prioritization.

Hierarchical extraction is permissive (the per-type prompt asks for _every_ distinct instance), so each type has a post-extraction cap to prevent any one type from saturating the slate. Within a capped type, signals with non-empty numeric fields (e.g. magnitude_pct for VOLUME_TREND, delta_bps for FX_IMPACT) are kept first; non-numeric signals fill remaining slots.

| Type               | Cap | Type                | Cap |
| ------------------ | --- | ------------------- | --- |
| GUIDANCE_REVISION  | 12  | MGMT_TONE           | 8   |
| MARGIN_DELTA       | 12  | PRICING_REALIZATION | 8   |
| VOLUME_TREND       | 10  | SEGMENT_MIX         | 8   |
| FX_IMPACT          | 10  | BALANCE_SHEET       | 8   |
| MARKET_SHARE       | 10  | EARNINGS_QUALITY    | 8   |
| FORWARD_SIGNAL     | 10  | ABSENT_ESTIMATE     | 8   |
| CAPITAL_ALLOCATION | 10  | ABSENT_CONVERSION   | 6   |
| ABSENT_MECHANISM   | 10  | CASH_FLOW           | 6   |
|                    |     | INCREMENTAL_MARGIN  | 6   |

#### Fact validation.

After extraction, every signal is passed through a fact-validation LLM call that checks six error classes against the verbatim supporting span: _geo_scope_ (region-specific figure attributed to the global segment), _period_scope_ (full-year forecast tagged as a quarterly actual), _metric_identity_ (segment-level figure labelled company-wide; guidance figure labelled actual), _composite_split_ (combined dividend + buyback amount assigned to one action), _organic_vs_reported_ (reported growth labelled organic), and _adjusted_vs_gaap_ (non-GAAP figure labelled GAAP). Errors with a confident correction are applied in place; errors without are flagged. The validation prompt is conservative (only flags errors with clear span evidence), and parse failures are treated as pass-through.

#### DataTales (deterministic).

For structured market data, signals are computed directly from OHLCV series in pandas with no LLM involvement. The extractor produces eight signal types: PRICE_MOMENTUM (1d/5d/20d returns above a 0.5% threshold), VOLATILITY_SIGNAL (annualized 20d realized vol versus 60d rolling baseline, classified as spike / elevated / normal / suppressed), VOLUME_ANOMALY (today’s volume versus 20d average), TREND_SIGNAL (close versus 20d MA), TERM_STRUCTURE (front-vs-second-month spread for futures markets), CONTRACT_ROLL (5d-average volume crossover), YIELD_CURVE (2s10s, 2s30s, 3m10s spreads for treasury markets), and CROSS_ASSET (VIX regime and 10Y vs equities for equity markets, USD direction for currencies, Brent-WTI spread for energy). For the equity market only, per-product signals are restricted to a set of primary instruments (S&P 500, Nasdaq Composite, Nasdaq 100, Dow Jones, Russell 2000, VIX, US 10-Year Bond Yield) to prevent the slate from being saturated by individual constituents.

#### Signal validation (span check).

For LLM-extracted signals, the supporting span is verified against the transcript via whitespace-normalized substring match; signals whose span cannot be located are flagged span_hallucinated and dropped. MARGIN_DELTA cause-types are additionally checked against the supporting span; unsupported causes are stripped from the signal rather than flagging it whole.

### C.2 Stage 2: Retrieval

Stage 2 retrieves a slate of k=5k=5 _Analyses_ from AnalysisBank given the signal list. Three retrieval modes and three backends are supported, with the defaults indicated below.

#### Embedding target.

The default retrieves by cosine similarity between signal descriptions and the data*signal field of each \_Analysis*. An ablation retrieves against reference_texts (concatenated with trailing source attributions stripped); this variant is reported in §[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

#### Sector boost.

Each _Analysis_’s similarity score is multiplied by 1.2 if the _Analysis_’s source sector matches the input’s; sector membership is checked as exact match or as set-membership when a _Analysis_ has multiple source sectors. The boost favors in-sector _Analyses_ without hard-filtering out cross-sector ones, since some analytical moves transfer across sectors.

#### Retrieval mode.

The default is _per-type_ retrieval: each fired signal type contributes one representative signal (selected by largest numeric magnitude using a per-type priority list — delta*bps for margin signals, magnitude_pct for volume, both old_guidance and new_guidance for guidance, etc.), and the best \_Analysis* for that representative is added to the slate. Types are processed in order of representative-signal significance, and remaining slate slots are filled by global cosine top-kk to avoid leaving the slate short when fewer than kk signal types fire. The alternative _cosine_ mode applies global top-kk directly without per-type structure.

#### Retrieval backend.

The default backend embeds signals and _Analyses_ with OpenAI’s text-embedding-ada-002. Two alternatives are available for ablation: BM25 over tokenized signal and _Analysis_ text, and a local sentence-transformer (all-MiniLM-L6-v2). Backend choice is independent of retrieval mode (e.g. BM25 + per-type is valid). All backends apply the same 1.2×\times sector boost and the same optional similarity-threshold cutoff (default 0, i.e. no filtering on raw similarity).

#### Trigger mapping.

For each _Analysis_ in the final slate, the top-2 signals by cosine similarity to the _Analysis_ embedding are tagged as the _Analysis_’s _triggering signals_; their verbatim spans are passed to Stage 3 alongside the _Analysis_.

#### Embedding cache.

_Analysis_ embeddings are computed once and stored in a SQLite cache keyed by _Analysis_ ID and embedding model. The default data_signal embeddings and the reference-text variant each live in their own cache table, so switching ablation variants does not require re-embedding.

### C.3 Stage 3: Per-_Analysis_ analysis

For each _Analysis_ in the Stage 2 slate, an independent LLM call applies the _Analysis_’s analytical*move to its triggering signals and supporting spans (transcript-side) or to the market data context (DataTales). The prompt forbids section headers and framing language, because Stage 4 imposes structure. Calls are issued in parallel across \_Analyses* via a thread pool.

The user prompt assembles three blocks: PATTERN, the analytical_move to execute; SIGNALS, the triggering signals serialized as JSON (type and structured fields); and EXCERPTS, their verbatim supporting spans.

#### Three reference modes (ablation).

The default mode (pattern) sends only the pattern, signals, and spans, omitting the _Analysis_’s reference_text. The pattern_with_refs mode additionally includes the reference text(s) as a depth and tone anchor, inserted as a REFERENCE EXAMPLES block between PATTERN and SIGNALS. The refs_only mode passes only the reference text(s) and signals, without the pattern — testing whether reference examples alone are sufficient. The ablation isolates which component of the three-field representation carries the analytical depth gain (§[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")).

#### DataTales adaptation.

For DataTales, Stage 3 uses a market-specific system prompt that forbids corporate-earnings language ("management", "guidance", "EPS") and asks for prices, spreads, and time-window references instead. Triggering signals are still the top-2 by cosine, but the supporting context is the deterministic market data summary (§[C.6](#A3.SS6 "C.6 Market data summary (DataTales only) ‣ Appendix C Narration Pipeline Configuration ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")) rather than transcript spans.

### C.4 Stage 4: Composition

A single LLM call composes the per-_Analysis_ findings into a final report. The prompt enforces three structural constraints: an executive summary (3–4 sentences naming takeaway, bull case, and key risk), theme sections with analyst-chosen titles drawn from the evidence, and an investment-recommendations block with horizon-differentiated calls (Next Day / Week / Month) each tagged Long / Short / Neutral with a one- to two-sentence rationale. The prompt directs the writer to treat findings as the analytical backbone and to use signals only for factual gap-filling.

#### Input variants.

Four prompt variants are used depending on what context Stage 4 receives:

_Default (findings + signals)_: the production configuration. Signals fill factual gaps the findings do not cover.

_With transcript_: additionally supplies the raw transcript or market data summary, with a primary rule that the findings still drive structure and the transcript only fills coverage gaps. Used when the deployment can tolerate the additional input length.

_Transcript-only / signals-only / findings-only_: ablations that strip the input progressively, used in the component analysis in §[6.1](#S6.SS1 "6.1 Ablation Study ‣ 6 Results and Discussions ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

For DataTales, the same four variants exist with adapted system prompts that swap earnings vocabulary for market-data vocabulary and that ask for trading-relevant horizon calls (momentum continuation, technical structure, term-structure outlook) rather than equity-analyst horizons.

#### DataTales context augmentation.

On DataTales, Stage 4 prompts may optionally include a _per-entity raw OHLCV block_ (the last 20 rows for each product on or before the report date). This is included automatically in the default mode and in the signals-only ablation when a DataFrame is provided to the pipeline. It is not used in the transcript-equivalent earnings flow.

### C.5 Validate-and-retry

After composition, a per-_Analysis_ validator checks whether each _Analysis_’s analytical pattern was applied in the report. The validator issues one LLM call per _Analysis_ in the slate (in parallel) and emits a JSON verdict with applied (boolean), quality ("high", "partial", or "missing"), and a one-sentence note. Verdicts of missing trigger a targeted re-run: Stage 3 is re-executed for only the missing _Analyses_, the updated findings are merged into the existing findings list, and Stage 4 is re-composed. The loop is bounded by a retry budget (default 1) and terminates as soon as no missing verdicts remain.

The validator uses the same backbone LLM as the rest of the pipeline. Parse failures default to missing=False, quality="missing", which is conservative in the sense that it does not trigger spurious retries but does flag the _Analysis_ as not validated.

### C.6 Market data summary (DataTales only)

For DataTales inputs, a deterministic summarizer converts the OHLCV DataFrame into a human-readable context block used by Stages 3 and 4. For each product on or before the report date, the summary emits: last close, 1d/5d/20d returns, position relative to the 20d moving average, annualized 20d realized volatility, and volume ratio against the 20d average. For futures markets, a term-structure line is appended (front vs. second-month spread with backwardation/contango label). For the equity market, primary instruments get a full paragraph each; secondary products are collapsed into a one-line "sector / other products" summary capped at ten entries.

### C.7 Concurrency and caching

Stage 1 hierarchical extraction, Stage 3 per-_Analysis_ analysis, and validate-stage checks all use thread pools sized to the number of items processed (one thread per signal type, per _Analysis_, or per validation call). LLM responses are cached at the level of (prompt, system*prompt, temperature) tuples; cached calls are served without an API hit, which lets ablations re-use intermediate results across configurations that share earlier stages. \_Analysis* embeddings are persisted to SQLite as described in §[C.2](#A3.SS2 "C.2 Stage 2: Retrieval ‣ Appendix C Narration Pipeline Configuration ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation").

The full default configuration on Earnings2Insights requires roughly 1+17+1+5+1+5=301+17+1+5+1+5=30 LLM calls per report (11 if hierarchical mode condenses to a single call, 1717 for the per-type fan-out, 11 for fact validation, 55 for Stage 3, 11 for Stage 4, 55 for the validator) before any retries; on DataTales it is 5+1+5=115+1+5=11 since Stage 1 is deterministic. Retries add up to 5+15+1 calls per cycle, bounded by the retry budget.

## Appendix D Structure-Level Baseline Adaptation

Buffer of Thoughts (BoT) [Yang et al. (2024a)](#bib.bib11) and Agent Workflow Memory (AWM) [Wang et al. (2025)](#bib.bib10) were originally evaluated on math reasoning and web-agent trajectories respectively. We adapt both to analytical report generation while preserving their native abstraction granularity (one full-report template or workflow per task), so that the comparison with AnalysisBank (§[5](#S5 "5 Experiments ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")) isolates decomposition granularity as the variable under test. Both methods are induced from the same 550-report corpus that AnalysisBank consumes, with the same backbone model for induction and inference.

### D.1 Agent Workflow Memory

AWM induces reusable workflows from training trajectories and injects the relevant workflow into the inference-time prompt.

#### Trajectory representation.

Each expert report in the induction corpus is decomposed into a sequence of (observation, action) pairs by splitting on section headings (markdown headings, bold headers, or colon-terminated section labels). Each pair represents one reasoning step the analyst took: the heading is the observation (the context the analyst was about to write into), and the section body is the action (what was written). Reports without recognisable section structure are split into fixed 400-character chunks. This mirrors AWM’s original trajectory format from web-agent execution traces.

#### Offline induction.

Workflows are induced per GICS sector (eleven sectors for Earnings2Insights; per-market for DataTales). For each sector, up to ten training reports are sampled, decomposed into trajectories, and passed to an LLM with an induction prompt that asks for a 5–10 step numbered workflow capturing the analytical pattern shared across the reports. The induction prompt enforces abstraction (“do not reproduce specific figures from these reports”) and reusability (“apply to any future report for this ticker/sector”). One workflow per sector is stored as a plain-text file in a sector-keyed directory.

#### Inference-time retrieval.

For a new input with ticker tt in sector ss, the workflow is resolved by a four-step fallback: (i) exact ticker match, (ii) exact sector match, (iii) LLM-selected closest peer from same-sector candidates, (iv) LLM-selected cross-sector fallback. Step (iii) uses a structured JSON prompt over a ranked menu of candidate workflows; step (iv) is reached only when sector metadata is unavailable. In our benchmark configuration, step (ii) resolves every test instance, so the LLM-selection fallback is rarely exercised.

#### Inference-time generation.

The selected workflow is injected at the top of the generation prompt as an “Analyst Workflow (induced from past reports)” block, followed by the task description, the source data, and a request to “follow the workflow above as a guide for structuring your analysis [and] adapt each step to the current data.” One LLM call produces the final report. Crucially, the workflow is the only retrieved artifact: AWM does not extract typed signals, does not retrieve multiple patterns, and does not run per-pattern execution before composition.

### D.2 Buffer of Thoughts

BoT maintains a meta-buffer of structured “thought templates” and applies a four-step inference pipeline (problem distillation →\to buffer retrieval →\to template instantiation →\to reasoner instantiation) per task. We use the canonical 5-section template format from the original paper: Key Information, Domain Constraints, Abstract Task Description, Python Logic, and Answer Format.

#### Offline induction.

Templates are induced per training report rather than per sector. For each report in the induction set (sampled at ten per sector to match AWM’s induction budget), the report is passed to an LLM with a thought-distillation prompt that asks for a 5-section template covering the analytical pattern the report instantiates, with all company-specific figures abstracted away. The resulting template is compared against the closest existing template in the buffer via an LLM-judged novelty check; templates judged novel are added, near-duplicates are skipped. The novelty filter prevents the buffer from accumulating paraphrases of the same template while still allowing genuinely distinct analytical patterns to coexist. Templates are stored in a persistent ChromaDB collection with sentence-transformer embeddings (all-MiniLM-L6-v2) of the template text.

#### Inference-time retrieval.

For a new input, an LLM first performs _problem distillation_: it produces a 4-section distillation of the input (Key Information, Domain Constraints, Abstract Task Description, Answer Format) that serves as the retrieval query. Cosine similarity against the meta-buffer returns the single closest template. The retrieved template is then _instantiated_ by a second LLM call, which adapts each abstract section to the current company, period, and data, producing a problem-specific briefing.

#### Inference-time generation.

The instantiated template is injected at the top of the generation prompt as an “Analyst Briefing (Buffer of Thought)” block, followed by the task description and the source data. One LLM call produces the final report. As with AWM, the template is the only retrieved artifact: a single top-down structure covers the whole report, and no per-move retrieval or per-pattern execution occurs.

#### Online buffer update.

The original BoT formulation supports an optional online update that distils each newly produced report back into a template and adds it to the buffer if a novelty check passes. We disable this in the evaluated configuration to keep the buffer fixed and comparable to AWM’s offline-only induction.

### D.3 Why this adaptation is fair

We preserve each method’s native abstraction granularity so that decomposition granularity is the variable under test. Adapting BoT or AWM to retrieve at the move level would convert them into variants of AnalysisBank rather than independent baselines. We do adapt both to consume the same induction corpus as AnalysisBank (§[3.2](#S3.SS2 "3.2 Extraction Pipeline ‣ 3 AnalysisBank ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")), so any performance gap reflects how the corpus is decomposed, not what it contains. The resulting contrast is explicit: at induction, each report yields one workflow or template versus the multiple analytical moves AnalysisBank extracts; at inference, one structure is retrieved top-down versus the slate of move-level patterns AnalysisBank retrieves and composes.

## Appendix E Metric

This appendix specifies the judge models, the per-metric judgment protocols, and the design choices that bear on reliability.

### E.1 Judge models

Two LLM judges are used in the evaluation pipeline:

Theme extractor (Claude Sonnet 4.6). Reads each source input (transcript or market-data summary) once, independently of any generated report, and emits the list of _material themes_ — themes a competent analyst would be expected to address. The same theme list is then reused across every model variant evaluated on that input, so coverage scoring is anchored to a fixed reference rather than re-elicited per condition.

Per-claim and per-report judge (Gemini 3 Flash). Runs claim extraction (Stage 1), reasoning-depth scoring (Stage 2a), data-analytic-style scoring (Stage 2b), theme-coverage matching, factual scoring, and head-to-head preference scoring against expert references. Every judgment uses temperature 0.0 and structured JSON output, with up to three retries on JSON-parse failure.

Both judges are different model families from any of the four evaluation backbones (Qwen3-8B, Qwen3.5-9B, DeepSeek-V4-Flash, GPT-5.1) to reduce self-preference bias in line with recent LLM-as-judge findings.

### E.2 Per-metric protocols

#### %insight and %analysis.

The judge first extracts analytical claims from the report in 80-character-minimum chunks split on paragraph breaks, with boilerplate (executive summary, investment-recommendations sections) stripped before extraction. Each claim is then labelled in one of four categories:

factual: depth-1 claims that restate a number or fact from the source.

novel: a data-specific insight that combines conditions, attributes causes, or projects consequences in a way not directly stated in the source.

standard: an analytical claim that a competent analyst would routinely make from this data.

generic: a claim that applies to any report of this type and does not depend on the specific data.

%insight is novel/(novel+standard+generic+factual)\text{novel}/(\text{novel}+\text{standard}+\text{generic}+\text{factual}); %analysis adds standard to the numerator.

#### depth.

For each extracted claim the judge counts _analytical hops_ — distinct inference steps needed to derive the claim from the source — and emits the chain of hop types (e.g. FACTUAL, COMPARE, ATTRIBUTE, PROJECT). depth is the mean hop count per claim. Depth-1 claims are auto-assigned the _factual_ label and skipped from analytical type scoring, so the two metrics share a single claim-extraction pass and are not double-counted.

#### %factual.

Numerical values in the report are checked sentence-by-sentence against the source. For Earnings2Insights the reference is the transcript itself: for each report sentence containing a financial number, candidate reference sentences are selected from the transcript by content-token overlap (stopwords stripped), and the judge labels each numerical value as CORRECT, INCORRECT, or DONT_KNOW. For DataTales the reference is a structured table of pre-computed values (OHLCV plus derived metrics: 1d/5d/20d returns, 20d moving average, annualized volatility, volume ratio, term-structure spread); every report sentence is checked against the full table without a token-overlap filter, since every entry is potentially relevant. Date/time tokens (years, quarters, ISO dates, day-of-month integers adjacent to month names) are filtered out before scoring so they do not contaminate the financial-value count. %factual is correct/(correct+incorrect)\text{correct}/(\text{correct}+\text{incorrect}) over the full report.

#### %win.

Each model report is judged head-to-head against the expert reference (Seeking Alpha analyst reports for Earnings2Insights, the dataset’s human-written market reports for DataTales) by two personas — _analyst_ and _investor_ — each with its own system prompt and rubric. To control for position bias, each persona judges the pair under both orderings (model first, expert first), yielding 2×2=42\times 2=4 judgments per report. The two ordering outcomes are aggregated per persona by majority: two agreeing outcomes set the persona’s verdict; _model+tie_ resolves to model and _expert+tie_ to expert, treating ties as the weaker signal in either direction; _model+expert_ resolves to tie. %win is reported per persona and as the mean across personas.

### E.3 Reliability checks

To test the claim-level labels against human judgment, two human annotators applied the LLM judge’s claim taxonomy (novel/standard/generic/factual) to 277 claims (10 instances, AnalysisBank and the best baseline), blind to both system identity and the LLM judge’s labels. Table [8](#A5.T8 "Table 8 ‣ E.3 Reliability checks ‣ Appendix E Metric ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") reports the results. Annotators mark AnalysisBank claims as novel significantly more often than baseline claims (15.3% vs. 1.7%) and as analytical significantly more often (51.0% vs. 25.4%), and human and judge per-report rates correlate for both metrics (Pearson r=0.64r{=}0.64 and 0.650.65). On the full-taxonomy taxonomy, the judge agrees with each annotator (κ=0.41\kappa{=}0.41 and 0.470.47) at a level comparable to the annotators’ agreement with each other (κ=0.50\kappa{=}0.50). Agreement is lowest on the novel-vs.-rest cut (κ=0.25\kappa{=}0.25): annotating a single claim as novel is subjective, so we treat the report-level rates as the unit of evaluation.

|                                            | %novel                 | %analysis               |
| ------------------------------------------ | ---------------------- | ----------------------- |
| Human rate: AnalysisBank (%)               | 15.3                   | 51.0                    |
| Human rate: baseline (%)                   | 1.7                    | 25.4                    |
| Δ\Delta (pp) [95% CI]                      | +13.7+13.7 [8.7, 18.3] | +25.6+25.6 [17.8, 33.7] |
| Report-level Pearson rr                    | 0.64                   | 0.65                    |
| Claim-level κ\kappa (inter-annotator)      | 0.25                   | 0.49                    |
| Full-taxonomy κ\kappa: LLM judge–annotator | 0.41, 0.47             |                         |
| Full-taxonomy κ\kappa: inter-annotator     | 0.50                   |                         |

## Appendix F Human Evaluation Details

### F.1 Insight quality

#### Sampling.

For each benchmark, we rank all Qwen3-8B test instances by the insight-rate gap between AnalysisBank and the best baseline, then stratify-sample 5 instances from each tercile (top, middle, bottom), yielding 15 sets per benchmark (30 total). Each set contains three reports: AnalysisBank, the best prompting baseline (CoT for DataTales, Direct for Earnings2Insights), and BoT.

#### Protocol.

Two annotators judge each set. Reports are labelled A, B, C with method identity hidden and presentation order randomized per set. Annotators rank the three reports from 1 (most insightful) to 3 (least insightful), with no ties allowed. The instruction defines insight as “substantive, non-obvious analytical content—e.g., specific causal explanations, comparisons, projections, or implications grounded in the input—rather than generic commentary, restated facts, or boilerplate language.”

#### Results by benchmark.

Table [9](#A6.T9 "Table 9 ‣ Results by benchmark. ‣ F.1 Insight quality ‣ Appendix F Human Evaluation Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") reports consensus pairwise outcomes (both annotators combined).

| Benchmark | Comparison             | Win | Loss | Win%  |
| --------- | ---------------------- | --- | ---- | ----- |
| E2I       | AnalysisBank vs Direct | 29  | 1    | 96.7  |
| E2I       | AnalysisBank vs BoT    | 30  | 0    | 100.0 |
| DataTales | AnalysisBank vs CoT    | 26  | 4    | 86.7  |
| DataTales | AnalysisBank vs BoT    | 19  | 11   | 63.3  |

#### Inter-annotator agreement.

Table [10](#A6.T10 "Table 10 ‣ Inter-annotator agreement. ‣ F.1 Insight quality ‣ Appendix F Human Evaluation Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation") reports inter-annotator agreement with bootstrap 95% CIs (N=30N{=}30). Annotators agree on the top-ranked report in 66.7% of sets (chance: 33.3%) and on the pairwise preferences in 90.0% (vs. prompting) and 70.0% (vs. BoT) of comparisons; agreement on the middle rank (36.7%) is near chance. Cohen’s κ\kappa (0.37 vs. prompting; 0.13 vs. BoT) is lower than raw agreement because AnalysisBank wins most comparisons and κ\kappa is deflated under skewed label distributions [Feinstein and Cicchetti (1990)](#bib.bib42).

|                                 |          |                            |
| ------------------------------- | -------- | -------------------------- |
| Statistic                       | Estimate | 95% CI                     |
| Rank-1 agreement                | 66.7%    | [48.8,80.8][48.8,80.8]     |
| Rank-2 agreement                | 36.7%    | [21.9,54.5][21.9,54.5]     |
| Rank-3 agreement                | 50.0%    | [33.2,66.8][33.2,66.8]     |
| Exact full-ranking match        | 33.3%    | [19.2,51.2][19.2,51.2]     |
| Mean Spearman ρ\rho             | 0.483    | [0.283,0.667][0.283,0.667] |
| Raw agreement (vs. prompting)   | 90.0%    | [74.4,96.5][74.4,96.5]     |
| Raw agreement (vs. BoT)         | 70.0%    | [52.1,83.3][52.1,83.3]     |
| Win: AnalysisBank vs. prompting | 91.7%    | [83.3,98.3][83.3,98.3]     |
| Win: AnalysisBank vs. BoT       | 81.7%    | [71.7,91.7][71.7,91.7]     |

### F.2 Factuality

We complement %factual with a human evaluation on a small sample covering both numerical and non-numerical claims: 564 claims, sampled as in the human–judge agreement study (Table [8](#A5.T8 "Table 8 ‣ E.3 Reliability checks ‣ Appendix E Metric ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")) across AnalysisBank and the baselines on Qwen3-8B and DeepSeek-V4-Flash, are each labelled _supported_, _contradicted_ by the source, or _unverifiable_ (blind to system identity; annotator fixed across backbones). We report the contradiction rate (Table [11](#A6.T11 "Table 11 ‣ F.2 Factuality ‣ Appendix F Human Evaluation Details ‣ AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation")); the baselines’ novel claims are too few for a meaningful rate and are skipped. On the stronger backbone, AnalysisBank’s contradiction rate is low (4.7% over all claims; 9.4% on novel claims) and below the pooled baseline (6.6%). On Qwen3-8B it is higher (15.3%; 28.6% on novel claims) while the baseline is stable (5.5%): valid inference tracks the reasoning capability of the backbone, most strongly for novel claims. Most novel claims are unverifiable against the source alone (61–69%), as they state content the input does not.

|                   | AnalysisBank   |              | pooled baseline |
| ----------------- | -------------- | ------------ | --------------- |
| Backbone          | all claims     | novel claims | all claims      |
| Qwen3-8B          | 15.3% (23/150) | 28.6% (8/28) | 5.5% (7/127)    |
| DeepSeek-V4-Flash | 4.7% (7/150)   | 9.4% (3/32)  | 6.6% (9/137)    |

![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

**Tip:** You can select the relevant text first, to include it in your report.

Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

![Simons Foundation](/static/base/1.0.1/images/funders/simons-foundation.png)
![Simons Foundation International](/static/base/1.0.1/images/funders/simons-foundation-international.png)
![Schmidt Sciences](/static/base/1.0.1/images/funders/schmidt-sciences.png)
