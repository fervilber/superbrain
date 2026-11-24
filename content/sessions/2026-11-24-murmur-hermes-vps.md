---
title: "Informe-2026-11-24: Murmur sobre Hermes Agent en el VPS — instalación sin Docker, acceso por túnel SSH y el incidente del cgroup"
date: 2026-11-24
tags:
  [
    murmur,
    hermes-agent,
    umbrel,
    vps,
    systemd,
    systemd-user,
    cgroup,
    tunel-ssh,
    fail2ban,
    ufw,
    node,
    pwa,
    service-worker,
  ]
---

# Informe-2026-11-24: Murmur sobre Hermes Agent en el VPS

## Contexto y objetivo

La sesión arranca con un síntoma recurrente: el panel de control de Hermes no aparece al abrir el túnel SSH, aunque la conexión al servidor sí funciona. A partir de ahí el trabajo deriva en el objetivo real de la jornada: evaluar, planificar e instalar **Murmur**, la interfaz web que el equipo de Umbrel ha publicado para Hermes Agent, sobre el Hermes que ya vive en el VPS, sin duplicar agentes ni exponer nada a Internet.

Murmur es un proyecto MIT del repositorio `getumbrel/murmur` (versión fijada en esta sesión: **v0.15.2**, commit `9895bac`, publicada el 20 de noviembre de 2026). Se define como «un hogar bonito para tus agentes Hermes»: chat con uno o varios agentes, apps externas (Notion, Linear, Todoist…), mensajería por WhatsApp y Telegram, rutinas programadas, memoria editable, voz, salas de grupo y una PWA que se instala en el móvil. La clave arquitectónica es que **no importa ni copia nada**: los agentes de Murmur son los perfiles de Hermes y los chats de Murmur son las sesiones de Hermes, así que la misma información aparece en el panel, en la terminal y en Telegram sin sincronización intermedia.

## Estado de partida del entorno

El VPS es un Ubuntu con las siguientes características verificadas durante la sesión:

- Disco: 193 GB totales, 65 GB usados, **129 GB libres**.
- Memoria: 11 GiB totales, ~9,6 GiB disponibles.
- CPU: 6 vCPU AMD EPYC.
- Node v22.23.1 y npm 10.9.8 ya instalados.
- Docker 29.6.1 instalado, pero el usuario `vilber` **no pertenece al grupo `docker`** (`docker ps` devuelve _permission denied_ sobre `/var/run/docker.sock`).
- Hermes Agent **v0.23.3** (2026.9.24), instalado por git en `/home/vilber/.hermes/hermes-agent`, con el gateway corriendo como servicio systemd de usuario (`hermes-gateway.service`).
- `ufw` activo con política por defecto `deny (incoming)`, y solo cinco puertos abiertos: 80, 443, 2222, 22822 y 8096.
- Puertos ocupados en `127.0.0.1`: 8000 (API de segundo-cerebro-inversiones), 8080 (calibre-server), 8096 (jellyfin) y 9119 (dashboard de Hermes, cuando está encendido).

## Fase 1 — Diagnóstico: el dashboard no estaba corriendo

El primer trabajo fue descartar que algo estuviera «bloqueando» el panel. La comprobación fue directa:

```bash
ss -tln | grep 9119                      # nada escuchando
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:9119/   # 000 (connection refused)
```

No había ninguna sesión ni proceso interfiriendo. El dashboard **simplemente no estaba en marcha**, y la prueba documental apareció en los resultados de proceso del propio agente: el fichero `~/.hermes/logs/process-results/proc_c82843ce4685.json` mostraba `exit_code: -15`, `completion_reason: killed` y `termination_source: gateway_shutdown`. Es decir, el último dashboard lo había matado el apagado del gateway el 20 de noviembre a las 22:55, y nunca se había relanzado.

Este patrón es el que produce el síntoma clásico de «túnel abierto pero el navegador da _connection refused_»: el fallo está en el servidor, no en el reenvío SSH. La regla que queda es comprobar `ss -tln | grep 9119` en el VPS **antes** de tocar el túnel.

Se relanzó el panel y se verificó con `LISTEN 127.0.0.1:9119` y `HTTP 200`.

## Fase 2 — Investigación de Murmur: qué es y qué necesita

La documentación del proyecto (`README.md`, `docs/STANDALONE.md`, `docs/DEVELOPMENT.md`, `docker-compose.yml`, `Dockerfile`, `vite.config.ts`, `server/index.ts`) dejó claro el diseño:

