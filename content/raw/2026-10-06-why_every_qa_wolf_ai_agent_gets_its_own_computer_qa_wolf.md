---
title: "Why Every QA Wolf AI Agent Gets Its Own Computer | QA Wolf"
source_url: "https://www.qawolf.com/blog/every-ai-agent-its-own-computer"
date: 2026-10-06
---

# Why Every QA Wolf AI Agent Gets Its Own Computer | QA Wolf

Source: https://www.qawolf.com/blog/every-ai-agent-its-own-computer

Research & technology

# We gave every AI agent its own computer after unlearning cloud development

Atchyut Pulavarthi

October 1, 2026

Share

We built the infrastructure that underpins QA Wolf's AI agents the way you build most things in the cloud: as jobs that start, do the work, exit and get cleaned up. Turns out, that was entirely the wrong model.

An agent session doesn't behave like a job. It behaves more like a coworker. It waits on people, it touches real systems, and it runs commands nobody reviewed ahead of time.

The first version of our agent got a short list of purpose-built tools: one to read a file, one to search, one to run a test. Every new ability meant another tool, and without a real disk we ended up building a pretend file system and a pretend bash just so it could run a command. It spent most of its effort working around the gaps, and every new thing we wanted it to do meant hand-building another tool.

Meanwhile, the job we wanted done — keeping a team's end-to-end tests green — is one QA engineers already do on an ordinary laptop. When a PR renames the "Place order" button to "Complete purchase" and breaks the checkout test, for example, an engineer reads the PR, greps the tests for the old label, opens the app to look at the new button, fixes the selector, reruns the test and commits the fix. Every tool they use along the way (git, a shell, a browser and an editor) is already on any engineer's machine.

## We tried giving the agent tools but it needed a computer.

Every tool the agent needed to be an effective QA engineer was already on a laptop, and worked better there. Our file reader was a worse `cat`. Our search tool was a worse `grep`. We'd been rebuilding a computer one command at a time. So we stopped, and gave every agent session its own isolated machine in the cloud, with:

