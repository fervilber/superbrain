---
title: "Informe Técnico: Implementación de TV en vivo en Jellyfin con IPTV-ORG"
date: 2026-08-06
tags: [jellyfin, iptv, vps, multimedia]
---
# Informe Técnico: Implementación de TV en vivo en Jellyfin

## Contexto
El objetivo era integrar una solución de televisión y radio en vivo dentro de la instancia de Jellyfin alojada en el VPS, buscando una configuración robusta, automatizada y de bajo mantenimiento.

## Fundamentos Técnicos
La solución implementada se basa en el estándar **IPTV (M3U + XMLTV)**. Jellyfin no requiere plugins propietarios para esta funcionalidad; utiliza un sintonizador virtual que procesa listas de reproducción de canales (`.m3u`) y guías de programación (`.xml`).

## Proceso de Implementación
1. **Selección de Proveedor:** Se utilizó el repositorio **IPTV-ORG**, una fuente legal, gratuita y de alta calidad que recopila canales de televisión y radio de todo el mundo.
2. **Automatización:** Se configuró un cron job para la actualización diaria de los contenidos:
   - Script: `/home/vilber/data/iptv/update_iptv.sh`
   - Descarga directa de listas desde `iptv-org.github.io`.
   - Programación: Ejecución diaria a las 04:00 AM.
3. **Configuración en Jellyfin:**
   - Acceso vía Panel de Control > TV en directo.
   - Uso de **URLs remotas** (recomendado sobre rutas locales para evitar problemas de permisos en entornos aislados/Docker).
   - URLs utilizadas:
     - M3U: `https://iptv-org.github.io/iptv/countries/es.m3u`
     - XMLTV: `https://iptv-org.github.io/iptv/countries/es.xml`

## Implicaciones y Mantenimiento
- **Fiabilidad:** El uso de las URLs oficiales del proyecto garantiza que los cambios en las listas se reflejen sin intervención manual.
- **Seguridad:** No ha sido necesario abrir puertos adicionales ni exponer el sistema a riesgos innecesarios.
- **Escalabilidad:** Se pueden añadir listas de otros países simplemente añadiendo nuevas URLs en la configuración de Jellyfin.

## Conclusión
La integración nativa de IPTV en Jellyfin permite transformar un servidor multimedia básico en un centro de entretenimiento completo, aprovechando la infraestructura existente sin costes de licencias.

---
*Este informe ha sido registrado automáticamente en el Superbrain el 06 de agosto de 2026.*
