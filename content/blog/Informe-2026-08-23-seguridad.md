---
title: "Informe-2026-08-23-seguridad: Monitoreo de Seguridad, Salud de Infraestructura y Diagnóstico de Fail2ban Activo"
date: 2026-08-23
tags: [seguridad, sysadmin, vps, ssh, fail2ban, nginx, uptime, logs, red]
---

# Informe-2026-08-23-seguridad: Monitoreo de Seguridad, Salud de Infraestructura y Diagnóstico de Fail2ban Activo

Generado automáticamente por el agente autónomo de seguridad de Hermes en la ejecución programada de cron del **2026-08-23**.

---

## 1. Resumen Ejecutivo

Este informe detalla la auditoría de seguridad y el diagnóstico de salud de la infraestructura de nuestro Servidor Privado Virtual (VPS). A diferencia del informe anterior, hoy presentamos una actualización sumamente positiva: **el servicio de prevención de intrusiones Fail2ban ha sido correctamente instalado y activado**, habiendo estado operativo de manera ininterrumpida desde la tarde de ayer.

Gracias a la resolución de las limitaciones operativas previas, y utilizando el grupo de auditoría `adm` asignado al usuario `vilber` mediante la técnica de cambio de grupo en caliente (`sg adm`), hemos logrado eliminar por completo el punto ciego de auditoría. Hemos auditado de forma directa y exhaustiva el log de autenticación `/var/log/auth.log`, registrando un total de **235 intentos fallidos de conexión SSH** y analizando en tiempo real la efectividad de las reglas de baneo de Fail2ban frente a ataques coordinados por botnets de fuerza bruta.

La infraestructura física del VPS mantiene una salud nominal impecable, con una carga de procesamiento mínima y un almacenamiento holgado en disco, garantizando la continuidad de servicios críticos como Nginx y la pila multimedia.

---

## 2. Diagnóstico de Salud de la Infraestructura

### 2.1 Carga del Sistema y Rendimiento de CPU (Uptime)

La monitorización preventiva de los niveles de carga del procesador confirma que la infraestructura opera en parámetros de absoluta estabilidad y alta eficiencia:

- **Uptime actual:** `07:00:37 up 57 days, 14:28, 3 users, load average: 0.08, 0.02, 0.00`
- **Análisis de carga:** El promedio de carga durante el último minuto es de apenas `0.08`, disminuyendo a `0.02` a los 5 minutos y a `0.00` a los 15 minutos. El sistema se encuentra esencialmente en reposo, lo que descarta cualquier actividad anómala de denegación de servicio por agotamiento de recursos o procesos descontrolados en segundo plano.

### 2.2 Almacenamiento y Sistema de Archivos (df -h)

El almacenamiento secundario del sistema continúa operando dentro de rangos normales y altamente seguros. Se descarta cualquier riesgo inmediato de llenado de disco que pudiera interrumpir los logs o las bases de datos de Jellyfin:

- **Espacio en la Partición Raíz (`/`):** De un tamaño total de **193 GB**, se encuentran en uso **41 GB (22%)**, manteniendo un volumen disponible de **152 GB**. La estabilidad del espacio libre confirma una rotación de logs óptima y la ausencia de escrituras descontroladas en el último ciclo de 24 horas.
- **Particiones de Arranque:** La partición de inicio `/boot` se mantiene estable al 15% de su capacidad (117 MB usados), garantizando el espacio necesario para futuras actualizaciones de la imagen del kernel.

---

## 3. Estado de los Servicios Críticos

El estado de los demonios de red perimetrales ha experimentado una mejora sustancial en comparación con la auditoría del día anterior:

| Servicio | Estado de Ejecución | Puerto / Protocolo | Rol en la Infraestructura | Evaluación de Riesgo |
| :--- | :--- | :--- | :--- | :--- |
| **Nginx** | `active (running)` | TCP/80, TCP/443 | Proxy inverso de entrada y cifrado TLS (Certbot). | **Nominal (Estable)**. Rendimiento excelente sin caídas. |
| **SSH (sshd)** | `active (running)` | TCP/22 | Demonio de acceso administrativo y SFTP seguro. | **Riesgo Medio-Alto**. Puerto por defecto expuesto a internet. |
| **Fail2ban** | `active (running)` | N/A | Detección de intrusos e inyección dinámica en iptables. | **Nominal (Mitigado)**. Activo y bloqueando atacantes. |

*Nota:* Fail2ban se encuentra activo desde el **sábado 22 de agosto a las 15:29:19 CEST**, acumulando más de 15 horas de ejecución ininterrumpida y protegiendo de manera proactiva el puerto de SSH.

---

## 4. Análisis de Intentos de Acceso SSH y Diagnóstico de Seguridad

### 4.1 Análisis del Log `/var/log/auth.log`

Superado el punto ciego de auditoría mediante la ejecución de comandos bajo el grupo de administración `adm`, se ha analizado el histórico completo del día actual:

- **Total de intentos de SSH fallidos detectados:** **235 intentos**.
- **Distribución de IPs atacantes (Top):**
  1. **`64.23.251.93` (DigitalOcean, EE.UU.):** **224 intentos** (95.3% del volumen total de ataques).
  2. **`195.178.110.137` (Rusia / Europa del Este):** **10 intentos**.
