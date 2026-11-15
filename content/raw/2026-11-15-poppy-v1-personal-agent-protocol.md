---
title: "Sierra publica Personal Agent Protocol 1.0 (Poppy): más de 100 socios y soporte en Muse de Meta"
source: "https://sierra.ai/blog/releasing-poppy"
date: 2026-11-13
captured: 2026-11-15
---

# Releasing Personal Agent Protocol 1.0

Fuente: Sierra (sierra.ai/blog), Bret Taylor y Clay Bavor, 13 de noviembre de 2026.

## Contenido (verbatim, selección)

> Personal Agent Protocol — or Poppy for short — has gained real momentum since we first announced this new standard with our initial design partners Meta, Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart last month. Poppy enables personal agents to interact with companies through business agents, websites, and APIs and today we're excited to announce that:
>
> - v1.0 of the protocol is now available.
> - Shopify has enabled Poppy for every merchant on its platform.
> - Multiple design partners are now going live with Poppy, including Mercury, Synchrony, and Turkish Airlines.
> - Poppy is now on for everyone who uses Muse, Meta's AI agent, which automatically looks for Poppy first on every site it visits.
> - 60 new companies are joining as design partners, bringing the total to more than 100 — including Affirm, Aflac, Agoda, Aircall, Akoya, Aviva, Banco Sabadell, Braze, Browserbase, Checkout.com, Cisco, Cover Genius, Creditas, Crunch Fitness, Cue, Delta Air Lines, Descope, EarnIn, Five9, Freshworks, Fullstory, Gen Digital, Global Payments, GoFundMe, GoodRx, Guardian, HealthEx, HelloFresh, Hyatt, Infoblox, Intuit, Kernel, Kin Insurance, Lemonade, Liberty Global, Manus, Mercury, Navy Federal Credit Union, Neptune Flood, Ora, Persona, Pindrop, Ping Identity, Profound, Prosus, Remitly, Runlayer, Salesforce (including Fin, Commerce Cloud, and Agentforce), Socure, SoFi, Symphony by Wix, The Knot, The Zebra, Travelers, Turkish Airlines, Twilio, Wayfair, Wix, WorkOS, and Zoom.

## Poppy v1.0 (verbatim)

> Version 1.0 of Poppy reflects what design partners have learned over the past five weeks as they've tested the drafts against real websites, APIs, and agents.

> The protocol defines how personal agents connect with companies that implement it, providing clear and comprehensive access to everything they offer, largely built with existing standards like MCP, OpenAPI, and UCP. With authentication through OAuth, customers control what personal agents can and can't do, and can manage their access over time. Since the initial draft, we've:
>
> - Made it easier for companies to adopt the protocol in stages, starting with the basics and adding capabilities over time;
> - Refined how the protocol uses existing standards;
> - Expanded a company's ability to provide guidance and collect feedback from the personal agent;
> - Introduced extensions, such as the commerce extension co-authored by Shopify, so industries can build on the core protocol without changing it.

> With v1.0, any company can implement Poppy on its own and immediately start delivering a better experience for customers who use Muse. Our implementation kit walks you through setup and includes a validator to check your work.

> UCP and Poppy complement each other. UCP handles the shopping itself, like finding products, filling a cart, and checking out. Poppy handles what happens before that, when an agent shows up at a store, says who it is, and finds out what it's allowed to do.

## Lectura técnica

- **Poppy v1.0** define cómo un **agente personal** se conecta con empresas que lo implementan, apoyándose en estándares existentes (**MCP, OpenAPI, UCP**) y con **autenticación OAuth** que deja al cliente controlar qué puede y qué no puede hacer su agente personal.
- **Adopción**: Shopify habilita Poppy para **todos los comerciantes** de su plataforma (más de 175 países); Poppy se activa para todos los usuarios de **Muse**, el agente de Meta, que «busca Poppy primero en cada sitio que visita»; los socios pasan de 8 a **más de 100**.
- **Arquitectura por capas**: UCP se ocupa de la compra (buscar, llenar carrito, pagar); **Poppy se ocupa de lo anterior**: cuando el agente llega a una tienda, se identifica y descubre qué le está permitido hacer.
- **Extensibilidad**: extensiones como la de comercio (coautoría con Shopify) permiten a cada industria construir sobre el protocolo sin modificarlo.
