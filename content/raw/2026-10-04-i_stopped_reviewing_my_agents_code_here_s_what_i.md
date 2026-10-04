---
title: "I stopped reviewing my agents' code. Here's what I do instead."
source_url: "https://alexeyindeev.substack.com/p/i-stopped-reviewing-my-agents-code"
date: 2026-10-04
---

# I stopped reviewing my agents' code. Here's what I do instead.

Source: https://alexeyindeev.substack.com/p/i-stopped-reviewing-my-agents-code

[![The Leveraged Mind](https://substackcdn.com/image/fetch/$s_!0-Qs!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47068a32-7e91-4fbc-8624-1620bc3dc896_1024x1024.png)](/)

# [![The Leveraged Mind](https://substackcdn.com/image/fetch/$s_!Tzn7!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F075f120e-d29a-4c5e-a7dc-b45e64085512_1201x236.png)](/)

SubscribeSign in

Playback speed

×

Share post

Share post at current time

Share from 0:00

0:00

/

3

## I stopped reviewing my agents' code. Here's what I do instead.

562 PRs in two weeks. The workflow, the guardrails that make it safe, and the exact prompt I use.

[![Alexey Indeev's avatar](https://substackcdn.com/image/fetch/$s_!LUT_!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2ae33c8-68f6-4dfe-88e9-54ee3d2671bc_1152x1152.jpeg)](https://substack.com/@alexeyindeev)

[Alexey Indeev](https://substack.com/@alexeyindeev)

Oct 04, 2026

3

Share

> **Heads up: this one is for power users.** It assumes you already build with coding agents like Claude Code every day and are comfortable with CI, merge queues, and feature flags. If you're earlier in your AI journey, bookmark it for later. The posts in Operate are a better place to start.

Two weeks ago, I changed how I build software. Since then I've merged 562 PRs, and honestly, I spent four of those nights hiking in the mountains.

In the video I walk through exactly how I work now. Below is the written companion: the setup, the prompt, the numbers, and the things to try this week.

If you're still reviewing every line your agent writes, this one's for you.

## The whole workflow in four lines

1. **Set the intent.** Plan with the agent until you agree on what's being built and why.

2. **Set the guardrails.** Tests, CI, and review bots that an agent can't get around.

3. **Set a goal.** One session, one coordinator agent, sub-agents doing the work.

4. **Let it merge in small pieces.** Auto-merge, feature flags, verify, repeat.

## What changed

The models changed dramatically in the last few weeks, Opus 5.5 especially. A couple of weeks ago, I wouldn't have told anyone to work this way. I always felt I had to check the work. Is the quality good enough? Should this get merged?

Now I feel an agent can work through a whole plan on its own, as long as two things are set up right: **the right intent** , and **the right guardrails** to make sure that intent is actually met. Get those right and you can let it really run.

Most of this work went into Sightline, our internal operations platform at Spare. It's where I try everything first.

## Guardrails are the real work now

AI code is non-deterministic and has risk. But human code is non-deterministic too, and it has the exact same risk. We built SRE systems so humans don't make mistakes. Now we need those same systems, way more beefed up, so agents don't make mistakes.

Same blameless culture we use for incidents: when an agent makes a mistake, don't blame the agent. Ask what guardrail was missing, and build that.

This doesn't mean quality stops mattering. Agents make messes too. That's exactly why the guardrails are the job. Here's what every Sightline PR goes through before it can merge:

- **Unit tests**

- **End-to-end tests**

- **CI, Bugbot, Strix**

- **Mergify** won't let a PR into the merge queue until all of the above pass

So when something's queued, I know it couldn't skip a single red flag.

The guardrails also guard themselves. We ask Bugbot to keep asking for more tests. Those feedback loops in CI are what let us go this fast without risking uptime. And when something slips through, we don't just fix the code. We fix the guardrail.

## The workflow, step by step

### 1\. Plan with the agent

Every session starts the same way. I open Claude and work out a plan together: how it's broken up, what the challenges are, what the risks are. I often ask for a UX preview too, so I can see what it'll feel like before anything gets built.

This is where I spend most of my time now. **I review the plan, not the code.**

### 2\. Set a goal, with the same prompt every time

Once I'm aligned on the plan, I open a session and set a goal. This is the prompt I use, word for word:

> Accomplish the plan. Ship code using auto-merge. You're the coordinator. Don't do work directly. Use sub-agents for everything, and parallelize when possible.

### 3\. Keep the coordinator's context clean

The coordinator part helps a lot. The top-level agent only holds the plan and the status, so its context stays clean. Sub-agents do the heavy work and come and go as the plan gets built out.

### 4\. Let it merge, in small pieces

I let it merge on its own, and honestly, it's fairly safe. These models are careful and don't want to break things. Ask them to feature-flag everything and they will. Because they can merge, they ship in small pieces: ship something, run end-to-end tests in staging or production, check that it works, ship the next thing. Multi-stage deploys, small increments.

A bit of a hot take: one big PR you're iterating on locally is probably riskier in the end than twenty small ones that each passed every check.

### 5\. Review progress reports, not diffs

I come back and ask for a progress report. The agent builds an HTML report: what's done, what's next, and what it needs from me. That's what I review.

### 6\. Let it run for days, and run several at once

Here's the part I think most people miss: let goals run overnight, for days if they need to. Our custom roles goal ran for over a day. I checked in periodically, read the report, nudged it when needed, and let it keep going until it actually hit the goal.

I usually have two, three, or four goals running at once, on unrelated features so they don't step on each other. That's what lets us rip through things really fast.

## Ask bigger

Most of us still use these tools like a really fast engineer: implement this ticket, add this endpoint. That works, but it's thinking too small. With the goal workflow you can set much higher-level intent, ask open-ended questions, or hand it a whole business problem and let it figure out what needs to happen.

- Instead of _"add a role editor,"_ the goal was _"make Sightline's permissions work like Spare's everywhere."_

- Instead of _"move OKRs into a package,"_ it was _"turn Sightline into a platform other teams can extend."_

You can push it much further:

- _"Our CI is too slow. Make it faster."_ That's it. Let it find where the time goes and fix it.

- _"We're seeing low PPVH for one of our enterprise customers. Dig into five days of data and figure out how we can optimize it."_ That's a real business problem, not a coding task.

- _"Our front-end UX is inconsistent across the admin panel. Find the inconsistencies and help us remove them."_

Those aren't tickets. They're outcomes. The models are now good enough to take an outcome, break it down, and work toward it for a day or more.

## Capacity: tokens become the bottleneck

Once you work like this, tokens become the bottleneck. Individual plans don't give us enough credits anymore, and the overages are super expensive.

What I've been doing is running multiple Claude accounts, about five at around $200 each, and switching between them with a tool called Claude Swap. It watches five-hour and seven-day usage on every account and switches automatically when one hits 90%, so everything keeps running in the background.

It's not perfect. When you switch accounts you lose things like Claude artifacts and remote control from the mobile app, and I'm constantly logging in again in the browser and on my phone. It wastes time. So this week I've been looking at tools that solve the same problem without the switching: Paseo, Orca, Superset, and a few others.

## Where this is going

Our job is moving away from shipping individual things. It's moving to building the systems that evolve our product. We set the intent, and we build systems that self-heal toward it.

We're already doing it: automations that fix our bugs, automations for SRE work, agents that do vulnerability research, and early work on remediating those security risks automatically. Next are systems that find poor quality, performance issues in the database and rendering, and inconsistencies in our UIs, and agents that fix them. Agents that find gaps in test coverage and write the tests.

It's not us figuring out each individual thing. It's standing up guardrails that keep healing the system into a better place.

## Three things to try this week

1. **Stop checking the code on one real feature.** Start with something low-risk. As you build confidence, try it on something bigger.

2. **Give it a problem, not a ticket.** See how far it gets.

3. **Look at the surface area you're touching.** What guardrail is missing so an agent can't get it wrong? What loop could fix things on its own?

I'd love to hear what's working for you. If you try this, hit reply or drop a comment with what happened. I'll be writing a lot more about how we're building with agents.

Alexey

#### Discussion about this video

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![The Leveraged Mind](https://substackcdn.com/image/fetch/$s_!0-Qs!,w_96,h_96,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47068a32-7e91-4fbc-8624-1620bc3dc896_1024x1024.png)](https://read.aindeev.com)

The Leveraged Mind

Subscribe

Authors

[![Alexey Indeev's avatar](https://substackcdn.com/image/fetch/$s_!LUT_!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2ae33c8-68f6-4dfe-88e9-54ee3d2671bc_1152x1152.jpeg)](https://substack.com/@alexeyindeev?utm_source=author-byline-face-podcast)

[Alexey Indeev](https://substack.com/@alexeyindeev)

### Ready for more?

Subscribe

© 2026 Alexey Indeev · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[ Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture

This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts
