---
title: "IBM TechXchange 2026: identidad y control para agentes de IA (Agent Identity, HashiCorp Vault, watsonx Orchestrate, NVIDIA OpenShell)"
source: "https://newsroom.ibm.com/2026-10-27-ibm-introduces-identity-and-control-for-ai-agents,-securing-frontier-intelligence-for-the-enterprise"
author: "IBM Newsroom"
date: 2026-10-27
captured: 2026-10-28
---

# Captura: IBM introduce identidad y control para agentes de IA

> Texto completo de la nota de prensa de IBM (27 de octubre de 2026, TechXchange 2026, Atlanta). Se conserva el original en inglés y se anotan al final las claves técnicas.

## IBM Introduces Identity and Control for AI Agents, Securing Frontier Intelligence for the Enterprise

- Enterprises are deploying agents faster than they can verify them. HashiCorp Vault uses Agent Identity to give each agent a governed identity
- Verified agents still need limits on access. Vault extends its established secrets management to AI agents, built to enforce least-privilege access and enable real-time revocation when an agent attempts an unauthorized action
- Enterprises can't scale agents they can't see, test or account for. IBM watsonx Orchestrate is designed to unify discovery, containment, and evaluation across Amazon Bedrock, Microsoft Foundry and Google Gemini

Oct 27, 2026

**ATLANTA, GA, Oct. 27, 2026 --** At TechXchange 2026, IBM (NYSE: IBM) is announcing new capabilities to help developers, IT and security teams put AI agents to work across business systems with clear authority and accountability. IBM brings together agent discovery, verified identities, access controls and performance evaluation to help organizations understand who owns each agent, control what it can access, and trace its actions across existing applications and infrastructure.

According to Gartner, by 2028 the average Fortune 500 enterprise will use over 150,000 AI agents. But only 13% of organizations believe that they have the right AI agent governance in place [1]. Persistent credentials, unclear ownership and disconnected controls make it harder to govern agents as they interact with other agents, invoke tools and act across teams, platforms and clouds.

> "The winners in enterprise AI are changing how their business runs, not simply adding more AI to it," said **Dinesh Nirmal, Senior Vice President, IBM Software**. "For agents to take on real work across the systems a company depends on, it requires an AI operating model - one that connects agents to the business's data, applications and infrastructure and runs them with the same discipline as its most critical systems. Build trust and control into that model, and agents stop being a technology and become a way of doing business."

Today's announcements extend IBM's portfolio to deliver an AI operating model of four essential systems working together: agents, data, automation and hybrid infrastructure. This starts with the trust and control every agent needs - a verified identity, only the access it needs, and one place to discover, secure and evaluate agents regardless of where they were built.

### Extending HashiCorp Vault to AI agents

**HashiCorp Vault** manages the secrets and credentials that applications and services use to access business systems. It provides that control through centrally managed secrets, automated rotation for supported credentials, and dynamically generated credentials that expire or can be revoked. These capabilities help reduce the time exposed credentials remain usable and limit access to the permissions configured for each role.

HashiCorp Vault already secures non-human identities for organizations including ABN AMRO, Adobe, athenahealth, BBVA, BlackRock, Canva, Duke Energy, Expedia, London Stock Exchange, Starbucks, Swiss Federal Railways and Target, across systems that process billions of dollars in transactions [2]. HashiCorp will now extend those capabilities to AI agents, issuing secured, short-lived credentials that limit each agent to what it needs.

### Establishing agent identity and accountability

AI agents are a growing class of non-human identity, alongside applications and services. As they begin acting across business systems, enterprises need a clear record of who owns each agent and what authority it has been granted. HashiCorp is combining governed agent identity with credential controls to help organizations delegate work with defined authority and accountability.

When used with **HashiCorp Vault, Agent Identity** establishes the authoritative record for each agent, such as who owns it, its lifecycle status and the authority it has been granted. Built to extend existing identity and security investments, it shares relevant identity and authorization context with **Vault's credential controls** - ultimately enforcing least-privilege access and enabling real-time revocation when an agent attempts an unauthorized action.

### Controlling agent credentials and access

Identifying an agent is only the start. Enterprises also need to control the credentials it uses to reach databases, applications and cloud services - and how long those credentials remain valid.

As agents invoke tools and act across business systems, their credentials become a critical security boundary. An agent with a long-lived, overprivileged credential can put systems and data at risk if it's compromised or acts outside its intended task. Enterprises need to establish what each agent's job is, limit the access it receives and revoke that access when circumstances change.

These controls extend beyond initial authentication. If an agent attempts to retrieve information or perform actions outside its approved permissions, the access can be denied and session revoked in real time to prevent unauthorized activity. Vault's short-lived credentials and least-privilege controls can further restrict what an agent accesses and the duration of those permissions.

Additional capabilities include:

- **Vault 2.2** gives agents their own secured accounts, automatically renews their credentials and incorporates post-quantum encryption for quantum-era threats.
- **Secure Hub** (public preview) gives companies centralized visibility across their Vault environments to make it easier to understand operational health, usage and security resources.

