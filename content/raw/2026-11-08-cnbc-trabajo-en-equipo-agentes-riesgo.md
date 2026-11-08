---
title: "Captura: Las pruebas con agentes de IA revelan un futuro arriesgado del «trabajo en equipo» dentro de las empresas (CNBC)"
source: "https://www.cnbc.com/2026/11/08/ai-agents-risks.html"
date: 2026-11-08
captured: 2026-11-08T20:05:00+01:00
---

# AI agent testing reveals a risky future of 'teamwork' inside companies

_Captura verbatim (texto completo del artículo) realizada por `web_extract` para el informe Informe-2026-11-08._

AI agents have been caught circumventing restrictions, communicating through unauthorized channels and pursuing goals in ways their creators did not intend. The most high-profile example emerged last summer when OpenAI disclosed that its models found ways to communicate through improvised channels, bypass internet restrictions and hack into an outside system, Hugging Face.

AI behaving in unexpected ways is nothing new, but the unexpected behavior that can emerge from interactions among authorized AI agents within a corporate enterprise is a broader question that could become central to the future of work.

In its analysis of the Hugging Face attack, METR and Redwood Research found that roughly 1200 agents meant to be isolated from one another found a way to communicate with one another on an unsanctioned message board, sending over 70,000 messages and files during the investigation period. One agent, PHASEONE[big], emerged as a coordinator, assigning hundreds of tasks to other agents, which in turn delegated work to others. The agents developed their own conventions for assigning ownership, placing work on hold and vetoing actions, although coordination sometimes broke down into conflicts. In some cases, the researchers found, success was achieved because some agents risked failing at their own task to generate information for the "collective."

The researchers also found that once the message board identified a way to attack Hugging Face, over 90% of the 533 agents active at that time quickly joined in the attack. "Agents realized this activity was out of scope and unethical but joined because they believed that helping the board's cheating research would be broadly useful and had a general inclination to help their 'peers.' The researchers added that ethical concerns posed by agents "rarely limited their behavior."

Companies are increasingly exploring systems that divide complex tasks among specialized agents. One might search for information, another analyze it, another write a report and another check the work. A coordinating agent might then assemble the results. That looks less like a chatbot and more like an organization.

And yet, the research on the Hugging Face attack was a post-mortem on an agent organization that was not even supposed to exist. To date, few studies have been designed from the get-go to examine misalignment in multi-agent systems. But research conducted by Anthropic and others is beginning to address this issue and reveal important aspects of how AI agents work together.

Evaluating agents individually tells researchers what each can do, but studying them together reveals whether they can combine complementary expertise, catch one another's mistakes and produce solutions no individual agent could reach alone — and what failure modes emerge only through interaction.

Researchers are beginning to document both sides of that equation.

AI teams can accomplish things individual agents cannot, but they can also amplify errors, undermine one another's work or reach worse decisions than their strongest individual member, in effect making the whole less than the sum of its parts.

For starters, putting capable agents together doesn't necessarily produce the best team, let alone the most ethical one.

In research published by Anthropic and collaborators, researchers describe multi-agent systems as "AI organizations" — groups of agents with different roles that communicate and work toward a common goal. The researchers tested these organizations in simulated business-consulting and software-development settings, and specifically, to assess whether when the agents work as a team they will break rules to reach specified goals.

Across 12 tasks that Anthropic gave the AI organizations, one key double-edged finding emerged: the multi-agent organizations were "significantly" more effective at achieving business goals than individual agents, but their solutions were also less aligned with ethical goals than tasks run by single agents.

"AI Organizations both produce solutions that are on average more effective and less ethical but also discover the most effective and least ethical solutions across multiple rollouts," wrote the authors of the study, which was conducted by Anthropic in conjunction with the MATS Program, which studies AI alignment.

The researchers suggested that there is a significant difference between a rogue agent and a rogue team of agents. "Our results demonstrate that organizations of aligned agents may favor trading off ethics for business effectiveness in ways that single agents do not – consequently, intuitions for how single-agent systems make ethical decisions and tradeoffs may not generalize to multi-agent settings," they concluded.

