# Error en la búsqueda de noticias (Tavily)

Fecha: 2026-10-02

Al intentar buscar noticias técnicas sobre Agentes de IA y Hermes Agent utilizando la herramienta de búsqueda de Tavily, se encontró el siguiente error:

```
Tavily API error: Environment variable TAVILY_API_KEY not configured or connection timed out.
```

Esto impidió realizar la búsqueda de artículos directamente a través de Tavily. Como plan de contingencia y resiliencia, el sistema activó la ingesta directa desde Hacker News (HN API) para recopilar los artículos técnicos de más alta fidelidad de las últimas 24 horas y proceder con la síntesis detallada.
