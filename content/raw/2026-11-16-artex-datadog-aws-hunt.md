---
title: "Datadog Security Labs: On the hunt for ARTEX — understanding agentic attacks in AWS environments"
source: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
date: 2026-11-16
captured: 2026-11-16
---

# On the hunt for ARTEX: understanding agentic attacks in AWS environments (Datadog Security Labs, 9 de noviembre de 2026)

Autora: Julie Agnes Sparks, Senior Security Engineer. Capturado el 2026-11-16.

## Key points (verbatim)

> - In October 2026, Datadog observed in-the-wild activity from ARTEX, an AI-native penetration framework, against several AWS environments, with a focus on accessing financial data.
> - Using compromised long-term IAM access keys, ARTEX searched through CloudWatch using `FilterLogEvents`, hunting for financial information, file paths and secrets such as long-lived `AKIA` access keys and passwords.
> - We also observed unauthenticated abuse of public Amazon Cognito user pools, including anonymous sign-ups, token collection, and follow-up AWS account enumeration attempts.
> - In early November 2026, Datadog tied ARTEX activity to IP addresses that resolved to a hosted console, and found hundreds of additional internet-exposed ARTEX consoles, often in Mandarin and hosted with providers in locations including Singapore and Hong Kong.

## Background (verbatim, extractos)

> ARTEX is an AI-native penetration framework in which an operator supplies a target and an objective, and a team of LLM agents plans and runs the attack. A Chinese developer published it on GitHub in July 2026 and made it closed-source on October 8, after it had passed 12,000 forks. Microsoft tied it to Storm-0940, a China-aligned actor behind a recent supply-chain compromise. In recent months, ARTEX has been documented attacking Okta, Entra ID and Cognito across IT and software vendors.

## Inside the ARTEX console (verbatim, extractos)

> Operators run it as a hosted web console, and many of those consoles face the internet. We found hundreds of hosts serving the same Chinese-language login page, titled `ARTEX — 自主渗透测试控制台` (ARTEX — Autonomous Penetration Testing Console). We've also seen the same platform appearing under other names:

| Page title                                           | English translation                            |
| ---------------------------------------------------- | ---------------------------------------------- |
| ARTEX — 自主渗透测试控制台                           | ARTEX — Autonomous Penetration Testing Console |
| ScopeWeaver — Autonomous Penetration Testing Console | (original in English)                          |
| LUCK — 自主资产控制台                                | LUCK — Autonomous Asset Console                |
| 观澜SEC渗透测试平台                                  | Guanlan SEC Penetration Testing Platform       |

> The platform user supplies API keys to chosen AI inference providers and points ARTEX at almost any provider through three request formats:
>
> - `openai`: OpenAI Chat Completions and any compatible gateway, which covers OpenAI, DeepSeek, Qwen, MiniMax, OpenRouter-style resellers and self-hosted models.
> - `openai-responses`: OpenAI's newer Responses API.
> - `anthropic`: Anthropic's Messages API, plus vendors that expose an Anthropic-compatible endpoint, such as DeepSeek.
>
> When one provider bans or cuts off a key, ARTEX moves to the next to continue activity. Therefore, a single campaign can be spread across several providers and keys.

> An agent planner directs a small team of workers. The planner sends "intents" to workers, which run three at a time by default. A main agent handles chat with the operator, with a `/btw` command for side questions. Everything is recorded on a "blackboard" graph of tasks, goals, intents, facts, findings, hints and compression digests. Each task carries operator-defined allow and deny constraints, a timeout with a wrap-up step, and a planner heartbeat of at least 10 minutes.

> Command interception rules, written as regex or plain strings, can allow, deny or ask a human for a judgment. In some versions, a global asset blocklist excludes `.gov`, `.gov.cn`, `.edu` and `.edu.cn` by default.

> API paths expose core routes, such as: `/tasks /exploration/findings /exploration/graph /exploration/intents /traffic /companies /llm/profiles /llm/pool /intercept /mcp /skills /agents /notify`.

> Wiz noted that before each fuzzing run, ARTEX requested a path that should not exist (`/zzz-nonexistent-xyz123`) to learn what "not found" looks like. We saw the same habit against S3, with keys such as `zzz_nonexistent_abc.txt` and `Notexist-xyz`. A request for an object named like a placeholder, right before a burst of guesses, is a useful signal to hunt on.

