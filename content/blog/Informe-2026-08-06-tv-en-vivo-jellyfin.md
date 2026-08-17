---
title: "Informe Técnico: Implementación de TV en vivo en Jellyfin con IPTV-ORG"
date: 2026-08-06
tags: [jellyfin, iptv, vps, multimedia]
---

# Informe Técnico: Implementación de TV en vivo en Jellyfin

## Contexto

El objetivo era integrar una solución de televisión y radio en vivo dentro de la instancia de Jellyfin alojada en el VPS, buscando una configuración robusta, automatizada y de bajo mantenimiento.

## Fundamentos Técnicos

La solución implementada se basa en el estándar **IPTV (M3U + XMLTV)**. Jellyfin utiliza un sintonizador virtual que procesa listas de reproducción de canales (`.m3u`) y guías de programación (`.xml`).

## Proceso de Implementación paso a paso

### 1. Obtención de fuentes (IPTV-ORG)

Se recomienda utilizar el repositorio [IPTV-ORG](https://github.com/iptv-org/iptv) debido a su carácter legal, gratuito y actualización constante.

### 2. Configuración en Jellyfin (Uso de URLs remotas)

Es preferible usar las URLs directas del repositorio en lugar de archivos locales para evitar problemas de permisos de sistema y garantizar la actualización automática.

**Pasos en el Panel de Control:**

1. Acceder al Panel de Control de Jellyfin (http://<IP>:8096).
2. Ir a **TV en directo** (Live TV).
3. **Configurar Sintonizador (Tuner):**
   - Haz clic en **Añadir**.
   - Selecciona **M3U Tuner**.
   - En **Archivo o URL**, pega la URL directa:
     - España: `https://iptv-org.github.io/iptv/countries/es.m3u`
     - Reino Unido: `https://iptv-org.github.io/iptv/countries/gb.m3u`
4. **Configurar Guía (Program Guide):**
   - En la misma pestaña de TV en directo, ir a **Fuentes de la guía** (Program Guide).
   - Haz clic en **Añadir**.
   - Selecciona **XMLTV**.
   - En **Archivo o URL**, pega la URL correspondiente:
     - España: `https://iptv-org.github.io/iptv/countries/es.xml`
     - Reino Unido: `https://iptv-org.github.io/iptv/countries/gb.xml`

### 3. Ajustes finales

- Asegurarse de activar la opción **"Actualizar guía automáticamente"**.
- Jellyfin refrescará los datos periódicamente. Si los cambios no se ven reflejados, puedes usar el botón de **"Refrescar guía"** manualmente desde el panel de control.

## Conclusión

La integración mediante URLs remotas elimina la necesidad de mantenimiento local (scripts, cron jobs, permisos), delegando la actualización de los canales a la comunidad que mantiene el repositorio de origen.

---

_Este informe ha sido actualizado el 06 de agosto de 2026 tras optimizar la configuración para uso de URLs remotas._
