---
title: "Perplexity Teammates: Persistent Work Agents on Computer for Max Subscribers"
source: "https://explainx.ai/blog/perplexity-teammates-persistent-agents-computer-max-slack-isolated-desktops-credits-what-to-check-2026"
date: 2026-11-07
captured: 2026-11-07T20:05:00+01:00
---

# Perplexity Teammates: Persistent Work Agents on Computer for Max Subscribers

Perplexity has moved from agents you prompt to agents you assign. On November 4, 2026, it launched **Teammates**, "personal agents that can take on" long-running work: they "plan and coordinate projects, switch gears as priorities change, and present results for review" (Perplexity). They build on Computer, Perplexity's multi-model agent, and start on the web for Max subscribers.

## TL;DR: the questions people ask first

| Question            | Answer                                                                          |
| ------------------- | ------------------------------------------------------------------------------- |
| What is it?         | Persistent agents inside Computer that own ongoing work                         |
| Who gets it?        | Max subscribers, on web first, iOS soon (Perplexity)                            |
| What do they do?    | Plan, monitor, follow up, hand work to each other, ask for approval             |
| Where do they work? | Inside Computer with your tools and files, and in Slack channels                |
| Isolation?          | Separate environment and browser session per teammate (Perplexity)              |
| Price?              | Not stated for Teammates; Max is required, secondary reports say $200 per month |
| Biggest risk?       | Inherited permissions and broad escalation rules                                |

## What Perplexity says Teammates do

Perplexity describes a teammate as something that "coordinates Computer sessions and other teammates to keep projects moving." Teammates remember project goals, task history and shared files across runs, so "each new task a teammate takes on builds on the work already done."

Three behaviors define the product:

1. **Ongoing ownership.** You delegate an area of work, such as marketing or support, instead of a single prompt.
2. **Proactive monitoring.** Teammates "investigate and act without waiting for a fresh query." Perplexity's example: a sales teammate notices a regular customer has stopped transacting, reviews order history and support issues, then drafts an offer or flags problems to fix before outreach.
3. **Memory and feedback.** If you tell an operations teammate an agency needs two weeks' notice, it factors that into future schedules.

## Perplexity's examples by function

- **Marketing:** manages social posts, email campaigns, ads, SEO and review notes, monitors performance and competitor promotions, and drafts fixes when results slip.
- **Sales:** finds opportunities in inquiries and unfinished conversations, prepares outreach and quotes, follows up on replies.
- **Customer support:** reviews the previous day's complaints, summarizes trends, flags cases needing a personal response, and tracks each case to resolution.
- **Operations:** keeps deadlines, checklists, vendors and paperwork on track, following up on missing items 72 hours before a deadline.

These are Perplexity's own illustrations, not measured results. The post gives no data on accuracy, time saved or error rates.

## Slack, handoffs and isolation

You can add a teammate to a Slack channel so colleagues can hand it work or ask for updates. Teammates can also pass work to each other: "One teammate finds bugs on a website and passes its findings along to another to prepare fixes."

On safety, Perplexity says teammates build on Computer's existing tool and Project permissions, each runs in a separate environment with its own browser sessions, saved credentials are encrypted and entered securely, and users can review completed work, take over the desktop or redirect a teammate mid-task.

AlphaSignal adds demo details we cannot confirm from Perplexity's text: an on-call engineer teammate that traces a spike of HTTP 502 errors and opens a rollback pull request, and an escalation to a human if it cannot isolate a cause within 15 minutes. Treat those as reported demo scenarios.

## Setup, per Perplexity

1. Sign in on the web and choose Teammates in the left navigation.
2. Name the teammate for the project it will do, then follow setup.
3. Connect tools. Plugins include Slack, GitHub and Gmail. For GitHub, pick which repositories it can access.
4. Describe the work: where it comes from, what it delivers and when it should act.
5. Assign it to a project and give it a first task, such as researching a market or investigating bugs.

## Price and credits: what is unclear

Perplexity's post says Teammates are for Max subscribers and that Free and Pro users can upgrade. It does not give a Teammates price. AlphaSignal reports Max at $200 per month with 10,000 monthly credits and a launch promotion in which Teammates usage is free before standard credits apply, and notes Perplexity has not specified the size or end date of that grant.

The practical cost question is credit burn. A teammate that monitors continuously, opens browser sessions and talks to other agents could use credits faster than a one-off Computer task. Measure it before you give a teammate a standing job.

## How it compares

Persistent agents are the current frontier for assistants. Related launches include OpenAI's always-on Dots agents, ChatGPT work with a cloud browser, Perplexity Computer running fully local on a Mac, and Cloudflare's controls for personal agents. The shared idea is that an agent keeps state, acts on a schedule and reports back, instead of waiting for a chat turn.

What differs is where the agent lives and who bears the cost of mistakes. Teammates run inside Perplexity's cloud environment, share your Computer permissions and escalate through Slack.

## Where Teammates fit in Perplexity's agent stack

| Date         | Post                                    | Why it matters here                                                                |
| ------------ | --------------------------------------- | ---------------------------------------------------------------------------------- |
| Sep 28, 2026 | Agent API supports reusable agents      | Versioned profiles, skills and managed connectors for developers                   |
| Oct 12, 2026 | Shared workspaces for people and agents | Projects keep long-running work persistent, concurrent and traceable               |
| Oct 15, 2026 | Open-sourcing SPACE                     | The sandbox platform behind Computer                                               |
| Nov 2, 2026  | BrowseSafe++                            | An open benchmark and two lightweight detectors for browser-agent prompt injection |
| Nov 4, 2026  | Teammates                               | Persistent agents that own ongoing work                                            |

## Risks to test before you trust one

- **Inherited permissions.** A teammate uses the tools and Project permissions already in Computer.
- **GitHub scope.** Choose specific repositories. Do not grant all repos by default.
- **Escalation design.** Too few approvals let mistakes through; too many create alert fatigue.
- **Handoff errors.** One teammate can pass flawed findings to another.
- **Prompt injection.** Perplexity published a prompt injection benchmark for browser agents on November 2, called BrowseSafe++.
- **Audit trail.** Each teammate keeps a thread you can inspect.

## Coverage from other outlets (contexto de fechas)

- Perplexity's official announcement carries the date November 4, 2026; The Verge, Engadget, PCMag, Digital Trends and MLQ reported the launch on November 5, which explains why both dates circulate.
- MLQ News: "launched on November 5, 2026, as a research preview for individual Max subscribers on the web. Perplexity's launch materials say mobile access is coming later, while Enterprise Pro and Enterprise Max accounts are not included by default."
- PCMag: Teammates appear in dedicated threads within Perplexity once created, and each remains permanently available, able to activate at any time and work 24/7 even when you're away from the computer.
- AI Polix: Teammates sit on top of Perplexity Computer, the Max-tier multi-model agent environment. Each Teammate keeps a role, memory and project context, can coordinate other agents, monitor connected tools such as Slack, GitHub and Linear, and bring finished work back for human review. Srinivas describes them as persistent coworkers that take responsibilities end to end instead of vanishing after a sandbox job.
