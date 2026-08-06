---
title: Informe-2026-07-04
date: 2026-07-04
tags: [viajes, nginx, vps, web-planner]
---

# Informe-2026-07-04: Despliegue de Planificador de Viajes

## Contexto

Necesidad de una herramienta sencilla para organizar los itinerarios de verano (Santander, julio 2026) sin depender de backends complejos.

## Solución Técnica

- **Frontend**: Aplicación web estática (HTML/CSS/JS) utilizando `localStorage` para persistencia local.
- **Servidor**: Despliegue en Nginx sobre VPS.
- **Configuración**: Se configuró `/var/www/html/` para servir los archivos estáticos.

## Evolución

El proyecto nació como una herramienta de uso local y se escaló a servicio web accesible por IP.
