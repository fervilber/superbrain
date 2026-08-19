---
title: "Informe-2026-08-19-seguridad: Seguridad y Salud de la Infraestructura VPS"
date: 2026-08-19
tags: [seguridad, sysadmin, vps, ssh, fail2ban, nginx, uptime, logs]
---

# Informe-2026-08-19-seguridad: Seguridad y Salud de la Infraestructura VPS

Generado automáticamente por el agente autónomo de seguridad de Hermes en la ejecución programada de cron del **2026-08-19**.

---

## 1. Resumen Ejecutivo

El presente informe detalla el estado actual de salud, utilización de recursos y telemetría de seguridad del Servidor Privado Virtual (VPS). A través de auditorías en caliente de los logs de acceso de Systemd y el análisis del espacio libre, se ha constatado un funcionamiento estable de la pila de servicios web, junto con una **actividad de fuerza bruta persistente y altamente coordinada** dirigida hacia el puerto por defecto de SSH (`22`).

- **Estado de Salud General:** Estabilidad nominal. Carga promedio muy baja.
- **Servicios Críticos:** Nginx se encuentra en ejecución operativa normal.
- **Servicio de Seguridad (Fail2ban):** **INACTIVO/DESACTIVADO**. Se identifica como un hallazgo crítico que requiere remediación inmediata.
- **Volumen de Intentos Fallidos SSH:** Se registraron **5058 intentos fallidos** de acceso en el intervalo analizado.

---

## 2. Diagnóstico de Salud de la Infraestructura

### 2.1 Carga del Sistema (Uptime)

La carga del sistema se mantiene dentro de los límites óptimos para la capacidad del hardware (1 vCPU / multiprocesamiento libre).

- **Uptime actual:** `07:04:32 up 53 days, 14:32,  2 users,  load average: 0.15, 0.12, 0.04`
- **Análisis:** Los promedios de carga (load average) indican que el procesador está prácticamente inactivo la mayor parte del tiempo, lo que descarta cuellos de botella por procesamiento de servicios concurrentes o ataques de denegación de servicio (DoS) por volumen de procesamiento.

### 2.2 Almacenamiento en Disco (df -h)

Se evalúa el espacio disponible en las particiones montadas para prevenir bloqueos por saturación de logs o cachés de Jellyfin.

```text
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.2G  1.2M  1.2G   1% /run
/dev/sda1       193G   36G  158G  19% /
tmpfs           5.9G  4.0K  5.9G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sda16      881M  117M  703M  15% /boot
/dev/sda15      105M  6.2M   99M   6% /boot/efi
tmpfs           1.2G   16K  1.2G   1% /run/user/0
tmpfs           1.2G   20K  1.2G   1% /run/user/1000
```

- **Partición Principal (`/`):** El sistema de archivos raíz de 193 GB tiene **36 GB utilizados (19%)** y **158 GB disponibles**. El margen de almacenamiento es sumamente holgado.
- **Partición de Boot (`/boot`):** Tiene 15% de uso, lo cual es normal para los kernels instalados.

---

## 3. Estado de los Servicios Críticos

| Servicio     | Estado de Ejecución | Descripción / Función                                                   |
| :----------- | :------------------ | :---------------------------------------------------------------------- |
| **Nginx**    | `active (running)`  | Servidor Web de Entrada y Reverse Proxy para servicios (Jellyfin/Wiki). |
| **SSH**      | `active (running)`  | Demonio de Acceso Remoto Seguro (sshd).                                 |
| **Fail2ban** | `inactive`          | **[ALERTA COLD]** Servicio de prevención de intrusiones.                |

---

## 4. Análisis Profundo de Intentos de Acceso SSH

Se analizaron las últimas **20,000 líneas de logs de SSH** del diario del sistema, identificando un volumen severo de accesos no autorizados mediante ataques de diccionario y fuerza bruta asíncronos.

- **Intervalo temporal analizado:** desde Aug 18 11:01:40 hasta Aug 19 07:04:28
- **Total de conexiones rechazadas:** `5058` intentos con credenciales erróneas.

### 4.1 Análisis de Direcciones IP Ofensoras (Top 10)

A continuación se detallan las direcciones IP de origen que concentran el mayor volumen de denegaciones de autenticación, enriquecidas con datos geográficos y de propiedad de red (ISP/Autonomous System).

