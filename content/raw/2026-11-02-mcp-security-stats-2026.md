---
title: "MCP Security Statistics 2026: CVEs, vulnerabilidades y datos de brechas"
source: "https://www.practical-devsecops.com/mcp-security-statistics-2026-report"
date: 2026-11-02
captured: 2026-11-02
---

# MCP Security Statistics 2026: CVEs, Vulnerabilities & Breach Data

Varun Kumar — Practical DevSecOps (26 de junio de 2026). Captura verbatim de los tramos sustantivos.

A data-led briefing for developers and security engineers building on the Model Context Protocol.

## TL;DR

- MCP adoption exploded in 2025 (97M+ monthly SDK downloads, 10,000+ active public servers, first-class client support across ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, and VS Code), but security maturity lagged badly: independent scans repeatedly find 30–82% of public MCP servers carry exploitable flaws, only 8.5% use OAuth, and major CVEs (CVE-2025-6514, CVE-2025-49596, CVE-2025-54136) have already hit hundreds of thousands of developer environments.
- The threat data is real, not hypothetical: 47–53% of organizations have had AI agents exceed permissions or suffer an incident, HackerOne logged a 540% surge in prompt-injection reports, and Trend Micro found 492 MCP servers exposed to the open internet with zero authentication.
- The biggest gap is governance: only ~23% of organizations have a formal AI-agent identity strategy, and only 14.4% of agents reach production with full security approval, even as Gartner predicts MCP-driven incident rates will climb sharply through 2028–2029.

## Key Findings (statistics organized by category)

### 1. MCP adoption & growth (2025–2026)

- 97 million+ monthly SDK downloads across Python and TypeScript (Anthropic/modelcontextprotocol.io ecosystem update, December 9, 2025). MCP Lead Core Maintainer David Soria Parra summarized it as "over 97 million monthly SDK downloads, 10,000 active servers, and first-class client support across major AI platforms like ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, and Visual Studio Code."
- 10,000+ active public MCP servers (Anthropic, December 9, 2025). An independent May 24, 2026, pull of the official MCP Registry API counted 9,652 latest server records and 28,959 server/version records (Digital Applied, 2026).
- 15,926 GitHub repositories carried the mcp-server topic as of May 24, 2026; the reference modelcontextprotocol/servers repo had 86,148 stars (Digital Applied, 2026).
- Download growth: from ~100,000 (November 2024) to 8 million (April 2025).

### 2. MCP-specific vulnerabilities & attack vectors

- Command injection: 43% of tested MCP servers vulnerable (Equixly, 2025–Feb 2026 offensive-security assessment).
- Path traversal: 82% use file operations prone to path traversal across 2,614 MCP implementations (Endor Labs, 2025).
- SSRF: 36.7% of 7,000+ servers vulnerable (BlueRock Security, 2026); a related Equixly figure put SSRF at 30%.
- Volume: 30+ CVEs filed against MCP servers in a single 60-day window in early 2026 (multiple researchers; 13 of 30 ≈ 43% were command-injection patterns).

### 3. CVEs & security advisories tied to MCP

- CVE-2025-53110 / CVE-2025-53109 (Filesystem MCP Server): directory containment bypass (CVSS 7.3) and symlink bypass (CVSS 8.4) (Trend Micro, 2025).
- Anthropic Git MCP server: three CVEs (CVE-2025-68143/68144/68145) disclosed January 2026 incl. path traversal and argument injection (Cyata/Dark Reading, 2026).
- CVE-2026-33032 ("MCPwn", nginx-ui MCP): CVSS 9.8 auth bypass, actively exploited; patched March 15, 2026 (Pluto Security/Recorded Future).
- CVE-2026-45609: SSRF in the mcp-security framework for Spring AI (OAuth Dynamic Client Registration fetching untrusted metadata URLs).
- Three new MCP server CVEs disclosed in August 2026: path traversal in Atlassian's Confluence MCP tool, a cleartext cluster-token leak in ArcadeDB, and a server-side request forgery flaw in a Facebook Ads MCP server — all classic web vulnerability classes with no model-specific component.

### 4. Public registries & % audited

- Only 8.5% of servers use OAuth for authentication.
- Trend Micro found 492 MCP servers exposed to the open internet with zero authentication.
- Independent 2026 scans found more than 12,000 MCP servers exposed to the public internet, roughly 40% running with no authentication at all.

### 5. AI agent / agentic security incident data

- 47–53% of organizations have had AI agents exceed permissions or suffer an incident.
- HackerOne logged a 540% surge in prompt-injection reports.
- 88% of organizations reported a confirmed or suspected AI agent security incident.

### 6. Supply chain

- Deadbugz is a supply chain campaign that distributed a malicious MCP server through GitHub pull requests, filing 23 of them across unrelated projects in 74 minutes from a single account. The server behaves normally for its first three tool calls, then rewrites its own tool metadata into instructions that hunt for SSH keys, cloud credentials, and shell history (disclosed September 2026).
- OX Security's April 2026 research, "The Mother of All AI Supply Chains," identified a command execution vulnerability embedded in Anthropic's official MCP SDKs for Python, TypeScript, Java, and Rust. The STDIO transport processes incoming configuration by passing parameters directly to the host operating system's shell without input sanitization or validation. Estimated 200,000 vulnerable instances across a supply chain encompassing more than 150 million package downloads.
