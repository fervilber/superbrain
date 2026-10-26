---
title: "OpenAI Decisions API: de beta a disponibilidad general (22 de octubre de 2026)"
source: "https://developers.openai.com/api/docs/guides/decisions | https://openai.com/index/decisions-api | https://cellcog.ai/blog/openai-decisions-api | https://releasebot.io/updates/openai"
author: "OpenAI / CellCog"
date: 2026-10-22
captured: 2026-10-26
---

# Captura: Decisions API (`POST /v1/decisions`)

> Captura por extractos verbatim. Fuentes: guía oficial de OpenAI, post de lanzamiento, changelog de la API y análisis de CellCog (revisado el 22 de octubre de 2026).

## Qué es

`POST /v1/decisions` toma **texto o imágenes más una lista de preguntas** y devuelve **respuestas tipadas** (una probabilidad, una opción o una puntuación) **en lugar de texto generado**. Corre únicamente sobre **`gpt-6-luna`**, cuesta **0,10 USD por millón de tokens de entrada no cacheados** y **nada por la salida**, y OpenAI afirma que "devuelve respuestas tipadas unas **10× más rápido** que la Responses API".

Producto lanzado en **beta pública el 6 de octubre de 2026** y en **disponibilidad general el 22 de octubre de 2026**.

## Ficha

| Elemento                | Decisions API                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Lanzamiento             | 6 de octubre de 2026 (beta pública)                                                                                                  |
| Disponibilidad general  | 22 de octubre de 2026                                                                                                                |
| Endpoint                | `POST /v1/decisions`                                                                                                                 |
| Modelo                  | solo `gpt-6-luna`                                                                                                                    |
| Entradas                | texto, imágenes (base64 inline o URL pública) o JSON                                                                                 |
| Tipos de pregunta       | `predicate`, `choice`, `score`                                                                                                       |
| Precio                  | 0,10 USD por millón de tokens de entrada no cacheados; sin cargo de salida; cache hits con descuento, escrituras de caché facturadas |
| Afirmación de velocidad | ~10× más rápido que la Responses API                                                                                                 |
| Controles de datos      | Zero Data Retention y HIPAA para clientes elegibles; procesamiento regional en EE. UU. y Europa                                      |
| Playground              | platform.openai.com/decisions                                                                                                        |

## Qué cambió al pasar a GA

| Elemento                  | Beta (6 oct)        | GA (22 oct)                                                 |
| ------------------------- | ------------------- | ----------------------------------------------------------- |
| Preguntas por petición    | 200                 | **400**                                                     |
| Imágenes                  | solo base64 inline  | base64 o URL pública HTTP/HTTPS; imágenes por pregunta      |
| Entrada JSON              | no soportada        | partes de contenido `input_json`                            |
| Caché de prompt           | sin cargos de caché | cache hits con descuento, escrituras de caché facturadas    |
| Historial de conversación | no listado          | mensajes más llamadas y salidas de funciones y herramientas |
| Reporte de uso            | no listado          | `GET /v1/organization/usage/decisions`                      |
| Modelo                    | `gpt-6-luna`        | `gpt-6-luna`                                                |

Sobre el precio de caché: el prefijo cacheado debe ser de **al menos 1.024 tokens** de entrada compartida, así que la caché compensa cuando muchas preguntas se hacen contra el mismo documento o imagen. Tarifas citadas de Luna: **0,01 USD por millón de tokens de entrada cacheados**, y **0,125 USD por millón por una escritura de caché de 30 minutos** o **0,25 USD por una de 12 horas**. El mismo modelo por la Responses API cuesta 0,10 USD por millón de entrada y **0,50 USD por millón de salida**: una llamada a Decisions elimina la factura de salida.

## Los tres tipos de pregunta

| Tipo        | Sirve para                                                             | Qué devuelve                                                                              |
| ----------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `predicate` | Comprobar si se cumple una condición (p. ej. daño visible en una foto) | Una probabilidad de 0 a 1 de que la condición sea cierta                                  |
| `choice`    | Elegir una opción de un conjunto fijo (p. ej. un departamento)         | El valor elegido, una probabilidad por cada opción y una confianza                        |
| `score`     | Puntuar una entrada en niveles ordenados (p. ej. severidad)            | La media ponderada por probabilidad de los índices de nivel, que puede caer entre niveles |

Consejo textual de la guía: fijar los umbrales a partir de ejemplos etiquetados propios, ponderados por el coste de un falso positivo frente a un falso negativo. Cuando la tarea es producir un objeto con forma propia (campos extraídos, una explicación escrita), la guía remite a **Structured Outputs** en la Responses API: **Decisions es para respuestas, no para generación**.

## Comparativa de precio con Jev (TypeSafe)

| Elemento                        | OpenAI Decisions API      | TypeSafe Jev 1.13      | gpt-6-luna en Responses       |
| ------------------------------- | ------------------------- | ---------------------- | ----------------------------- |
| Precio de entrada por 1M tokens | 0,10 USD                  | 0,042 USD              | 0,10 USD                      |
| Precio de salida por 1M tokens  | Ninguno                   | Gratis                 | 0,50 USD                      |
| Imágenes                        | Sí (base64 o URL pública) | No, solo texto         | Sí                            |
| Tipos de respuesta              | predicate, choice, score  | boolean, choice, score | Texto libre o tu esquema JSON |

Cálculo de la fuente: 1M de clasificaciones de 500 tokens cuestan unos **21 USD en Jev** frente a **50 USD en OpenAI**. Ninguno de los dos ha publicado una comparativa de precisión cara a cara.

## Clientes citados y una cifra

El post de lanzamiento nombra a **Box, Datadog, Ramp, Sierra y Speak** como clientes, y tres usuarios internos: el equipo de dots, Personal Finance (categorizar descripciones de transacciones) y Communications (clasificar cobertura por temas y puntuar si refuerza o cuestiona narrativas clave). La única cifra de cliente es de Box: "en nuestra evaluación, la Decisions API logró una **selección de ruta ~5× más rápida en 30 casos** de certificado de seguro, con la misma precisión que la Responses API". Son 30 casos, muestra pequeña, y la afirmación titular de OpenAI sigue siendo "hasta 10× más rápido". El post añade también un **trigger nativo de GPT-Live**, para que una sesión de voz pueda llamar a Decisions mientras el usuario habla, y más capacidad en varias regiones asiáticas.

## Forma de la petición

Una petición tiene tres partes: el `model` (solo `gpt-6-luna` hoy), el `input` (una cadena de texto, o mensajes de usuario mezclando texto e imágenes) y las `questions`, cada una con un nombre único, un tipo e instrucciones. La respuesta es un array `answers` indexado por esos nombres.

## Qué vigilar (según la fuente)

- Si otros modelos se suman al endpoint ahora que es GA.
- Una cifra publicada de calibración o precisión, de OpenAI o de un evaluador independiente, contra Jev o una línea base de Responses.
- Cualquier cambio de precio o funciones de TypeSafe tras el 6 de octubre.
- Mediciones independientes de latencia que confirmen la afirmación de 10×.

## Contexto de plataforma (DevDay 2026)

Del recap de DevDay 2026 (22 de octubre): la **Agents API** ahora soporta **computer use**, para construir agentes que interactúan con software y completan tareas, y trae a la aplicación las capacidades multiagente de Codex, búsqueda de herramientas, llamada de herramientas y compactación de contexto. OpenAI ejecuta la infraestructura subyacente.
