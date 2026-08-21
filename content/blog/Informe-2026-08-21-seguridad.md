---
title: "Informe-2026-08-21-seguridad: Seguridad y Salud de la Infraestructura VPS"
date: 2026-08-21
tags: [seguridad, sysadmin, vps, ssh, fail2ban, nginx, uptime, logs]
---

# Informe-2026-08-21-seguridad: Seguridad y Salud de la Infraestructura VPS

Generado automáticamente por el agente autónomo de seguridad de Hermes en la ejecución programada de cron del **2026-08-21**.

---

## 1. Resumen Ejecutivo

El presente informe detalla el estado actual de salud, utilización de recursos y telemetría de seguridad del Servidor Privado Virtual (VPS). A través de auditorías en caliente de los logs de acceso de Systemd y el análisis del espacio libre, se ha constatado un funcionamiento estable de la pila de servicios web, junto con un importante riesgo estructural debido a la ausencia de mecanismos activos de mitigación contra ataques de fuerza bruta en SSH.

- **Estado de Salud General:** Estabilidad nominal. Carga promedio baja y recursos de hardware holgados.
- **Servicios Críticos:** Nginx se encuentra en ejecución operativa normal como proxy inverso principal.
- **Servicio de Seguridad (Fail2ban):** **NO INSTALADO / INACTIVO**. Se reconfirma como un hallazgo crítico que requiere remediación inmediata.
- **Auditoría de Logs (SSH/Sudo):** Se identifica una limitación técnica y de sintaxis en las directivas de privilegios sudo que impide auditar los intentos de accesos fallidos externos tradicionales, registrándose únicamente eventos asociados a la elevación interna de privilegios.

---

## 2. Diagnóstico de Salud de la Infraestructura

### 2.1 Carga del Sistema (Uptime)

La carga del sistema se mantiene dentro de los límites óptimos para la capacidad del hardware, indicando que el VPS opera con una excelente holgura de procesamiento.

- **Uptime actual:** `07:00:46 up 55 days, 14:29,  2 users,  load average: 0.11, 0.05, 0.01`
- **Análisis:** Con una carga media de 0.11 en el último minuto, el procesador se encuentra prácticamente ocioso. No existen indicios de cuellos de botella por hilos en cola, procesos zombie o ataques de denegación de servicio (DoS/DDoS) por saturación de CPU.

### 2.2 Almacenamiento en Disco (df -h)

Se evalúa la ocupación del sistema de archivos con el fin de predecir o prevenir fallos por saturación en la escritura de base de datos, transcripción de contenidos de Jellyfin o registros excesivos de logs.

```text
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.2G  1.2M  1.2G   1% /run
/dev/sda1       193G   41G  153G  22% /
tmpfs           5.9G  4.0K  5.9G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sda16      881M  117M  703M  15% /boot
/dev/sda15      105M  6.2M   99M   6% /boot/efi
tmpfs           1.2G   16K  1.2G   1% /run/user/0
tmpfs           1.2G   20K  1.2G   1% /run/user/1000
```

- **Análisis de Partición Principal (`/`):** La partición raíz dispone de **193 GB totales**, de los cuales se están utilizando **41 GB (22%)**, dejando libres un total de **153 GB**. El incremento de 5 GB respecto al informe de seguridad del 2026-08-19 (donde el uso era de 36 GB / 19%) es consistente con la ingesta y almacenamiento de metadatos o cachés multimedia de Jellyfin.
- **Particiones del Sistema (`/boot`):** El directorio de arranque `/boot` está al 15% de su capacidad total, lo que asegura un margen suficiente para futuras actualizaciones del kernel de Linux.

---

## 3. Estado de los Servicios Críticos

A continuación se detalla la situación operativa de los demonios centrales del servidor VPS:

| Servicio     | Estado de Ejecución    | Descripción / Función                                                            |
| :----------- | :--------------------- | :------------------------------------------------------------------------------- |
| **Nginx**    | `active (running)`     | Servidor Web de Entrada y Reverse Proxy para servicios (Jellyfin/Wiki).          |
| **SSH**      | `active (running)`     | Demonio de Acceso Remoto Seguro (sshd) en el puerto por defecto.                 |
| **Fail2ban** | `Not Found / Inactive` | **[ALERTA CRÍTICA]** El servicio de prevención de intrusiones no está instalado. |

---

## 4. Análisis de Intentos de Acceso SSH y Limitación de Auditoría

### 4.1 Diagnóstico de la Limitación de Sudo

En el entorno VPS actual, el acceso directo de lectura al archivo de logs del sistema de autenticación `/var/log/auth.log` se encuentra restringido a usuarios de los grupos `syslog` y `adm`. Para mitigar esto, se ha provisto una directiva de sudo en `/etc/sudoers` para permitir la auditoría remota sin contraseña:

`    (ALL) NOPASSWD: /usr/bin/grep 'Failed password' /var/log/auth.log`