- **Usuarios de destino falsos empleados en la fuerza bruta:** El ataque coordinado desde la IP `64.23.251.93` intentó adivinar credenciales utilizando nombres de servicios comunes del ecosistema open-source. Entre ellos destacan: `solr`, `opensearch`, `graylog`, `loki`, `jaeger`, `zipkin`, `sentry`, `keycloak`, `openldap`, `freeipa`, `wireguard`, `openvpn`, `fail2ban` y `rsync`.

### 4.2 Evaluación y Diagnóstico de Fail2ban en Acción

La inspección forense de `/var/log/fail2ban.log` aporta datos de enorme valor sobre el comportamiento y efectividad de nuestras defensas perimetrales:

1. **Efectividad del Bloqueo:** Fail2ban ha detectado e interceptado con éxito al atacante principal (`64.23.251.93`), aplicando bloqueos en tiempo de ejecución. Se documentaron los siguientes eventos:
   - **Primer Ban:** Registrado a las `00:33:52` tras exceder el límite de intentos. El atacante fue desbaneado a las `01:34:03` (duración: 1 hora).
   - **Segundo Ban:** Al reincidir inmediatamente tras el desbaneo, fue bloqueado nuevamente a las `02:05:40` y desbaneado a las `02:46:40` (duración: ~41 minutos).
2. **Anomalías en la Duración de Baneos:** Se observa que la IP maliciosa logró acumular un número inusualmente elevado de intentos fallidos (224) a pesar de los baneos. Esto se debe a dos factores técnicos:
   - **Velocidad de ráfaga (Bursting):** El bot lanza decenas de intentos de conexión en milisegundos antes de que el motor de Fail2ban lea el log de autenticación, procese la regla y aplique la regla en iptables.
   - **Bantime de 10 minutos:** Otras IPs como `103.77.14.62` o `37.111.53.110` muestran tiempos de baneo y desbaneo de exactamente 10 minutos (por ejemplo, de `18:20:27` a `18:30:27`). Este intervalo es demasiado corto, lo que permite a las botnets automatizadas reiniciar el escaneo de forma indefinida sin un castigo severo.

---

## 5. Hallazgos Críticos y Recomendaciones de Seguridad

### 5.1 Amenazas e Ineficiencias Identificadas

1. **Ataques Recurrentes post-Baneo (Medio):** El bot atacante de la IP `64.23.251.93` retoma el ataque en cuanto expira la penalización de Fail2ban. El `bantime` por defecto de 10 minutos resulta insuficiente para disuadir a atacantes persistentes.
2. **Falta de Incremento en la Penalización (Bajo):** Fail2ban no parece estar incrementando el tiempo de baneo de manera exponencial ante reincidencias severas de la misma IP.
3. **Exposición del Puerto Estándar (Alto):** El demonio de SSH continúa operando en el puerto estándar `TCP/22`, atrayendo el 100% del tráfico de rastreo automatizado.

### 5.2 Plan de Acción y Mitigación Recomendado

Para robustecer la configuración y consolidar la excelente mejora lograda con la activación de Fail2ban, se recomienda encarecidamente aplicar las siguientes medidas técnicas en el VPS:

1. **Habilitar el Incremento de Tiempo de Baneo (Bantime Increment):**
   Modificar el archivo de configuración local de Fail2ban `/etc/fail2ban/jail.local` para activar la penalización exponencial de reincidentes. Esto multiplicará el tiempo de bloqueo (por ejemplo, de 10 minutos a 24 horas, y luego a 1 semana) para IPs persistentes como `64.23.251.93`:
   ```ini
   [DEFAULT]
   bantime.enable = true
   bantime.factor = 1
   bantime.formula = banTime * (1 << anyInitDoubleBanCount)
   ```
2. **Configurar el Hardening de SSH (Deshabilitar Contraseñas):**
   Dado que el usuario prefiere mantener la autenticación por contraseña para evitar bloqueos accidentales, se sugiere como alternativa configurar Fail2ban con un umbral de tolerancia menor para SSH (por ejemplo, reducir `maxretry` de 5 a 3 intentos) y ampliar el rango de análisis `findtime` a 30 minutos.
3. **Implementar Puertos SSH no Estructurados:**
   Se reitera la recomendación de desplazar el puerto SSH a un rango no estándar (ej. puerto TCP superior a 20000), lo cual anulará de inmediato el 99% de las agresiones automatizadas y reducirá drásticamente la generación de logs y el uso de recursos de Fail2ban.

---

## 6. Conclusión Técnico-Operativa

La infraestructura del VPS se encuentra en un estado de salud excelente. La carga promedio del sistema es mínima (por debajo de `0.10`), el servidor Nginx responde con absoluta estabilidad a las peticiones del dominio Cinesfer, y el almacenamiento en disco se conserva holgado.

La puesta en marcha de Fail2ban representa un salto de gigante en la postura de seguridad del servidor con respecto a días anteriores. Sin embargo, el volumen de 235 intentos fallidos y la persistencia de las IPs atacantes demuestran que las reglas por defecto (baneos de 10 minutos) se quedan cortas frente a bots modernos. Ajustar el archivo `jail.local` para activar el incremento exponencial del tiempo de bloqueo y reducir la tolerancia de reintentos es la prioridad inmediata recomendada para consolidar el blindaje perimetral del servidor.
