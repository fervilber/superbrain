---
title: "Hosted agents in Foundry Agent Service at Ignite 2026"
source: "devblogs.microsoft.com/foundry"
date: 2026-11-18
captured: 2026-11-25T20:05:00+01:00
---

# Hosted agents in Foundry Agent Service at Ignite 2026: from pilot to production inside your enterprise boundaries

URL: https://devblogs.microsoft.com/foundry/hosted-agents-foundry-agent-service-ignite-2026/
Author: Muzz Imam, Eamon

Over the last few months I've worked with a lot of teams taking a hosted agent from pilot to production. A working demo is only the start. The questions that decide whether it ships come next: Will the subnet hold up when usage takes off? Can the agent call internal services that use our own certificates? Where exactly can it connect, and who decides? Can it run on the Azure Kubernetes Service (AKS) clusters we already operate? And what happens when a two-hour job gets interrupted?

At Microsoft Ignite 2026, we're announcing a solution to each of these challenges for hosted agents in Foundry Agent Service. Below you'll find what's new, what you can use today, and what's still to come. The egress and private CA updates apply to managed hosted agents, the ones Foundry runs for you; BYO-AKS support will be documented separately.

## At a glance

| What's new                                    | What it means for you                                                                         | Status                                     |
| --------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Shared subnet IPs                             | Run many more sessions from the same subnet; your session quota still applies                 | Generally available (GA)                   |
| Private CA trust                              | Call internal services that use your company's certificates, with certificate checks still on | Public preview                             |
| Network egress controls                       | One place to decide where an agent can connect, enforced outside the agent                    | Generally available (GA)                   |
| Azure Policy governance for egress            | Admins require compliant egress settings across a subscription or resource group              | Public preview, starting in three regions  |
| Deploy hosted agents to your own AKS clusters | Foundry's agent runtime on your own AKS cluster                                               | Public preview targeted for early December |
| Long-running resilient execution              | Opt-in recovery for long jobs after a crash or redeploy                                       | Generally available                        |
| Configurable idle timeout                     | Sessions can wait from 2 minutes to 4 hours between requests                                  | Generally available                        |
| Memory snapshots                              | Faster cold starts for agents with heavy startup                                              | Public preview                             |

## Scale: run far more sessions from the subnet you already have (GA)

If you run hosted agents in your own virtual network, each session used to take its own IP address from your delegated subnet. A /24 topped out at about 250 concurrent sessions, and teams with a tight IP plan hit that wall fast.

Hosted agent sessions now share subnet IP addresses. Each session still runs in its own VM-isolated sandbox. What changes is how far your subnet goes: our planning estimate for a /24 is now about 60,000 concurrent sessions, and even a /27, the smallest supported size, is planned for about 7,500. IP sharing is on for everyone, with no request needed.

These are planning estimates, not guarantees, and we still recommend a /24 or larger for production so there's room for upgrades and maintenance. For most teams, your regional session quota is now the practical ceiling: by default 2,000 or 1,000 concurrent sessions per subscription, depending on the region. You can ask for more through a support request.

## Trust: call internal services that use your company's certificates (public preview)

Internal MCP servers, APIs and model gateways often use certificates from a private certificate authority (CA). Agents didn't trust them, so calls failed, and the tempting fix was turning off certificate checks. Security teams don't like that fix, for good reason.

Now you register your CA once on the Foundry resource. The CA certificate lives in Azure Key Vault, and every project in the resource picks it up. Certificate and hostname checks stay on, public CAs stay trusted, and you don't bake CA files into container images or recreate project capability hosts. Trust covers two paths. Tools, toolboxes and bring-your-own-model gateways use your CA in projects on your own virtual network, usually within a minute of the update. Hosted agent code that calls internal services directly trusts your CA in new sessions. The docs list what isn't covered yet, such as remote builds and mutual TLS.

## Control: network egress controls are generally available (GA)

A tool list isn't a network boundary. Agent code can start a subprocess, a library can follow a redirect, and generated code can call anything. Security teams want one place to say "these hosts, nothing else." Network egress controls for hosted agents are now generally available. You attach an ordered list of rules to an agent: allow or deny hosts, add headers on the way out, or send traffic through your own gateway. Foundry enforces the rules outside the agent's sandbox, before requests reach their destination, so they don't depend on the agent's code behaving. If a policy can't be evaluated, the request is denied. Egress controls add to your own network controls, like Azure Firewall; they don't replace them.

If security review is what's holding your agent back, start here. Turn on Audit mode with a default of deny. In Audit mode, Foundry logs every request it would have blocked but lets it through. Header changes and rewrites still apply, so test them in a non-production environment first. Run representative tasks, review the destinations you see, and refine the allowlist. Then switch to Enforce and deploy a new agent version, since running sessions keep the policy they started with. Your security team reviews a list built from real traffic instead of a guess.

Admins get a central check too. With Azure Policy governance (public preview), you assign policy at a scope such as a subscription or resource group, and Azure Policy checks that egress settings and new hosted agent versions follow your rules, like Enforce mode, a default of deny, and only approved destinations. Start in Audit to see what doesn't comply, then switch to Deny to block noncompliant changes. Sessions that are already running keep going uninterrupted. The governance preview starts in Canada Central, Spain Central and Korea Central.

Status: Egress controls are generally available (GA). Azure Policy governance is in public preview.

## Related (Minutes of AI)

Microsoft listed a public preview of native Agent2Agent (A2A) passthrough for hosted agents in Foundry Agent Service. Microsoft also announced a public preview in Microsoft Foundry Agent Service that lets organizations route MCP tool traffic through AI Gateway or Azure API Management endpoints they manage themselves.

Fuente: https://minutesofai.com/topics/agents
