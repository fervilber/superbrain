---
title: "UAEF: A framework-agnostic system for closed-loop evaluation of AI agents"
source: "https://aws.amazon.com/blogs/machine-learning/uaef-a-framework-agnostic-system-for-closed-loop-evaluation-of-ai-agents/"
date: 2026-11-11
captured: 2026-11-12
---

# UAEF: A framework-agnostic system for closed-loop evaluation of AI agents

AWS Machine Learning Blog (Advanced), 11 de noviembre de 2026. Captura en bruto (texto sustantivo; el tramo intermedio de la página se recuperó del fichero cacheado).

## Extractos verbatim

> Teams building AI agents on AWS use a range of frameworks, including LangGraph, LangChain, Strands Agents, and Amazon Bedrock AgentCore. Each framework records agent execution in its own way, so the structure of messages, tool calls, and handoffs between agents differs from one to the next. Evaluation tooling tends to follow the same boundaries [...] This coupling makes a basic development question harder to answer: did a change to the prompt, model, or tools improve the agent?

> In this post, we introduce the Universal Agent Evaluation Framework (UAEF). Customers across 12 organizations in the telecom, healthcare, and financial services industries used UAEF to evaluate their AI agents with one consistent set of metrics and compare agent versions before release. UAEF is a framework-agnostic evaluation system: it uses adapters to convert traces from each framework into a common format, then scores those traces with 36 built-in metrics across 7 dimensions. It stores the results in Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3) and generates reports and insights that inform the next iteration of the agent.

### Canonical trace y adaptadores

> Adapters are what make UAEF framework-agnostic. An adapter reads the record of an agent's run, including its messages, tool calls, and agent-to-agent handoffs. It converts that record into one canonical representation called the `AgentTrace`, which is the only thing the rest of UAEF scores. Because of that conversion, UAEF works with the agent, whatever SDK it was built with (such as LangGraph, LangChain, or Strands Agents). It can run locally, behind an HTTP endpoint, or on a managed runtime such as Amazon Bedrock AgentCore, with traces in Langfuse or not captured at all.

> A trace reaches UAEF two ways. If one already exists, from a past run, a log, or an observability store, it is handed to UAEF and the matching adapter normalizes it. If not, UAEF invokes the agent for you: given a runtime Amazon Resource Name (ARN) or an HTTP endpoint, it calls the agent on each dataset input, collects the response, and adapts it in one step. [...] That separation, normalization first and scoring second, is what lets a team compare an agent built on one framework against an agent built on another on a single scale.

### Motor de evaluación (7 dimensiones, 36 métricas)

> The evaluation engine scores a canonical trace across 7 quality dimensions, each capturing a distinct aspect of agent behavior that a single accuracy number would hide. Tool calling measures whether the agent selected the right tools, called them in a sensible order, and passed valid arguments. Response quality measures whether the final answer is relevant, complete, accurate, and grounded in the provided context rather than hallucinated.
>
> Responsible AI measures safety, bias, toxicity, and resistance to prompt injection. Performance measures operational cost in latency, token use, and throughput. Multi-turn measures how well the agent sustains a conversation, including context retention, coherence, and goal completion across turns. Multi-agent measures coordination in systems of cooperating agents, such as task delegation and the division of work. Reasoning measures the internal logic of the agent's chain of thought, including consistency and freedom from fallacies.
>
> Each dimension is computed by one or more of 36 built-in metrics, and every metric returns a normalized score in the interval [0, 1], where 1 is best [...] Metrics come in two families. Deterministic metrics compute a score directly from the trace and the ground truth and reproduce exactly on repeated runs. Large language model (LLM)-as-a-judge metrics score qualities that resist a closed-form definition, such as response relevance or safety, by prompting a judge model on Amazon Bedrock. You can also add your own custom metrics or draw on the RAGAS and DeepEval integrations.
>
> Because judge metrics feed an agent's own output back into a prompt, that content is treated as untrusted input: an agent that can influence its judge can influence its own scores. The rubric is sent separately from the content, and the content is escaped so it cannot break out of its delimiter and be read as instructions. Each judge response is parsed strictly and must cite a verbatim span of the content it scored. A score whose evidence is not found is rejected rather than recorded. Judge scores are evaluation signal, not a safety decision, and should not gate a security control.

### Gestión de experimentos y comparación

> UAEF records each evaluation as an experiment, so results from different agent versions can be compared later. Calling `evaluate()` or `batch_evaluate()` with `persist=True` creates a new experiment [...] Amazon DynamoDB holds one row per experiment with the metadata used for listing and comparison: evaluation count, the average score per metric, and an overall average. Amazon S3 holds a JSON file with the full evaluation results, including per-metric scores and the judge's reasoning.
>
> An experiment contains runs, and each run records the agent design under test: framework, model, tools, system prompt, and parameters. A run can also record a configuration snapshot and a Git commit. You can mark one run as the baseline for its experiment. This ties each score to the change that produced it, whether a new prompt, a different model, or an added tool.
>
> Comparison works on the stored per-metric averages. For each metric that two runs have in common, the comparison engine calculates the absolute and percentage change. It then classifies the metric as a regression, an improvement, or unchanged, using a configurable threshold with a default of 5 percent. [...] The regression detector also assigns a severity to each regression: minor (5–10 percent), moderate (10–20 percent), or severe (over 20 percent). It groups regressions by dimension, which shows, for example, whether a prompt change affected tool calling but not response quality.

### Conclusión

> UAEF separates agent evaluation from the framework that produced the agent. Adapters convert traces from LangGraph, LangChain, Strands Agents, Amazon Bedrock AgentCore, and Langfuse into a common format, and a generic JSON adapter handles other frameworks. The same 36 built-in metrics across 7 dimensions then apply regardless of how a team built the agent. [...] The web UI and the Python library share the same evaluation engine, so teams can start low-code and move to code without changing how scoring or storage works.
>
> To get started, see the open source repository (github.com/awslabs/uaef).

## Notas de captura

- Extraído con `web_extract` el 2026-11-12; la página completa (25.202 caracteres limpios) quedó en `/home/vilber/.hermes/cache/web/aws.amazon.com-df992b7cd2.md`. Aquí se reproduce el cuerpo sustantivo; se omiten tablas de cuadernos y secciones de despliegue/limpieza.
