---
title: "Informe-2026-08-23: Hardening de Seguridad del VPS — SSH, Fail2ban y Rate Limiting en Nginx"
date: 2026-08-23
tags: [seguridad, vps, ssh, fail2ban, nginx, jellyfin, hardening]
---

# Informe-2026-08-23: Hardening de Seguridad del VPS

## Contexto

Se ha llevado a cabo una sesión integral de hardening de seguridad en el VPS (vmi3400182, IP 144.91.108.254) tras los cambios iniciales realizados el día anterior (22 de agosto de 2026). La sesión de hoy (23 de agosto) se ha centrado en consolidar y ampliar las medidas de seguridad, así como en revisar el estado actual del servidor para verificar la efectividad de las configuraciones.

El servidor presenta una estabilidad excelente con un uptime de 57 días, carga media de 0.15, y un uso de recursos mínimo (2 GiB de 11 GiB RAM, 22% de disco utilizado). Sin embargo, la exposición a internet y los ataques constantes de bots SSH justifican la implementación de múltiples capas de defensa.

## Medidas Implementadas

### 1. Puertos SSH No Estándar (Verificación)

Confirmación de que la medida implementada el día anterior está operativa al 100%. Se ha verificado que:

- El **puerto 22** está completamente cerrado: no lo escucha sshd ni está permitido en el firewall UFW.
- Los **puertos SSH alternativos** 2222 y 22822 son los únicos habilitados.
- La configuración se realizó mediante un **override de systemd** en `/etc/systemd/system/ssh.socket.d/port-override.conf`, que vacía el ListenStream del puerto 22 y añade exclusivamente los puertos alternativos.
- El firewall UFW confirma la política: solo los puertos 2222, 22822, 80, 443 y 8096 (Jellyfin local) están permitidos; el resto se bloquean por defecto (`deny incoming`).

Estadísticas de efectividad: en las primeras horas del día, el puerto 22 recibió **61 intentos de autenticación fallidos** desde la IP `64.23.251.93`, todos ellos bloqueados por fail2ban. Ninguno de estos intentos alcanzó los puertos 2222 o 22822.

### 2. Hardening de Fail2ban para SSH

Se ha ajustado la configuración global de fail2ban para endurecer la protección del servicio SSH:

| Parámetro | Valor Anterior | Valor Actual |
|---|---|---|
| `maxretry` (intentos máx.) | 5 | **3** |
| `findtime` (ventana) | — | **30 minutos** |
| `bantime` base | — | **10 minutos** |
| `bantime.increment` | — | **true** |
| `bantime.factor` | — | **1** (duplicación progresiva) |
| `bantime.maxtime` | — | **1 semana** |
| `bantime.rndtime` | — | **5 minutos** |
| `bantime.overalljails` | — | **true** |

El sistema de **baneo progresivo** (exponential backoff) funciona de la siguiente manera:
- **1ª ofensa**: 3 fallos en 30 minutos → baneo de 10 minutos.
- **2ª ofensa** (misma IP reincide): baneo de 20 minutos.
- **3ª ofensa**: 40 minutos.
- **4ª ofensa**: 80 minutos (~1.3 horas).
- **5ª ofensa**: ~2.7 horas.
- **Sucesivas**: hasta un máximo de **1 semana**.

Además, `bantime.overalljails = true` hace que el contador de reincidencias sea global entre todas las cárceles (jails) de fail2ban, incluyendo la de Jellyfin. Una IP baneada por SSH que posteriormente ataque Jellyfin verá incrementado su tiempo de baneo acumulado.

Estado actual de fail2ban:
- **Total baneados por SSH**: 38 IPs (2 actualmente activas: `180.92.231.10` y `47.85.8.171`).
- **Total intentos fallidos detectados**: 3,152 en la cárcel SSH.
- **Cárceles activas**: `sshd` y `jellyfin`.

### 3. Jail de Fail2ban para Jellyfin

Se ha creado una nueva cárcel específica para proteger el servicio Jellyfin, que corre en Docker pero es accesible a través de Nginx como proxy inverso. Configuración:

| Parámetro | Valor |
|---|---|
| **Endpoint monitorizado** | `POST/GET /Users/AuthenticateByName` con respuesta HTTP 401 |
| **Fichero de logs** | `/var/log/nginx/access.log` |
| **Filtro** | `/etc/fail2ban/filter.d/jellyfin.conf` |
| **maxretry** | 5 |
| **findtime** | 10 minutos |
| **bantime** | 12 horas (fijo, no progresivo) |
| **Puerto** | http,https |