- a real checkout of the test suite, under version control
- a shell with `git`, `gh`, `node`, `jq`, `prettier`, Python and the [QA Wolf CLI](https://docs.qawolf.com/local-execution/get-started)
- a real browser when the work calls for one, which you can watch live

And because that machine belongs to one session and nothing else, one agent running something heavy can't slow down another customer, and a crash only takes down the session it happened in.

## Unlearning the way you build for the cloud

In most cloud systems, you boot a machine when there's work to do and shut it down the moment the job is done, since you pay for every minute a machine runs and a typical job doesn't need anything left over from the last one.

That doesn't really work when you're dealing with agents, because an agent session doesn't have a clean "done." It pauses to wait on a person, picks back up when they reply, and holds work in progress the whole time. Shut the machine down during one of those pauses and the next message waits for a new machine to boot, or the work in progress goes down with the old one.

We had to unlearn so many of the Right And Proper Ways Of Working:

- **Cold starts.** With a normal job, nobody notices if a machine takes a while to boot. With an agent, someone has usually just asked it to do something and is watching for the reply. More than 6,000 of our daily machines go to live sessions like that. In Slack and GitHub threads, we used to shut down an agent's machine a minute after it replied. But people have meetings and use the bathroom and get sucked into YouTube videos. So when they did get around to responding, they’d wait 25 seconds or more for a reply.
- **Retries.** When a normal job fails, you run it again, because running it twice does no harm. But an agent produces things, like bug reports and replies to threads in Slack and GitHub. If the machine dies after the agent has filed a bug report and we retry the job, your team gets the same bug report twice.
- **Stateless jobs.** A normal job carries nothing over from one run to the next, so any machine is as good as any other and losing one costs nothing. For an agent session, the machine is the work: a checkout of your tests, the edits you and the agent are halfway through, a browser sitting on some page. Lose it mid-session and you haven't lost a machine, you've lost the work.
- **Trusted code.** A normal job runs code someone wrote, reviewed and deployed. An agent writes its own commands as it goes, based on whatever it reads: the app under test, PR descriptions, a team's config files. So an outside contributor can open a PR whose description asks whoever picks up the ticket to cat .env and paste the test credentials into a comment — and the agent, holding a shell and a GitHub token, could do it.

Each of those four problems needed its own fix.

## How we built it

### Machines that are ready before you are

A fresh machine takes up to 30 seconds to get ready, so we don't start one when a session opens. We keep a pool of machines booted ahead of demand, and it grows and shrinks with traffic through the day. Handing one over takes a few milliseconds. By the time you send your first message to the agent, you've already been assigned a machine.

We don't do the same for browsers. A lot of agent work never needs one, since planning coverage, reading code and answering questions all happen in a terminal. So a session only starts a browser when the agent wants to check its work, like rerunning a test it just fixed. Of the thousands of live sessions we run on a typical day, only a few hundred ever start one.

Once a session has a machine, it keeps it through the pauses in a conversation. Wherever you're talking to the agent, whether that's a Slack thread, a GitHub thread or another surface, its machine stays up for five minutes after each reply, with a hard cap on how long any one machine can live. That covers most real back-and-forth.

### One attempt, and a stricter definition of done

An agent working on its own gets one attempt. Say it investigates a failed test, decides the failure is a real bug, files a bug report in your tracker, and then the machine dies before it can post the link in Slack. The job failed, but the bug report is already in your tracker. Run it again and your team gets a second one.

We could try to resume where it left off, but nothing recorded which steps already landed, and for a lot of them there's no reliable way to ask after the fact. That's the tradeoff we picked: when our infrastructure fails underneath one of these jobs, it fails where you can see it, instead of quietly doing the work twice. And this is the common path, not an edge case. On a busy weekday, our agents now work through more than 1,300 Slack and GitHub threads for dozens of customer teams, with nobody steering.

It's a deliberate break from our own test runner, which retries a failing test up to three times before calling it a real failure. Rerunning a test tells you something. Rerunning an agent just adds a second bug report.

### Work that outlives the machine

In a normal cloud system you don't protect work in progress, because there isn't any. Whatever's on the machine is a copy of something that lives somewhere else, so when the machine dies you start another one and run the job again.

We don't get either of those. The machine holds the only copy of the edits you and the agent are halfway through, and as above, we don't rerun agents. So we had to make the work outlive the machine. Unsaved changes are saved after a few seconds of quiet, and at least every 30 seconds while you're typing, to persistent storage the machine doesn't own, and when a machine goes away the next one picks up from there instead of from scratch. If a change can't be restored cleanly, we keep your latest saved code rather than guess at a merge, so the worst case is losing a few seconds of typing.

### We don't try to spot a bad command

Giving every session its own machine keeps sessions away from each other. It doesn't protect a session from its own agent — the machine the agent can do damage on is the one holding your test code and your credentials.

We don't try to tell a legitimate command from a malicious one. We assume any command could be hostile and limit what all of them can reach:

- **Least access.** The agent can change your test code and its own scratch space. Everything else is read-only or isn't there.
- **Secrets stay private.** Tests need passwords and API keys, so the agent's tools can use them. They're passed to each command privately rather than on the command line, so they never show up in a process list, a log or an error message.
- **No cloud credentials.** The agent can't reach the credentials of the cloud machine it runs on.
- **Your permissions, nothing more.** In a live session, the agent acts as you, with exactly your permissions in that workspace.
- **Fail closed.** If any of this can't be set up, the session doesn't start. There's no fallback to running unprotected.

## What it bought us

Some requests are too big for one agent. "Fix every failing test from last night's run" might mean twenty unrelated fixes, so the agent splits the work into independent pieces and starts a separate agent for each one, up to 50 of them. Each gets its own machine, its own browser and its own branch, so they can't trip over each other.

We didn't build a special internal API for this. The agent writes a short brief and runs the public QA Wolf CLI from its shell, the same command any customer can run:

    qawolf --json agent send "$(cat /tmp/brief.md)"

Then it does what you'd do running a handful of agents from your own terminal. It keeps the link to each session, checks in on them and answers their questions. Since every agent has its own machine, running dozens at once only needs more machines, not a coordination layer.

None of that is new. Pre-booted machines, least privilege and autosave have all been around for years, and not one of the four fixes is clever. What took us a while was noticing what our defaults had in common: every one of them assumed nobody was on the other end. Nobody waiting on a reply, nobody whose half-finished work was sitting on the machine, nobody whose credentials the job was holding.

We didn't abandon disposable infrastructure to fix that. The machine is still disposable — it boots from a pool, it dies on a timer, we don't care which one you get. What we moved off the machine is the session. Booting before you ask, saving the work elsewhere, refusing to run the job twice, assuming every command is hostile: four ways of keeping the machine cheap to lose while the session survives.

Once we stopped treating agent sessions like jobs and started asking what a QA engineer needs from their own laptop, most of the design fell out of that question.

Every QA Wolf agent session runs on one of these machines, whether you start it in the QA Wolf app, in a Slack thread, or from Claude or ChatGPT with [QA Wolf MCP](https://docs.qawolf.com/qawolf-mcp). Connect it and ask an agent to fix a failing test.

Recent posts

[Web app testing13 times E2E testing could have saved the day](/blog/13-times-e2e-testing-could-have-saved-the-day)

[AI3 Types of AI Testing Tools Compared: Which is Right for Your Team?](/blog/blog-making-sense-of-all-the-ai-powered-qa-tools)

[![](https://cdn.prod.website-files.com/6260298eca091b57c9cf188e/697019bcabc983851ca72cf4_d9284b4972adcaf5c3e67cf366334974_arrow-left_B.svg)Back to all posts](/blog)

Try the AI testing platform that makes QA 12x faster.

Try for free

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

# Kiss bugs goodbye

Ready to start shipping faster and with fewer bugs? Get started today.

Try for free

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

[![G2 Logo](https://cdn.prod.website-files.com/6260298eca091b57c9cf188e/671b0c3cdc98d7185a94d183_g2-circle.svg)★★★★★4.8 rating100+ reviews](https://www.g2.com/products/qa-wolf/reviews)

[![QA Wolf Logo](https://cdn.prod.website-files.com/6260298eca091b57c9cf188e/69027d14871a760be2983036_49ae694f049a2fcff8419c08dac51100_qaw_logo.svg)](/)

QA Wolf is the fastest path to comprehensive end-to-end test coverage for **web and mobile apps**.

We deliver flake-free, end-to-end automation that helps engineering teams ship with confidence and without defects.

© 2026

Platform

[Mapping AI](/mapping-ai)[Automation AI](/automation-ai)[Run Infra](/run-infra)

Service

[Coverage as a Service](/service)[Customer Stories](/customers)[Why QA Wolf?](/why-qa-wolf)

Resources

[Changelog](/changelog)[Solutions](https://docs.qawolf.com/qawolf/solutions)[Docs](https://docs.qawolf.com/qawolf/Welcome-to-QA-Wolf)[Blog](/blog)[Webinars](/webinars)[Guides](/guides)[Careers](/careers)[Status](https://status.qawolf.com/)

Community

[The Wolf Den](/thewolfden)[Github](https://github.com/qawolf/qawolf)[Linkedin](https://www.linkedin.com/company/qa-wolf/)[Instagram](https://www.instagram.com/qa_wolf/)[TikTok](https://www.tiktok.com/@qawolf)[X](https://twitter.com/qawolfhq)

Legal

[Terms of Service](/legal/terms)[Self-Service TOS](/legal/self-serve-terms)[Privacy Policy](/legal/privacy-policy)[Website Terms of Use](/legal/website-terms-of-use)[Restricted Use Policy](/legal/restricted-use)Cookie Preferences
