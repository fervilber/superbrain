---
title: Source - 2026-08-22-replacing-node-agent-graph
source_url: https://www.netic.ai/blog/replacing-node-agent-graph-with-open-source-llm
date: 2026-08-22
---

Skip to main content

[](/)

Product

[ConvertNever miss a lead, never miss a dollar.](/convert)[CultivateCampaigns that run themselves.](/cultivate)[EmpowerEmpower strategic decisions with data.](/empower)[EvaluateIntelligent call scoring for your call center.](/evaluate)[Expand (soon)](/expand)

Industries

[Home Services](/industries-home-service)[Pest Control](/industries-pest)[Roofing](/industries-roofing)[Consumer Health](/industries-consumer-health)[Veterinary](/industries-veterinary)

Careers

[Roles](/company#open-roles)[Netician Stories](/netician-stories)

[Company](/company)[Customers](/customer)

Resources

[Events](/events)[Press](/press)[Engineering](/engineering)

[Book a demo](/book-a-demo)

## We replaced our 223-node agent graph with a single open-source LLM

Aug 20, 2026

•

Netic

Ajay Arora

![](https://cdn.prod.website-files.com/67d1b2757aed7051cae78460/6a8757968b4abd84d19ffe2b_netic-agent-graph-hero-1920x768.png)

When Netic initially began exploring new voice agent architectures six months ago, we tested a wide variety of complex harnesses, from graph approaches to planner sub-agents to swarms and codifying conversational flows. None of these solved the main problems with voice agents today: they take too long to respond, they loop, they deflect instead of answering, and they miss things a human would instantly catch.

With the release of flagship models like Kimi K2.6 and GLM 5.2, we’ve seen for the first time that open-source LLMs can handle 100s of operating procedures concurrently in context while adjusting on the fly to the nonlinear nature of human conversations.

Today, Netic’s agents book at over 15 points higher on containment and appointment booking than they did just three months ago. Time to first token has halved to under 500ms. This post explains the guiding principles behind our decision to switch to a single LLM architecture and how we orchestrate our voice agents to achieve over $500M in autonomous job bookings for our customers.

## A brief history

Netic started encoding Standard Operating Procedures (SOPs) as a graph in 2024. Every step in a procedure became a node, with edges gated by conditions. Some were boolean checks over variables extracted from the caller's speech. Others were natural-language conditions evaluated turn by turn. Existing members, after-hours requests, or any other category got its own branch. In an era when LLMs frequently hallucinated instructions, writing procedures in code let us out-perform competing vendors on reliability.

As we grew, the complexity and volume of procedures we supported began to grow too. Single if-else conditions became if-elif-elif-elif-else chains, and edge conditions stopped fitting in one readable sentence. Under vague, real-world caller speech, the agent started choosing wrong branches, so we added dedicated classifiers: intent classifiers, ownership classifiers, trade classifiers, etc. These first lived on our backend behind tool calls, but as the product matured, we built them into the orchestration layer as classifier nodes to remove network hops.

The conditions kept misfiring on real speech anyway. This example of a caller trying to buy a full system replacement (a high revenue job) shows where it veered off-path.

Transcript

Customer

New furnace and new air conditioning.

Agent

Just so I understand, are you looking for an estimate to install a new furnace and air conditioner, or do you need service on your current systems?

Customer

I need financing for… oh.

mention of "financing" → escalation edge

Agent

Since it's after hours, I'll need to leave a message for a team member to call you back about financing and your new furnace and air conditioner.

Customer

We need this as soon as possible. I have five kids and a baby.

Agent

I understand, that sounds stressful with little ones at home. Since it's after hours, I do need to leave a message for our team…

The fix was a band-aid commit: “stop escalating when financing is mentioned on new-system calls." As models improved, we kept building primitives to facilitate these classifier patches and stitch new agentic capabilities onto a growing graph. But two years later, this became unsustainable, and failures would keep emerging from the graph architecture.  
‍

### **Guiding Principles**

The system we run today is simple yet effective: one agent, with the full conversation history and a procedure library it loads from as the conversation develops. It runs on a single open-weight model which streams out dialogue and thus gives us control over our own inference.  
‍  
Behind it are four principles:  
‍  
1\. **Constrain outcomes, not paths.** Determinism lives at the tool boundary, at the points of irreversible action. The conversation itself has no prescribed shape.  
2\. **The model sees everything.** Full conversation history and the relevant procedures in context. Most of our graph-era failures were context starvation in disguise.  
3\. **Instructions over primitives.** Ordering and policy are stated once as procedure text. Current models follow them reliably enough that structural enforcement is redundant.  
4\. **One agent per conversation.** Context never fragments across specialists, and there is no handoff to go wrong.

We derived these lessons from watching a graph architecture break down over two years in production.

### **Why graphs fail at conversation**

The failures we saw compress into four mechanisms, and each one reflected one of the principles above.

‍\*\*1\. Constrain models, not paths

‍\*\*A graph forces a commitment to a classification at the moment you have the least information, when the caller first speaks. Real callers reveal what they need gradually, out of order, and often after the system has acted on a best guess.

A representative call:

Transcript

Customer

It's got no electric.

triage → ELECTRICAL branch

Agent

Got it. Sounds like you're dealing with an electrical issue. Let me see what we can do to help.

Customer

No. No. It's no. It's the boiler. It's the boiler.

Agent

Understood. It's an issue with the boiler. Let me confirm your details…

Customer (moments later)

No. Boiler. You got the wrong…

Agent

I see, let me correct that. Could you confirm the age of your boiler?

Customer

Old. It's really old.

In this trace, the agent verbally accepted the correction twice, but the system state never changed. After triage fired on "no electric," the graph moved forward, with no edge back. The job was booked days out as an electrical service while a customer had no heat.

The fix here was an edge routing backwards. But that edge would mean another condition evaluated against live speech, requiring weeks of tuning until it fired properly. A graph assumes a call moves forward, so correcting an unpredictable one meant fighting the architecture every time.

‍\*\*2\. The model sees everything

‍\*\*Each node in a graph-based approach intentionally sees only the context its authors wired into it. While this maintains great reliability, it also means the answer to a caller's question is often held by a different node than the one they're speaking with.

A caller whose AC has stopped working, deciding whether to pay for emergency service:

Transcript

Customer

Okay, before anything, how much is the emergency visit?

Agent

Based on what you're describing, we do have emergency service available for this. A technician would be notified right away and reach out as soon as possible. Would you like to move forward with emergency service, or would you prefer regular scheduling?

Customer

You said that. I'm asking what it costs.

emergency-offer node: no pricing in context; pricing gated behind accepting the offer

Agent

Based on what you're describing, we do have emergency service available for this. A technician would be notified right away…

Customer

How much will it cost?

Agent

Based on what you're describing, we do have emergency service available for this…

Though the price existed in our system, the node offering the service didn't have it in context. It couldn't reach the node that did without the customer first accepting the offer, and it repeated the script six times until the customer hung up.

When a model is confined to a node with a handful of instructions, without context or an exit for an unexpected situation, it can only invent an answer or repeat itself.

‍\*\*3\. Instructions over primitives

‍\*\*A graph approach requires enumerating every conversational situation as an edge, and each new edge is another place for the next call to fall through. By the end, we were maintaining 223 nodes and 646 edges. Taken to its limit, that gradient produces a complete graph, where every node connects to every other one. You get a single agent with extra steps and worse latency.

Every new customer exacerbated the maintainability problem. Graphs were assembled from shared components, so a branch tuned for one customer had to be rewired for the next, while an override written early would silently miss refinements the shared components picked up later.

Standing up a customer required learning a large vocabulary of primitives, which made the graph itself an onboarding bottleneck. Stating policy in natural language, by contrast, requires no per-customer wiring and leaves nothing to drift.

‍**4\. One agent per conversation  
‍**  
A brief experiment with multi-agent systems didn’t remedy these problems. A subagent system is a graph at coarser granularity, meaning each specialist is a node holding partial context and each handoff is an edge chosen on incomplete information. Handoffs also require summarizing the conversation before passing it along, but there isn’t time for that on a live call. A summary of a two-turn trace is barely smaller than the trace itself.

Specialists answered questions that belonged to other specialists by paraphrasing general knowledge. Because a handoff never happened, the booking agent quoted one process on one run and a different one on the next when asked about pricing structure. Specialists also declined capabilities the system had. In one session, a subagent whose tool roster lacked location confirmation scheduled a job to an address the customer had moved out of.

The deeper problem is that a specialist cannot recognize it is stuck on its own. Once a handoff is made, recovery depends on the wrong specialist diagnosing its own misfit and handing back. Futility is only visible from outside its own context. In one conversation, a customer texted to cancel service because they had sold their house, and the cancellation specialist called the wrong tool twenty-five times despite receiving the complete job history early on. No agent in the system could see the loop; the run ended when the framework's recursion limit killed it, and the customer left: 'I don't have time for this, bye.' Orchestrators and their specialists drift out of sync, since each holds its own picture of the conversation, and every handoff is a chance for those pictures to diverge.

### Why change now: the models caught up

While we were patching edges, the frontier suddenly moved beneath us. One weekend, as a fun experiment to establish a baseline, we concatenated every subagent prompt, routing rule, and procedure into a single prompt. We then gave it to one agent without a graph, orchestrator, or any classifiers underneath it.  
‍  
We were pleasantly surprised. The single agent handled the calls that had been filling our incident tracker, absorbing late reveals and mid-call corrections the graph couldn't, because it had the full conversation and the full procedure set in context at once. We immediately began building evaluation infrastructure to measure it properly, starting from everything-in-context as the floor, then optimizing what sits in context and when.  
‍  
Instruction following ability crossed the quality threshold for real-world calls in closed models in 2025, and open-weight models have since caught up. That shift, along with model mastery of benchmarks like TauBench, is what enabled our production decision. (We'll cover our internal benchmarks behind it in a follow-up post). Running open-weight also means running our own inference, which is what lets reasoning at low effort fit inside a voice latency budget.

We built a proprietary harness to make an open-weight approach work in production, since even a strong model still needs its context loaded and actions gated. It holds the procedure library, decides what loads into context and when, guards every irreversible action before it executes, and runs regression evals behind every change. We shifted from constraining the model to provisioning it; a model that can see the whole call doesn't need a graph telling it where to go.

The numbers moved accordingly. Containment rate, the share of calls our agent finishes without handing off to a human, and booking rate on bookable calls have both gone up 15 points. Time to first token dropped from over a second to roughly 500ms. Now, standing up a new customer takes one hour instead of days.

### **Looking Ahead**

We're super excited about the capabilities of flagship models and their ability to handle long-running tasks. We fully believe that giving an LLM the context it needs and verifying what it does _is_ enough in 2026 to hold the principles above without the structure that used to hold them. As they get better and better, we will further be able to remove even more abstractions that fill in their remaining capability gaps.  
‍  
We've found the existing literature on voice-agent specific harnesses to be minimal and hope this post kicks off more open discussion in the space. Long-running coding agents can checkpoint and retry sections, run subtasks in parallel, inspect intermediate state, rewrite code, and gate expensive steps behind guardrails, all while nobody waits on the line. A conversation on the other hand gives you one shot in front of the customer - every sale rides on getting it right the first time.  
‍  
 _We're hiring engineers who enjoy tackling intelligence problems like this. If harness engineering for real-time voice interests you,_[_let’s talk_](https://www.netic.ai/company#open-roles) \_.

Netic _[\_builds the AI revenue engine_](https://www.forbes.com/sites/richardnieva/2026/07/28/next-billion-dollar-startups-2026/) _for essential services businesses. We serve HVAC, electrical, plumbing, pest control, consumer wellnesswellness centers, veterinary care, and other industries that form the backbone of the American economy. One platform acts as the intelligence layer across a company's entire revenue operation, from answering inbound calls to running autonomous outbound campaigns to booking the job. We work_[ _directly_](https://www.netic.ai/customer-stories/hoffmann-brothers) _with enterprise-grade operators, and build around their systems and operational rules they already run on._

## Transform the backbone

of our economy

Join us in bringing frontier AI to the industries that keep America running.

[Open Roles](/company)

[![](https://cdn.prod.website-files.com/67d1b2757aed7051cae78460/683b17fb978fcd7ee4f2ce1b_Netic%20Brandmark%20Green.png)](/)

Product

[Cultivate](/cultivate)[Convert](/convert)[Empower](/empower)[Evaluate](/evaluate)[Expand (soon)](/expand)

Industries

[Home Services](/industries-home-service)[Pest Control  
](/industries-pest)[Roofing](/industries-roofing)[Consumer Health](/industries-consumer-health)[Veterinary](/industries-veterinary)

About

[Company](/company)[Roles](/company#open-roles)[Netician Stories](/netician-stories)[Blog](/press)

Connect

[Book a demo](/book-a-demo)[LinkedIn](https://www.linkedin.com/company/netic-ai)[Facebook](https://www.facebook.com/neticai)[X](https://x.com/Netic_AI)

Copyright

©

year

Cybernetic Labs Inc.

[Privacy Policy](/privacy-policy)[Security  
](https://cybernetic-labs.secureframetrust.com/)

![](https://cdn.prod.website-files.com/67d1b2757aed7051cae78460/69051f9c614e3d235df4156f_SOC_CPA_Black.png)