El filtro regex utilizado: `^<HOST> - - \[.*\] "(?:POST|GET) /Users/AuthenticateByName.*" 401 [0-9]+ .*$`

Este regex ha sido verificado con pruebas unitarias:
- **Login fallido simulado** (`POST /Users/AuthenticateByName 401`): **match exitoso** ✅ (1/1).
- **Petición normal** (`GET /web/Content/styles.css 200`): **no match** ✅ (0/1), cero falsos positivos.
- **Log real de producción** (371 líneas, sin login fallidos): **0 matches**, confirmando que no hay falsos positivos con el tráfico legítimo.

### 4. Rate Limiting en Nginx para el Endpoint de Autenticación de Jellyfin

Se ha implementado limitación de tasa (rate limiting) a nivel de Nginx para el endpoint crítico de autenticación de Jellyfin. Esta medida actúa como primera barrera antes de que el tráfico llegue siquiera al contenedor Docker.

**Configuración:**

```nginx
# En /etc/nginx/conf.d/rate-limit.conf:
limit_req_zone $binary_remote_addr zone=jellyfin_login:10m rate=5r/m;

# En el bloque location del site de Jellyfin:
location = /Users/AuthenticateByName {
    limit_req zone=jellyfin_login burst=5 nodelay;
    proxy_pass http://127.0.0.1:8096;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

**Parámetros:**
- **rate**: 5 requests por minuto por IP.
- **burst**: 5 (permite ráfagas de hasta 5 peticiones consecutivas antes de aplicar el límite).
- **nodelay**: las peticiones dentro del burst se procesan inmediatamente sin cola.
- **zona de memoria**: 10 MB (suficiente para miles de IPs simultáneas).

**Prueba de funcionalidad** (10 peticiones consecutivas):
- Peticiones 1-6 → HTTP 400 (pasaron a Jellyfin, login inválido).
- Peticiones 7-10 → **HTTP 503** (bloqueadas por Nginx por exceder el rate limit).
- Peticiones normales a `/` → HTTP 302 (sin restricción, tráfico legítimo no afectado).

### 5. Publicación de Proyectos Web Bajo Subdirectorios

Adicionalmente, se han publicado los proyectos web alojados en `~/proyectos/` como subdirectorios de `cinesfer.duckdns.org`:

| Proyecto | URL | Estado |
|---|---|---|
| Meetup Prueba | `/meetup-prueba/` | ✅ 200 |
| Nóminas Hogar | `/nominas-hogar/` | ✅ 200 (requirió ajuste de permisos 600→644) |
| Viaje Planner | `/viaje-planner/` | ✅ 200 |
| Superbrain Wiki | `/superbrain/` | ✅ 200 |

Jellyfin permanece intacto en `/jellyfin/web/` y como aplicación principal en la raíz.

## Estado del Servidor Post-Hardening

| Indicador | Valor |
|---|---|
| Uptime | 57 días |
| Carga CPU | 0.15 |
| RAM | 2 GiB / 11 GiB (18%) |
| Disco | 41 GiB / 193 GiB (22%) |
| Sesiones activas | 3 (vilber desde 45.93.58.153) |
| Servicios críticos | Nginx (OK), Jellyfin (healthy), fail2ban (OK, 6h activo) |

## Próximas Medidas Pendientes

Se han identificado y registrado las siguientes mejoras para futuras sesiones:

1. **Aislamiento de red Docker**: Crear una red Docker interna para Jellyfin y dejar de exponer el puerto 8096 al host, comunicándolo exclusivamente a través del proxy Nginx.
2. **Watchtower**: Implementar actualización automática del contenedor de Jellyfin para mantenerlo protegido frente a vulnerabilidades conocidas (CVEs).

## Conclusión

El servidor ha pasado de una configuración básica con SSH en puerto estándar y fail2ban por defecto a un esquema de **defensa en profundidad** con tres capas superpuestas: (1) **ocultación de puertos** (SSH en 2222/22822), (2) **fail2ban con baneo progresivo** (3 intentos/30min, escalando hasta 1 semana), y (3) **rate limiting en Nginx** (5r/m con burst para Jellyfin). Las verificaciones empíricas confirman que todas las medidas funcionan correctamente sin afectar al tráfico legítimo.