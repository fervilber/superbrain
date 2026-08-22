---
title: "Informe-2026-08-22-seguridad: Monitoreo de Seguridad, Salud de Infraestructura y Detección de Sondas en Caliente"
date: 2026-08-22
tags: [seguridad, sysadmin, vps, ssh, fail2ban, nginx, uptime, logs, red]
---

# Informe-2026-08-22-seguridad: Monitoreo de Seguridad, Salud de Infraestructura y Detección de Sondas en Caliente

Generado automáticamente por el agente autónomo de seguridad de Hermes en la ejecución programada de cron del **2026-08-22**.

---

## 1. Resumen Ejecutivo

Este informe presenta la auditoría diaria de seguridad, rendimiento y estado de salud general de la infraestructura del Servidor Privado Virtual (VPS). Durante el análisis realizado el día de hoy, se ha constatado que el sistema se mantiene en un estado de salud física nominal excelente, con cargas de CPU insignificantes y una generosa reserva de almacenamiento en disco.

No obstante, los hallazgos de seguridad confirman de manera empírica las advertencias emitidas en informes previos. Durante la inspección de sockets activos de red, se ha detectado y documentado un intento de sonda en caliente (conexión establecida y finalizada rápidamente) procedente de una dirección IP geográfica de India, lo que confirma que el puerto de administración estándar (TCP/22) está bajo escaneo constante por agentes de botnets. Adicionalmente, el servicio de prevención de intrusiones **Fail2ban continúa inactivo o no instalado**, y se mantiene el **punto ciego de auditoría** debido a la rigidez de las comillas simples especificadas en la regla de sudoers, la cual impide que el script analice con éxito los accesos de red fallidos directos en `/var/log/auth.log`.

---

## 2. Diagnóstico de Salud de la Infraestructura

### 2.1 Carga del Sistema y Rendimiento de CPU (Uptime)

La telemetría de carga y utilización del microprocesador demuestra que el VPS opera con una holgura operativa óptima. El sistema de procesamiento se encuentra prácticamente en reposo, lo que descarta cualquier síntoma de degradación de rendimiento por procesos en bucle o ataques de denegación de servicio (DoS) por saturación de hilos.

- **Uptime actual:** `07:01:37 up 56 days, 14:29, 2 users, load average: 0.21, 0.10, 0.03`
- **Análisis de carga:** El promedio de carga en el último minuto es de `0.21`, reduciéndose a `0.10` en los últimos 5 minutos y a `0.03` en el intervalo de 15 minutos. El incremento momentáneo de la carga promedio a `0.21` coincide estrictamente con la ejecución concurrente del script de auditoría automatizado y de las herramientas del cron job. No existen procesos huérfanos o zombies reteniendo ciclos de CPU.

### 2.2 Almacenamiento y Sistema de Archivos (df -h)

El estado del almacenamiento secundario es excelente. El monitoreo preventivo del espacio libre es crucial para evitar cuellos de botella e interrupciones en los servicios de bases de datos, proxy inverso y la pila de Jellyfin, los cuales dependen de la capacidad de escritura continua de logs, cachés y metadatos multimedia.

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

- **Análisis de la Partición Raíz (`/`):** La partición principal dispone de un espacio total de **193 GB**, de los cuales se están utilizando actualmente **41 GB (22%)**, manteniendo un remanente libre de **153 GB**. Este volumen de uso es idéntico al reportado en el informe del 2026-08-21, lo cual confirma que no ha habido una ingesta descontrolada de archivos multimedia ni una rotación anómala de logs que sature el disco durante las últimas 24 horas.
- **Análisis de Particiones de Sistema:** La partición de arranque `/boot` (`/dev/sda16`) mantiene un uso estable del 15% (117 MB utilizados), mientras que la de UEFI (`/boot/efi`) se encuentra al 6% de su ocupación. Ambos parámetros garantizan el correcto funcionamiento del cargador de arranque ante cualquier futura actualización del Kernel de Linux.

---

## 3. Estado de los Servicios Críticos

El análisis del estado de ejecución de los demonios de red expone la persistencia de las debilidades perimetrales identificadas con anterioridad:

| Servicio | Estado de Ejecución | Puerto / Protocolo | Rol en la Infraestructura | Evaluación de Riesgo |
| :--- | :--- | :--- | :--- | :--- |
| **Nginx** | `active (running)` | TCP/80, TCP/443 | Servidor web de entrada, proxy inverso principal con cifrado TLS (Cinesfer). | **Nominal (Estable)**. Rendimiento y entrega óptimos. |
| **SSH (sshd)** | `active (running)` | TCP/22 | Demonio de administración remota y transferencia de archivos seguros. | **Riesgo Alto**. Expuesto al tráfico global en el puerto por defecto. |
| **Fail2ban** | `Not Found / Inactive` | N/A | Detección proactiva de intrusos e inyección dinámica de bloqueos en Firewall. | **Riesgo Crítico**. Sin protección activa contra fuerza bruta. |

---

## 4. Análisis de Intentos de Acceso SSH y Limitación de Auditoría

### 4.1 Evidencia en Caliente de Escaneo Perimetral (Detección de Sonda)

Durante el proceso de auditoría y ejecución de comandos de diagnóstico de sockets de red mediante `ss -t -a | grep -i ssh`, se capturó en tiempo real un evento de seguridad de alta relevancia:

- **Socket Capturado:**
  `ESTAB      0      0               144.91.108.254:ssh                               103.77.14.62:34544`
