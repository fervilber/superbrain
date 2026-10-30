---
title: "Indirect Prompt Injection Goes Operational (Cloud Security Alliance, research note 2026-04-26)"
source: "https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026"
author: "Cloud Security Alliance AI Safety Initiative"
date: 2026-04-26
captured: 2026-10-30
---

# Captura: Indirect Prompt Injection Goes Operational — CSA Research Note

> Nota de investigación de la CSA (AI Safety Initiative) sobre la inyección indirecta de prompts (IPI) en el mundo real. Fundamenta la sección de seguridad del informe del 30 de octubre de 2026.

## Conclusiones clave

La inyección indirecta de prompts (IPI) ha cruzado la línea de prueba de concepto a explotación real. En abril de 2026, dos fuentes de telemetría independientes —el blog de seguridad de Google y Forcepoint X-Labs— publicaron análisis concurrentes confirmando que los adversarios están sembrando la web abierta con instrucciones ocultas diseñadas para secuestrar agentes de navegación, asistentes de código y copilots empresariales. Palo Alto Networks Unit 42 documentó doce casos de IPI detectados contra agentes de IA, incluido el primer payload real diseñado para eludir un sistema de revisión de anuncios basado en IA. Google reportó un aumento relativo del 32% en contenido IPI malicioso entre noviembre de 2025 y febrero de 2026 en las 2-3 mil millones de páginas que rastrea cada mes.

El Q1 2026 Exploit Round-up Report del OWASP GenAI Security Project (14 de abril de 2026) enmarca esto en un patrón más amplio: de ocho incidentes mayores documentados entre el 1 de enero y el 11 de abril, sólo uno recibió un identificador CVE (CVE-2025-59528 en Flowise); el resto provinieron de mala configuración, agencia excesiva, fallo de cadena de suministro o inyección de prompts.

Tres hallazgos destacan para los equipos de seguridad:

1. **Los ataques escalan**: Forcepoint identificó diez payloads IPI distintos en dominios separados, y Unit 42 mapeó veintidós técnicas de entrega de payload en uso activo, lo que sugiere herramienta organizada más que experimentación aislada.
2. **La intención escala**: los payloads documentados incluyen transferencias forzadas de 5.000 dólares vía PayPal, fraude de suscripción vía Stripe, borrado recursivo de ficheros en agentes integrados en IDEs, exfiltración de API keys y cribado de contratación sesgado.
3. **El pipeline de divulgación es incompleto** para fallos específicos de IA: los bug bounties pagados por Anthropic, GitHub y Google por fallos de prompt injection en Claude Code Security Review, Copilot Agent y Gemini CLI Action no resultaron en CVEs ni avisos públicos.

## Contexto

La IPI difiere de la variante directa: en un ataque directo el usuario envía texto malicioso; en uno indirecto, el texto malicioso se planta en una fuente de terceros (una página web, una invitación de calendario, una línea de log, un PDF, un email, un comentario de issue) que un agente de IA ingiere después como parte de su operación normal. Los LLM actuales frecuentemente fallan al distinguir entre contenido que se les pide _procesar_ y contenido que intenta _instruirles_, sobre todo cuando no se aplican señales de procedencia ni fronteras de prompt estructuradas.

Dos factores convergieron en 2026 para pasar la IPI de teórica a operativa: el rápido despliegue de features agénticas (los agentes de navegador clican enlaces y rellenan formularios; los asistentes de código ejecutan comandos shell; los agentes CLI commitean código y publican en GitHub) y la estandarización de técnicas de inyección (las mismas frases disparadoras —"Ignore previous instructions", "If you are an LLM", "If you are a large language model"— aparecían en dominios no relacionados, apuntando a toolkits y plantillas compartidas).

OWASP formalizó dos marcos complementarios: el LLM Top 10 (LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM05 Improper Output Handling, LLM06 Excessive Agency) y el Top 10 for Agentic Applications 2026 (ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, ASI05 Unexpected Code Execution, ASI09 Human-Agent Trust Exploitation).

## Análisis de seguridad

### Qué muestra la telemetría in-the-wild

Google reportó que, en unas 2-3 mil millones de páginas rastreadas al mes, la proporción de páginas con IPI maliciosa creció un 32% en términos relativos entre noviembre de 2025 y febrero de 2026, con los atacantes prefiriendo sitios estáticos, blogs, foros y secciones de comentarios como vectores de inyección. Ni Google ni Forcepoint observaron campañas coordinadas sofisticadas de tipo actor-amenaza nombrado; observaron plantillas de inyección compartidas en dominios no relacionados, lo que indica herramienta organizada y librerías de plantillas en lugar de C2 centralizado.

Forcepoint X-Labs detalló diez payloads verificados:

