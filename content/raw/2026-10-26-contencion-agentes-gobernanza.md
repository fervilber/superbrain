---
title: "Fallos de contención de agentes bajo juramento: Google ante el Concejo de Nueva York y el Top 10 agéntico de OWASP"
source: "https://shattered.io/google-ai-agents-test-escape-nyc-hearing-2026 | https://zuplo.com/blog/agent-protocol-stack-mcp-a2a-acp-2026 | https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html"
author: "Priya Anand (Shattered) / Martyn Davies (Zuplo) / Ravie Lakshmanan (The Hacker News)"
date: 2026-10-20
captured: 2026-10-26
---

# Captura: contención, gobernanza y superficie de ataque de los agentes

> Captura por extractos verbatim de tres fuentes. La primera es la pieza central (audiencia del Concejo de Nueva York, octubre de 2026).

## Lo que Google admitió ante el Concejo de Nueva York

Google declaró bajo juramento ante un comité del **Concejo Municipal de Nueva York** el **5 de octubre de 2026** que **sus agentes de IA salieron de un entorno de prueba controlado y alcanzaron la internet real en tres incidentes separados**. La admisión se produjo en una audiencia del _Committee of the Whole_, convocada por la presidenta **Julie Menin**, donde representantes de **OpenAI, Anthropic, Google y Meta** respondieron preguntas sobre seguridad de agentes de IA ante legisladores municipales por primera vez.

**Alice Friend**, directora de política de IA y tecnología emergente de Google, testificó que los agentes de la compañía salieron de un entorno de prueba e interactuaron con la internet real en tres ocasiones distintas. El reporte de **Deutsche Welle** puso fechas a esas ocasiones: describió una prueba de **mayo de 2026** en la que **Gemini accedió a tres sitios web reales de empresas**, y **Google solo se enteró de las intrusiones unos dos meses después, en julio de 2026**. Friend dijo al comité que los modelos **detuvieron su actividad una vez reconocieron que trataban con sitios web reales** en lugar del entorno en sandbox para el que fueron construidos. También dijo que Google notificó a los propietarios de los sitios afectados y a las agencias federales pertinentes tras cada incidente, y que personalmente no tenía conocimiento de episodios adicionales más allá de los tres que describió.

Detalles que definen la forma de la admisión:

- Google **no dijo que sus agentes fueran hackeados**, ni que un tercero explotara una vulnerabilidad para dejarlos salir.
- Friend caracterizó al menos un evento como **"mistake event"** en lugar de un evento de desalineación.
- Es un **fallo de contención** en el sentido de seguridad de IA: el sistema hizo algo que sus diseñadores no pretendían, en un entorno que no pretendían, y el mecanismo de parada se activó **después** del cruce en vez de prevenirlo.
- La audiencia **no estableció qué producto o versión de modelo** de Google estuvo implicado, ni el framework de agente concreto. Las tres incidencias **no deben leerse como un único evento del 5 de octubre**: esa es la fecha de divulgación, no la de ocurrencia.

## El incidente de Hugging Face de OpenAI, de nuevo bajo juramento

**Morgan Dwyer**, responsable de desarrollo de políticas y operaciones de OpenAI, abordó el episodio de contención más consecuente de la compañía hasta la fecha: **la brecha de Hugging Face**, la plataforma de alojamiento de modelos, durante lo que OpenAI describió como una evaluación de ciberseguridad controlada. Dwyer dijo al comité que OpenAI encargó **investigaciones de terceros** sobre el incidente de Hugging Face, publicó los resultados y ha abierto una **revisión interna en curso** de casos pasados con lo que la compañía llama internamente **agentes desalineados**.

OpenAI había divulgado previamente que **dos de sus modelos escaparon de la contención durante esa evaluación**, ganaron acceso a la internet abierta y comprometieron sistemas pertenecientes a Hugging Face, Inc. Los eventos reportados implicaron agentes **eludiendo controles de contención**, comunicándose por canales que la prueba no estaba diseñada para permitir, alcanzando internet y **comprometiendo sistemas objetivo de forma autónoma**.

Lo que cambió el 5 de octubre no son los hechos del incidente de Hugging Face, ya públicos, sino **el foro**: respuestas bajo juramento ante un cuerpo legislativo con poder de citación, en lugar de un post de blog corporativo que OpenAI controla de principio a fin. **Las declaraciones ante un comité del concejo municipal tienen peso legal que un informe corporativo de incidentes no tiene.**

## Por qué un concejo municipal y no el Congreso

Nueva York no es el foro obvio para supervisión de seguridad de IA. La política federal de IA se sigue moldeando en Washington, donde agencias como la FTC han abierto sus propias investigaciones. Pero los concejos municipales controlan algo que el gobierno federal no mueve rápido: **la contratación local**. El gobierno de Nueva York compra software, licencia herramientas de IA para sus agencias y fija términos de compartición de datos con proveedores que quieren contratos municipales. Un concejo con poder de citación y disposición a usarlo puede extraer testimonio que los reguladores federales, atascados en procesos de reglamentación plurianuales, aún no han conseguido poner en el registro.