At TechXchange, client speakers will share how they use Vault to secure enterprise applications, workloads and AI agents: athenahealth (automating certificate management with Vault's PKI engine); Albert Einstein College of Medicine (IBM Verify and Vault for AI agent identity, just-in-time access, dynamic secrets and auditability); Optum (Vault Radar for exposed secrets, Boundary for just-in-time identity-based access); Seven-Eleven Japan (Vault Enterprise secret centralization/encryption, Vault Radar for hardcoded secrets); Yum! Brands (identity security platform with IBM Verify, machine identities and secrets management).

> "AI presents extraordinary opportunities to accelerate biomedical research and discovery, but realizing its potential requires a foundation of security, trust, and responsible governance," said **Shailesh M. Shenoy, Assistant Dean for Information Technology at Albert Einstein College of Medicine**.

### Managing agents across platforms

Identity tells organizations what an agent is. But they also need to see every agent they have, wherever it was built. **IBM watsonx Orchestrate** works across the AI ecosystem, not inside a single vendor's platform, to give organizations one place to discover, secure and evaluate their agents. Capabilities include:

- **Discover** (tech preview): connects to platforms such as Amazon Bedrock, Microsoft Foundry and Google Gemini to find agents built in third-party environments, so teams can see and manage agents instead of adding them manually. This capability also extends to models and MCP servers.
- **Contain** (tech preview): runs agents in isolated sandboxes so a rogue agent can't interfere with others. Teams also now have access to a kill switch to shut down any agent.
- **Evaluate:** test the quality, accuracy and compliance of agents, models and MCP servers before deployment, then monitor them in production. Built-in cost tracking shows each agent's model and token use.

Orchestrate also works with Vault's credential controls and Agent Identity to establish what each agent's job is, govern its authority and enforce least-privilege credential access.

### Connecting agents to the business

Once agents are authorized to use a company's APIs and tools, they need to know what already exists, how systems connect, what can be reused safely and what their actions could affect. **IBM Integration Intelligence Hub** is built to provide that knowledge through its Unified Context Engine, so agents can fix problems like stuck messages or deploy an API using what's already in place. Skills, approval policies and audit controls keep those actions in check.

### Scaling agents with NVIDIA

Agent Identity and HashiCorp Vault integrate with NVIDIA OpenShell secure runtime software, the foundation of the NVIDIA OpenShell Architecture. Together, they pair a protected environment for agents to run in with a verified identity and short-lived credentials for every agent, so each action can be traced, limited and reviewed.

> "Businesses need enforceable control over how agents operate and what they can access," said **John Fanelli, vice president, enterprise software, NVIDIA**. "Our work with IBM combines NVIDIA OpenShell's policy-governed runtime with Agent Identity and HashiCorp Vault to help enterprises scale AI agents with secure execution, verified identities and tightly scoped access to business systems."

### Responding to emerging security threats

**IBM Concert** integrates observability, optimization, incident management and security across applications, infrastructure and networks. With AI-powered insights and proof of exploitability, Concert helps teams identify high-risk vulnerabilities, assess operational impact, and coordinate responses.

**HashiCorp Terraform** provides infrastructure context and governed workflows for change implementation. New features now generally available and in public preview, including **Terraform policy**, **Terraform Developer Portal** and **Terraform remote MCP server**, enable developers and AI agents to access approved configurations and implement infrastructure changes through established controls. Terraform powered by Infragraph also helps teams understand infrastructure relationships and dependencies.

**IBM Z Atlas** maps a client's entire z/OS stack across infrastructure, middleware, and applications, and then uses that intelligence to address the manual effort of tasks like patch management, regulatory response, and sharing system knowledge across teams. Atlas addresses the leading cause of unplanned z/OS outages - changes that aren't proven to be safe - by mapping how a change impacts the z/OS stack and testing and validating it.

### Availability

HashiCorp Vault 2.2, Agent Identity, watsonx Orchestrate evaluate capabilities, IBM Concert, and HashiCorp Terraform policy are generally available. Secure Hub, Terraform Developer Portal, Terraform remote MCP server, and IBM Z Atlas are in public preview. IBM Integration Intelligence Hub and watsonx Orchestrate discover and contain capabilities are in tech preview.

### Notas técnicas (resumen del capturador)

1. **El agente pasa a ser una identidad no humana de primera clase**: Agent Identity registra propietario, estado de ciclo de vida y autoridad delegada; Vault emite credenciales de vida corta y revoca en tiempo real ante acciones fuera de política.
2. **La credencial es la frontera de seguridad**: el argumento central es que un agente con credencial de larga duración y sobreprivilegiada es un riesgo equivalente a una aplicación comprometida, pero con capacidad de acción autónoma.
3. **Plano de control multi-nube**: watsonx Orchestrate descubre agentes, modelos y servidores MCP en Bedrock, Foundry y Gemini; sandboxing por agente y kill switch como controles de contención.
4. **Runtime confiable**: la integración con NVIDIA OpenShell coloca el aislamiento de ejecución en la capa de sistema operativo, no solo en la capa de política de la aplicación.
5. **MCP entra en la gobernanza**: los servidores MCP aparecen explícitamente como activos a descubrir, evaluar y gobernar, y Terraform expone un servidor MCP remoto para cambios de infraestructura gobernados.
