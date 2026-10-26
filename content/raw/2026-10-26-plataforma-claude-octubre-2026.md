---
title: "Notas de versión de la plataforma Claude (octubre de 2026): API 2026-10-21, OpenTelemetry, flujos dinámicos y perfiles de usuario"
source: "https://platform.claude.com/docs/en/release-notes/overview"
author: "Anthropic"
date: 2026-10-22
captured: 2026-10-26
---

# Captura: notas de versión de la plataforma Claude (octubre de 2026)

> Extracto verbatim de las entradas de octubre de 2026 de las notas de versión oficiales. Se reproduce el contenido, ordenado de más reciente a más antiguo; se omiten las entradas anteriores a octubre de 2026.

## 22 de octubre de 2026

- Lanzamiento de **Claude Models on Google Cloud (Anthropic managed)**: la API de Claude operada por Anthropic y alcanzada a través de tu proyecto de Google Cloud. El IAM de Google Cloud controla el acceso; Google Cloud Marketplace gestiona la facturación.
- **Fast mode** disponible para Claude Opus 5.5 en Claude Models on Google Cloud (Anthropic managed).

## 21 de octubre de 2026

- Release de la versión de API **`2026-10-21`**. Hay guía de migración.
- Nuevas versiones de los SDK cliente y del CLI `ant` que envían la versión de API `2026-10-21` por defecto: Python SDK 2.0.0, TypeScript SDK 1.0.0, C# SDK 13.0.0, Go SDK 2.0.0, Java SDK 3.0.0, PHP SDK 1.0.0, Ruby SDK 2.0.0 y `ant` CLI 2.0.0.
- Las nuevas versiones de SDK y CLI también tienen **cambios de ruptura que no dependen de la versión de API**, y pasan a licenciarse bajo **Apache 2.0** en lugar de la licencia MIT.
- Añadidos los campos `enforcement_status` y `enforcement_actions` a los **perfiles de usuario**, para ver si Anthropic ha restringido o vetado a uno de tus clientes finales. Se pueden listar los perfiles con restricción o veto abiertos con el nuevo filtro `enforcement_status[]`.

## 20 de octubre de 2026

- La **Claude Tag API** está disponible en beta para organizaciones Claude Enterprise con la cabecera beta `experimental-claude-tag-2026-10-21`. Sus endpoints `/v1/organizations/claude_tag/` leen y cambian los ajustes de Claude Tag en canales y espacios de trabajo de Slack, muestran qué ajustes aplican en un canal y de dónde vienen, y adjuntan _Access bundles_. Se llama con una clave de Admin API con scope `read:claude_tag` o `write:claude_tag`. No disponible para organizaciones de Claude Platform (Claude Console).
- Los **hooks de inferencia** salen de beta para organizaciones Claude Enterprise.
- Lanzamiento de **perfiles de usuario**, para decirle a Anthropic a qué cliente final corresponde cada petición de API. Si operas una plataforma o gateway, o revendes acceso a la API, una acción de cumplimiento de seguridad puede aplicarse a un cliente final en lugar de a toda tu organización.
- Añadidos **webhooks de organización** a la Admin API, en beta con la cabecera `webhooks-2026-10-07`. Sus endpoints `/v1/organizations/webhooks` registran destinos de webhook para dos tipos de evento: cuando Anthropic restringe o veta uno de los perfiles de usuario de tu organización, y cuando la restricción o veto termina.
- Los administradores de organización pueden **desactivar el web fetch** para su organización en la página **Capabilities** de la Claude Console. Con web fetch desactivado, una petición a la Messages API que incluya la herramienta de web fetch falla con error 400. En una sesión de Claude Managed Agents, las llamadas a `web_fetch` devuelven un resultado de error al agente. Con web fetch activado, los administradores también pueden fijar dominios permitidos o bloqueados.
- En Claude Managed Agents, la herramienta `web_fetch` ahora sigue las restricciones de dominio de web fetch de tu organización. Una URL, incluida una alcanzada por redirección, debe pasar tanto la lista de la organización como la lista `allowed_domains` o `blocked_domains` de la herramienta `web_fetch` del agente.
- En Claude Managed Agents, las sesiones siguen los ajustes de búsqueda web de tu organización: el ajuste **Allow web search** desde el 6 de octubre, y sus restricciones de dominio desde el 14 de octubre.

## 15 de octubre de 2026

