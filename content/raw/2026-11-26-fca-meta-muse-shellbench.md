---
title: "Regulador y benchmark: la FCA, Meta Muse y ShellBench miden al agente"
source: "agentnewsdaily.com / aiagentnews.io / nhip.verai.vn"
date: 2026-11-26
captured: 2026-11-26T20:09:00+01:00
---

# El regulador entra en el bucle y el benchmark pone nota

URL: https://agentnewsdaily.com/brief/2026-11-26
URL: https://aiagentnews.io/
URL: https://nhip.verai.vn/en/2026-11-26

## La FCA advierte a las firmas de agentes de IA

La **Financial Conduct Authority (FCA)** británica advirtió el 24 de noviembre, según Reuters, que las empresas de tecnología y redes sociales cuyos agentes de IA ofrezcan servicios financieros podrían enfrentarse a acción regulatoria. No nombró empresas, pero dijo que los agentes que hagan promociones financieras, den asesoramiento o presten servicios de pago pueden quedar bajo sus reglas. Instó a las firmas a hablar con sus supervisores pronto.

La FCA subraya que la **responsabilidad de cumplimiento sigue recayendo en las firmas y sus altos directivos** incluso cuando se usan proveedores externos, y espera que las firmas comprendan la autonomía y los riesgos de sus sistemas. Deberían considerar también cómo verificar que están tratando con un agente, qué está autorizado a hacer y la responsabilidad cuando aceptan instrucciones de pago de agentes o de carteras controladas por agentes.

### Meta rechazó las pruebas conjuntas de Muse

La FCA dijo que **Meta declinó su sugerencia de probar conjuntamente el asistente personal Muse** en el sandbox del regulador. Varios organismos de vigilancia británicos han advertido además a Meta que se asegure de que sus productos de IA cumplen la ley de protección del consumidor.

## Meta lanza Muse en el Reino Unido sin acceso a datos bancarios

Meta lanzó su agente personal **Muse** en el Reino Unido con socios de retail y viajes, entre ellos Sainsbury's, Argos, Marks & Spencer, Trainline y easyJet, según Retail Insight Network. Reuters informó de que, **a diferencia de la versión estadounidense, la versión británica no puede leer saldos bancarios, inversiones ni detalles de hipotecas**. Meta dice que conectará servicios bancarios solo tras consultar a los reguladores y obtener las licencias que necesite.

Además, Meta llevó Muse a los **DM de Instagram**: usuarios de EE. UU., Canadá, México, Japón y Singapur pueden chatear con Muse dentro de hilos de mensajes directos, compartir publicaciones para que actúe sobre ellas (por ejemplo, añadir una cafetería a un itinerario) y organizar publicaciones guardadas en Colecciones. Meta afirma que nada se envía ni se publica sin aprobación del usuario y que las acciones del agente pueden deshacerse.

## ShellBench: los agentes líderes fallan unas 4 de cada 10 tareas reales

En un benchmark de 100 tareas del mundo real, **GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2 y Gemini 4 Carbon completaron solo unas seis de cada diez**. El **51 % de los fallos** consistieron en **omitir detalles clave incluso cuando el agente había encontrado la información**. Los resultados variaron acusadamente entre ejecuciones y arneses, y **el coste por ejecución difirió unas seis veces** entre modelos de puntuación similar.

La lección: el cuello de botella ya no es tanto «encontrar» la información como «usarla» de forma fiable, y el coste de un resultado comparable puede variar enormemente según el harness. Es un recordatorio de que un score de benchmark no dice nada sobre el precio real de operar ese agente.

## Tooling: releases del día

- **E2B Python SDK 2.65.0**: añade métodos para leer los detalles de una plantilla y su historial de builds; marca como obsoletos los métodos `sandbox.git` (se sustituyen por ejecutar git a través de `sandbox.commands.run()`).
- **E2B CLI 2.25.0**: añade `e2b sandbox port-forward` (alias `pf`), que mapea un puerto local a un puerto dentro de un sandbox en ejecución; actualiza dependencias (undici, con correcciones de seguridad).
- **@e2b/acp 0.1.0**: paquete para ejecutar agentes ACP (goose, OpenCode, Claude Code) dentro de un sandbox de E2B.
- **Langfuse v4.87.0**: añade guardarraíles a su AI gateway, acción de reinicio de presupuesto para usuarios y claves de API, y un proveedor AWS Bedrock Guardrails.
- **Cline v4.1.28 / SDK v0.2.2**: refresca el catálogo de modelos, elimina modelos OpenAI deprecados, añade proveedores (Concentrate, Prima Labs) y retira exports de telemetría.