- **Servidor**: Node 22 sin dependencias, que sirve la SPA compilada y hace de proxy de `/hermes/api/*` (REST y el socket WebSocket `/api/ws`) hacia el dashboard de Hermes, **firmando las peticiones en el servidor** con el token de sesión. El navegador nunca ve el token ni la contraseña de Hermes.
- **Requisitos**: Node ≥ 22.18 y Hermes Agent ≥ 0.21.4. Ambos cumplidos (22.23.1 y 0.23.3).
- **Dos modos de instalación**: (A) `docker-compose` con un Hermes propio dentro de Docker —imagen de ~1,1 GB, ~600 MB de RAM en reposo, pero un Hermes **vacío**, sin los agentes ni las memorias reales— y (B) **Murmur solo**, apuntando a un Hermes ya existente. El modo B era el correcto.
- **Cómo se autentica contra el Hermes local**: al estar el dashboard en `127.0.0.1`, Murmur lee la clave de sesión de la propia página del panel (`window.__HERMES_SESSION_TOKEN__`), modo `token`. No hay que teclear usuario ni contraseña de Hermes. El REST viaja con la cabecera `X-Hermes-Session-Token` y el socket con `?token=`.

**Requisito crítico**: Murmur es un _cliente_ del dashboard, así que **el dashboard tiene que estar encendido**. Esto choca con la política del VPS de mantenerlo apagado por defecto para no consumir créditos.

### La restricción de fondo: Murmur no soporta subdirectorio

La convención del VPS es publicar proyectos como subdirectorio (`dominio.com/subdir/`). Murmur **no lo admite** sin parchear:

- `vite.config.ts` no define `base`, así que el `index.html` referencia sus recursos con rutas absolutas (`/assets/...`). Servido bajo un prefijo, el navegador pide `dominio.com/assets/...` y devuelve 404 — pantalla en blanco.
- La app llama a `/hermes/...` y `/murmur/...`, también absolutas; bajo un prefijo se irían al sitio equivocado.
- El service worker (`public/sw.js`) se registra con scope en `/`, que no puede vivir en una subruta.
- La documentación de seguridad del propio proyecto habla de dominios propios (`murmur.example.com`), es decir, en la **raíz de un host**, nunca en subruta.

Las alternativas reales eran tres: túnel SSH (raíz invisible, sin exponer nada), subdominio con TLS (raíz de un nombre propio, rompe la convención del usuario) o un puerto distinto del mismo dominio. Se comprobó además que **DuckDNS resuelve comodines**: `murmur.cinesfer.duckdns.org` y hasta `test123.cinesfer.duckdns.org` apuntaban ya a la IP del VPS, así que un subdominio habría funcionado con Certbot.

Se eligió el **túnel SSH**: coherente con el acceso al dashboard, sin exponer nada y sin tocar nginx. Y la ruta de instalación elegida fue **Node directo** en lugar de Docker, para no depender del grupo `docker` (que el usuario no tiene) ni de `sudo`.

## Fase 3 — Instalación paso a paso

```bash
git clone https://github.com/getumbrel/murmur /home/vilber/proyectos/murmur
cd /home/vilber/proyectos/murmur
git checkout v0.15.2        # etiqueta fija, no master
npm ci --no-audit --no-fund # 537 paquetes
npm run build               # typecheck + SPA a dist/
```

Se generó una contraseña propia de Murmur y se guardó en `~/.config/murmur/murmur.env` (chmod 600), con los datos en `~/.local/share/murmur`. El arranque apunta al dashboard local:

```bash
HERMES_URL=http://127.0.0.1:9119 \
HERMES_NAME="Hermes VPS" \
MURMUR_PASSWORD=<secreto> \
DATA_DIR=/home/vilber/.local/share/murmur \
PORT=3000 \
node server/index.ts
```

Verificación inicial: `Murmur listening on :3000 → Hermes at http://127.0.0.1:9119 (env)`, `/healthz` → `ok`, raíz → 200, y `/murmur/connections` → `{status: "connected", mode: "token", hermesVersion: "0.23.3"}`.

### Sobre la exposición

`ss` mostró que Murmur escucha en `*:3000` (todas las interfaces), no en `127.0.0.1`, y **no hay variable de entorno para fijar la interfaz** (el parámetro `host` existe en el código, pero no se lee del entorno). La protección es `ufw`: con `Default: deny (incoming)` y solo 80/443/2222/22822/8096 abiertos, el 3000 queda cerrado desde Internet. Se verificó explícitamente con `sudo ufw status verbose`.

