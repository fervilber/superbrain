---
title: "How we built the agents that built AWS Emulator"
source: "https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator"
date: 2026-11-11
captured: 2026-11-12
---

# How we built the agents that built AWS Emulator

Matthew Goldberg, Sr. Principal Engineer, AWS. Publicado el 11 de noviembre de 2026 (aboutamazon.com). Captura íntegra en bruto de la fuente.

## Key takeaways (verbatim)

- AWS Emulator is a local emulator of AWS services, 100% written by autonomous AI agents.
- Thousands of autonomous agents write tests, find issues, and fix code without human review.
- The source code is available on GitHub under a CC0 license and is constantly being updated.

## Texto de la fuente

> Today, we released AWS Emulator, a local emulator of AWS services that you can run on your machine to build and test your AWS applications. The emulator was written entirely by autonomous agents. Our team hasn't written or reviewed any of the code. We could do this because the guardrails we've put in place gave the agents space to work independently and us the trust that they don't color outside these lines.

### AWS Emulator started as a weekend experiment

> Earlier this year, researchers at Anthropic demonstrated that AI agents could autonomously build a C compiler. This was a lightbulb moment: If given a well-defined spec and a reference implementation, agents can autonomously build a solution that faithfully implements the specification. AWS has both of those; the AWS API Models are our spec and the actual AWS cloud is our reference implementation. To test my hypothesis, I gave Kiro the simplest prompt that I could think of without any expectation that this would work:
>
> 1. Write tests based on the AWS Command Line Interface (CLI)
> 2. Iterate on those tests until they pass against real AWS
> 3. Build an in-memory implementation that those same tests pass against
>
> Kiro came back after 15 minutes with a passable first version of an Amazon Simple Queue Service (Amazon SQS). I refined my prompt and had Kiro build me the rest of AWS over the weekend. And it did. It obviously had gaps, but it was compelling enough that my team started using it to test our software that Monday.
>
> Turning that into a robust product took more than a weekend. There's a natural temptation these days to see results like those and believe that AI can build anything. Maybe it will eventually. But building something that you feel confident putting in your customers' hands still requires serious engineering effort. In the case of AWS Emulator, it required building guardrails that ensure the agents color within our lines.

### How three teams of AI agents build AWS Emulator

> AWS Emulator is fundamentally built by three teams of agents. One team manages a test suite; one team finds issues in the emulator; and one team fixes those issues. We divide agent responsibility into these teams because we've found they have more success on bounded tasks.

> The first team's test suite measures fidelity against the real AWS cloud. Each test is a real-world AWS scenario. For example, a test for Amazon SQS might include creating a queue, sending a message, receiving it, acknowledging it, and deleting the queue. Agents devise these tests from publicly released AWS API Models and verify each one against real AWS before submitting. We have tens of thousands of fidelity tests across all of AWS, and that test suite constantly grows as our agents discover new things that they can do with AWS. These tests are one of our most fundamental guardrails in our system because they provide an unambiguous goal that the agents need to meet and can be rerun repeatedly without calling AWS again.

> The second team of agents replays the fidelity tests to find divergence in the emulator. When the system initially created the repository, it generated an empty web server that could handle requests for the 438 AWS API Models but did nothing. The agents swarm the repository to figure out what doesn't work. To kickstart the process, the first issues simply say "build a first version of Amazon SQS." Once the service is bootstrapped, the agents replay the fidelity tests and file issues for the failing tests. They're told to reason about the failures and group failures that may share a root-cause.

> Each issue is given to an agent in the third team, whose job is to fix that single issue. They check out the code, root-cause the issue, and edit the code until it's addressed. They must then pass their code change through a gate that ensures it meets our bar. This gate obviously blocks changes that don't compile. But it also includes agents that review against coding standards, verify the code is secure, and ensure that the change did not regress fidelity. If any of those checks fail, the change is sent back to the agent for rework; if they all pass, it is merged to mainline. We've seen thousands of issues fixed every day as hundreds of agents concurrently work on the codebase. Without this merge gate, we wouldn't trust what our agents are building. We focus a lot on optimizing it because it's so critical to how quickly and reliably the agents build.

### How AWS Emulator ships to GitHub

> Once merged to mainline, the changes flow through a release pipeline built entirely on AWS Developer Tools, with AWS CodeCommit as the agents' primary code repository. Commits typically stack up together and are built and retested before we merge them to a release branch. We then package up the emulator as a binary that you can download. Only at the end of the release process do we also publish the code to GitHub.

> We release the code to GitHub so that you can also see what the agents have done building this emulator over thousands of commits. Every issue filed is in the repository. The ones they've fixed are in the directory "issues/things-that-now-work"; the ones in their backlog are in "issues/things-that-do-not-work." You'll find fascinating stuff if you dig. We've had our agents build many versions of this emulator as we've refined the building machine. My personal favorite was from an earlier version, when they decided to build their own Python interpreter to support AWS Lambda functions. We've since given them guidance to reuse existing libraries, something that may seem obvious to someone who doesn't need a coloring book. I'm looking forward to what other novel solutions the agents come up with in this version. But I trust the outcome because of our guardrails.

### What's next

> This is the first in a series of posts where I'll dive deeper into topics such as how we architected our multi-agent workflow, how we measure fidelity, and how we ensure our quality and security bar. The source code (github.com/aws/aws-emulator) and fidelity tests (github.com/aws/aws-emulator-evaluation-suite) are both available on GitHub.

## Notas de captura

- Extraído con `web_extract` el 2026-11-12; el texto anterior es la mayor parte íntegra de la página (los bloques de imágenes y el módulo de «Trending news» se omiten).
- Cifras clave: 438 AWS API Models, decenas de miles de tests de fidelidad, miles de issues corregidos por día, cientos de agentes concurrentes.
