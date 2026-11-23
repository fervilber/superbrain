---
title: "OpenRouter retira tres proveedores tras la investigación de Dragos sobre robo de prompts"
source: "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ · https://novita.ai/blog/minimax-requests-privacy-notice/ · https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html · https://www.axios.com/2026/11/23/openrouter-minimax-china-customer-data"
date: 2026-11-23
captured: 2026-11-23T20:00:00+01:00
---

# Data Processing Incidents on Inference Providers (OpenRouter, 22 nov 2026)

Earlier this week, security researchers reported that certain inference providers had data compromised or otherwise shown evidence that their data policies were not being upheld. We have been collaborating closely with the researchers and with providers to understand the findings and encourage the providers to address them.

These findings did not show any breach or unauthorized access of OpenRouter. The results of this testing revealed new findings about specific inference providers. A live list of the security announcements we have received from providers is below.

As the operating layer between customers and a fast-moving ecosystem of models and providers, we take data policy enforcement very seriously. We have taken the following actions:

- Off-boarded three providers from OpenRouter, based on the results of our investigations.
- Removed 125 endpoints from Zero Data Retention (ZDR) eligibility. The removals included providers flagged by researchers, plus additional endpoints that we removed as a precautionary measure.
- Notified all potentially affected customers.

The following work is underway:

- We are adapting the researchers' testing approach so we can run these checks on an ongoing basis.
- We are conducting technical verification of network paths to identify instances where requests and responses may be being forwarded to third parties.
- We are requiring appropriate assurances and validation before restoring ZDR eligibility to any endpoint removed in this review.

We are grateful for the Dragos report. As we integrate similar testing techniques into OpenRouter, we will keep raising the bar, and providers that want to be on OpenRouter will need to meet it.

## Provider security announcements

- Atlas Cloud: Our commitment to your security and privacy
- Novita: Privacy notice regarding MiniMax requests on Novita
- Phala: November preliminary incident report
- Together: Security event: prompt leakage for requests in June and July of 2026

Not all affected providers have posted publicly. We have notified affected users regardless of whether there is a public post. We are encouraging all providers to create incident write-ups and will keep this list updated.

---

# Privacy Notice Regarding MiniMax Requests on Novita (22 nov 2026)

We received a report from an independent security researcher concerning the handling of MiniMax requests on Novita. Our review confirmed that some requests were forwarded to MiniMax's official API rather than processed on Novita-hosted infrastructure. We promptly suspended the affected models.

## What happened

A routing configuration issue caused an API forwarding path intended for specific customers to apply more broadly.

If you used MiniMax models through Novita between 2026-05-28 and 2026-11-11, your request contents may have been accessed or retained by a third party. This includes requests made directly through Novita and those routed to Novita through OpenRouter.

## Investigation findings

The researcher observed accesses to URLs and hostnames embedded in test requests. No use of the AWS test key markers was observed. The access patterns suggest automated content review may have been involved. We are following up with MiniMax to verify this assessment and its handling of the affected data.

Novita itself does not retain customer prompts or generated outputs or use them for model training.

## Actions and next steps

We are verifying the processing paths for the affected MiniMax endpoints and following up with MiniMax regarding any retained customer data and its deletion.

We are also improving Partner API labeling and disclosures of the relevant providers' data retention policies and Terms of Service.

If your requests included live credentials, API keys, or other secrets, we recommend revoking or rotating them as a precaution.

---

# OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms (The Hacker News, 22 nov 2026)

Attackers stole data from inside three AI inference providers for months, and none of the three knew until researchers told them, the industrial cybersecurity company Dragos said this week. Some of the stolen requests were flagged as Zero Data Retention, the setting that is supposed to mean a prompt is never stored.

The earliest of the three breaches began in mid-July. The planted prompts were bait, but they were processed alongside real customer requests, and those were almost certainly copied too, the firm said.

The finding comes from canary token research that seeded about two million prompts with unique web links and credentials between July and November, then watched for anyone using them. A planted secret can only be learned in one place, so any use of it means someone read the prompt that carried it.

The largest of the three breaches involved a couple hundred AWS keys that were planted, each sent in exactly one request to one provider during a few short windows in late October. Every request sent during those windows was stolen, and some came from requests the provider had rejected before a model ever ran, indicating the attacker was copying traffic at the first point of arrival rather than deeper in the inference stack.

The second finding needed no break-in. Sellers on an AI inference marketplace listed models at the lowest prices, enabled request logging, and collected what flowed through, the research found.

A Chinese AI lab, which the research does not name, fetched the secret links from more than half of the seeded prompts sent to its models between July and October, including about two-thirds of the requests marked no data collection or Zero Data Retention. Prompts sent to U.S. hosting providers that resell the lab's models triggered the same scraper, thereby flowing back to the lab. A git client on another cloud later tried to clone private repositories referenced in the prompts, but only for that lab's models, and one large U.S. provider kept crawling a secret link more than two months after a single request to its search endpoint.

In practice, Moore wrote, the flagged prompts were kept, passed to other companies, and read by human beings.

An attacker took control of an inference server at Phala and could view request data while it was being processed, the provider said in a preliminary incident report. The incident was contained on November 8, and the model service has been restored with added protections. Requests to the DeepSeek V4 Flash 0731 model that reached Phala through the gateway between October 21 at 00:00 UTC and November 8 at 05:35 UTC should be treated as exposed, and every key, token, password, or other secret within them should be rotated.

---

# OpenRouter warns some AI user data was sent to China's MiniMax (Axios, 23 nov 2026)

Users of several AI services may have had their private conversations exposed to an unknown third party after their requests were routed to Chinese AI company MiniMax, according to an email OpenRouter sent to affected customers.

OpenRouter warned customers that prompts and responses sent to MiniMax models may have been accessed by a third party between July and October. A spokesperson for Stripe, which owns OpenRouter, confirmed to Axios that the emails are legitimate.

In its customer emails, the company also identified three providers that had forwarded requests to China-based MiniMax. OpenRouter also removed privacy protections from 125 ways of accessing AI models that had previously been designated as not storing customer conversations.
