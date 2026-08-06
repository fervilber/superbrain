---
title: Informe-2026-08-04
date: 2026-08-04
tags: [hermes, infraestructura, tavily, busqueda]
---

# Informe-2026-08-04: Migración de Motor de Búsqueda a Tavily

## Contexto

El sistema de búsqueda previo basado en **SearXNG** presentaba fallos constantes debido a la falta de configuración de la URL (`SEARXNG_URL is not set`) y restricciones de acceso desde el entorno del servidor.

## Solución Técnica: Implementación de Tavily AI

Se ha migrado toda la infraestructura de búsqueda de Hermes Agent a **Tavily AI**, un motor optimizado para agentes autónomos.

### Pasos realizados:

1. **Instalación de la CLI**: Se utilizó el script oficial de instalación de Tavily.
   ```bash
   curl -fsSL https://cli.tavily.com/install.sh | bash
   ```
2. **Autenticación**: Configuración de la API Key (`tvly-dev-...`) en el entorno de ejecución del VPS.
3. **Instalación de Skills**: Se instalaron las habilidades específicas de Tavily para Hermes mediante `npx skills add tavily-ai/skills --all`.
4. **Verificación**: Se confirmó el funcionamiento mediante `curl` a la API oficial de Tavily, validando la recepción de resultados técnicos precisos.

## Implicaciones para la Evolución

- **Fiabilidad**: La búsqueda deja de ser un punto de fallo en las tareas programadas (cron jobs).
- **Calidad de Ingestión**: Las futuras actualizaciones del `superbrain` serán más profundas, al disponer de una API diseñada para extraer datos estructurados.
- **Seguridad**: La configuración sigue buenas prácticas manteniendo la clave en variables de entorno, sin exposición en archivos del repositorio.

---

_Este conocimiento fue registrado como parte del proceso de mejora continua del sistema._
