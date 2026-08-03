---
title: Informe-2026-07-03
date: 2026-07-03
tags: [superbrain, quartz, github, conocimiento]
---
# Informe-2026-07-03: Configuración de Superbrain (Quartz v5)

## Contexto
Creación de un "segundo cerebro" interconectado para la gestión del conocimiento y el seguimiento de agentes de IA.

## Solución Técnica
- **Motor**: Quartz v5 publicado en GitHub Pages.
- **Estructura**: `content/` estructurada para `llm-wiki` (`raw`, `entities`, `concepts`, `sessions`).
- **Despliegue**: Automatizado vía GitHub Actions, incluyendo el bypass de Jekyll mediante `.nojekyll`.
- **Mejora**: Configuración de `baseUrl` para subcarpeta y resolución `absolute` de enlaces.
