---
title: "We’re going to need default hard budget caps on pretty much everything"
source_url: "https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/"
date: 2026-10-04
---

# We’re going to need default hard budget caps on pretty much everything

Source: https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/

# [Simon Willison’s Weblog](/)

[Subscribe](/about/#subscribe)

**Sponsored by:** Deepgram — Flux TTS remembers the conversation, so your agent sounds right on reply 20. [Hear the demo](https://fandf.co/4dat4R0)

## We’re going to need default hard budget caps on pretty much everything

3rd October 2026

Here’s a product feature which the world is going to need a whole lot more of over the coming months and years: **default hard budget caps**. I’m talking about the feature of pay-by-usage services and APIs that lets you say “after $X/month, cut this thing off and return errors”. These need to be **hard** limits. Soft caps, “after $X/month, send me a warning email”, will not cut it.

Coding agents, and personal agents (coding agents wrapped in a less threatening UI), greatly reduce the friction of spinning up code that can do useful things. Sometimes those things cost money—calls to paid APIs, or hosted web applications, or systems that can bill for additional storage and compute.

Nobody wants to wake up to an email sent at midnight warning about a budget limit and find that, while they slept, their rogue service had consumed several hundred (or several thousand) more dollars of usage.

An argument against this is that businesses don’t want their hosted applications to start throwing errors because some budget was exceeded. I expect that most businesses and individuals would prefer errors to a surprise $10,000+ bill.

I think hard budget caps need to be the default. If someone wants to live dangerously they should be able to do that, but it needs to be on an opt-in basis. Have a nice, clear checkbox somewhere prominent:

> Remove the budget cap. My application will not be shut down if I exceed the configured budget limit, and I will be responsible for subsequent charges.

The service I most want to see this from is AWS. I’ve heard plenty of stories from people who refuse to use AWS for personal projects out of (justified) fear that a runaway service might bankrupt them. I’ve also heard stories from people who _didn’t_ anticipate this and ended up seriously burned.

... and it turns out AWS finally launched spending limits a few weeks ago! From their announcement [New AWS experience helps builders get started and ship faster](https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience/) on 16th September:

> When you’re ready to upgrade to a paid plan, you can set a monthly spend limit for your project based on your usage patterns so that you stay within your budget. If a project’s usage reaches its spend limit, your project is paused for that month.

See also [Create a spend limit in AWS Settings](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html), though that page warns that “We’re currently releasing our new experience to a limited number of customers.” Here’s hoping that hits general availability for existing accounts soon.

Google Cloud [launched a similar feature](https://cloud.google.com/blog/topics/cost-management/new-early-anomalies-and-spend-caps-on-google-cloud-budgets) in July, called Spend Caps, which lets you “set a monthly financial cap on specific services within a project”. Looks like this is becoming a trend!

In an ideal world, our agents could help with this. It would be great if agents started biasing towards recommending providers with hard budget caps, and warning new and inexperienced builders against deploying applications using uncapped services that might get them into trouble.

Posted [3rd October 2026](/2026/Oct/3/) at 11:34 pm · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## More recent articles

- [OpenAI DevDay 2026 live blog](/2026/Sep/29/openai-devday-2026-live-blog/) \- 29th September 2026
- [2026 in LLMs (so far)](/2026/Sep/27/2026-in-llms-so-far/) \- 27th September 2026

This is **We’re going to need default hard budget caps on pretty much everything** by Simon Willison, posted on [3rd October 2026](/2026/Oct/3/).

[ amazon-web-services 83 ](/tags/amazon-web-services/) [ ai 2,259 ](/tags/ai/) [ coding-agents 254 ](/tags/coding-agents/)

**Previous:** [OpenAI DevDay 2026 live blog](/2026/Sep/29/openai-devday-2026-live-blog/)

### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[ Sponsor & subscribe ](https://github.com/sponsors/simonw/)

- [Disclosures](/about/#disclosures)
- [Colophon](/about/#about-site)
- ©
- [2002](/2002/)
- [2003](/2003/)
- [2004](/2004/)
- [2005](/2005/)
- [2006](/2006/)
- [2007](/2007/)
- [2008](/2008/)
- [2009](/2009/)
- [2010](/2010/)
- [2011](/2011/)
- [2012](/2012/)
- [2013](/2013/)
- [2014](/2014/)
- [2015](/2015/)
- [2016](/2016/)
- [2017](/2017/)
- [2018](/2018/)
- [2019](/2019/)
- [2020](/2020/)
- [2021](/2021/)
- [2022](/2022/)
- [2023](/2023/)
- [2024](/2024/)
- [2025](/2025/)
- [2026](/2026/)
-