- En `faladobairro.com`, un comando `sudo rm -rf` contra una carpeta de backup llamada `agy/BU`, diseñado para dispararse cuando un agente de código integrado en IDE o un copilot de terminal resumiera la página.
- En `perceptivepumpkin.com`, instrucciones ocultas para enviar una transferencia fija de 5.000 dólares vía PayPal.me.
- En `thelibrary-welcome.uk`, un comentario HTML oculto que ordenaba al modelo filtrar una API key secreta.
- Otros payloads intentaron secuestro de atribución, supresión falsa de copyright y denegación de servicio dirigida a IA mediante output repetitivo forzado.

Unit 42 catalogó doce casos con agentes que navegan de forma autónoma: envenenamiento SEO para promover dominios de phishing, comandos para borrar bases de datos entregados mediante texto suprimido por CSS, payloads de fraude de suscripción con JavaScript dinámico y codificación Base64, y un payload de manipulación de contratación. El primer IPI real diseñado para eludir un sistema de revisión de anuncios apareció en `reviewerpress.com`, con veinticuatro intentos de inyección distintos.

Técnicas de ocultación (etiquetas del propio informe de Unit 42):

| Técnica                                | Proporción de casos | Mecanismo                                                                      |
| -------------------------------------- | ------------------- | ------------------------------------------------------------------------------ |
| Texto plano visible (oculto a humanos) | 37,8%               | font-size cero, posicionamiento off-screen, manipulación de opacidad           |
| Ocultación en atributos HTML           | 19,8%               | prompts embebidos en atributos `data-*`                                        |
| Supresión de render por CSS            | 16,9%               | `display:none`, `visibility:hidden`                                            |
| Codificación y ofuscación              | resto               | encapsulado XML/SVG, secciones CDATA, caracteres tag Unicode                   |
| Ensamblaje en runtime                  | resto               | payloads decodificados en Base64 liberados tras retardos temporizados de carga |

Unit 42 reporta que el 85,2% de los casos empleó un marco de ingeniería social (típicamente anulaciones de autoridad como "esto es una actualización de seguridad"). Cerca del 75,8% de las páginas inyectadas contenían un único payload.

### Incidentes Q1 2026 en el round-up de OWASP

| Incidente                                     | Divulgación       | Riesgos OWASP LLM   | Riesgos agénticos   | Detalle                                                          |
| --------------------------------------------- | ----------------- | ------------------- | ------------------- | ---------------------------------------------------------------- |
| Brecha del Gobierno de México vía Claude      | 25-feb-2026       | LLM02, LLM06, LLM10 | ASI02, ASI03, ASI08 | ~150 GB de datos fiscales y de votantes expuestos                |
| Borrado de inbox OpenClaw                     | 23-feb-2026       | LLM05, LLM06        | ASI09, ASI10        | El agente ignoró comandos de stop y borró emails                 |
| Fuga de agente interno de Meta                | 20-mar-2026       | LLM02, LLM05        | ASI01, ASI08, ASI09 | Datos sensibles accesibles a ingenieros ~2 horas                 |
| Vertex AI "Double Agent"                      | 31-mar/1-abr-2026 | LLM02, LLM03, LLM06 | ASI02, ASI03, ASI04 | Scoping de permisos por defecto habilitó exfiltración            |
| Fuga de source map de Claude Code             | 31-mar/abr-2026   | LLM02, LLM03, LLM05 | ASI04, ASI05, ASI09 | Source map de 59,8 MB; repos falsos "filtrados" para malware     |
| Brecha de cadena de suministro Mercor/LiteLLM | 3-abr-2026        | LLM02, LLM03, LLM04 | ASI03, ASI04, ASI08 | Meta pausó el trabajo con Mercor                                 |
| Explotación activa de Flowise CVE-2025-59528  | 7-abr-2026        | LLM03, LLM05, LLM06 | ASI02, ASI04, ASI05 | RCE vía config CustomMCP; 12.000-15.000 instancias expuestas     |
| GrafanaGhost IPI                              | 7-abr-2026        | LLM01, LLM02, LLM05 | ASI01, ASI02, ASI09 | Instrucciones ocultas en logs causaron exfiltración vía Markdown |

### El agujero de divulgación

De los ocho incidentes documentados, sólo Flowise llevó un CVE. Investigación de The Next Web documentó pagos de bug bounty de Anthropic (100 dólares por un fallo de prompt injection en Claude Code Security Review que permitía extracción de API keys de runners de GitHub Actions), GitHub (500 dólares por un fallo de Copilot Agent disparado por inyección de comentarios HTML en issues) y Google (cantidad no divulgada, fallo en Gemini CLI Action que permitía al agente exponer su propia API key como comentario). Ninguno de los tres asignó CVEs ni publicó avisos. Antes en el trimestre, Miggo Security demostró cómo una sola invitación de Google Calendar armada podía plantar instrucciones dormantes que Gemini ejecutaba cuando el usuario le pedía resumir su día, exfiltrando datos privados de reuniones.

