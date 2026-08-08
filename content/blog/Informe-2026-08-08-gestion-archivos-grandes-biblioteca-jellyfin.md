---
title: "Informe Técnico: Gestión de Archivos Grandes y Configuración de Biblioteca de Películas en Jellyfin"
date: 2026-08-08
tags: [jellyfin, vps, multimedia, sftp, winscp, nginx]
---

# Informe Técnico: Gestión de Archivos Grandes y Configuración de Biblioteca de Películas en Jellyfin

## 1. Introducción y Contexto

Durante la administración y enriquecimiento de nuestro servidor multimedia **Jellyfin** alojado en el VPS (`144.91.108.254`), se identificó un problema crítico al intentar transferir archivos de vídeo de gran tamaño (películas en alta definición de varios gigabytes) utilizando la interfaz web de Hermes Dashboard. Cada intento de subida resultaba en un error inmediato o en interrupciones persistentes de la transferencia HTTP. 

Este informe técnico analiza las causas subyacentes de estos fallos, detalla la solución exitosa adoptada mediante la transferencia SFTP con **WinSCP** y describe el procedimiento para configurar correctamente una nueva biblioteca de películas dentro de la interfaz de Jellyfin.

---

## 2. Diagnóstico Técnico del Problema (Límites HTTP)

El error de subida no se debió a un fallo en el servidor, sino a restricciones de diseño y seguridad implementadas tanto a nivel de aplicación como del proxy inverso:

1. **Limitación de Hermes Dashboard (100 MB):**
   La constante `_MANAGED_FILE_MAX_BYTES` en el servidor backend de Hermes (`hermes_cli/web_server.py`) está restringida a un límite duro de **100 MB** para los endpoints `/api/files/upload` y `/api/files/upload-stream`. Cualquier archivo que sobrepase este umbral es rechazado por el backend con un código de estado `413 File is too large` para evitar la saturación de memoria de la API del agente.
   
2. **Limitación del Proxy Inverso de Nginx (1 MB):**
   Por defecto, el proxy inverso de Nginx limita el cuerpo de las solicitudes de los clientes a **1 MB** mediante la directiva `client_max_body_size`. Si el dashboard está expuesto a través de Nginx sin configurar este parámetro, el servidor web rechazará la transferencia con un error `413 Request Entity Too Large` antes de que los datos puedan llegar al backend del agente.

3. **Ineficiencia del Protocolo HTTP para Grandes Archivos:**
   El protocolo HTTP convencional carece de mecanismos nativos eficientes para la fragmentación, verificación de integridad (checksums) y reanudación automática tras cortes de conexión en subidas masivas de datos continuos, lo que lo convierte en una opción inviable para subir archivos del tamaño de una película.

---

## 3. Solución Implementada: Transferencia Segura con WinSCP (SFTP)

Para omitir los cuellos de botella del protocolo HTTP y las limitaciones de tamaño de los proxies web, se ha optado por utilizar **SFTP (SSH File Transfer Protocol)**, un protocolo diseñado específicamente para la transferencia robusta de archivos. 

El usuario ha ejecutado exitosamente la subida utilizando **WinSCP** en su máquina local.

### Mapeo de Volúmenes en el VPS (Host vs. Contenedor)
El contenedor Docker de Jellyfin (`/home/vilber/proyectos/jellyfin/docker-compose.yml`) está configurado con montajes de volumen (bind mounts) que mapean directorios del VPS (Host) dentro de la estructura de archivos virtual del contenedor. El esquema de almacenamiento es el siguiente:

* **Ruta Física en el VPS (Host):** `/home/vilber/media/peliculas/`
* **Ruta de Montaje en el Contenedor:** `/media/peliculas/`

Cualquier archivo de vídeo subido al directorio real en el host es visible instantáneamente por el contenedor en la ruta interna indicada, con plenos permisos de lectura gracias a que el directorio del host pertenece al usuario `vilber:vilber`.

### Configuración en WinSCP:
1. **Protocolo:** SFTP (puerto `22`).
2. **Nombre de Host:** `144.91.108.254`
3. **Credenciales:** Usuario `vilber` y autenticación por clave SSH o contraseña.
4. **Directorio Destino:** `/home/vilber/media/peliculas/`
5. **Acción:** Arrastrar y soltar los archivos de películas (formatos `.mp4`, `.mkv`, etc.) desde el sistema local. El cliente SFTP maneja de manera nativa la reanudación si la conexión experimenta inestabilidades.

---

## 4. Guía de Configuración: Creación de una Nueva Biblioteca en Jellyfin

Una vez subidas las películas al VPS mediante WinSCP, el siguiente paso indispensable es configurar y registrar la biblioteca multimedia dentro de Jellyfin para que procese el contenido y descargue los metadatos correspondientes de internet.