| Dirección IP      | Intentos | % del Total | Ubicación y Proveedor (AS)                                    |
| :---------------- | :------- | :---------- | :------------------------------------------------------------ |
| `158.220.93.99`   | 768      | 15.18%      | Portsmouth, GB (AS51167 Contabo GmbH)                         |
| `93.127.184.34`   | 439      | 8.68%       | Frankfurt am Main, DE (AS136897 Enjoyvc Cloud Group Limited.) |
| `79.72.3.119`     | 430      | 8.50%       | Jeddah, SA (AS31898 Oracle Corporation)                       |
| `15.235.32.243`   | 384      | 7.59%       | Montréal, CA (AS16276 OVH SAS)                                |
| `91.92.40.46`     | 262      | 5.18%       | Amsterdam, NL (AS197170 TechTies Inc.)                        |
| `77.239.124.246`  | 237      | 4.69%       | N/A (Fuera del top 5)                                         |
| `155.117.120.109` | 174      | 3.44%       | N/A (Fuera del top 5)                                         |
| `195.178.110.218` | 152      | 3.01%       | N/A (Fuera del top 5)                                         |
| `45.148.10.152`   | 130      | 2.57%       | N/A (Fuera del top 5)                                         |
| `45.148.10.141`   | 120      | 2.37%       | N/A (Fuera del top 5)                                         |

### 4.2 Análisis de Nombres de Usuario Atacados (Top 10)

Se evalúa el patrón de diccionarios utilizados por los atacantes para identificar si están dirigidos o si son genéricos para servidores expuestos en la red.

| Usuario Solicitado | Intentos | % del Total |
| :----------------- | :------- | :---------- |
| `root`             | 2664     | 52.67%      |
| `admin`            | 238      | 4.71%       |
| `ubuntu`           | 105      | 2.08%       |
| `user`             | 65       | 1.29%       |
| `test`             | 55       | 1.09%       |
| `oracle`           | 30       | 0.59%       |
| `deploy`           | 29       | 0.57%       |
| `debian`           | 28       | 0.55%       |
| `administrator`    | 28       | 0.55%       |
| `postgres`         | 25       | 0.49%       |

**Interpretación de Datos:**

1.  El usuario `root` acapara el **52.67%** de los intentos de intrusión. Esto demuestra que los bots atacantes asumen por defecto la disponibilidad del superusuario para iniciar sesión.
2.  La presencia de usuarios genéricos como `admin`, `ubuntu`, `user`, `oracle`, y `debian` confirma el uso de scripts automatizados de escaneo que barren el rango global de direcciones IPv4 buscando configuraciones por defecto.

---

## 5. Hallazgos Críticos y Recomendaciones de Seguridad

### 5.1 Hallazgos Identificados

1.  **Ausencia de Bloqueo Activo (Fail2ban inactivo):** El servicio `fail2ban` se encuentra en estado `inactive`. Esto significa que los atacantes pueden realizar miles de intentos continuos (como la IP `158.220.93.99` que realizó 768 intentos) sin sufrir ninguna penalización técnica o restricción temporal.
2.  **Exposición Directa del Puerto SSH:** El puerto `22` por defecto es ampliamente escaneado, facilitando el descubrimiento del servidor por parte de redes de bots (botnets) mundiales ubicadas en nubes de servidores (Contabo, Oracle, OVH).

### 5.2 Plan de Mitigación Inmediato Recomendado

Para elevar el perfil de seguridad del servidor, se suger aplicar la siguiente guía de endurecimiento (hardening) del sistema:

1.  **Habilitar y Configurar Fail2ban:**
    Instalar y activar `fail2ban` para crear "jails" automáticos en iptables tras 3-5 intentos fallidos:
    ```bash
    sudo apt install fail2ban -y
    sudo systemctl enable --now fail2ban
    ```
2.  **Deshabilitar el Acceso de Root y Autenticación por Contraseña:**
    Editar `/etc/ssh/sshd_config` para forzar únicamente el uso de claves SSH públicas y prohibir el login de root:
    ```text
    PermitRootLogin no
    PasswordAuthentication no
    PubkeyAuthentication yes
    ```
    Luego reiniciar el servicio: `sudo systemctl restart ssh`.
3.  **Cambiar el Puerto de SSH:**
    Modificar el puerto por defecto `22` a un puerto aleatorio alto (ej. `2222` o similar) para eliminar el 99% de los escaneos automatizados de bots sencillos.

---

## 6. Conclusión Técnico-Operativa

El VPS opera con una salud de hardware y recursos excelente (80%+ de disco libre y <10% de CPU de carga media). No obstante, la seguridad del canal de administración SSH está comprometida estructuralmente por la falta de un demonio de baneo automático como Fail2ban. Es de extrema urgencia aplicar el endurecimiento de SSH y activar Fail2ban para evitar que un ataque de fuerza bruta exitoso ponga en peligro los servicios alojados (como Jellyfin y el wiki Superbrain).

---
