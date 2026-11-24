---
title: "Meta lanza Muse en el Reino Unido con aprobación obligatoria por compra"
source: "Startup Fortune / Emergent / The Guardian"
date: 2026-11-24
captured: 2026-11-24T20:05:00+01:00
---

# Meta lanza Muse en el Reino Unido con aprobación obligatoria por compra

> Captura por extractos verbatim de la cobertura del 23-24 de noviembre de 2026 (Startup Fortune, Emergent, The Guardian). El artículo de The Guardian no se pudo extraer (Failed to fetch); su contenido se cita a través de la cobertura secundaria.

## Startup Fortune — "Meta launches its Muse AI agent in the UK just as Christmas shopping peaks"

Meta launched Muse, its personal AI agent, in the UK this week, with a post on its newsroom dated November 23 and coverage from The Guardian on November 24 framing it as a tool that can do your Christmas shopping. According to Meta's announcement, Muse is open to UK users aged 18 and over on iOS, Android, muse.ai and WhatsApp.

It arrives with a list of named UK partners. Meta's post lists Marks & Spencer, Currys, Trainline and Sainsbury's among its connectors, alongside Debenhams Group, Ocado Retail, Argos, ASOS, Jet2 and easyJet. Spotify and OpenTable are on the list too, and Muse can also connect to Instagram, email and calendar.

The agent can browse, compare and put together a basket across those connected services. The brake is on payment: according to coverage of Meta's announcement, users must approve every purchase and every outgoing email. A separate security agent checks Muse's actions against the permissions you've granted, and passwords and payment methods sit in a credentials store the AI model can't see.

That design is a direct answer to the obvious fear, an agent that buys the wrong thing at 11pm. It also means Muse is, for now, closer to a very good shopping assistant than a delegate with your card.

Meta launched its Muse AI agent on September 8, 2026 promising to handle errands and negotiations on your behalf. Weeks later, a YouTuber says Muse gave his home address to a Facebook Marketplace buyer and arranged a pickup without asking him, part of a wider pattern of the agent oversharing private information without permission.

The detail worth watching is which retailers have actually done work for Muse. Superpower Daily reports that Meta has agreements with M&S, Currys, Sainsbury's and easyJet to make their sites easier for the agent to navigate, and its list doesn't include Trainline, which Meta's own post does name. Coverage differs on how deep each tie goes, so treat the partner list as a map of intent rather than a guarantee that every checkout works end to end.

Search and affiliate economics depend on a shopper typing a query, seeing ads and clicking through. If a gift request in WhatsApp ends in a basket at Currys, the click that Google or a comparison site used to take a cut of never happens. Meta already makes its money from advertising, so an agent that sits between a shopper's intent and a retailer's checkout is a natural place for it to build a new ad and fee line. Frankly, that is the real reason this launch matters more than the gadgetry.

Meta isn't alone. OpenAI and Google both have shopping agents, and Muse has passed 10 million downloads, according to Meta. In May, Debenhams Group said it had become the first UK retailer to enable AI-driven checkout on Meta, though only for US customers of Karen Millen, boohoo, boohooMAN and PrettyLittleThing.

For a retailer, the trade is awkward. Being on Muse puts you in front of people already inside Instagram and WhatsApp. It also hands Meta the customer relationship, and the data on what that customer nearly bought.

Muse's US run hasn't been clean. Reuters reported that Meta staff raised internal concerns about undesired actions by the agent after its US debut, including access to encrypted messages and wrong purchase information. Meta told Reuters the flagged examples were isolated incidents and that many of the messages in question were hallucinations it has since addressed. Superpower Daily also notes that tests showed different access to Signal messages across Android, iPhone and macOS, which is the sort of permission gap that makes a privacy-minded user wary.

UK regulators have already flagged the category. Coverage of the launch cites a warning last month that AI agent products may "amplify and accelerate risks" for consumers. Nobody has yet answered the practical question of who pays when an agent misreads a request and the user taps approve anyway. Under UK consumer law the retailer and the buyer have well-worn duties, but a third-party agent in the middle isn't something those rules were written around.

Meta hasn't said how Muse will be paid for by retailers in the UK, or whether partner placement will be influenced by advertising. That is the answer that will decide whether this is a neutral assistant or a new shopfront.

## Emergent — "Meta Muse AI Agent Launches in UK with Purchase Controls"

Meta officially launched Muse, its personal AI agent, for UK adults on November 23, 2026, becoming the first Big Tech company to ship an AI agent product in the United Kingdom. The autonomous assistant handles tasks like booking travel, managing refunds, and coordinating shopping across integrated apps, but every purchase requires explicit user approval before execution.

Muse integrates with launch partners including Marks & Spencer, Ocado, Trainline, Currys, easyJet, Spotify, and OpenTable. The agent autonomously plans and executes multi-step workflows across these services, handling tasks from comparing insurance quotes to tracking school calendars. Users connect the apps they want Muse to access, with granular permission controls determining whether the agent can read, send, or execute actions within each service.

Meta implemented a layered security model with an isolated runtime environment and Sentinel permission authority that validates every action against granted permissions. User credentials including passwords and usernames are stored in a secure credentials store that allows Muse to complete authorized actions without exposing sensitive data to the underlying AI model. The system automatically ignores one-time codes and password-reset links in email to prevent credential leakage.

Users control approval frequency through settings, choosing between per-action confirmation or longer-duration permissions for specific task types. All purchases mandate individual approval regardless of other permission settings. Meta maintains a complete audit log of every action Muse has executed and plans to take.

Meta explicitly acknowledged that prompt injection, a vulnerability where malicious instructions embedded in external content can hijack agent behavior, "remains an open problem" across the AI industry. The company relies on runtime isolation and the Sentinel permission layer to contain potential damage from compromised instructions, but did not claim to have solved the fundamental security challenge.

The UK's Digital Regulation Cooperation Forum issued a warning that AI agents "may amplify and accelerate risks" to consumers, highlighting regulatory scrutiny of autonomous systems with purchasing authority.

Conversations with Muse and stored personal information remain separate from Meta's advertising systems. Users can opt out of having their interactions used to develop and improve Meta's AI models, though this setting defaults to enabled at signup. Private messages from email or Instagram Direct Messages are excluded from model training entirely.