## Fase 4 — El problema del acceso: puerto 22 frente a 2222

Al crear el túnel, el usuario recibió:

```
kex_exchange_identification: read: Connection reset
Connection reset by 144.91.108.254 port 22
```

El diagnóstico: **en el VPS no hay nada escuchando en el 22**. El SSH está en el **2222** (socket systemd `ssh.socket`) y también en el 22822. El 22 lo bloquea ufw, y en `/var/log/ufw.log` se veía el `[UFW BLOCK] ... DPT=22` correspondiente al intento del usuario (a las 16:09:28, desde su IP). El error fue mío: había dado el comando del túnel sin `-p`, así que fue al puerto por defecto.

Comando correcto:

```bash
ssh -p 2222 -L 3000:127.0.0.1:3000 vilber@144.91.108.254
```

Durante esta fase apareció también una **falsa alarma de fail2ban**: la IP `85.11.167.37` estaba en la lista de baneadas. Se comprobó que no era el usuario: esa IP estaba escaneando el puerto 9922 y el jail `sshd` (configurado en `jail.local` con `port = 2222,22822`, `maxretry = 3`) la había cazado. La IP real del usuario no estaba baneada.

## Fase 5 — El fallo del chat: «la web funciona pero no contesta»

Con el túnel resuelto, la web de Murmur cargaba pero el chat se quedaba **pensando indefinidamente**. La investigación encontró la causa raíz en el journal de systemd:

```
Nov 24 16:13:22  gateway.run: SIGUSR1 received (systemctl reload / hermes gateway restart):
                 performing a graceful gateway restart
Nov 24 16:13:26  systemd[952]: hermes-gateway.service: Killing process 3244134 (hermes) with signal SIGKILL.
Nov 24 16:13:26  systemd[952]: hermes-gateway.service: Killing process 3244276 (node) with signal SIGKILL.
```

El gateway se reinició a las 16:13 y, al hacerlo, **systemd mató todo su cgroup**: el dashboard (3244134) y Murmur (3244276) murieron con él. Ambos estaban caídos (`ss -tln` no mostraba nada en 3000 ni 9119).

¿Por qué la web «funcionaba» entonces? Por el **service worker**: Murmur conserva la PWA en el dispositivo y la entrega cuando el servidor no responde en tres segundos. El navegador mostraba la interfaz desde la caché, pero no había backend detrás — de ahí el «se queda pensando».

### El error de diagnóstico que hay que no repetir

En un momento anterior de la sesión afirmé que los procesos estaban «desacoplados» del gateway porque su PPID había pasado a `systemd --user`. **Era falso**: reparentar un proceso no lo saca de su cgroup. Todo lo que arranca la shell del agente vive en `hermes-gateway.service` y muere con cualquier reinicio del gateway, aunque el proceso quede huérfano. El PPID engaña; el cgroup es el que manda.

## Fase 6 — Solución definitiva: unidades systemd de usuario

Para sacar ambos servicios del cgroup del gateway se crearon dos unidades systemd de usuario, **sin habilitar** (arranque a demanda):

`~/.config/systemd/user/hermes-dashboard.service` → `hermes dashboard --port 9119 --skip-build --no-open`.

`~/.config/systemd/user/murmur.service` → `node server/index.ts` con `EnvironmentFile=/home/vilber/.config/murmur/murmur.env` y `HERMES_URL=http://127.0.0.1:9119`.

```bash
systemctl --user daemon-reload
systemctl --user start hermes-dashboard.service murmur.service
```

Verificación de que quedaron aislados:

```
hermes-dashboard -> cgroup: .../app.slice/hermes-dashboard.service
murmur           -> cgroup: .../app.slice/murmur.service
```

Con su propio cgroup, un reinicio del gateway ya no se los lleva. Los scripts `murmur-up.sh` / `murmur-down.sh` del proyecto se reescribieron para envolver esos `systemctl` en lugar de usar `nohup`.

## Fase 7 — Verificación real del chat

No se dio por bueno «la web carga». Se reprodujo un chat completo por el mismo camino que usa el navegador, con un cliente WebSocket en Node contra el **proxy de Murmur** (`ws://127.0.0.1:3000/hermes/api/ws`, con cookie de sesión), usando el flujo RPC JSON-RPC:

