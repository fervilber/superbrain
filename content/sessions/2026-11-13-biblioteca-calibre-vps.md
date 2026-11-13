---
title: "Informe-2026-11-13: Biblioteca Calibre autoalojada en el VPS — instalación aislada sin root, systemd de usuario y publicación en /libros"
date: 2026-11-13
tags: [calibre, vps, nginx, systemd, self-hosting, biblioteca, opds, sqlite, epub]
---

# Informe-2026-11-13: Biblioteca Calibre autoalojada en el VPS

## Contexto y objetivo

El objetivo de la sesión era convertir el VPS en un servidor de biblioteca personal: una colección de libros en PDF y EPUB, accesible desde el móvil y compartible con la familia, sin depender de servicios de terceros ni de aplicaciones propietarias. El usuario ya utiliza Calibre en su PC y quiere que el servidor sea la copia Always-on de la biblioteca: subir libros por SFTP y poder leerlos o descargarlos desde cualquier navegador.

La restricción de diseño más importante es que el VPS es headless: no hay escritorio, no hay servidor X y no tiene sentido intentar ejecutar la interfaz gráfica de Calibre. La pieza correcta es `calibre-server`, el servidor de contenido oficial que Calibre usa internamente para "compartir por red". Expone una SPA adaptada a pantallas táctiles, búsqueda por metadatos, visor de EPUB en el navegador, descarga por formato y un catálogo OPDS para aplicaciones de lectura. Todo eso se puede ejecutar sin entorno gráfico y mantener con systemd.

El servidor es un Ubuntu 24.04.4 LTS (amd64), con 11 GiB de RAM, 136 GB libres en `/` y nginx ya ocupando 80/443 con certificados Let's Encrypt válidos para `bolsafer.duckdns.org` y `cinesfer.duckdns.org`. El puerto 8080 estaba libre y el 8000 lo ocupa la API de otro proyecto, así que 8080 era el candidato natural para el backend de la biblioteca.

## Restricciones reales del entorno

Antes de instalar nada se verificó el estado del sistema, y aparecieron tres condicionantes que determinaron el resto del diseño:

1. **Sin contraseña de root disponible para el agente.** `sudo -l` mostraba NOPASSWD únicamente para `/usr/sbin/nginx` y `/usr/bin/systemctl`, además de una regla muy concreta sobre `grep 'Failed password'`. Cualquier `apt install` habría requerido una contraseña que el agente no tiene ni debe manejar. La instalación tenía que hacerse, por tanto, sin privilegios.
2. **Sin sistema de paquetes utilizable de forma no interactiva.** La versión de Calibre en los repositorios de Ubuntu 24.04 es la 7.6.0, dos años por detrás de la 9.18.0 actual, y arrastra 170 paquetes Qt6. Además, instalarla habría exigido root y habría mezclado la aplicación con el sistema.
3. **Sin escritorio.** La GUI de Calibre no solo es innecesaria: es contraproducente en un servidor, porque mantiene un bloqueo sobre la base de datos y requiere un display.

La conclusión fue usar el instalador binario oficial en modo aislado, dentro del home del usuario, y ejecutar el servicio como unidad systemd de usuario. Ubuntu ya tenía `Linger=yes` para el usuario `vilber`, de modo que las unidades de usuario arrancan al boot y sobreviven al cierre de sesión sin necesidad de root.

## Instalación: el instalador oficial y las librerías que faltaban

El instalador de Calibre (`download.calibre-ebook.com/linux-installer.sh`) es un wrapper que descarga un tarball de unos 240 MB, verifica su firma SHA-512 y lo extrae. Acepta parámetros como `install_dir=` e `isolated=true`; con ellos la instalación queda en `/home/vilber/opt/calibre` y no toca `/usr/bin` ni `/opt`.

El primer intento falló antes de descargar nada, con un mensaje engañoso: _"You are missing the system library libOpenGL.so.0"_. El instalador comprueba con `ctypes.CDLL` una serie de bibliotecas del sistema antes de arrancar. En un servidor mínimo faltaban `libOpenGL.so.0` y `libxcb-cursor.so.0`, y la segunda arrastraba a su vez `libxcb-render-util.so.0` y `libxcb-image.so.0`. Sin root, la solución fue descargar los `.deb` de Ubuntu con `apt-get download` (que no requiere privilegios), extraerlos con `dpkg-deb -x` en `/home/vilber/opt/calibre-libs` y exportar `LD_LIBRARY_PATH` durante la instalación. Las bibliotecas implicadas fueron `libopengl0`, `libxcb-cursor0`, `libxcb-render-util0`, `libxcb-image0`, `libxcb-keysyms1`, `libxcb-icccm4`, `libxcb-xinerama0`, `libxkbcommon-x11-0`, `libxcb-xkb1`, `libxcb-randr0`, `libxcb-shape0`, `libxcb-sync1`, `libxcb-xfixes0`, `libxcb-shm0`, `libxcb-util1` y `libxcb-xinput0`.

