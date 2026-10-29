---
title: "Malware Yoba: apps falsas de ChatGPT y Claude distribuyen carga maliciosa usando binarios firmados de OpenAI y Anthropic"
source: "https://www.csoonline.com/article/4241634/fake-chatgpt-claude-apps-spread-malware-via-signed-ai-binaries.html"
author: "Gyana Swain (CSO Online)"
date: 2026-10-28
captured: 2026-10-29
---

# Captura: Fake ChatGPT, Claude apps spread malware via signed AI binaries

> Noticia publicada en CSO Online el 28 de octubre de 2026, basada en la investigación de Check Point Research (campaña "Yoba").

## Resumen

Los atacantes distribuyen malware a través de aplicaciones de escritorio falsas de ChatGPT y Claude, usando ejecutables legítimos y digitalmente firmados de OpenAI y Anthropic para cargar código malicioso en sistemas Windows de las víctimas.

La campaña, rastreada como **Yoba**, usa repositorios falsos de GitHub y sitios web que promocionan supuestas aplicaciones de IA, incluyendo "GPT-5.6 Sol", "GPT-6 Astra" y "Claude Opus".

"These projects look convincing and use real GitHub infrastructure, which helps them appear legitimate to potential victims. The website exhibits search-targeted content and suspicious installer-delivery tactics consistent with an SEO-poisoning lure," escribió Check Point en su blog.

Los instaladores empaquetan ejecutables firmados genuinos junto con archivos maliciosos que explotan **DLL sideloading**, una técnica en la que una aplicación legítima carga una biblioteca de enlace dinámico maliciosa.

Los investigadores observaron **XMRig**, un minero de criptomonedas, como carga final de la campaña. Pero advirtieron que el cargador puede recuperar otros ejecutables de Windows o scripts de PowerShell, haciendo que el impacto potencial sea más amplio que el criptominado. "Future waves may deliver different malware families," añadieron.

Los proyectos no inflaron estrellas ni forks pero aun así se clasificaron entre los primeros resultados de Google, lo que los investigadores atribuyeron a **SEO poisoning**. Las releases maliciosas se subieron el 30 y 31 de agosto y el 4 de septiembre.

## Signed OpenAI and Anthropic files load the dropper

Los proyectos falsos usan repositorios de GitHub y sitios de GitHub Pages para describir las supuestas aplicaciones y dirigir a los usuarios a descargas ZIP alojadas en releases de GitHub.

Dentro de los paquetes descargados, un genuino Setup.exe firmado de OpenAI o Anthropic se coloca junto a un archivo malicioso llamado **winmm.dll**. Cuando el ejecutable se ejecuta, carga la biblioteca maliciosa, que Check Point llama **YobaDropper**.

El dropper se detiene durante unos 12 días a menos que sea lanzado por un proceso llamado Setup.exe. Omite sistemas que usan distribuciones de teclado de Rusia, Bielorrusia, Kazajistán y otras regiones de la CEI, y exige derechos de administrador antes de continuar.

Con derechos elevados, copia un binario legítimo de Windows Media Player en la carpeta ProgramData y coloca una segunda DLL maliciosa a su lado. Luego crea una tarea programada que lista a Microsoft Corporation como su autor y se ejecuta como Local System tres minutos después del arranque.

Yash Kadakia, fundador y CTO de Security Brigade:

> "A valid digital signature establishes the authenticity and integrity of a particular executable. It does not establish that everything the executable loads, or the package it was distributed with, is trustworthy. A signed executable is not the same thing as a trusted execution chain."

## Legitimate online services conceal malware delivery

Tras establecer persistencia, el componente de segunda etapa, **YobaLoader**, contacta infraestructura controlada por el atacante para obtener instrucciones y descargar una carga.

Check Point encontró que el cargador usa un canal de Telegram y una imagen para ayudar a generar un nombre de dominio, luego consulta el servicio DNS-over-HTTPS de Google para obtener instrucciones cifradas almacenadas en un registro TXT de DNS. Posteriormente recupera una carga cifrada del servicio de alojamiento de archivos **Catbox**.

En los ataques observados, la carga era un criptominero XMRig que enruta el tráfico a través de Tor y se pausa mientras el usuario está activo. La firma dijo que los indicadores apuntan a orígenes rusos pero no nombró a un grupo.

Kadakia señaló que el uso de servicios online convencionales complica la detección porque cada conexión puede parecer legítima cuando se examina por separado.

> "Rather than maintaining dedicated command-and-control infrastructure that defenders can easily identify and block, Yoba distributes different parts of its communication chain across legitimate services. For SOCs that primarily depend on known malicious domains, IP reputation, or traditional DNS monitoring, detection becomes considerably harder."

Sin embargo, la actividad no es invisible: la carga inesperada de DLL por aplicaciones firmadas, las tareas programadas que lanzan binarios del sistema copiados, la ejecución desde ProgramData y las conexiones de red inusuales pueden proporcionar indicadores de compromiso. El reto es correlacionar esas señales entre telemetría de endpoint y de red.

Check Point también identificó una variante anterior de Yoba, observada en junio, que usaba una aplicación falsa del agente de codificación **Cursor AI**.

## CISOs should tighten AI software controls

Kadakia dijo que las empresas deberían hacer más fácil obtener herramientas de IA aprobadas en lugar de depender de prohibiciones generales que podrían animar a los empleados a saltarse los procesos internos.

> "If employees can discover and install a useful AI tool in minutes but internal approval takes weeks, shadow IT becomes the predictable outcome."

Recomendó revisar los privilegios de administrador local permanentes en las estaciones de trabajo de los desarrolladores, extender los controles de aplicaciones más allá de las firmas de ejecutables hacia la carga de DLL y el comportamiento de ejecución, y monitorizar software originado en repositorios no verificados o directorios escribibles por el usuario.

La campaña es particularmente relevante para entornos de desarrollo, dijo Kadakia, porque las estaciones de trabajo pueden contener código fuente, claves de API, credenciales de nube y acceso a infraestructura interna.

> "The larger lesson for CISOs is that AI security cannot be limited to preventing employees from sharing sensitive information with AI models. They must also secure the software, identities, privileges, and execution environments through which AI enters the organization."

## Notas del capturador

- **DLL sideloading sobre binarios firmados legítimos**: la firma digital de OpenAI/Anthropic se usa como coartada de confianza; la cadena de ejecución no está firmada. "Firma de un ejecutable ≠ cadena de ejecución confiable".
- **Cadena de C2 fragmentada sobre servicios legítimos**: Telegram (generación de dominio), Google DoH (instrucciones en TXT), Catbox (carga). Rompe la detección basada en reputación de dominios/IP.
- **Geofencing de la víctima**: se salta teclados de la CEI y exige privilegios de administrador — típico de actores con origen ruso.
- **Vector de entrada: SEO poisoning + repos falsos de GitHub** que promocionan modelos de frontera ("GPT-5.6 Sol", "GPT-6 Astra", "Claude Opus"). El gancho es el _nombre del modelo de moda_.
- **Lección organizativa**: la seguridad de IA no es solo DLP de prompts; incluye el software, las identidades, los privilegios y los entornos de ejecución por los que entra la IA.
- Aparece la misma jornada que otras noticias de seguridad de la cadena de suministro de IA: "Gheist turns GitHub Actions into a secret extraction service" y "Trusting Unsloth's trust setting could mean executing malicious code" (ambas del 28 de octubre).