### Paso 1: Acceso al panel de administración
1. Abre tu navegador web y navega a la URL de Jellyfin (normalmente `http://144.91.108.254:8096` o el dominio configurado).
2. Inicia sesión con una cuenta que disponga de privilegios de administrador.
3. Haz clic en el menú de tres líneas horizontales (hamburguesa) en la esquina superior izquierda y selecciona **Panel de control** (Dashboard).

### Paso 2: Creación de la biblioteca
1. En el menú lateral izquierdo, bajo la sección **Servidor**, haz clic en **Bibliotecas** (Bibliotecas).
2. Haz clic en el botón con el icono `+` que dice **Añadir biblioteca de medios** (Add Media Library).

### Paso 3: Definición del tipo de contenido
1. **Tipo de contenido:** Selecciona **Películas** (Movies). Esto le indica a Jellyfin qué bases de datos de metadatos (como TheMovieDb o OMDb) debe consultar para identificar correctamente los archivos.
2. **Nombre visible:** Escribe un nombre amigable para la interfaz de usuario (ej. `"Películas VPS"`).

### Paso 4: Selección de la ruta del contenedor (¡Crítico!)
1. Junto al campo **Carpetas**, haz clic en el botón `+`.
2. En el cuadro de diálogo, debes introducir **la ruta del contenedor**, NO la ruta física del host. Escribe o navega hasta:
   `/media/peliculas`
3. Haz clic en **Aceptar** para confirmar la selección.

> 💡 **Nota Importante:** Si introduces `/home/vilber/media/peliculas`, Jellyfin fallará al intentar escanearla, ya que el contenedor de Docker está aislado del host y no puede ver rutas directas del host fuera de sus volúmenes configurados.

### Paso 5: Personalización y Configuración de Metadatos
Para asegurar una biblioteca limpia y en español, ajusta las siguientes opciones dentro de la misma pantalla de creación:
* **Idioma preferido para metadatos:** Selecciona `Spanish; Castilian` (Español).
* **País/Región preferida:** Selecciona `Spain` (o tu país correspondiente).
* **Descarga de imágenes:** Deja activos los proveedores de imágenes por defecto (TheMovieDb, Fanart.tv) para obtener carteles, fondos (fanarts) y logotipos de alta calidad.
* **Guardar metadatos en formato NFO:** (Opcional) Activar la escritura de archivos `.nfo` en la carpeta de la película es una excelente práctica para salvaguardar los metadatos localmente por si la biblioteca debe ser reconstruida en el futuro.

### Paso 6: Confirmar y Escanear
1. Desplázate hasta el final de la página y haz clic en **Aceptar** (Ok).
2. Jellyfin iniciará un escaneo inicial en segundo plano. Analizará los archivos de vídeo que subiste mediante WinSCP, extraerá las pistas de audio/subtítulos y descargará automáticamente las carátulas, sinopsis, reparto y calificaciones.
3. Puedes monitorizar el progreso del escaneo en la pestaña **Inicio** del panel de control o regresando a la biblioteca en la pantalla de inicio del reproductor.

---

## 5. Métodos Alternativos para Administradores de Sistemas

Si bien WinSCP es excelente para entornos de escritorio gráficos, como administradores de sistemas en el VPS contamos con otras opciones potentes para transferir archivos grandes:

### A. Sincronización robusta con `rsync` (Consola de comandos)
Si trabajas desde una terminal en Linux o macOS local, `rsync` es el estándar de oro para subidas con posibilidad de reanudación automática de archivos interrumpidos:
```bash
rsync -P --resume-only /ruta/local/pelicula.mkv vilber@144.91.108.254:/home/vilber/media/peliculas/
```

### B. Descarga directa en el VPS con `wget` o `aria2`
Si las películas se encuentran en un servidor remoto de internet y dispones del enlace de descarga directo, es ineficiente descargarlas en local para luego subirlas al VPS. En su lugar, conéctate por SSH al VPS y descárgalas directamente en la carpeta de Jellyfin:
```bash
cd /home/vilber/media/peliculas/
wget -c "https://enlace-directo-pelicula.com/video.mp4"
```
*(El flag `-c` asegura que si la descarga se interrumpe, se pueda reanudar ejecutando el mismo comando)*.

---

## 6. Conclusión y Lecciones Aprendidas

1. **Protocolos específicos para tareas específicas:** La interfaz web (HTTP) de Hermes es ideal para archivos de configuración, scripts y depuración de código de tamaño moderado, pero debe evitarse para el almacenamiento masivo.
2. **Aislamiento en Docker:** Es crucial entender la separación entre el host de almacenamiento y la vista virtualizada de Jellyfin, asegurándonos de que al configurar carpetas siempre seleccionemos las rutas internas del contenedor (`/media/...`).
3. **Automatización:** WinSCP ofrece una excelente interfaz para mantener la biblioteca sincronizada cómodamente desde el ordenador local, minimizando la intervención en la terminal del VPS.

---
_Este informe ha sido redactado de forma autónoma tras resolver la incidencia técnica con la transferencia de archivos de gran tamaño en Jellyfin y documentar la solución para el Wiki Superbrain._