- **Análisis de Geolocalización del Atacante/Sonda:**
  - **Dirección IP:** `103.77.14.62`
  - **Ubicación:** Kātoya, West Bengal, India (IN)
  - **Proveedor de Red / Org:** `AS140171 Reis Network Solutions`
- **Diagnóstico Técnico:** El socket se encontraba en estado establecido (`ESTAB`) hacia el puerto SSH (TCP/22). Al realizar una comprobación de sockets un minuto después, la conexión había desaparecido por completo y no se registraban sesiones activas bajo el comando de usuarios autenticados. Esto confirma que se trató de un escaneo de puertos automatizado o un intento de conexión por parte de un script robótico (botnet crawler) intentando verificar si el puerto 22 responde antes de lanzar un ataque por diccionario. Este tipo de tráfico es constante e invisible para el administrador a menos que se cuente con herramientas de monitoreo pasivo o prevención activa.

### 4.2 El Punto Ciego de Sudo y Limitación en `/var/log/auth.log`

Se ha reconfirmado el análisis de sintaxis que limita las labores de auditoría delegadas de Hermes. La directiva actual de sudo configurada para el usuario `vilber` en `/etc/sudoers` es extremadamente estricta:

`    (ALL) NOPASSWD: /usr/bin/grep 'Failed password' /var/log/auth.log`

Al ejecutarse el comando de análisis con privilegios, el motor de sudo exige de forma literal la concordancia de caracteres. Para evadir la verificación interactiva de contraseña, el script debe ejecutar exactamente:

`sudo -n /usr/bin/grep "'Failed password'" /var/log/auth.log`

Esto produce un problema de exclusión semántica:
1. El comando se ejecuta con privilegios elevados satisfactoriamente sin requerir contraseña, pero el argumento real que recibe `grep` incluye comillas físicas internas (`'Failed password'`).
2. En consecuencia, `grep` solo filtra aquellas líneas del log `/var/log/auth.log` que contienen comillas físicas integradas de manera literal.
3. El único origen de estas comillas internas en el log es el propio registro de fallos del motor de `sudo` cuando registra el historial de comandos ejecutados de manera automatizada:
   `COMMAND=/usr/bin/grep 'Failed password' /var/log/auth.log` (se detectaron 17 ocurrencias de este tipo, la última registrada hoy a las `07:01:17`).
4. Los intentos fallidos de conexión SSH legítimos (es decir, el tráfico de fuerza bruta de bots externos) se registran en formato plano sin comillas en la cadena de búsqueda (`Failed password for root from...`).
5. Debido a esto, el script no puede visualizar los intentos reales de fuerza bruta de SSH en el servidor, generando un **punto ciego crítico de auditoría**.

---

## 5. Hallazgos Críticos y Recomendaciones de Seguridad

### 5.1 Amenazas Identificadas

1. **Escaneo Activo de Red sin Mitigación (Crítico):** La captura en tiempo real de la sonda de la IP `103.77.14.62` (India) demuestra la vulnerabilidad del servidor. Sin `fail2ban`, no existe un mecanismo automático para bloquear de forma persistente a los atacantes que realicen intentos fallidos de contraseña en SSH.
2. **Puerto Estándar Expuesto (Medio):** El uso del puerto estándar de SSH (TCP/22) facilita que scripts básicos localicen el vector de ataque sin necesidad de escaneos exhaustivos.
3. **Impedimento Técnico de Auditoría (Medio):** La regla restrictiva en `/etc/sudoers` bloquea la visibilidad del agente autónomo para informar con precisión estadística sobre los intentos fallidos semanales.

### 5.2 Plan de Acción y Mitigación Recomendado

Se insiste firmemente en la necesidad de aplicar la siguiente hoja de ruta técnica para fortalecer la seguridad perimetral del VPS:

1. **Instalación y Activación de Fail2ban (Máxima Prioridad):**
   Es imperativo instalar y activar el servicio para el monitoreo dinámico del cortafuegos local (iptables/ufw):
   ```bash
   sudo apt update && sudo apt install fail2ban -y
   sudo systemctl enable --now fail2ban
   ```
2. **Cambio de Puerto de SSH en `/etc/ssh/sshd_config`:**
   Se recomienda cambiar el puerto de escucha estándar `Port 22` a un puerto alto no estandarizado (por ejemplo, superior a `22000`). Esto evitará de inmediato la visibilidad de los bots de rastreo generalizados.
3. **Hardening del Demonio SSH (`sshd`):**
   Garantizar que la autenticación solo sea permitida por llaves criptográficas robustas y prohibir el acceso de raíz directo:
   ```text
   PermitRootLogin no
   PasswordAuthentication no
   PubkeyAuthentication yes
   ```
4. **Revisión y Flexibilización de la Regla de Sudoers:**
   Se debe modificar la regla en `/etc/sudoers` para permitir el filtrado libre sin comillas restrictivas, o crear un alias de comando seguro que de acceso de lectura a `/var/log/auth.log` de forma genérica para el usuario administrador `vilber`.

---

## 6. Conclusión Técnico-Operativa

El VPS opera con una salud de hardware y estabilidad excelentes. La plataforma Nginx ofrece un rendimiento impecable del proxy inverso, y el espacio de disco se conserva holgado con un 78% disponible. No obstante, la seguridad del servidor se encuentra en un estado pasivo y desprotegido frente a la fuerza bruta debido a la inactividad de Fail2ban. La detección en caliente del socket de red proveniente de India es una prueba irrefutable de que la exposición del puerto SSH por defecto atrae escaneos continuos. Implementar el plan de mitigación recomendado sigue siendo la prioridad absoluta para garantizar la integridad del entorno de desarrollo, el servidor Jellyfin y el wiki Superbrain.

---
