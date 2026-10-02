# Benchmarking retrieval for agents on messy real-world company knowledge

URL: https://www.kapa.ai/blog/company-knowledge-bench

---

[](../blog)

# Benchmarking retrieval for agents on messy real-world company knowledge

Introducing Company Knowledge Bench

Oct 2, 2026

Finn Bauer

How teams do retrieval is changing fast, in every domain. Cursor recently stopped [searching your code via embeddings](https://forum.cursor.com/t/what-do-you-think-about-cursor-removing-the-codebase-indexing-settings/165899) in favour of relying only on grep and indexed search. Others are swapping their traditional rerankers for new models like [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

One of the most important kinds of knowledge that agents rely on is company knowledge: documentation, tickets, chat messages, internal wikis, and code. Yet most teams cannot tell which retrieval works best on it, because they have no way to measure how their retrieval performs on real data.

Kapa is a platform for indexing your company knowledge and letting your agents search them for context. You connect your sources, Kapa turns them into one searchable knowledge base, and any agent can query it for the information it needs. Retrieval is the core of what we build, and we change how we do it constantly.

The **Company Knowledge Bench** is what we built for ourselves to improve our own system: 1,000 eval cases annotated from real production data. In this post we explain how it works, and score a few common retrieval implementations on it.

Company Knowledge Bench results: score against time per query

Fixed retrieval, agentic grep and Kapa: 7 retrievers on 1,000 eval cases. Higher and further left is better.

Fixed retrieval (traditional RAG)Agentic retriever with grepKapaBest score for the time

Retrieval score0.40.50.60.70 s5 s10 s15 sTime per query, secondsHybrid search 0.41Hybrid search + rerank 0.50Query decomposition 0.56Kapa Default 0.61Kapa Deep 0.65Agent + grep (Luna) 0.54Agent + grep (Sol) 0.61

The takeaway: a frontier model with nothing but grep matches a tuned modern retrieval pipeline at 0.61, but takes five times as long. An optimized agentic retriever (Kapa Deep) does better still: 0.65 in about five seconds.

A note on bias: retrieval is core to our product, and all seven retrievers were built by us and use documents ingested with our pipeline.

## Why public benchmarks do not work for us

Public benchmarks do not work for us because none of them cover all the use cases and types of queries that we see.

**Use cases**

Teams index their sources in Kapa and connect an agent to the retrieval, and that agent can serve quite different use cases, each with its own documents and its own people asking questions:

- **Developers** ask about a product over its docs, API specs, code and GitHub issues, often through Claude Code.

- **Sales and other employees** ask about products, processes and customers over Slack, Confluence, Notion and Google Drive.

- **Support teams** draft replies to new tickets from old tickets, help center articles and internal handbooks.

**Queries**

As these use cases show, many different kinds of agents send queries to Kapaâs retrieval, and the queries look different depending on who wrote them:

- **People** put everything into one message: several questions, a pasted error, a reference to something said earlier.

- **Agents** like Claude Code write their own, breaking a complex question into short, precise searches, like `webhook retry backoff config`

Public retrieval benchmarks are mostly too narrow, built around one domain like law or medicine, or too artificial, built from synthetic documents and questions. None of them cover this range, so we built our own.

## How we score retrieval for agents

Before we can measure good retrieval, we have to define what it is.

A few terms first. A **query** is what is sent to the retriever. The **corpus** is everything a team has indexed in Kapa. A **chunk** is a short piece of it, such as a section of a page. A **retriever** takes a query and returns the most relevant chunks from the corpus for it.

Our definition:

> The retrieverâs goal is to collect a minimal set of chunks that completely answers the query, using the highest-quality sources available.

The Company Knowledge Bench rests on three properties:

- **Completeness.** The agent you hand the chunks to needs nothing else to answer the query. If the set is incomplete, the agent gives an incomplete or incorrect answer.

- **Minimality.** Removing any chunk would make the set incomplete. Extra chunks the query does not need cost money and make it harder for the model to reason.

- **Source preference.** A corpus often holds several sets of chunks that could answer the same query, and they are almost never of equal quality. Our benchmark only accepts the preferred ones. Deciding which source is preferred is hard and has a lot of grey zones, but in general it comes down to two factors:
  - **Source authority.** A dedicated reference page outranks a tutorial, an issue thread, or a blog post that repeats the same fact.

  - **Currency.** A current source outranks an outdated one. A Slack thread from last week beats a Confluence page last edited three years ago.

Beyond these, the benchmark enforces rules for specific situations. For example:

- **The query is ambiguous.** The retriever has to return chunks for every reasonable reading of it. Picking one reading is the agentâs job.

- **A problem has several valid solutions.** The retriever has to return chunks for each documented solution, so the agent can explain the options and their trade-offs.

- **The corpus holds nothing that answers the query.** The retriever has to return the strongest evidence there is: a statement that the feature is not supported, a complete list the feature is missing from, or a documented workaround. If none of those exists, the right result is nothing at all.

All of it is written down precisely in our benchmark labelling handbook.

## What an eval case looks like

Our benchmark is a set of eval cases. Each one consists of a real production **query** , a snapshot of the **corpus** as it was when the query was asked, and a **retrieval criterion** : a boolean expression that specifies which chunks from the corpus are valid to retrieve for the query.

Here is a simplified eval case, scored against the chunks one retriever returned:

**Query**

     "Which plans include SSO, and how do I turn it on?"


    "Which plans include SSO, and how do I turn it on?"


    "Which plans include SSO, and how do I turn it on?"


    "Which plans include SSO, and how do I turn it on?"

**Retrieval criterion**

    {
      "operator": "AND",
      "operands": ["chunk_1", "chunk_2"]
    }


    {
      "operator": "AND",
      "operands": ["chunk_1", "chunk_2"]
    }


    {
      "operator": "AND",
      "operands": ["chunk_1", "chunk_2"]
    }


    {
      "operator": "AND",
      "operands": ["chunk_1", "chunk_2"]
    }

**Chunks the retriever returned**

    chunk_1  Pricing page
             "SSO is included in the Team and Enterprise plans."

    chunk_2  SSO setup guide
             "To enable SSO, go to Settings > Security, choose your identity
             provider, and paste in its metadata URL."

    chunk_3  Community forum post
             "You get SSO on the Team and Enterprise plans."

    chunk_4  Changelog
             "Dark mode is now available in the dashboard."


    chunk_1  Pricing page
             "SSO is included in the Team and Enterprise plans."

    chunk_2  SSO setup guide
             "To enable SSO, go to Settings > Security, choose your identity
             provider, and paste in its metadata URL."

    chunk_3  Community forum post
             "You get SSO on the Team and Enterprise plans."

    chunk_4  Changelog
             "Dark mode is now available in the dashboard."


    chunk_1  Pricing page
             "SSO is included in the Team and Enterprise plans."

    chunk_2  SSO setup guide
             "To enable SSO, go to Settings > Security, choose your identity
             provider, and paste in its metadata URL."

    chunk_3  Community forum post
             "You get SSO on the Team and Enterprise plans."

    chunk_4  Changelog
             "Dark mode is now available in the dashboard."


    chunk_1  Pricing page
             "SSO is included in the Team and Enterprise plans."

    chunk_2  SSO setup guide
             "To enable SSO, go to Settings > Security, choose your identity
             provider, and paste in its metadata URL."

    chunk_3  Community forum post
             "You get SSO on the Team and Enterprise plans."

    chunk_4  Changelog
             "Dark mode is now available in the dashboard."

**Score**

- **Pass.** The criterion requires chunk_1 and chunk_2, and both were returned.

- **Precision: 2 of 4, or 50%.** chunk_3 and chunk_4 are not in the criterion.

The forum post is not in the criterion because of source preference. It answers the same part of the query as the pricing page, which plans include SSO, and the pricing page has more source authority. The changelog is simply not relevant. Both count against precision, but for different reasons: one is irrelevant, the other is relevant but not preferred.

In total, we created **1,000 eval cases** for the Company Knowledge Bench, and they are what the results later in this post are based on.

## How we created the benchmark

Labelling a thousand eval cases by hand is not feasible. Sampling them properly makes it even harder: the queries come from every type of source we ingest, internal as well as public corpora, and the industries we serve. So to achieve this scale, the labelling has to be done by agents.

Of course, letting agents create the benchmark only works if they do it correctly. A wrong criterion means a wrong score for every retriever we test against it. So before the agents can build our benchmark, we need a second benchmark that measures how well they build it: a benchmark for benchmark creation.

That second benchmark is a set of 170 eval cases that humans labelled completely by hand, following the same benchmark labelling handbook. Each has a real query, a corpus, and a retrieval criterion a person wrote after working through the corpus themselves, so together they encode the handbookâs rules.

So the process was: build agents that can do the same task the humans did for this set, run them on its queries, and compare the criteria they write with the human ones. We kept improving the agents until they reached a high enough agreement rate with the human labellers. Only then did we let them generate the 1,000 eval cases of the benchmark from production queries.

The labelling is split between two kinds of agents:

- **Candidate agents** scan the full corpus for chunks that might belong in the retrieval criterion. They are built for recall and return a large set of possibly relevant chunks.

- **Criteria agents** take those candidates and turn them into the actual retrieval criterion, following the rules in the benchmark labelling handbook.

The agents do not have to reproduce the human criteria exactly for the benchmark to give a good signal, but they do have to come close. Getting there took many iterations, on the agents and on the handbook itself. We made sure the agents reached sufficient agreement with the human labellers, and validated them extensively, before moving on to generate the benchmark.

The result is labels that are close to what a human would write, and unlike hand labels they scale well beyond the 1,000 eval cases we generated for this benchmark.

## How the retrievers compare

We ran seven retrievers on the Company Knowledge Bench. All of them search the same corpora, ingested and chunked the same way, so the only thing that differs is the retrieval strategy.

### Fixed pipelines

These are the traditional RAG approaches of the last few years. They run the same steps for every query, with no model deciding what to do next.

- **Hybrid search.** The baseline most RAG pipelines start from. The query is matched against a keyword index and an embedding index at once, using `gemini-embedding-001` for the embeddings, and the top 15 chunks are returned.

- **Hybrid search with a reranker.** The same search, but it retrieves the top 100 chunks and passes them through a reranker, Voyage AIâs `rerank-2`, which reads the query and each chunk together and scores how well the chunk answers it. The top 15 after reranking are returned.

- **Query decomposition, hybrid search, and a reranker.** Before searching, a model, `gpt-6.1-luna`, splits the query into up to three sub-queries. Each sub-query retrieves its top 50 chunks through hybrid search, and the pooled results are reranked together down to the top 15.

### Agentic retrievers

This is where retrieval is moving. A model drives the search, deciding what to look for next and when it has enough. That used to be too slow and expensive for every query, but models are getting better, cheaper, and faster.

- **Agentic grep, large model.** `gpt-6.1-sol` with a single tool: full-text and regex search over the chunks. No embeddings at all, the way a coding agent explores a repository.

- **Agentic grep, small model.** The same setup with `gpt-6.1-luna`, a smaller and faster model, to see how much the strength of the model matters.

### Kapaâs retrieval

- **Default mode.** Kapaâs faster mode: a fixed pipeline with a small planning step and a strict budget, returning a fixed number of the best-ranked chunks.

- **Deep mode.** Kapaâs retrieval agent. It searches, reads on in documents it has found, and prunes what turns out not to be relevant, returning as many chunks as the query needs.

### Results

To compare the retrievers, we look at them across four dimensions: retrieval score, latency, precision, and how many tokens they return. A retriever that scores well can still be too slow to put in front of a user, or return so much that the agent reading it pays for it on every call.

Company Knowledge Bench results by retriever

Score, time, precision and tokens returned per query. 7 retrievers on the same ingested data, 1,000 eval cases.

Scorehigher is betterTime per querylower is betterPrecisionshare of chunks neededTokens returnedfewer is betterKapa Deep0.655.1 s26%5.1kKapa Default0.613.3 s12%9.9kAgent + grep (Sol)0.6117 s4%40.8kQuery decomposition0.561.8 s10%10.2kAgent + grep (Luna)0.5413 s4%38.8kHybrid search + rerank0.500.7 s9%10.6kHybrid search0.410.4 s8%11.1k

#### Fixed pipelines

**Reranking is the cheapest big win.** Plain hybrid search scores 0.41. Retrieving 100 candidates and reranking them down to 15 lifts that to 0.50, for a third of a second more, no more tokens, and a reranker call that is cheap compared with a language model. If you change one thing in a basic RAG pipeline, add a reranker.

**Searching with several queries helps, at a price.** Splitting the query into sub-queries first lifts the score to 0.56. But it comes with a latency penalty, more than doubling the time to 1.8 seconds, and it adds the cost of a model call to every query.

**An optimized fixed pipeline gets surprisingly far.** You can view Kapa Default as a fully optimized fixed pipeline. It scores 0.61 in 3.3 seconds, the same score as the strongest grep agent in a fifth of the time, with the best precision of any fixed pipeline.

#### Agentic retrievers

**A strong model with simple tools goes a long way.** Throwing a reasoning model at retrieval works well, even when its only tool is grep. `gpt-6.1-sol` reaches 0.61, the same score as Kapa Default, and the smaller `gpt-6.1-luna` reaches 0.54, close to query decomposition.

**For agentic retrievers, intelligence matters.** Swapping `gpt-6.1-sol` for the smaller `gpt-6.1-luna` costs 0.07 in score. Query decomposition, a fixed pipeline, beats the small-model agent on score in a seventh of the time. An agentic loop is not better by default.

What the answering model pays to read what each retriever returns

Input cost per 1,000 queries, with GPT-6.1 Sol as the answering model at $2.00 per million tokens

Kapa Deep$10.16Kapa Default$19.85Query decomposition$20.46Hybrid search + rerank$21.10Hybrid search$22.27Agent + grep (Luna)$77.58Agent + grep (Sol)$81.67

**The biggest caveat with agentic retrievers is cost.** It shows up in latency, with the grep agents taking 13 to 17 seconds per query, and in money, in two places. The first is the retriever itself: the `gpt-6.1-sol` grep agent spends about $0.17 in model calls per query, which at production volumes can be prohibitively expensive. The second is what it returns. Every retrieved chunk becomes input tokens for the agent you hand the result to, and the grep agents return about 40,000 tokens per query, roughly four times as much as any fixed pipeline, with only one chunk in twenty-five actually needed. The chart above prices that second cost. It assumes the agent receiving the retrieval result also runs on `gpt-6.1-sol`, at $2.00 per million input tokens with tokens counted by the `o200k_base` tokenizer, and shows what you pay in inference per 1,000 queries just to read the retrieved chunks once.

**An optimized agentic retriever gets the best of both.** You can think of Kapa Deep as an optimized agentic retriever, built to return only what the query needs. It has the highest score, at 0.65 in about five seconds, and the highest precision, at 0.26 against 0.12 or less for every other retriever. It returns about 5,000 tokens per query, half of any fixed pipeline and an eighth of the grep agents, which also makes it the cheapest for the agent to read, at about $10 per 1,000 queries.

## Whatâs next

Weâve built retrieval benchmarks before, but this is the first that looks like how agents actually use company knowledge, and it shows a lot of headroom left. As enterprises put more agents to work, latency and cost matter as much as accuracy, so weâll keep growing the benchmark and climbing it on all three. Weâll publish more findings as we go, so follow [the blog](https://www.kapa.ai/blog) if youâre curious.

The benchmark is private since itâs built from real production data. If you have questions though, please [reach out](mailto:emil@kapa.ai).

[](../)

Product

[Connect](../product/connect)

[Deploy](../product/deploy)

[Answer Engine](../product/answer-engine)

[Analytics](../product/analyze)

Industries

[Developer Tools](../solutions/for-dev-tools)

[Semiconductors](../solutions/for-semiconductor)

[Software](../solutions/for-software)

[Hardware & Industrials](../solutions/for-hardware-and-infrastructure)

Resources

[Data Security](https://www.kapa.ai/security)

[Trust Center](https://app.vanta.com/kapa.ai/trust/qrse873laj3emze0gfmibm)

[Terms of Service](https://www.kapa.ai/content/terms-of-service)

[Privacy Policy](https://www.kapa.ai/content/privacy-policy)

Socials

[Twitter](https://twitter.com/kapa_ai)

[LinkedIn](https://www.linkedin.com/company/kapa-ai)

[Y Combinator](https://www.ycombinator.com/companies/kapa-ai)

Solutions | Customers

[Website Agent](../solutions/website-agent)

[Support Form Deflector](../solutions/support-form-agent)

[Product Copilot](../solutions/in-product-agent)

[MCP Server](../solutions/mcp)

Solutions | Teams

[For Documentation Teams](../solutions/for-documentation-teams)

[For Support Teams](../solutions/for-support-teams)

[For Product Teams](../solutions/for-product-teams)

[For Engineering Teams](../solutions/for-engineering-teams)

Solutions | Agents

[Agent Framework](../solutions/product-agent-sdk)

[Agent SDK](../solutions/product-agent-sdk)

[Retrieval API](../solutions/agents)

[Hosted MCP Server](../solutions/mcp)

Content

LLMs.txt

[Library](../library)

Kapa Customer Examples

[How Silicon Labs uses Kapa](../customer-examples/silicon-labs)

[How Espressif uses Kapa](../customer-examples/espressif)

[How Nordic Semiconductor uses Kapa](../customer-examples/nordic-semi)

[How Cortex uses Kapa](../customer-examples/cortex)

[How Nokia uses Kapa](../customer-examples/nokia)

[How Reddit uses Kapa](../customer-examples/reddit)

[How Planet Labs uses Kapa](../customer-examples/planet-labs)

[How Logitech uses Kapa](../customer-examples/logitech)

[How Netlify uses Kapa](../customer-examples/netlify)

[How Monday.com uses Kapa](../customer-examples/monday)

[How Coralogix uses Kapa](../customer-examples/coralogix)

[How Redpanda uses Kapa](../customer-examples/redpanda)

[How Mapbox uses Kapa](../customer-examples/mapbox)

[How CircleCI uses Kapa](../customer-examples/circleci)

Â© 2026 Kapa.ai Inc. All rights reserved.

[SOC 2 Type II Certified](https://docs.kapa.ai/security/certifications)

[](../)

Product

[Connect](../product/connect)

[Deploy](../product/deploy)

[Answer Engine](../product/answer-engine)

[Analytics](../product/analyze)

Industries

[Developer Tools](../solutions/for-dev-tools)

[Semiconductors](../solutions/for-semiconductor)

[Software](../solutions/for-software)

[Hardware & Industrials](../solutions/for-hardware-and-infrastructure)

Resources

[Data Security](https://www.kapa.ai/security)

[Trust Center](https://app.vanta.com/kapa.ai/trust/qrse873laj3emze0gfmibm)

[Terms of Service](https://www.kapa.ai/content/terms-of-service)

[Privacy Policy](https://www.kapa.ai/content/privacy-policy)

Socials

[Twitter](https://twitter.com/kapa_ai)

[LinkedIn](https://www.linkedin.com/company/kapa-ai)

[Y Combinator](https://www.ycombinator.com/companies/kapa-ai)

Solutions | Customers

[Website Agent](../solutions/website-agent)

[Support Form Deflector](../solutions/support-form-agent)

[Product Copilot](../solutions/in-product-agent)

[MCP Server](../solutions/mcp)

Solutions | Teams

[For Documentation Teams](../solutions/for-documentation-teams)

[For Support Teams](../solutions/for-support-teams)

[For Product Teams](../solutions/for-product-teams)

[For Engineering Teams](../solutions/for-engineering-teams)

Solutions | Agents

[Agent Framework](../solutions/product-agent-sdk)

[Agent SDK](../solutions/product-agent-sdk)

[Retrieval API](../solutions/agents)

[Hosted MCP Server](../solutions/mcp)

Content

LLMs.txt

[Library](../library)

Kapa Customer Examples

[How Silicon Labs uses Kapa](../customer-examples/silicon-labs)

[How Espressif uses Kapa](../customer-examples/espressif)

[How Nordic Semiconductor uses Kapa](../customer-examples/nordic-semi)

[How Cortex uses Kapa](../customer-examples/cortex)

[How Nokia uses Kapa](../customer-examples/nokia)

[How Reddit uses Kapa](../customer-examples/reddit)

[How Planet Labs uses Kapa](../customer-examples/planet-labs)

[How Logitech uses Kapa](../customer-examples/logitech)

[How Netlify uses Kapa](../customer-examples/netlify)

[How Monday.com uses Kapa](../customer-examples/monday)

[How Coralogix uses Kapa](../customer-examples/coralogix)

[How Redpanda uses Kapa](../customer-examples/redpanda)

[How Mapbox uses Kapa](../customer-examples/mapbox)

[How CircleCI uses Kapa](../customer-examples/circleci)

Â© 2026 Kapa.ai Inc. All rights reserved.

[SOC 2 Type II Certified](https://docs.kapa.ai/security/certifications)

[](../)

Product

[Connect](../product/connect)

[Deploy](../product/deploy)

[Answer Engine](../product/answer-engine)

[Analytics](../product/analyze)

Industries

[Developer Tools](../solutions/for-dev-tools)

[Semiconductors](../solutions/for-semiconductor)

[Software](../solutions/for-software)

[Hardware & Industrials](../solutions/for-hardware-and-infrastructure)

Resources

[Data Security](https://www.kapa.ai/security)

[Trust Center](https://app.vanta.com/kapa.ai/trust/qrse873laj3emze0gfmibm)

[Terms of Service](https://www.kapa.ai/content/terms-of-service)

[Privacy Policy](https://www.kapa.ai/content/privacy-policy)

Socials

[Twitter](https://twitter.com/kapa_ai)

[LinkedIn](https://www.linkedin.com/company/kapa-ai)

[Y Combinator](https://www.ycombinator.com/companies/kapa-ai)

Solutions | Customers

[Website Agent](../solutions/website-agent)

[Support Form Deflector](../solutions/support-form-agent)

[Product Copilot](../solutions/in-product-agent)

[MCP Server](../solutions/mcp)

Solutions | Teams

[For Documentation Teams](../solutions/for-documentation-teams)

[For Support Teams](../solutions/for-support-teams)

[For Product Teams](../solutions/for-product-teams)

[For Engineering Teams](../solutions/for-engineering-teams)

Solutions | Agents

[Agent Framework](../solutions/product-agent-sdk)

[Agent SDK](../solutions/product-agent-sdk)

[Retrieval API](../solutions/agents)

[Hosted MCP Server](../solutions/mcp)

Content

LLMs.txt

[Library](../library)

Kapa Customer Examples

[How Silicon Labs uses Kapa](../customer-examples/silicon-labs)

[How Espressif uses Kapa](../customer-examples/espressif)

[How Nordic Semiconductor uses Kapa](../customer-examples/nordic-semi)

[How Cortex uses Kapa](../customer-examples/cortex)

[How Nokia uses Kapa](../customer-examples/nokia)

[How Reddit uses Kapa](../customer-examples/reddit)

[How Planet Labs uses Kapa](../customer-examples/planet-labs)

[How Logitech uses Kapa](../customer-examples/logitech)

[How Netlify uses Kapa](../customer-examples/netlify)

[How Monday.com uses Kapa](../customer-examples/monday)

[How Coralogix uses Kapa](../customer-examples/coralogix)

[How Redpanda uses Kapa](../customer-examples/redpanda)

[How Mapbox uses Kapa](../customer-examples/mapbox)

[How CircleCI uses Kapa](../customer-examples/circleci)

Â© 2026 Kapa.ai Inc. All rights reserved.

[SOC 2 Type II Certified](https://docs.kapa.ai/security/certifications)

[](../)

Product

Solutions

Resources

[Pricing](../pricing)

[Documentation](https://docs.kapa.ai)

[Sign in](https://app.kapa.ai)

[Get started](https://app.kapa.ai/auth/signup)

[Book a demo](../request-demo)

[](https://app.kapa.ai)

[Get started](https://app.kapa.ai/auth/signup)

[](../)

[Get started](https://app.kapa.ai/auth/signup)
