---
title: Informe-2026-07-05
date: 2026-07-05
tags: [seguridad, cron, vps, monitorización]
---

# Informe-2026-07-05: Monitorización de Seguridad y Salud

## Contexto

Monitorización activa del VPS frente a accesos no autorizados y salud de servicios críticos.

## Solución Técnica

- **Herramienta**: Skill `security-watchdog` ejecutada mediante `cron`.
- **Alcance**:
  - Verificación de carga (`uptime`) y disco (`df -h`).
  - Detección de intentos de login fallidos en `/var/log/auth.log`.
  - Verificación del estado de `nginx` mediante `systemctl`.
- **Notificación**: Informe diario automatizado a las 07:00.