Con ese `LD_LIBRARY_PATH` el instalador completó la descarga, la verificación de integridad y la extracción. El resultado: `/home/vilber/opt/calibre/calibre-server` y `/home/vilber/opt/calibre/calibredb` en versión 9.18. Es una instalación de unos 910 MB que no contamina el sistema y se puede borrar con un `rm -rf` si algún día se migra a otro modelo.

## Arquitectura final

```
navegador / móvil
      │ HTTPS (443, cert Let's Encrypt existente)
      ▼
nginx  bolsafer.duckdns.org
      │ location /libros/  → proxy_pass 127.0.0.1:8080
      ▼
calibre-server  --url-prefix /libros
                --enable-auth --auth-mode basic
                --userdb ~/.config/calibre/server-users.sqlite
      │
      ▼
/home/vilber/libros          ← árbol gestionado por Calibre (metadata.db incluida)
/home/vilber/libros-inbox    ← bandeja de entrada para las subidas SFTP
/home/vilber/importados      ← originales ya importados + import.log
/home/vilber/backups/libros  ← copias de metadata.db (tar.gz, rotación 14 días)
```

La decisión clave es el uso de `--url-prefix /libros`. Sin ese parámetro, la SPA genera enlaces absolutos a `/get/...`, `/ajax/...` y `/opds`, que al publicarse bajo una subruta acaban en 404. Con el prefijo, el propio servidor genera todas sus rutas relativas al montaje y nginx puede reenviar sin reescribir el path. Es la diferencia entre una interfaz que funciona y una que carga en blanco.

## Autenticación y usuarios

El servidor arranca con `--enable-auth --auth-mode basic` y una base de usuarios SQLite propia, creada con:

```bash
calibre-server --userdb ~/.config/calibre/server-users.sqlite --manage-users
```

El asistente interactivo permite añadir, editar y borrar usuarios, y marcar cada uno como administrador o de solo lectura. Se creó el usuario principal y se dejó documentado el procedimiento para añadir familiares en el futuro. La contraseña inicial se generó con `openssl rand`, se guardó en un archivo con permisos 600 (`~/.config/calibre/credenciales.txt`) y no se escribió en el informe ni en la unidad de systemd.

Un detalle de verificación importante: con autenticación activada, la raíz `/libros/` responde **200** porque sirve la página de login de la SPA. Los endpoints de datos (`/libros/ajax/books`, `/libros/opds`) sí devuelven **401** sin credenciales. Juzgar la protección por el código de la raíz habría sido un falso positivo; el criterio correcto es comprobar los endpoints que exponen contenido.

Se eligió `--auth-mode basic` y no digest porque el servidor va detrás de un proxy TLS. La documentación de Calibre lo recomienda explícitamente en ese escenario: basic es más rápido y más fiable al atravesar nginx. El navegador muestra un diálogo nativo de credenciales una vez y luego las reutiliza.

## Publicación en nginx

El vhost de `bolsafer.duckdns.org` es propiedad de root, así que el agente no podía editarlo directamente. La solución fue preparar un script idempotente, `setup-nginx-libros.sh`, que el usuario ejecutó una sola vez con `sudo`. El script:

1. Hace una copia del vhost con timestamp.
2. Inserta un bloque `location` antes del catch-all que hoy apunta a Jellyfin.
3. Ejecuta `nginx -t`.
4. Si la sintaxis es válida, recarga nginx; si no, restaura la copia y aborta.

El bloque final es:

```nginx
location = /libros {
    return 301 /libros/;
}

location /libros/ {
    client_max_body_size 1024M;
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
    proxy_read_timeout 300s;
    proxy_send_timeout 300s;
}
```

`client_max_body_size` y `--max-request-body-size` se alinearon a 1024 MB para que un PDF grande no choque con el límite por defecto de nginx (1 MB). `proxy_buffering off` evita que las descargas grandes se acumulen en memoria y mantiene el streaming hacia el cliente. Los timeouts amplios cubren la conversión y la generación de portadas.

## Ingesta: por qué no se escribe en la biblioteca

Calibre no es una carpeta de archivos: es una base de datos SQLite (`metadata.db`) más un árbol de directorios por libro. Copiar un EPUB directamente dentro de `/home/vilber/libros` no lo añade al catálogo: deja un archivo huérfano que el servidor no indexa y que puede confundir las operaciones posteriores. Además, `metadata.db` tiene bloqueo exclusivo, y Calibre detecta si otro programa suyo está usando la biblioteca.

El primer importador intentó usar `calibredb add --library-path ...` con el servidor en marcha y falló con un mensaje explícito: _"Another calibre program such as calibre-server ... is running"_. La solución correcta es la que documenta Calibre: hablar con el servidor en marcha como si fuera una biblioteca remota.

```bash
calibredb --with-library "http://127.0.0.1:8080/#libros" \
          --username "$CALIBRE_USER" --password "$CALIBRE_PASS" add archivo.epub
```

El identificador `libros` se obtiene de `/libros/ajax/library-info`. Así, las escrituras pasan por el proceso que ya tiene la base de datos abierta y se evita el conflicto de bloqueo. También se descubrió que `--ignore-duplicates` no existe en esta versión; el flag real es `--duplicates`, y el comportamiento por defecto ya omite duplicados, que es lo que interesa en una importación periódica.

