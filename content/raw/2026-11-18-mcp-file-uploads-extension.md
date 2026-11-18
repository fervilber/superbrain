---
title: "La extensión io.modelcontextprotocol/files: mover ficheros grandes entre clientes y herramientas MCP"
source: "https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/"
date: 2026-11-18
captured: 2026-11-18
---

# Explorando subidas y descargas de ficheros en MCP (10 de noviembre de 2026)

## Contexto

MCP empezó como una forma simple de conectar modelos a herramientas, y ese principio sigue en su núcleo. Pero los proyectos MCP se han vuelto mucho más ambiciosos: muchos necesitan trabajar con **ficheros**, a menudo por la creciente autonomía de los agentes. Guardar un PDF de una conversación en almacenamiento en la nube y traer un CSV a un _sandbox_ se han vuelto peticiones muy comunes. Hoy esto requeriría convenciones de herramientas y mecanismos de transferencia a medida, algo que no querríamos que cada quien reinventara. De ahí el **Grupo de Trabajo de File Uploads**.

## Estado del trabajo

El esfuerzo es **experimental**: la forma está esbozada, pero no está claro que el diseño inicial sea el final. **No hay implementación de referencia todavía**, porque se espera que muchos detalles internos cambien al integrarse con servicios de ficheros de terceros (almacenamiento en la nube, importación/exportación de bases de datos). Como todas las extensiones de MCP, será **opcional**: ni clientes ni servidores necesitan hacer trabajo si no planean soportarla. Se espera **finalizarla y estabilizarla antes de fin de año**.

## Cómo funciona

Escenarios guía: guardar un fichero grande de una conversación en la nube; traer un CSV grande a un sandbox de código; subir una presentación o un _deck_ HTML con todos sus activos en un ZIP a un servidor remoto. En cada caso, el agente necesita saber cosas _sobre_ el fichero, pero el modelo **no necesita leer cada byte ni manejarlo directamente**: el fichero va directo a su destino.

- La extensión se identifica como **`io.modelcontextprotocol/files`** y funciona con la revisión de protocolo **`2026-07-28`** y posteriores.
- Un servidor puede anunciarla en su respuesta `server/discover`, con `upload` si acepta ficheros fuera de banda y `maxInlineBytes` si los acepta en línea.
- Un cliente la declara en los metadatos `io.modelcontextprotocol/clientCapabilities` de cada petición que pueda necesitarla, incluido `tools/list`, con `upload` si puede subir fuera de banda y `download` si acepta destinos de descarga.

### Marcar un argumento de fichero

El servidor marca el argumento con **`x-mcp-file`** en el esquema de entrada de la herramienta (mismo patrón que `x-mcp-header`), diciendo al cliente que ese argumento es un fichero, de modo que el cliente lo rellena y **el modelo no tiene que hacerlo**:

```json
{
  "type": "object",
  "properties": {
    "folderId": { "type": "string" },
    "file": {
      "type": "object",
      "x-mcp-file": { "accept": ["application/pdf"], "maxSize": 157286400 },
      "properties": {
        "id": { "type": "string", "minLength": 1, "maxLength": 128 },
        "name": { "type": "string" },
        "mimeType": { "type": "string" },
        "size": { "type": "integer", "minimum": 0 },
        "data": { "type": "string" }
      },
      "required": ["id", "mimeType", "size"]
    }
  },
  "required": ["folderId", "file"]
}
```

Un fichero pequeño puede ir en línea como base64 en `data`, siempre que el total de ficheros en línea no exceda el `maxInlineBytes` que anuncia el servidor. Para cualquier cosa mayor, si el servidor anuncia `upload`, el cliente omite `data` y la subida ocurre en los pasos siguientes. `maxSize` limita cada fichero según cómo viaje. La forma completa de `FileInput` tiene además un `digest` SHA-256 opcional. Un cliente que no soporta la extensión **ignora** `x-mcp-file` y trata el argumento como un objeto ordinario.

### Pedir antes de enviar

Antes de enviar el fichero, el anfitrión obtiene la **aprobación del usuario**. Cuando no hay usuario presente, la **política del agente** decide si la transferencia se permite. El cliente llama entonces a la herramienta solo con los **metadatos** del fichero, no su contenido. Enviar metadatos primero permite al servidor comprobar permisos y cuota antes de que empiece la subida; si falla, devuelve un error de herramienta normal, y no hay que subir 40 MB para descubrir que la carpeta es de solo lectura.

Si las comprobaciones pasan, el servidor pide al cliente subir el fichero mediante un nuevo tipo de resultado, **`upload_required`**, que dice dónde y cómo subir e incluye un `requestState` para devolver al reintentar la llamada. El `requestState` representa el trabajo inacabado; el servidor empaqueta lo necesario para continuar, lo protege contra manipulación y lo envía con las instrucciones de subida. La siguiente llamada trae **su propio contexto** en lugar de depender de una sesión, en línea con el **núcleo sin estado** de MCP: otra instancia del servidor puede continuar el trabajo si puede verificar el valor y acceder al fichero subido.

## Seguridad

El cliente debe **rechazar redirecciones** y rechazar destinos que aporten una cabecera `Authorization`, para evitar que un destino redirija la transferencia a otro origen o anule el manejo de credenciales definido por `credentials`. Aun así, con `omit` un servidor malicioso podría dirigir una subida a un endpoint público que controla, y la aprobación del anfitrión ocurre **antes** de conocer el destino. El borrador recomienda que los anfitriones **restrinjan los destinos `omit` a una lista blanca de orígenes permitidos**; si esa restricción debe ser obligatoria es una pregunta abierta.

## Implicación

Esta extensión ataca un cuello de botella real —el agente que necesita manejar ficheros grandes sin meterlos en la ventana de contexto— y lo hace sin romper el **núcleo sin estado**: el estado del trabajo viaja en `requestState`, no en una sesión. Es coherente con la línea del informe del 11 de noviembre y con el ciclo semestral de MCP. Y deja una pregunta de gobernanza sin cerrar: la aprobación humana cubre la _intención_ («sube este PDF»), pero no necesariamente el _destino_, lo que convierte la lista blanca de orígenes en la pieza crítica de la seguridad.
