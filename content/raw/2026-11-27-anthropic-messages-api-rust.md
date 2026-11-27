---
title: "Anthropic reescribe la Messages API en Rust: 70% menos CPU, 80% menos memoria y la verificación como nuevo cuello de botella"
source: "Anthropic Research / explainx.ai / MLQ.ai / AI Weekly / Unusual Whales"
date: 2026-11-25
captured: 2026-11-27T20:10:00+01:00
---

# Anthropic reescribe la Messages API en Rust

URL: https://www.anthropic.com/research/migrating-api-to-rust
URL: https://explainx.ai/blog/anthropic-messages-api-rust-shadowing-claude-agents-november-2026
URL: https://mlq.ai/news/anthropic-rewrites-claudes-api-in-rust-cutting-cpu-per-request-70
URL: https://aiweekly.co/alerts/anthropic-rust-rewrite-cuts-messages-api-cpu-70-memory-80

## Cifras de cabecera

Anthropic publicó el 25 de noviembre de 2026 cómo movió la **Messages API** —«la forma principal en que los clientes, así como nuestras propias aplicaciones como Claude Code y Cowork, llegan a Claude»— de Python a Rust sin ventana de mantenimiento. La compañía afirma que el servicio Rust en producción usa **alrededor de un 70% menos de CPU por petición**, **más de un 80% menos de memoria por petición** y recorta la **mediana de tiempo hasta el primer token en torno a un 20%** en las peticiones de Claude Code registradas en los gráficos. El tráfico público se movió al servicio Rust en **septiembre de 2026**.

La API Python data de 2023, cuando un ingeniero temprano la llamó «básicamente un reenviador de peticiones». Desde entonces creció hasta validar peticiones, construir prompts, tokenizar, ejecutar clasificadores de seguridad y parsear salida en streaming, mientras el tráfico de la API creció **unas 1.800 veces** desde principios de 2024 hasta el otoño de 2026.

## El intento parcial que no valió la pena

Una reescritura parcial anterior, en marzo de 2026, movió solo el parseo de respuestas a Rust y recortó la CPU **entre un 8% y un 10%**, un ahorro que el equipo juzgó no merecía la complejidad añadida: cada respuesta cruzaba la frontera de lenguaje **tres veces**. Para la reescritura completa, «Claude escribió una primera versión de la ruta de petición central de la API en aproximadamente una semana».

Probar que coincidía llevó meses: unos **700 tests de integración** existentes estaban atados al código Python, una auditoría encontró **más de 100 aserciones debilitadas** en los tests portados, y unas 20 opciones binarias producen más de un millón de combinaciones. En abril, **el 98% de los tests pasaba**, pero solo **una cuarta parte de las entradas de producción coincidía**.

## Shadow traffic cuando los tests no pueden definir «correcto»

Anthropic enumera tres fuentes de corrección: reglas fijas (como un asistente de pruebas), ejemplos (suites de tests), o **el sistema de producción existente como oráculo**. La Messages API seguía enviando nuevos modelos y funciones, así que el oráculo se movía.

**Shadowing** significa ejecutar peticiones reales por el código viejo y el nuevo y comparar resultados estructurados. Para Claude aparecen dos bloqueadores de inmediato:

1. **Facturación y límites de tasa** — no se puede ejecutar el modelo dos veces por petición de cliente.
2. **No determinismo** — prompts idénticos pueden producir textos distintos, así que herramientas de diff ingenuas tratarían la creatividad del modelo como errores de API.

La solución de Anthropic: **ejecutar el modelo una vez** y luego **reproducir su salida** por Python y Rust en la ruta de la API. El equipo comparó **cada etapa antes y después** de la llamada al modelo para que un bug sutil de prompt no se escondiera dentro de una respuesta todavía plausible.

### Diffs que preservan la privacidad