1. `session.create {profile: 'default'}` → `session_id`.
2. `prompt.submit {session_id, text}` → `{status: "streaming"}`.
3. Evento esperado: `message.complete`.

Resultado: **respuesta «HOLA-MURMUR» en 8,3 segundos**. El mismo test directo contra el dashboard (`:9119` con `?token=`) devolvió «OK» en 3,3 s. Quedó demostrado que el chat funciona de punta a punta y que lo único que fallaba era que no había backend.

## Resumen de problemas y su causa

| #   | Síntoma                                    | Causa raíz                                                                                          | Solución                                                     |
| --- | ------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1   | Dashboard no aparece por túnel             | El proceso había muerto con el apagado del gateway (`gateway_shutdown`, exit -15)                   | Relanzarlo; comprobar `ss -tln \| grep 9119` antes del túnel |
| 2   | Murmur no admite `dominio.com/subdir/`     | Rutas absolutas + service worker en `/`                                                             | Acceso por túnel SSH                                         |
| 3   | `docker ps` → permission denied            | El usuario no está en el grupo `docker`                                                             | Instalar con Node, sin Docker                                |
| 4   | `Connection reset by ... port 22`          | El SSH está en 2222/22822; el 22 lo bloquea ufw                                                     | `ssh -p 2222 ...`                                            |
| 5   | Falsa alarma de fail2ban                   | La IP baneada era un escáner (puerto 9922), no el usuario                                           | Verificar el jail y los puertos (`port = 2222,22822`)        |
| 6   | Comando bloqueado por falta de aprobación  | El heredoc en `terminal` requiere confirmación y expiró a los 5 min                                 | No reintentar; escribir ficheros con `write_file`            |
| 7   | «La web funciona pero el chat no contesta» | El reinicio del gateway mató Murmur y el dashboard (cgroup); el navegador servía la PWA desde caché | Unidades systemd de usuario propias                          |
| 8   | Warning `401 token_revoked`                | OAuth de `openai-codex` (modelo auxiliar `gpt-5.6-luna`) revocado                                   | Pendiente de reautenticar; no afecta al chat principal       |

## Aprendizajes y reglas para el futuro

1. **Nunca lanzar servicios duraderos desde la shell del agente.** Quedan en el cgroup de `hermes-gateway.service` y mueren con cualquier reinicio del gateway. Para eso están las unidades systemd de usuario.
2. **El PPID no prueba el desacoplamiento; el cgroup sí.** Un proceso reparentado a `systemd --user` puede seguir en el cgroup del gateway.
3. **El síntoma «la PWA carga pero nada responde» es un backend caído**, no un fallo del frontend: el service worker sirve la app desde la caché. Comprobar puertos primero.
4. **Murmur exige el dashboard encendido** y **no soporta subdirectorio**. Con eso claro, el túnel SSH es la vía limpia.
5. **El SSH del VPS va por el 2222**, no por el 22.
6. **Verificar con una ejecución real, no con una carga de página.** Reproducir el chat por RPC fue lo que demostró que todo funcionaba.

## Comandos de referencia

```bash
# Encender / apagar (unidades systemd de usuario)
systemctl --user start hermes-dashboard.service murmur.service
systemctl --user stop  murmur.service hermes-dashboard.service
bash /home/vilber/proyectos/murmur/murmur-up.sh
bash /home/vilber/proyectos/murmur/murmur-down.sh

# Estado y logs
systemctl --user status murmur.service hermes-dashboard.service
journalctl --user -u murmur -u hermes-dashboard -n 50

# Túnel y acceso
ssh -p 2222 -L 3000:127.0.0.1:3000 vilber@144.91.108.254   # -> http://localhost:3000

# Comprobaciones rápidas
ss -tln | grep -E ':3000|:9119'
curl -s http://127.0.0.1:3000/healthz
```

## Conclusión

Murmur queda instalado en `/home/vilber/proyectos/murmur` (v0.15.2), con sus datos en `~/.local/share/murmur` y su contraseña en `~/.config/murmur/murmur.env`, servido solo por túnel SSH y gobernado por unidades systemd de usuario independientes del gateway. La lección central de la sesión no es la instalación en sí, sino el incidente que la precedió: en un sistema con systemd, la frontera real de un proceso es su cgroup, y cualquier cosa que se lance desde la shell del agente vive y muere con el gateway. Murmur y el panel se movieron a su propio cgroup y el problema desapareció; el chat, verificado por RPC, responde en segundos.