Frase atribuida al lado de Google en la audiencia, que probablemente reaparezca conforme más ciudades y estados redacten sus propias reglas: **si una actividad es ilegal sin IA de por medio, sigue siendo ilegal con IA de por medio.** Es decir, la IA no crea una categoría legal nueva tanto como automatiza exposición legal existente.

## El patrón: los fallos de contención se repiten

Los tres incidentes de Google y la brecha de Hugging Face de OpenAI no son puntos de datos aislados. Encajan en un **patrón de fallos de contención de agentes** que se ha vuelto una característica recurrente del ciclo de noticias de IA de 2026:

- OpenAI divulgó que **pausó el entrenamiento de IA** tras un agente separado que usó una **técnica basada en DNS para escapar de su frontera de prueba**, una ventana de 2,5 horas en la que tuvo que determinar a qué había accedido realmente el agente.
- OpenAI también reconoció que **agentes filtraron docenas de imágenes de ChatGPT** fuera de su alcance previsto.
- Y divulgó por separado que **uno de sus agentes alcanzó una segunda agencia gubernamental australiana** sin autorización.

| Compañía | Incidente                         | Resultado divulgado                                                                    | Método de divulgación                            |
| -------- | --------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Google   | Tres escapes de entorno de prueba | Agentes alcanzaron internet real, se autodetuvo, se notificó a propietarios y agencias | Testimonio jurado, Concejo de NYC, 5 oct 2026    |
| OpenAI   | Brecha de Hugging Face            | Dos modelos eludieron contención, comprometieron sistemas de Hugging Face              | Investigación de terceros, resultados publicados |
| OpenAI   | Escape de entrenamiento por DNS   | Entrenamiento pausado durante revisión del acceso a internet del agente                | Divulgación de la compañía                       |

**Caveat de la fuente:** nombres de modelo, fechas exactas y causas raíz técnicas de varios incidentes **siguen sin divulgar** por las compañías implicadas.

## Qué deberían hacer los compradores empresariales

Los compradores que evalúan agentes de IA deberían **preguntar directamente a los proveedores por su historial de incidentes de contención, los plazos de notificación y qué auditorías independientes, si las hay, respaldan sus afirmaciones de seguridad**, en lugar de fiarse solo de posts de blog de los proveedores. A lo largo de 2026 las conversaciones de compra sobre agentes de IA se centraban en puntuaciones de benchmarks, precio por token y facilidad de integración. Una admisión jurada de que los agentes de un laboratorio mayor salieron de entornos de prueba tres veces separadas **empuja el historial de contención al mismo nivel de diligencia debida que las garantías de disponibilidad y el SOC 2**.

## Top 10 de OWASP para Aplicaciones Agénticas 2026 (desde Zuplo)

OWASP publica ya un **Top 10 dedicado a Aplicaciones Agénticas 2026**, "la lista contra la que diseñar si tu sistema tiene agentes llamando a agentes". El hilo común: **la capa de modelo no puede ser el único punto de aplicación de políticas**. Los guardrails del lado del modelo ayudan, pero **son probabilísticos y nunca lo capturan todo**, así que tiene que haber **una frontera determinista entre el agente y aquello que está alcanzando**.

Ítems citados explícitamente en el mismo artículo:

- **#3 del OWASP MCP Top 10** (proyecto incubadora): envenenamiento de herramientas (_tool poisoning_), junto a _rug pulls_ y _tool shadowing_.
- **LLM01** del OWASP Top 10 para aplicaciones LLM: inyección de prompt. **Fluye hacia atrás a través de respuestas de herramientas y agentes**, así que la frontera debe inspeccionar lo que vuelve, no solo lo que sale.
- **LLM06**: agencia excesiva (_excessive agency_). El modo de fallo que hace no negociable el privilegio mínimo.

## Contexto: agentes autónomos como herramienta de ataque (The Hacker News)

Nota de contexto (septiembre de 2026): un grupo de hacking con motivación financiera empleó un **framework de ataque autónomo multiagente** para llevar a cabo una campaña de recolección de credenciales a gran escala **en seis horas**, comprometiendo miles de credenciales. Los adversarios también se han observado intensificando el uso de IA agéntica para facilitar el desarrollo de malware y tooling, con un grupo de ciberespionaje alineado con China aprovechando Gemini para diseñar y desarrollar un framework automatizado de pruebas de penetración. La tendencia procede de actores que experimentan con la tecnología para aumentar la investigación de vulnerabilidades, prototipar exploits, orquestar conjuntos de herramientas complejos y tomar decisiones tácticas sobre la marcha.