- Añadido `capabilities.thinking.types.between_tools` a la **Models API**. `GET /v1/models` y `GET /v1/models/{model_id}` ahora informan de si cada modelo acepta `thinking: {type: "between_tools"}`, que desactiva el pensamiento previo.
- La **Compliance API** ahora devuelve el texto que cada miembro de la organización guardó como **Instructions for Claude** en claude.ai y como **Global instructions** en Cowork, en beta para Claude Enterprise.
- **Fast mode** sale de research preview para Claude Opus 5.5 y ya no requiere solicitar acceso. Las peticiones a Claude Opus 5.5 ya no requieren la cabecera beta `fast-mode-2026-02-01`, y las que la sigan enviando siguen funcionando. Fast mode para Opus 5 y Opus 4.8 permanece en research preview.
- Fast mode para Claude Opus 5.5 disponible en **Claude in Microsoft Foundry** para despliegues alojados en Azure.

## 14 de octubre de 2026

- Lanzamiento de **OpenTelemetry export** en beta, para trazar peticiones a la Messages API y sesiones de Claude Managed Agents en tu plataforma de observabilidad. El SDK de Claude emite spans en Python, TypeScript, C#, Go, Java, PHP y Ruby. Para obtener spans de la API, hay que añadir un destino OpenTelemetry en la Claude Console.
- Los **despliegues programados** de Claude Managed Agents están disponibles en Claude Platform on AWS.

## 9 de octubre de 2026

- Se puede dejar que un agente de Claude Managed Agents use **flujos dinámicos**, en beta con la cabecera `managed-agents-2026-04-01`. Para trabajo con muchas piezas, como revisar cientos de documentos, el agente puede escribir un _workflow_: un programa que ejecuta muchos agentes en fases y combina sus resultados. El servidor lo corre en segundo plano como una _workflow run_. Para activarlo, poner el campo `multiagent` del agente a `{"type": "multiagent_20261001", "workflows": {"type": "enabled"}}`. Seguir cada ejecución mediante eventos `workflow_run.*` en el flujo de eventos de la sesión.

## 8 de octubre de 2026

- Los endpoints de chat de la **Compliance API** ahora devuelven también chats de la experiencia unificada de Claude, en beta para Claude Enterprise.
- La Compliance API puede descargar documentos de Claude Docs como ficheros de Word, en beta.

## 7 de octubre de 2026

- **Bajada de precio de las lecturas de caché de prompt en Claude Sonnet 5.5**, de 0,20 USD a **0,10 USD por millón de tokens**: 0,05x del precio base de entrada en lugar de 0,1x. Las escrituras de caché y todos los demás precios no cambian.
- Lanzamiento de **Claude Haiku 5.5** (`claude-haiku-5-5`), el modelo más capaz de Anthropic ajustado para trabajo de alto volumen y sensible a latencia. Tiene ventana de contexto de **1M tokens**, 128k tokens máximos de salida, y pensamiento adaptativo con el parámetro `effort`. Disponible en la API de Claude, Claude in Amazon Bedrock, Claude Platform on AWS, Claude on Google Cloud y Claude in Microsoft Foundry.
- El código escrito para Claude Haiku 4.5 puede romper en Haiku 5.5: el pensamiento extendido manual (`budget_tokens`), los parámetros de muestreo `temperature`, `top_p` y `top_k`, y el prefill de mensaje de asistente pueden devolver un error 400 cada uno. `computer_20250124` también devuelve 400: usar el toolset `computer_toolset_20260801` en la API de Claude y Google Cloud, o `computer_20251124` en Amazon Bedrock.
- Los SDK de Python y TypeScript ahora incluyen clases, en beta, para la **herramienta de uso de navegador** y la **herramienta de uso de ordenador**. Se hereda una clase y se escribe un método por herramienta contra tu propio navegador o automatización de escritorio. El SDK corre el bucle de herramientas, las políticas de URL y ficheros que fijes para el navegador, y tu callback de aprobación.
- Los planes Claude Max y Team ahora incluyen **créditos mensuales de API**.
- En Claude Managed Agents, un entorno de nube con red `limited` aplica ahora sus `allowed_hosts` también a las herramientas `web_search` y `web_fetch`.

## Fuente original

- Anthropic — _Claude Platform release notes_ (octubre de 2026): https://platform.claude.com/docs/en/release-notes/overview

## Nota de captura

Captura por extracto verbatim de las entradas de octubre de 2026. El texto completo limpio (que incluye el histórico hasta 2024) está en la caché de `web_extract` (`/home/vilber/.hermes/cache/web/platform.claude.com-4182359e79.md`).