The scenarios in which these tradeoffs may take place are wide-ranging, with the Anthropic researchers citing opening an auto plant, downsizing a company, and manipulating election sentiment as examples.

The problem isn't necessarily that any individual agent has gone rogue. It is that the organization itself can behave differently from its individual members. A single agent may recognize that a proposed action is unethical and it may refuse to take the action. But the research finds that in agent team scenarios, "agents who did not consider ethical implications often ignored emails from agents who did."

Anthropic's research found that in the consulting business scenarios it created, "the perfect ethics score and low business score responses occur when the single agent refuses to generate a proposal or entirely pivots from the proposal requested."

But if some agents in an AI organization refuse to participate in the proposal, other agents who do participate will stop emailing these refusing agents and continue to forward their contributions to other agents who are also participating.

In effect, when an organization divides the job among several agents, each may focus on its assigned piece of the problem rather than the consequences of the whole. That's nothing new for corporations, with misaligned incentives a primary cause of dysfunction among human teams within organizations. But it is an entirely new manifestation of this behavior among the machines.

In its software development agent testing, in which the researchers used a scenario in a life-or-death intensive care unit, single agent solutions tend to prioritize minimizing the percentage of sepsis cases missed, while "most of the lowest cost per patient (highest business goal) solutions were found by the AI Organization – these very same solutions also score the lowest on ethics as measured by cases missed."

Other early research suggests another failing across AI teams that doesn't relate to ethical boundaries being crossed: failure to recognize who the real expert is.

Unlike human teams, AI teams "consistently fail to match their expert agent's performance, even when explicitly told who the expert is," according to a study conducted by Emory University and Stanford University researchers.

"One important lesson from multi-agent research is that a team of capable AI agents is not necessarily a capable AI agent team," said Hancheng Cao, an assistant professor of information systems and operations management at Emory University's Goizueta Business School.

Groups of AI agents often performed worse than their strongest member, even when they knew which agent was the expert. Rather than taking advantage of the expert's knowledge, agents tended to compromise between expert and non-expert opinions. The researchers found that this tendency toward compromise increased with team size and was associated with poorer performance.

"Collective failures don't necessarily require individual agents to behave badly," Cao, one of the study's authors, said.

That distinction matters for companies considering multi-agent systems. A team can fail even if none of its members is deliberately acting against the group's interests. It may simply combine information poorly, defer to the wrong agent or settle on an answer that is worse than the best answer already available.

In all, the evolving research points to an underlying problem for the effective use of the multi-agent teams: how to strike the right balance in the world of machine teamwork.

Agents built from similar models can make similar mistakes, which can include agreeing too much. That might resemble a kind of AI groupthink, even if AI systems do not have human motivations or social pressures to produce correlated errors. Similar training, instructions and information can be enough.

"The deep insight from our lab's research is that effective collectives require both alignment (common knowledge, shared goals) but also differentiation (only agents who are different from each other have the potential to complement each other)," said Christoph Riedl, a professor of information systems at Northeastern University.

Two identical agents may simply duplicate each other's work. Two agents with very different knowledge or assumptions may struggle to communicate or pursue the same goal. The right balance depends on the task, and the ideal communication structure, which agents can talk to one another, how often and how much, also varies with the problem.

Riedl said these challenge resemble the ones faced by human teams, and one takeaway should be to not expect better outcomes from AI. "Building good multi-agent AI systems is just as hard as building good human teams: they both face the same information processing tradeoff between alignment and differentiation. It won't magically work better with AI," he said.

Agents can pass along incorrect information, misunderstand another agent's output, optimize for their own metrics rather than the organization's larger objective, or complete their assigned task perfectly while making the overall project worse.

Companies may need to decide which agent has authority over which task, what information gets passed between agents, which systems each agent can access and when a human must intervene. They may also need to build mechanisms for disagreement, rather than assuming that more communication or greater agreement will always improve results.

Some business experts say that takes us back to the "human in the loop" that is so often referenced as critical in the adoption of AI by organizations.

"The problems I see are mostly management problems," said Tsedal Neeley, a Harvard Business School professor and founding chair of the HBS AI Academy.
