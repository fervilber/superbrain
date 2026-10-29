---
title: "Nous Research — Hermes Agent: suscripciones renovadas, plugin de SFX de ElevenLabs y NousCon 2026"
source: "https://x.com/NousResearch"
author: "Nous Research (@NousResearch, X)"
date: 2026-10-27
captured: 2026-10-29
---

# Captura: Nous Research — novedades de Hermes Agent (26-27 de octubre de 2026)

> Extractos de la cuenta oficial de Nous Research en X y del catálogo de plugins de Hermes Agent, con anuncios del 26 y 27 de octubre de 2026 y contexto de NousCon 2026.

## Suscripciones renovadas (27 de octubre de 2026)

> "We've revamped Hermes Agent subscriptions. Every new plan now includes a cloud agent out of the box, and usage has daily and weekly limits instead of one monthly block of credits. Subscribers can switch to the new plans any time at portal.nousresearch.com/billing"

**Lectura:** el agente en la nube pasa a ser parte del plan base (no un extra), y el modelo de consumo cambia de un bloque mensual de créditos a **límites diarios y semanales** — el mismo patrón de "cuota de cómputo flexible" que introduce GitHub con su pool en dólares.

## Plugin de SFX de ElevenLabs (27 de octubre de 2026)

> "Introducing the @ElevenLabs SFX plugin, built to continue the work on a suite of Game Dev Studio capabilities for your Hermes Agent! Hermes made this demo video to see it in action, you can install it right now from the plugins catalog: hermes-agent.nousresearch.com/docs/plugins/e…"

> "Generate SFX with @ElevenLabs straight from Hermes Desktop with looped playback, one-click variation generation, and a helpful library of all your sounds."

**Lectura:** los plugins oficiales de Hermes continúan expandiéndose (el catálogo lista 24 plugins del autor NousResearch, 19 oficiales, ~9.9k estrellas de GitHub). El plugin de SFX se instala desde el catálogo y se usa desde Hermes Desktop.

## NousCon 2026 (30 de octubre, Nueva York)

> "NousCon 2026 October 30th, NYC" (anuncio del 29 de septiembre de 2026).

Anuncios relacionados de la misma ventana: hackathon anti-slop en la sede de Pangram (NYC); "Hermes Index" (media de benchmarks de rendimiento de modelos); varios modelos gratuitos o con descuento en Nous Portal (Step 5 Preview de StepFun, Solar Mini 4 de Upstage, Grok 4.7 de xAI al 50% durante una semana); "Sign in with ChatGPT" en asociación con OpenAI; consolidación de los plugins oficiales de Hermes; y el catálogo de plugins de Hermes Agent.

## Contexto (del blog de desglose de Hermes Agent)

Hermes Agent es un agente de IA autónomo, open source, de Nous Research, bajo licencia MIT, publicado en febrero de 2026. Se ejecuta en tu propio servidor, persiste memoria entre sesiones, construye sus propias skills a partir de la experiencia y te alcanza a través de Telegram, Discord, Slack y apps de escritorio para macOS, Windows y Linux. Soporte Tier 1: macOS Apple Silicon, Windows 10/11, Linux, WSL2 y Docker; Tier 2: Android vía Termux y Nix. Los modelos Hermes 4 (70B, 405B) están disponibles en el Portal pero no se recomiendan dentro del propio agente (están afinados para chat, no para el bucle rápido de tool-calling).

## Notas del capturador

- **El agente en la nube es ahora parte del plan base** y el consumo se mide en límites diarios/semanales, no en un bloque mensual. Convergencia con GitHub (pool en dólares) y con el resto del sector: el coste del agente deja de ser lineal por token.
- **Catálogo de plugins como superficie de extensión**: SFX de ElevenLabs, NVIDIA Broadcast (vía gateway MCP local), Meshy AI (MCP para 3D). El plugin de Meshy es notable: cada llamada que gasta crédito pasa por el prompt de aprobación de Hermes.
- **NousCon 2026 el 30 de octubre** en NYC: cae un día después de este informe; es el evento donde es previsible que se anuncien capacidades nuevas del agente.
- Se mantiene la línea de "modelo intercambiable, arnés propio": Hermes no recomienda sus propios modelos de chat dentro del bucle de agente.