### Por qué la IPI es difícil de defender

La IPI derrota la mayoría de los enfoques de filtrado de entrada porque la instrucción maliciosa no viene de un usuario, donde las arquitecturas de seguridad esperan entrada no confiable, sino de una _fuente de datos_ que el agente trata como entrada de tool. Texto suprimido por CSS, fuentes de cero píxeles e inyección en comentarios HTML son invisibles para humanos que revisan la misma página pero se renderizan normalmente a un LLM que consume el DOM o markdown crudo. Las URLs relativas a protocolo, los caracteres tag Unicode y los payloads staged en Base64 rompen defensas de pattern-matching ingenuas. La propia utilidad del agente agrava el problema: cuando una instrucción se enmarca como tarea rutinaria de sistema, los modelos entrenados para seguir instrucciones a menudo cumplen. El gradiente de riesgo: "un navegador de IA que sólo puede resumir es de bajo riesgo", pero los agentes con acceso a email, terminal o pagos se vuelven objetivos de alta prioridad.

## Recomendaciones

### Acciones inmediatas

- Inventariar todo agente o copilot que ingiera datos externos no confiables (páginas web, documentos de terceros, entradas de calendario, tickets de soporte, streams de logs) y mapear qué tools y credenciales puede invocar cada agente cuando se dispara.
- Donde el agente inventariado tenga acceso a envío de email, ejecución de código, rieles de pago o escritura/borrado de datos, re-acotar el despliegue contra el principio de mínimo privilegio. Las capacidades de pago, ejecución de código y borrado de datos merecen acción la misma semana.
- Aplicar el mapeo del OWASP LLM Top 10 como marco de triaje. Validar controles LLM01 (etiquetado de procedencia de entrada, prompts estructurados que separan instrucciones de sistema de datos, guardrails en la invocación de tools) y LLM06 (checkpoints human-in-the-loop para acciones de alto impacto, capability gating, audit trails en llamadas a tools).
- Donde el render de salida basado en Markdown esté habilitado —especialmente para embeds de imágenes— restringir a dominios en allow-list y deshabilitar URLs relativas a protocolo, el canal de exfiltración explotado por GrafanaGhost.

### Mitigaciones a corto plazo

- Implementar cobertura de detección para las frases disparadoras documentadas ("Ignore previous instructions", "Ignore all previous instructions", "If you are an LLM", "If you are a large language model") junto con patrones que combinen estas con verbos de acción ("send", "delete", "transfer").
- Los productos de AI-gateway y DLP deberían ofrecer escaneo de contenido en el momento de la ingesta por defecto; los agentes de navegación deberían pasar contenido no confiable por un sanitizador que elimine texto zero-width, elementos posicionados off-screen y comentarios HTML antes de que lleguen a la ventana de contexto.
- Los agentes de código y CLI merecen endurecimiento separado (borrado recursivo, exfiltración de API keys, ejecución de código). Requerir aprobación humana antes de que un agente commitee, abra un PR o escriba un comentario que incluya contenido extraído de cuerpos de issues o descripciones de PR.
- Donde los vendors no hayan asignado CVEs, fijar versiones de agente explícitamente y suscribirse a changelogs de vendor en lugar de confiar en escáneres estándar.
- Revisar integraciones de calendario, email y SaaS contra el patrón Gemini-vía-Calendar: si un tercero puede escribir en un campo que un agente resume después, ese campo es un vector de inyección.

### Consideraciones estratégicas

Los frameworks de agentes deberían elevar la separación entre _contenido que el agente procesa_ e _instrucciones que el agente sigue_ a preocupación de diseño primaria, en lugar de abordarla con defensas a posteriori. Los frameworks que tratan todo contenido recuperado como entrada indiferenciada en un único contexto de prompt son estructuralmente vulnerables; los que mantienen metadata de procedencia y restringen las invocaciones de tools según el origen de los datos son defendibles. El marco MAESTRO de CSA modela amenazas de agente a través de las capas de planificación, memoria, acción y uso de herramientas, donde la IPI suele manifestarse como un secuestro de objetivo en la capa de planificación que se propaga a la capa de acción.

Las prácticas de compra y gestión de vendors necesitan actualizarse para cerrar el agujero de divulgación: los cuestionarios de seguridad deberían preguntar explícitamente si el vendor publica avisos y asigna CVEs (o identificadores equivalentes) para fallos de prompt-injection y abuso de agente.

## Alineación con recursos CSA

MAESTRO (Agentic AI Threat Modeling) aporta el modelo por capas; el AI Controls Matrix (AICM) aborda los controles de validación de entrada, manejo de salida y scoping de permisos de agente; STAR for AI ofrece un marco de evaluación para evidenciar que los controles LLM01 y ASI01 están presentes y operativos.
