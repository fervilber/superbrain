---
title: "Cairn: un agente ofensivo explota un zero-day por su cuenta en 11 minutos"
source: "Amazon Threat Intelligence vía BleepingComputer / nhip.verai.vn / agentnewsdaily.com"
date: 2026-11-26
captured: 2026-11-26T20:08:00+01:00
---

# El agente ofensivo ya no necesita humano: Cairn explota un zero-day en 11 minutos

URL: https://nhip.verai.vn/en/2026-11-26
URL: https://agentnewsdaily.com/brief/2026-11-26

## El hallazgo

**Amazon Threat Intelligence** informó que operadores vinculados —con confianza moderada— a un grupo de nexos con China dieron a agentes que corrían sobre la plataforma de pentesting de código abierto **Cairn** la única instrucción de «obtener acceso a una shell» (_obtain shell access_). Según BleepingComputer, los agentes entonces **encontraron por su cuenta una vulnerabilidad de path traversal** en la herramienta de imagen médica **MONAI Label** y la explotaron **en 11 minutos**.

Los ataques corrieron del **8 al 10 de septiembre** de 2026, principalmente contra universidades de Asia Oriental. Los mantenedores publicaron un parche el **18 de noviembre**; Gizmodo siguió el caso el 24 de noviembre.

## Por qué importa

Es el patrón que la industria venía anticipando y que ahora tiene un caso documentado: **el ataque automatizado por agentes ya es real**, y no requiere que un humano descubra el fallo ni que escriba el exploit. Un agente al que se le da un objetivo de alto nivel —acceso a shell— explora, encuentra un fallo no divulgado y lo explota, encadenando capacidades que antes requerían a un analista humano en el bucle.

Esto empuja a los defensores a repensar el hardening: si el tiempo entre «objetivo» y «explotación» se mide en minutos y no en días, la ventana de detección y respuesta se estrecha drásticamente. Es el reverso ofensivo de la misma ola que en otras ediciones documentó frameworks como PentAGI o exploit_agent que automatizan descubrimiento y explotación sin humano en el bucle.