Sin embargo, debido a la forma rigurosa en que el motor de `sudo` valida los argumentos textuales, la regla exige que la cadena de búsqueda contenga de manera literal comillas simples integradas dentro del propio argumento (ej. `'Failed password'`).

Esto provoca un comportamiento de exclusión mutua:

1. Al ejecutar la instrucción con comillas simples literales en el argumento (`sudo /usr/bin/grep "'Failed password'" /var/log/auth.log`), la ejecución se autoriza sin contraseña, pero el comando `grep` únicamente filtra líneas del log que contienen comillas físicas simples.
2. Como los registros de autenticación SSH nativos del demonio `sshd` registran los fallos con el formato plano `Failed password for...` (sin comillas), dichos registros no son capturados por esta búsqueda literal.
3. El comando únicamente devuelve las alertas registradas en el log interno de `sudo`, las cuales se producen de manera recursiva cada vez que se intenta verificar la directiva de privilegios para el análisis de seguridad:
   `COMMAND=/usr/bin/grep 'Failed password' /var/log/auth.log` (15 ocurrencias totales registradas).

### 4.2 Estado de Conexiones Activas de SSH

Al ejecutar una inspección del estado de los sockets activos mediante `ss -t -a | grep -i ssh`, se ha verificado la siguiente topología de red:

```text
LISTEN     0      4096                   0.0.0.0:ssh                                    0.0.0.0:*
ESTAB      0      0               144.91.108.254:ssh                              103.200.20.41:59728
LISTEN     0      4096                      [::]:ssh                                       [::]:*
```

Se identifica un socket establecido (`ESTAB`) hacia el puerto SSH desde la IP externa **103.200.20.41**. Se recomienda vigilar la persistencia de esta sesión y cerciorarse de que corresponda a conexiones legítimas de administración.

---

## 5. Hallazgos Críticos y Recomendaciones de Seguridad

### 5.1 Hallazgos Identificados

1.  **Inexistencia de Fail2ban (Peligro Crítico):** No contar con un demonio de detección proactiva de intrusos expone al servidor a que atacantes externos realicen ataques de diccionario ininterrumpidos y masivos, consumiendo ancho de banda, CPU e incrementando exponencialmente el riesgo de compromiso de credenciales.
2.  **Exposición Continua del Puerto SSH (`22`):** El uso del puerto estándar de SSH atrae escaneos automatizados constantes provenientes de botnets e intermediarios de la red.
3.  **Punto Ciego en la Auditoría de Logs:** La sintaxis actual de la directiva de sudo para `/usr/bin/grep` genera un punto ciego que impide al agente monitorear los intentos reales de fuerza bruta de SSH sobre `/var/log/auth.log`.

### 5.2 Plan de Acción y Mitigación Recomendado

Se propone una hoja de ruta técnica clara para blindar la seguridad perimetral del VPS:

1.  **Instalación y Activación Inmediata de Fail2ban:**
    Proceder a la instalación del paquete `fail2ban` para que administre dinámicamente las reglas del cortafuegos local (iptables/ufw):
    ```bash
    sudo apt update && sudo apt install fail2ban -y
    sudo systemctl enable --now fail2ban
    ```
2.  **Hardening del Demonio SSH (Edición de `/etc/ssh/sshd_config`):**
    Restringir la superficie de ataque forzando las mejores prácticas de autenticación criptográfica:
    ```text
    PermitRootLogin no
    PasswordAuthentication no
    PubkeyAuthentication yes
    ```
    _Nota:_ Reiniciar el servicio mediante `sudo systemctl restart ssh` únicamente tras cerciorarse de que existen llaves SSH públicas correctamente configuradas en el archivo `~/.ssh/authorized_keys` del usuario legítimo.
3.  **Modificación del Puerto Estándar de SSH:**
    Cambiar el puerto de escucha en `/etc/ssh/sshd_config` (o la unidad de socket systemd correspondiente) a un puerto alto aleatorio (ej. superior al `20000`). Esto detendrá de inmediato el 99.9% del tráfico espurio generado por scripts básicos de escaneo.
4.  **Revisión de la Directiva Sudoers:**
    Modificar la línea de privilegios para permitir una auditoría de logs sin restricciones de comillas. Se sugiere habilitar un alias de comando o reescribir la regla para dar cobertura genérica al análisis sobre el archivo `/var/log/auth.log`.

---

## 6. Conclusión Técnico-Operativa

El estado físico del VPS es insuperable, operando con una holgura de recursos excelente (80%+ de disco libre y carga de CPU prácticamente nula). Nginx proporciona estabilidad perfecta al ecosistema web. No obstante, a nivel de seguridad, el servidor carece de una barrera de contención dinámica frente a ataques automatizados (Fail2ban). La implementación de las mitigaciones descritas en este documento es altamente prioritaria para garantizar la integridad continua del entorno de desarrollo, el servidor de Jellyfin y el wiki Superbrain.

---
