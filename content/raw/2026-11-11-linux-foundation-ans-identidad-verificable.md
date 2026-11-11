---
title: "Linux Foundation Welcomes Agent Name Service (ANS) — identidad verificable para agentes de IA"
source: "https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents"
date: 2026-11-10
captured: 2026-11-11
---

# Linux Foundation Welcomes Agent Name Service to Bring Verifiable Identity and Discovery to AI Agents

SALT LAKE CITY – KubeCon + CloudNativeCon North America – Nov. 10, 2026 – The Linux Foundation, the nonprofit organization enabling mass innovation through open source, today announced that Agent Name Service (ANS), an open standard built on Domain Name System (DNS) infrastructure that provides trusted identity, verification, and discovery for AI agents operating across the internet, has launched as a Linux Foundation project.

The ANS specification defines how AI agents are named and registered, how their identities are published through DNS, and how those identities can be verified. It also outlines how to monitor identity records for unauthorized changes and how agents can verify one another's identities. This gives developers a common framework for building systems that work across platforms and services. The specification is now formalized and will be governed by the project's technical steering committee under the Linux Foundation.

"Autonomous AI agents are transacting and operating across global systems, but they can't succeed without verifiable identity," said Jim Zemlin, CEO of the Linux Foundation. "Under the neutral governance of the Linux Foundation, ANS provides a common foundation for trust that the entire industry can adopt, implement and improve together."

Tools that help AI agents find one another now use ANS identities. The AGNTCY Agent Directory Service, another Linux Foundation project, supports verification of ANS identities. Separately, ANS Finder implements the Agentic Resource Discovery (ARD) specification and passes its registry conformance tests, showing how agent discovery can incorporate verifiable identities.

Since ANS's intent to launch in June, 11 organizations have contributed to or adopted the standard, including Cisco, Cloudflare, DigiCert, DistributedApps.ai, GoDaddy, HOL, Infoblox, Radix, Salesforce, OWASP and Trustmodel.ai.

## Cómo funcionan registro y autenticación (Unite.AI, 10 nov 2026)

ANS is designed to let a system establish which registered agent it is dealing with before applying its own security policy. It binds a versioned name to a domain controlled by the agent's operator, uses the Domain Name System (DNS) to publish discovery information, and records signed lifecycle events in a transparency log. The approach reuses existing internet infrastructure instead of requiring a single proprietary agent registry.

The seven-layer specification covers identity, registration, versioned naming, DNS publication, transparency, integrity monitoring and agent authentication. An ANS name binds a version to a domain, as in `ans://v1.0.0.payments.example.com`; a new version requires a new registration.

During registration, the operator submits the agent host, version, endpoints and certificate material to a Registration Authority, which verifies domain control and the required proofs. The operator publishes the returned DNS records, and the authority checks them before activation. It then signs the lifecycle event and has the Transparency Log seal it, producing public artifacts that bind the registration to authorized certificates.

Peers use a supported discovery profile to locate endpoints and the shared `_ans-badge` record to find transparency evidence. Discovery alone does not authenticate the caller. Authentication requires three checks: the certificate is bound to the registered identity, the registration remains valid, and the caller holds the corresponding private key.

The ANS-6 authentication draft gives mutual TLS (mTLS) and application-layer Demonstrating Proof of Possession (DPoP) equal standing. mTLS suits an end-to-end TLS path, while DPoP binds a single-use proof to an HTTP request and can survive gateways that terminate TLS. A badge-tier verifier queries the Transparency Log for current evidence; the SCITT tier verifies a receipt and status token locally without per-request network calls. DPoP requires the SCITT binding.

The available software includes a Go reference implementation of the Registration Authority, Transparency Log and offline verifier.

## Modelo de seguridad y límites

The security model establishes identity rather than permissions. Authorization, delegation across a call chain and trust scoring are outside ANS-6, leaving each application to decide what an authenticated agent may do. Sealed metadata digests do not attest code running on a remote machine or guarantee agent behavior, and clients still need trusted log keys, correct signature and proof verification, freshness checks and a failure policy. Public badges, receipts and status tokens can also be replayed if a verifier omits possession checking. A receipt proves log history rather than current validity and can continue verifying after an agent is revoked, so it must be paired with a current status check.

Integration maturity also varies. The NVIDIA OpenShell work is labeled a research preview, and its destination-registration checks do not implement ANS-6 binding to the actual TLS peer certificate.

The initial technical steering committee has five voting members: Scott Courtney, Keith Perry and Connor Snitker of GoDaddy, Ken Huang of DistributedApps.AI, and Michael Kantor of Hashgraph Online.

## Anuncio de intención (23 jun 2026) y contexto

ANS builds on the existing Domain Name System (DNS) and establishes a federated framework for securely identifying autonomous agents at internet scale without relying on proprietary registries or centralized control. According to World Economic Forum data, 82% of executives plan to adopt AI agents within the next one to three years, despite widespread uncertainty around how to securely evaluate and manage autonomous systems. The ANS framework also supports decentralized identifiers (DIDs) and Legal Entity Identifiers (LEIs). Repositorio: https://github.com/agentnameservice. Más información: https://ansinfo.ai/.

## Riesgos del sustrato DNS (InfoWorld)

"DNS was not originally designed for high-assurance identity. This will make it susceptible to spoofing, hijacking, and latency or propagation inconsistencies that can undermine trust guarantees," dijo Dai. Para sortear estos problemas, las empresas deberían complementar ANS con IAM, identidad de carga de trabajo, gateways de IA y controles de seguridad de API, según Prakash. La Fundación sostiene que DNS por sí solo no pretende ser el único mecanismo de confianza dentro de ANS y que el marco admite DIDs y LEIs para vincular agentes a sistemas de identidad organizativos existentes.