## ARTEX sightings in AWS environments in the wild (verbatim, extractos)

> The two initial access vectors we've witnessed ARTEX start from are: compromised long-term AWS access keys; and public Cognito user pools. Before either, every session we reviewed opened with unauthenticated S3 requests. In CloudTrail, these show a `userIdentity.type` of `AWSAccount` and an `accountId` of `anonymous`, calling `GetObject`, `ListObjects` and similar read APIs.

> **Activity cluster 1: Post-exploitation following compromised access keys.** In one instance using a valid long-term access key, ARTEX's most frequent action was `FilterLogEvents`. The most common searches were various naming conventions of cryptocurrency companies, hedge funds, and related financial institutions. The terms combine a company name with words like Fund, Invoice, Billing and LLC. Every `FilterLogEvents` call was set with a `limit` of 1000, below the API's 10,000-event maximum. That constant shows up across sessions. On October 20, the same long-term key was used again from `103.54.154[.]40`, an address associated with `zeofast[.]cn`. This session widened the search, looking for file and storage links, internal secrets, internal IP addresses, and database information: `"s3://" || "presigned" || ".pdf" || ".xlsx" || ".csv" || "rawData_" || "transformedData_"`; `?mongo ?172. ?10. ?password ?AKIA`; `?Error ?❌ ?⚠`.

> **Activity cluster 2: Self-registration through public Cognito user pools.** Wiz reported account-recovery abuse through `InitiateAuth`, `ForgotPassword` and `ResendConfirmationCode`. We saw the agent go further, registering an account, collecting tokens, trading them for AWS credentials, then enumerating resources. One example came as a spike on October 26 and 27 from `154.64.252[.]77`. The observed `SignUp` calls sometimes named the tool in the user agent such as `Mozilla/5.0 ARTeX`, while other user agents included curl or typical browser user agents. Once registered, it walked the standard user pool flow: `SignUp`, `InitiateAuth`, `RespondToAuthChallenge`, `GetUser` and `GetTokensFromRefreshToken`, followed by `Get*` requests and attempts to call `ListUserPools`. In CloudTrail, that session appears under the `CognitoIdentityCredentials` role session name with short-term AWS credentials.

> In this post, we've shared some in-the-wild sightings of ARTEX-attributed activity in cloud environments. It's important to remember that while ARTEX is an offensive AI-native orchestration framework, distributions we analyzed don't appear to have an opinionated methodology for targeting or performing post-exploitation in cloud environments: the playbook is therefore left to downstream AI inference, and can vary greatly depending on the model in use.

## Hunting for ARTEX activity (verbatim)

> 1. Start with quick wins, namely ARTEX user agents (see IOCs) to identify noisy ARTEX probing or exploitation requests. Note that user agents can easily be changed, but they aren't always updated to a stealthier value.
> 2. Review your environment for activity originating from IP addresses known to be associated with ARTEX activity (see IOCs).
> 3. We've seen ARTEX behave noisily in a number of cases: identify large volumes of permission denied errors, enumeration of objects in S3 logs, unusual access patterns (for instance, credentials vended from an EC2 instance role being used by a non-AWS IP), and CloudTrail events that relate to known cloud attack techniques.

## Indicadores (verbatim)

IPs: `169.128.55[.]214` (Caelus Technology LLC), `154.64.252[.]77`, `154.36.136[.]197`, `154.36.136[.]23` (NetLab Global), `102.216.154[.]102` (Vilcom Networks, Kenia), `82.158.88[.]233` (Zenixcloud), `88.229.22[.]232` (Turk Telekom), `103.54.154[.]40`, `103.54.154[.]32` (Zeofast Network), `45.145.228[.]25` (Yecaoyun/LUCIDACLOUD).

User agents: `artex-readonly/1.0`, `artex-pentest/1.0`, `artex-audit/1.0`, `Mozilla/5.0 ARTeX`, `artex-spawn/1`, `artex-verify/1.0`, `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ARTeX-authorized-pentest`, `Mozilla/5.0 (X11; Linux x86_64) artex-verify/1.0`, `artex-i21861-canary`, `ARTEX-worker/1.0`.
