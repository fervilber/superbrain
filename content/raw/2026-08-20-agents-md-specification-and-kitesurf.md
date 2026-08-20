# Specification: AGENTS.md and the A2A Discovery Protocol

**Source URL:** https://agentskills.io/spec/agents-md-and-a2a

---

# The AGENTS.md Specification (A2A Protocol v1.1)

With the Agent2Agent (A2A) protocol transitioning to the Agentic AI Foundation in August 2026, the ecosystem has moved to formalize how autonomous agents discover, negotiate, and delegate tasks to each other without human intervention. The core of this discovery mechanism is the `AGENTS.md` file—a structured metadata file that agents publish on their host or expose via an endpoint.

## 1. Directory Placement and Discovery

An A2A-compliant agent or service host MUST publish an `AGENTS.md` file at its root or via a well-known URI (e.g., `https://agent.domain.com/.well-known/agents.md`). When an agent initiates contact with another agent, the first step is fetching and parsing this file to understand the host’s capabilities, security boundaries, and supported tools.

## 2. File Structure and Schema

The `AGENTS.md` file consists of two sections: a YAML frontmatter block for machine-readable schema registration, and a Markdown body for human-readable fallback documentation and developer guidelines.

```yaml
---
a2a_version: "1.1.0"
agent_id: "hermes-default-v2"
organization: "Nous Research"
endpoints:
  mcp_gateway: "https://agent.cinesfer.duckdns.org/mcp"
  a2a_handshake: "https://agent.cinesfer.duckdns.org/a2a/handshake"
capabilities:
  - domain: "software-engineering"
    tasks: ["code-refactoring", "syntax-validation", "pull-request-review"]
    reliability_index: 0.98
  - domain: "system-administration"
    tasks: ["nginx-reverse-proxy-setup", "ssl-certificate-renewal"]
    reliability_index: 0.95
security:
  trust_level: "restricted"
  required_scopes: ["read:workspace", "write:sandbox"]
  encryption: "TLS_1.3_AES_256_GCM"
---
```

## 3. Dynamic Handshaking Process

Once the initiator agent parses the `AGENTS.md` file:

1. **Capability Matching**: It compares the required task with the target's listed capabilities.
2. **Handshake Initiation**: The initiator sends a signed JSON-RPC payload to the `a2a_handshake` endpoint containing the task specification, the required context window, and a cryptographically signed token identifying the caller.
3. **Session Negotiation**: The receiving agent returns a session token and dynamically maps an isolated sandbox workspace for the incoming work, matching the declared security scopes.

---

# Kitesurf: Cloudflare’s V8-Isolate Browser Runtime for AI Agents

**Source URL:** https://blog.cloudflare.com/kitesurf-v8-isolate-agent-browser

## The Overhead of Chromium in Agentic Workflows

Until recently, agents that needed to drive a web browser for scraping, testing, or UI automation relied on running full instances of headless Chromium via Puppeteer or Playwright. Under production scaling, this architecture is a resource disaster:

- Headless Chromium requires up to **500MB of RAM** per idle session.
- Startup latency averages **1.5 to 3 seconds**, which degrades agent responsiveness.
- Multi-tenant isolation is difficult to enforce securely without heavy virtualization overhead.

## Enter Cloudflare Kitesurf

Kitesurf is a headless browser runtime written from scratch to run inside Cloudflare Workers using lightweight V8 Isolates instead of traditional OS processes.

### Key Innovations:

1. **Shared Rendering Pipeline**: Rather than spinning up a new browser process per agent, Kitesurf uses a shared, secure rendering engine that runs on V8. Each agent gets an isolated JS execution context that targets a virtualized DOM.
2. **Unbelievable Resource Savings**: Kitesurf drops idle memory consumption to **under 40MB per session**—a 90%+ reduction. Startup latency is virtually zero (less than 50ms).
3. **Native MCP Server Binding**: Kitesurf exposes its automation interface directly as a Model Context Protocol (MCP) server. External agents do not need to load heavy automation libraries; they simply send standard MCP tool calls like `browser:navigate`, `browser:click_selector`, and `browser:extract_dom` over an active JSON-RPC session.

```javascript
// Example of a native Kitesurf Worker handler
export default {
  async fetch(request, env) {
    const browser = await env.KITESURF.launch({
      headless: true,
      isolation: "strict",
    })
    const page = await browser.newPage()
    await page.goto("https://news.ycombinator.com")
    const stories = await page.$$eval(".titleline a", (el) => el.map((a) => a.textContent))
    await browser.close()
    return new Response(JSON.stringify(stories), {
      headers: { "content-type": "application/json" },
    })
  },
}
```

This architecture makes multi-agent web execution fast, secure, and incredibly cheap to host.