Como Anthropic no leería los prompts ni las respuestas de los clientes para este flujo, registró **formas** de las diferencias —nombres de paso, índices de piezas del prompt, desplazamientos de bytes, longitudes—, no texto crudo. El **checkpointing** encontraba la primera etapa del pipeline donde Python y Rust divergían. Las **huellas (fingerprints)** combinaban paso, pieza, desplazamiento y delta de longitud, de modo que una clase de bug producía la misma firma a través de miles de peticiones. Esos registros alimentaban a los agentes Claude sin exponer contenido del usuario.

## Bucles de verificación: interno, externo y de memoria

Anthropic describe tres bucles anidados:

- **Bucle interno (segundos):** los agentes trabajan en sandboxes en la nube con ambos códigos. Las comprobaciones locales construyen prompts o reproducen respuestas de modelo guionizadas en **menos de un segundo** sin llamar a Claude. Un agente conjetura una causa raíz a partir de una huella, escribe una petición que la reproduce, edita Rust hasta que las salidas coinciden y añade un test que falla en el código viejo.
- **Bucle externo (horas a días):** tras la revisión humana de pull requests, los arreglos se despliegan a staging y producción. El **shadow traffic** rastrea si cada huella desaparece en las nuevas compilaciones. Cuando los arreglos de sandbox pasan pero el shadowing de producción sigue mostrando la firma, el trabajo vuelve al bucle interno.
- **Bucle de memoria (reglas que persisten):** cuando los ingenieros rechazan un atajo —el ejemplo de Anthropic es **codificar a fuego la descripción de una herramienta de búsqueda web** en lugar de llamar al servicio interno en vivo—, la decisión se convierte en una **regla que todo agente posterior lee**, una búsqueda en el repo del mismo error y, a menudo, un lint o test. Los comentarios de revisión también se destilaron en guías **CLAUDE.md** y puertas de merge que exigían que los cambios en Python se reflejaran en Rust.

Bugs que el sistema capturó: un límite de contexto de 1M de tokens leído como 200K y una descripción de herramienta ausente. La proporción de entradas coincidentes pasó de **alrededor del 24% a finales de abril al 99,6% en agosto**.

Los agentes Claude hicieron gran parte del arreglo: un agente orquestador agrupaba los registros de desajuste cada 10-30 minutos y asignaba trabajadores, que escribían una petición que reproducía el fallo, editaban el código hasta que ambas versiones coincidían y añadían un test, con merges condicionados a revisión humana de pull request. Los ingenieros aún rechazaron algunos atajos de agentes que pasaban las comprobaciones. «La verificación es el nuevo cuello de botella», escriben los autores.

## Lo que se envió

Anthropic grafica tres métricas de producción mientras el tráfico pasaba de Python (gris) a Rust (azul) entre agosto y octubre de 2026:

- **CPU por petición** — alrededor de **70% de reducción** en la región medida.
- **Memoria por petición** — **más del 80% de reducción** en la ventana graficada.
- **Mediana de tiempo hasta el primer token** — alrededor de **20% de reducción** en las peticiones de Claude Code.

Esas cifras superan el rango del **40-50% de CPU** que se había filtrado antes de la nota de ingeniería. Miden **orquestación de API**, no inferencia en GPU: la factura de Claude la dominan los tokens, pero el coste de servicio por token de Anthropic bajó en el lado de la CPU. Por **mayo de 2026**, más del **80% del código mergeado** en el proyecto lo escribió Claude.

## Lecciones para equipos que planean reescrituras asistidas por IA

1. **La verificación es el nuevo cuello de botella** cuando Claude u otros agentes escriben la mayoría de las líneas.
2. **Diseñar la señal del verificador deliberadamente** — checkpoints y huellas superan a un único bit de pasa/falla.
3. **Mantener los bucles simples** — los agentes eligen hipótesis; los verificadores juzgan resultados; los humanos deciden el producto.
4. **Mover a los humanos hacia los bucles externos** conforme sube la confianza — de depurar a mano a escribir reglas y arquitectura.
