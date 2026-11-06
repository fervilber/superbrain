---
title: "MCP Security Statistics 2026: What the Vulnerability Data Reveals About AI Agent Risk"
source: "https://blog.bonfy.ai/mcp-security-statistics-2026-what-the-vulnerability-data-reveals-about-ai-agent-risk"
date: 2026-11-06
captured: 2026-11-06T20:07:00+01:00
---

# MCP Security Statistics 2026: What the Vulnerability Data Reveals About AI Agent Risk

By Gidi Cohen · September 24, 2026

MCP servers are exploding in enterprise use and lagging badly on security. Independent security audits conducted since 2025 and compiled into 2026 industry reporting put anywhere from 30 percent to 82 percent of public Model Context Protocol servers carrying an exploitable flaw such as path traversal, server-side request forgery, or command injection, only 8.5 percent of servers use OAuth for authentication, and 88 percent of organizations reported a confirmed or suspected AI agent security incident in the past year. The mechanism behind nearly every one of those numbers is mundane: missing authentication, secrets returned in plain text, and ordinary web application bugs, now sitting behind a caller with the speed and persistence of an autonomous agent rather than a human clicking through a browser.

## Key Takeaways

- Independent audits found MCP servers carrying widespread exploitable flaws in 2026, including 82 percent of implementations handling file operations in a way prone to path traversal (Endor Labs, 2,614 implementations examined) and only 8.5 percent of servers using OAuth for authentication (Astrix, 5,200-plus servers audited).
- A malicious MCP supply chain campaign called Deadbugz filed 23 pull requests across unrelated developer projects in 74 minutes in September 2026, shipping a server that behaves normally for three tool calls before rewriting its own instructions to hunt for SSH keys and cloud credentials.
- Three new MCP server CVEs disclosed in August 2026, a path traversal in Atlassian's Confluence MCP tool, a cleartext cluster-token leak in ArcadeDB, and a server-side request forgery flaw in a Facebook Ads MCP server, all involved classic web vulnerability classes with no model-specific component.
- Gartner projects that 25 percent of enterprise breaches will trace back to AI agent abuse by 2028, and MCP's authorization gaps, with only 8.5 percent of servers using OAuth, are a named driver behind that forecast.

## The Numbers Behind MCP's Security Problem

Model Context Protocol adoption has moved faster than almost any developer standard in recent memory. Anthropic's own count put monthly SDK downloads above 97 million by December 2025, with more than 10,000 active public servers and first-class client support across ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, and Visual Studio Code. Team8's 2025 CISO Village Survey found 70 percent of enterprises already running AI agents in production, with another 23 percent planning deployment in 2026.

Security maturity has not kept pace. Endor Labs found that 82 percent of MCP implementations handle file operations in a way prone to path traversal, across 2,614 servers examined. A separate Equixly assessment found 43 percent of tested servers vulnerable to command injection. BlueRock Security found 36.7 percent of more than 7,000 servers vulnerable to server-side request forgery, and Enkrypt AI found 33 percent of 1,000 scanned servers carrying a critical vulnerability. On the authentication side, an Astrix audit of more than 5,200 servers found that while 88 percent require some form of credential, 53 percent rely on static API keys or personal access tokens, 79 percent pass those keys through environment variables, and only 8.5 percent use OAuth at all. Trend Micro's own internet scan found 492 MCP servers exposed publicly with no authentication or encryption at all, a figure that nearly tripled to 1,467 in a follow-up count.

The incident data tracks the exposure. HiddenLayer's 2026 AI Threat Report found autonomous agents now account for more than one in eight reported AI breaches. Gravitee's 2026 survey found 88 percent of organizations reported a confirmed or suspected AI agent incident in the past year, rising to 92.7 percent in healthcare specifically. HackerOne's ninth annual report logged a 540 percent surge in prompt-injection vulnerability reports, calling it the fastest-growing threat category in AI security, alongside more than 30 MCP-related CVEs filed in a single 60-day window in early 2026. Gartner's own forecast, that 25 percent of enterprise breaches will trace to AI agent abuse by 2028 and that more than half of successful attacks on AI agents through 2029 will exploit access-control issues, is not a hypothetical extrapolation. It is a straight-line projection from numbers that are already this large.

## Deadbugz: When Review Happens Before the Server Turns Hostile

If one event captures where MCP security stands in September 2026, it is the Deadbugz campaign. A single GitHub account filed 23 pull requests across unrelated AI and developer tool projects in 74 minutes, each one offering a small, plausible-looking MCP server for text formatting and summarization. Reviewers who checked the server before merging it found nothing wrong, because there was nothing wrong yet. The server behaves exactly as advertised for the first three tool calls. Only after that does its metadata rewrite itself into instructions hunting for SSH keys, AWS credentials, shell history, and Kubernetes configuration files, while concealing the activity from the user running it.

That design defeats one-time review by construction. A security team that scans a new MCP server once before approving it, the standard practice at most organizations today, will see a clean report, because the payload does not exist at scan time. It only exists once the server has been trusted, connected, and used. The practical lesson researchers drew from Deadbugz is to monitor tool metadata for changes after approval rather than treating a single pre-approval scan as sufficient, and to compare tool definitions on every reconnect if a client caches them, since drift after the fact is the signal a one-time audit cannot catch.

## Three CVEs, Zero Model Involvement

The same month's CVE disclosures reinforce a related point: most of what is going wrong with MCP servers has nothing to do with the language model calling them. CVE-2026-73498 affects the Atlassian Confluence MCP tool, where the `confluence_upload_attachment` function passed a client-supplied file path directly into a file-open call with no validation, giving any authenticated client an arbitrary file read across everything the server process could reach. CVE-2026-67357 hit ArcadeDB, where a settings tool exposed over MCP returned its high-availability cluster token in cleartext, a token that was enough on its own to impersonate root through specific request headers. CVE-2026-19956 affected a Facebook Ads MCP server, where a server-side request forgery flaw in a pagination function let an authenticated remote caller drive requests from the server's own network position.