Con ese mecanismo, la bandeja de entrada queda separada del árbol gestionado: el usuario sube por SFTP a `/home/vilber/libros-inbox`, y un timer de systemd ejecuta cada 5 minutos un script que recorre los formatos admitidos, importa uno a uno, mueve el original a `/home/vilber/importados` y registra el resultado en `import.log`. Los fallos no se borran: se quedan en la bandeja para revisión. La prueba se hizo con dos EPUB sintéticos generados a mano (zip con `mimetype`, `container.xml`, OPF y XHTML), que se importaron, aparecieron en la API y se eliminaron al terminar.

## Copias de seguridad

El backup no puede ser un `cp` de `metadata.db` mientras el servidor escribe. Se usa la API de backup de SQLite desde Python (`con.backup(out)`), que produce una copia consistente aunque haya conexiones abiertas, y después se comprime en `tar.gz` con fecha. Un timer diario a las 03:15 (separado del cron de otro proyecto que corre a las 03:30) mantiene 14 días de rotación y registra cada ejecución en `backup.log`.

Queda una limitación consciente: el backup cubre la base de datos, no los archivos de los libros. Para una recuperación completa haría falta copiar también el árbol de formatos; el README lo deja anotado como trabajo futuro, junto con la posibilidad de replicar a otro destino.

## Verificación

La verificación no se limitó a comprobar que el proceso estuviera activo. Se hizo en tres capas:

1. **Backend local:** `curl` a `127.0.0.1:8080/libros/` y a los endpoints de datos, con y sin credenciales.
2. **Externo a través de nginx:** `https://bolsafer.duckdns.org/libros/` devuelve la SPA; `/libros/opds` devuelve 401 sin credenciales y 200 con ellas; `/libros/get/epub/1/libros` descarga un EPUB válido (`application/epub+zip`); `/libros` redirige con 301 a `/libros/`; la portada responde `image/jpeg`.
3. **Navegador real:** con Chrome vía CDP y la cabecera `Authorization` de basic auth se cargó la SPA, se entró en la biblioteca `libros`, se abrió la ficha de un libro y se pulsó **Read**. El visor se abrió con sus controles táctiles ("Tap to turn page"), lo que confirma la lectura en navegador sin apps. También se comprobó que `/bolsa/` sigue respondiendo 200 y que `nginx -t` pasa después del cambio.

Los dos libros de prueba se eliminaron al final; la biblioteca quedó vacía esperando los reales.

## Operación diaria

- Subida: SFTP con la clave SSH existente, puerto 2222, usuario `vilber`, destino `/home/vilber/libros-inbox`. No se instaló ningún servidor FTP: SFTP ya funciona, no abre un puerto nuevo y es más seguro.
- Importación: automática cada 5 minutos, o manual con `systemctl --user start calibre-import.service`.
- Estado: `systemctl --user status calibre-server`, `journalctl --user -u calibre-server -f`.
- Usuarios: `calibre-server --userdb ... --manage-users` (añadir, cambiar contraseña, borrar).
- Regla de oro: nunca escribir a mano dentro de `/home/vilber/libros`.

## Lecciones aprendidas

1. **El instalador de Calibre comprueba bibliotecas X aunque el servidor sea headless.** En un Ubuntu mínimo hay que satisfacer `libOpenGL.so.0` y `libxcb-cursor.so.0`, y sus dependencias XCB. Se pueden extraer sin root con `apt-get download` + `dpkg-deb -x` y `LD_LIBRARY_PATH`.
2. **`calibre-server` no acepta `--library-path`.** La ruta de la biblioteca va como argumento posicional; `--library-path` es una opción de `calibredb`. Un `systemd` con el flag equivocado entra en bucle de reinicio.
3. **El 200 en la raíz no significa que no haya autenticación.** La SPA devuelve su página de login con 200; hay que probar endpoints de datos y OPDS para ver el 401.
4. **`calibredb` no puede escribir mientras `calibre-server` tiene la biblioteca abierta.** Hay que usar `--with-library http://127.0.0.1:8080/#<id>` con credenciales, no la ruta local.
5. **`--url-prefix` es obligatorio si se publica en una subruta.** Sin él, los enlaces absolutos de la SPA apuntan a la raíz del dominio.
6. **systemd de usuario + `linger` es suficiente** para un servicio Always-on sin root, y encaja mejor con la instalación aislada que una unidad de sistema.
7. **nginx sigue necesitando root**, pero el cambio se puede encapsular en un script idempotente con backup y rollback automático si `nginx -t` falla.

## Trabajo futuro

La biblioteca queda funcional, pero el diseño deja puertas abiertas: Calibre-Web como frontend alternativo (estanterías, usuarios más ricos, sincronización con Kobo) apuntando a la misma biblioteca en modo lectura; sincronización automática PC→VPS por `rsync` si el flujo manual se hace pesado; copia de seguridad del árbol completo de libros, no solo de `metadata.db`; y prueba de restauración real en un directorio temporal. Ninguna de esas piezas exige rehacer lo instalado.
