# Error en la búsqueda de noticias

Fecha: 2026-09-23

Al intentar buscar noticias técnicas sobre Agentes de IA y Hermes Agent utilizando la herramienta de búsqueda web, se encontró el siguiente error:

```
SEARXNG_URL is not set
```

Esto indica que el motor de búsqueda configurado (SearXng) no tiene la variable de entorno SEARXNG_URL establecida, lo que impide realizar búsquedas externas.

Como resultado, no se pudieron extraer artículos para la ingestión diaria.

Se recomienda verificar la configuración de la herramienta de búsqueda en el entorno de Hermes Agent.
