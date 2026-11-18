---
title: "MCP servers v2.5.0: ocho vulnerabilidades corregidas en tres servidores de referencia"
source: "https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0"
date: 2026-11-18
captured: 2026-11-18
---

# modelcontextprotocol/servers v2.5.0 (18 de noviembre de 2026)

## Qué cambió

La release **v2.5.0** del repositorio de servidores de referencia de MCP corrige **ocho vulnerabilidades en tres servidores**. Hay que actualizar `mcp-server-git` a 2026.11.18, `@modelcontextprotocol/server-filesystem` a 2.4.0 y `@modelcontextprotocol/server-everything` a 2.3.1.

| Paquete                                   | Afectado                                                                      | Corregido en |
| ----------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| `mcp-server-git`                          | hasta 2026.11.11                                                              | 2026.11.18   |
| `@modelcontextprotocol/server-filesystem` | todas las versiones antes de 2.4.0, y versiones por fecha 2025.1.14–2026.8.31 | 2.4.0        |
| `@modelcontextprotocol/server-everything` | hasta 2.3.0                                                                   | 2.3.1        |

## `mcp-server-git` 2026.11.18 (cinco correcciones)

- **Un merge ya no arranca el mantenimiento automático de Git.** Un `git_merge` exitoso, incluido un _fast-forward_, terminaba en `git maintenance run --auto`, cuya recolección de basura ejecuta los comandos que nombra el propio `gc.recentObjectsHook` del repositorio, **con los privilegios del servidor**. Ahora `maintenance.auto` es `false` y `gc.auto` es `0` en cada comando Git que corre el servidor (GHSA-h2g3-rwxm-xfm3).
- **Git nunca descarga por sí solo un objeto ausente.** La configuración de un repositorio podía declarar un _promisor remote_ y nombrar el programa que Git ejecuta para traer de él (`remote.<name>.uploadpack`, `core.sshCommand`), que una herramienta de solo lectura arrancaba al necesitar un objeto ausente. Se desactiva la descarga perezosa (`GIT_NO_LAZY_FETCH=1`) y un Git demasiado antiguo para honrarlo **rechaza** un repositorio que declare un _promisor remote_ (GHSA-87qg-cmw8-jc5m).
- **Los drivers se releen tras una escritura en el árbol de trabajo.** La configuración puede incluir un fichero que un merge o checkout crea, de modo que un _filter_ o _merge driver_ podía aparecer después de que el servidor vaciara los que encontró, y ejecutarse durante el `git merge --abort` posterior a un conflicto. `git_checkout`, `git_merge` y ese abort releen ahora los drivers antes de cualquier otro comando Git. **La comprobación de confinamiento `--repository` todavía no se repite tras tal escritura** (issue #5599) (GHSA-9vjp-x34c-xg6v).
- **Un filtro o merge driver con nombre vacío también se vacía.** Git acepta `[filter ""]`, seleccionado por `filter=` en `.gitattributes`, y la lista del servidor lo omitía, de modo que su comando corría (GHSA-pm7p-vphh-2cg7).
- **Se rechazan entradas del índice que apuntan fuera del árbol de trabajo.** Con `--repository`, un `.git/index` manipulado que nombraba una ruta como `../outside/secret` hacía que `git_diff_unstaged` y `git_diff` devolvieran el contenido de ese fichero, y `git_status` informara de si existe. El índice se comprueba desde arriba antes de que cualquier herramienta lo lea, y la caché de no rastreados —que puede nombrar un directorio fuera del árbol— se desactiva (GHSA-r2q8-f657-4r56).
- **La configuración propia de un submódulo ya no ejecuta programas.** Con `diff.submodule=diff`, `git_diff` corría un diff anidado dentro de cada submódulo cambiado bajo el `diff.external` y los drivers de textconv propios del submódulo; `git_checkout` y `git_add` corrían Git dentro de un submódulo bajo su propia configuración. Ahora `diff.submodule` es `short`, se sobrescriben los drivers que define un submódulo extraído, y un Git anterior a 2.33 —que no pasaría las sobrescrituras a un submódulo— se rechaza para un repositorio con uno extraído (GHSA-8wv7-r664-7594).

## `@modelcontextprotocol/server-filesystem` 2.4.0

- **Los listados de directorio se quedan con el directorio que se comprobó** (Linux y macOS). `list_directory`, `list_directory_with_sizes`, `directory_tree` y `search_files` listan ahora el directorio _in place_ tras comprobarlo, de modo que un directorio intercambiado por un enlace simbólico entre la comprobación y el listado ya no puede devolver nombres de entradas fuera de los directorios permitidos. **En Windows un listado aún no está anclado** (issue #5600) (GHSA-rq2p-q7c4-6g27).

## `@modelcontextprotocol/server-everything` 2.3.1

- **`gzip-file-as-resource` trata una dirección NAT64 como la dirección IPv4 que transporta.** La guarda de direcciones privadas leía direcciones en `64:ff9b::/96` como públicas, de modo que en una red con pasarela NAT64 una URL podía alcanzar una dirección IPv4 privada a través de ella. Ahora se comprueba la dirección IPv4 incrustada (GHSA-38j4-j742-j7r3).

## Nota de actualización

Los servidores TypeScript pasaron de versiones por fecha (2025.x, 2026.x) a versiones semánticas en 1.0.0. Los gestores de paquetes clasifican 2.4.0 **por debajo** de cualquier 2025.x y 2026.x, así que no lo ofrecerán como actualización. Si estás en una versión por fecha de `@modelcontextprotocol/server-filesystem`, instala 2.4.0 explícitamente: `npm install @modelcontextprotocol/server-filesystem@2.4.0`.

## Implicación

Es una muestra concreta del patrón que el sector lleva semanas señalando: **los servidores MCP son superficie de ataque**. Aquí no hay fallos del protocolo, sino del _código_ de los servidores de referencia: la configuración del repositorio (hooks, drivers, filtros, _promisor remotes_, submódulos) se convierte en **ejecución arbitraria con los privilegios del servidor**. Cinco de las ocho correcciones están en `mcp-server-git`, lo que ilustra por qué un servidor MCP que toca Git debe tratarse como código privilegiado y auditable, no como una utilidad inocua.
