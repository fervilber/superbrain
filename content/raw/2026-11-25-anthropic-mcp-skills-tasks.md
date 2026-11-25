---
title: "Anthropic: Skills over MCP, Tasks, Elicitation y File Uploads"
source: "thenextweb.com / thenewstack.io / aiagentstore.ai"
date: 2026-11-24
captured: 2026-11-25T20:05:00+01:00
---

# Anthropic lets MCP servers ship skills and run background jobs in Claude

URL: https://thenextweb.com/news/anthropic-claude-skills-over-mcp-tasks-elicitation
Published: 2026-11-24 - 7:22 pm GMT
Author: Ana Maria Constantin

Shopify, GitHub and Supabase are among the first to use the new features in Claude and Claude Code.

Anthropic has opened Skills over MCP in public beta, letting apps that connect to Claude ship playbooks alongside their tools. Tasks, for long background jobs, and Elicitation, which pauses for user input, are now generally available, with File Uploads coming soon.

Apps that plug into Claude through MCP can now also tell it how to use them, Anthropic said on Tuesday. The feature, Skills over MCP, is in public beta in Claude and Claude Code.

MCP is the open standard Anthropic launched two years ago to link AI agents to outside apps and data. Servers built on it already list the tools Claude can use. With skills, they can also ship step-by-step guides and best practices, which Claude loads only when needed.

Shopify uses skills to help Claude design and update online stores, and HubSpot to onboard customers. Skills update with the server, so users have nothing extra to install. More apps are opening up, too: Canva opened its MCP server to all developers on Tuesday.

The beta is on by default for Pro, Max and Ultra plans. Team admins can switch it on, and Enterprise support is coming soon.

Two other features are now generally available. Tasks lets a server run long jobs in the background while Claude keeps working, which ZoomInfo uses for deeper research. Elicitation lets a server pause and ask the user for input.

GitHub, for example, makes users type a repository's name before an agent deletes it. Supabase confirms costs before creating a paid project. A fourth feature, File Uploads, will soon let Claude send PDFs, spreadsheets and images to servers.

The features are part of MCP, so servers that support them also work in other compatible apps. Anthropic says MCP now sees over 700M SDK downloads a month. In August, OpenAI and four rivals agreed on a standard for packaging skills and MCP servers.

Skills carry risks, too. That same month, researchers found malicious agent skills that stole passwords and keys after about 1.7 million installs.

---

## The New Stack — TNS Daily, November 24, 2026

URL: https://thenewstack.io/tns-daily/november-24-2026/
Author: Amanda Caswell

### MCP gets its act together

Anthropic on Tuesday marked the second anniversary of the Model Context Protocol (MCP) by bringing support for skills, long-running tasks, and file uploads over MCP to Claude.

Skills over MCP, which lets MCP servers publish skills alongside their tools, is now available in public beta, while Tasks, which first landed in Claude Code as a beta in October, and Elicitation are now generally available. File uploads will roll out soon.

All three are meant to help agents work more autonomously and for longer stretches of time, which, according to the protocol's maintainers, is also where the project focused much of its second year. In its announcement, Anthropic says these features let Claude treat an MCP server more like another agent that it can learn from and delegate work to.

---

## AI Agent Store — Daily AI Agent News, November 25, 2026

URL: https://aiagentstore.ai/ai-agent-news/daily/2026-11-25

### Anthropic: MCP adds "Skills", long-running Tasks, Elicitation, and File Uploads

What changed: Anthropic updated the Model Context Protocol (MCP) so MCP servers can publish server-provided "skills" (public beta), run long-running asynchronous Tasks (GA), pause for user confirmation with Elicitation (GA), and soon accept File Uploads that don't flow through the model context.

Why it matters: These extensions let agents delegate multi-step business procedures to servers that keep guidance up to date, reduce per-chat context usage, and resume work after background processing — meaning teams can centralize operational logic and let an agent pick up results later instead of keeping every step in the chat. Availability is rolling by plan (Skills beta on Pro/Max/Ultra by default; Tasks and Elicitation GA for those plans; File Uploads is experimental).

Try / watch: If you run agent workflows, prototype one MCP-backed "skill" for a single repeatable procedure (e.g., invoicing or research) to validate updates and approval flows; treat File Uploads as experimental and audit how approvals and file integrity are enforced before production use.

### Meta brings Muse (personal agent) to the UK with retail and travel connectors

What changed: Meta rolled Muse out in the UK (Nov 24) with partner connectors across retail and travel (Sainsbury's, Argos, M&S, easyJet, Trainline and others) so the agent can plan shopping, build baskets, and prepare bookings; payments are handled via a Stripe-built Link wallet and user approval is required for purchases.

Why it matters: This is a live consumer-scale agent commerce test ahead of a major retail season — a practical example of agents acting on behalf of people across third-party services. For retailers and platform integrators, it shows how connectors, payment flows, and approval UX need to be designed for real money and regulatory scrutiny.

Try / watch: Retailers and marketplace operators should test connector flows in a controlled pilot (validate identity, authorization, refund and consent paths) and monitor regulator guidance closely — agents that perform purchases increase exposure on terms, dispute handling, and data-sharing obligations.

---

## Claude Code v2.1.332 (AI Agent News, Nov 24)

Anthropic has released Claude Code v2.1.332, which adds beta support for skills served by MCP servers and a new hook that can block a skill's inline shell commands. The release also fixes a range of freezes and hangs and changes which Sonnet and Opus versions several cloud providers and aliases resolve to.

Fuente: https://aiagentnews.io/topics/frameworks
