---
title: "Proof lanza su MCP en ChatGPT con x401: identidad verificada y autorización firmada para agentes"
source: "https://www.globenewswire.com/news-release/2026/11/18/3405765/0/en/proof-launches-its-mcp-in-chatgpt-starting-with-x401-so-ai-agents-can-prove-who-they-act-for-and-what-that-person-approved.html"
date: 2026-11-18
captured: 2026-11-18
---

# Proof MCP en ChatGPT y el protocolo x401 (Proof, 18 de noviembre de 2026)

## Qué cambió

Proof, la empresa de autorización de identidad, lanzó el 18 de noviembre de 2026 la primera versión del **Proof MCP**, su servidor de Model Context Protocol para asistentes de IA, disponible ya dentro de ChatGPT. El primer flujo que expone ese MCP es **x401**, de modo que cualquier persona que use ChatGPT puede añadir la app de Proof y dejar que el asistente lleve su identidad verificada al trabajo que realiza.

Cuando ChatGPT llega a un sitio web o servicio que pregunta quién autorizó una petición, la persona revisa los detalles, aprueba con biometría, y el negocio verifica la firma por sí mismo.

## Cronología

- **15 de octubre de 2026:** Proof lanza x401, el protocolo abierto que permite a cualquier sitio web o API pedirle a un agente de IA evidencia de la persona que está detrás, más la cartera de identidad que responde a esa petición. Se anunció en producción con soporte para _dots_, y los desarrolladores podían conectar el servidor MCP de Proof a ChatGPT mediante configuración manual.
- **18 de noviembre de 2026:** el Proof MCP, y con él x401, pasa a estar disponible para los usuarios de ChatGPT directamente desde dentro del producto, sin configuración manual del lado del usuario.

## El problema: el hueco probatorio del agente (Agent Evidentiary Gap)

Los agentes de IA ya pueden comprar, firmar y enviar dinero en nombre de una persona. El problema para los negocios del otro lado es que **la llegada de un agente prueba muy poco**. Una contraseña, un token OAuth, una clave de API o una tarjeta almacenada demuestran que el agente _tiene acceso_. Ninguno demuestra que **una persona real aprobó esa acción concreta**. Proof llama a esto el _Agent Evidentiary Gap_ («hueco probatorio del agente»), y es la razón por la que servicios que van desde minoristas hasta bancos han estado **bloqueando** agentes en lugar de admitirlos.

## Cómo funciona x401

x401 extiende el **HTTP 401**, la respuesta estándar «unauthorized» de la web. Cierra el hueco permitiendo que un sitio declare exactamente qué evidencia debe aportar un agente antes de proceder:

- El agente transporta la petición; la persona detrás de él **firma** la petición.
- Una clave protegida por hardware vincula su identidad legal verificada a los términos exactos de la operación.
- El negocio puede verificar el resultado **por sí mismo y offline**.
- Si se cambia un solo término, **la firma falla**.

El Proof MCP hace que ese intercambio esté disponible en cualquier conversación de ChatGPT, sin que el negocio tenga que integrarse con ChatGPT.

## Alcance para cada lado de la transacción

- **Personas:** añaden la app de Proof desde el directorio de apps de ChatGPT y se autentican una vez. A partir de ahí, ChatGPT puede presentar su identidad verificada cuando un sitio o servicio la pida, y **toda acción consecuente vuelve a la persona para su aprobación**.
- **Negocios que hablan x401:** pueden esperar que los usuarios de ChatGPT lleguen con una respuesta verificable a «¿quién te envía y dijo que sí?». El negocio verifica la respuesta firmada por sí mismo.
- **Desarrolladores:** conservan el mismo protocolo, especificación y servidor MCP publicados el 15 de octubre. Nada de lo que construyeron cambia; su _challenge_ x401 simplemente alcanza a los usuarios de ChatGPT sin configuración por parte del usuario.

## Disponibilidad

- El Proof MCP está disponible ya como conector en el directorio de apps de ChatGPT.
- Los consumidores pueden configurar su credencial Proof en proof.com/digital-credential.
- Los desarrolladores pueden añadir x401 a cualquier sitio o API usando la especificación, el esquema de identidad y la implementación de referencia en proof.com/x401.
- Las organizaciones que necesitan mayor garantía, evidencia de autorización firmada o emisión de credenciales pueden contactar a Proof.

## Implicación

x401 convierte la pregunta «¿tiene el agente permiso?» en «¿qué persona autorizó exactamente esto, y lo firmó?». Es un movimiento desde la autenticación de transporte (tokens, claves) hacia la **atestación de intención humana**, y llega al asistente más usado del mundo como un conector de un clic. Para los negocios que hoy bloquean agentes por miedo al fraude, es la primera vía práctica para admitirlos con evidencia verificable.
