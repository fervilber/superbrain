---
title: "The state of MCP security in 2026 (Microsoft Security Community Blog)"
source: "https://techcommunity.microsoft.com/blog/microsoft-security-blog/the-state-of-mcp-security-in-2026/4531327"
author: "Jitesh Thakur (Microsoft), co-autor Shalabh Pradhan"
date: 2026-06-26
captured: 2026-10-30
---

# Captura: The state of MCP security in 2026 (Microsoft)

> Checkpoint de Microsoft sobre el estado de la seguridad de MCP en 2026. Fundamenta la sección de seguridad/identidad del informe del 30 de octubre de 2026.

MCP es ahora la forma por defecto en que los agentes alcanzan herramientas y datos, y ese alcance es la superficie de ataque. El momento en que un modelo puede elegir y llamar tools, deja de ser una caja de preguntas y respuestas y se convierte en software que actúa. Todo lo que actúa tiene una frontera de confianza, y las descripciones de tools, esquemas, salidas y credenciales están dentro de ella.

Lo que ha cambiado es la escala: MCP pasó de idea prometedora a la forma en que los agentes se conectan a tools, datos y sistemas. Las empresas dejaron de experimentar y empezaron a enviar a producción.

### Una especificación que sigue moviéndose

MCP evoluciona rápido y la especificación se revisa con cadencia regular. El último release candidate eleva la línea base de seguridad: las peticiones ahora llevan lo que necesitan, así un gateway puede inspeccionar y aplicar política en cada llamada en lugar de confiar en una sesión oculta; las comprobaciones de identidad entre clientes y servidores son más estrictas; y una nueva capacidad MCP Apps permite a un servidor enviar UI interactiva que el host renderiza dentro de un sandbox. El protocolo deliberadamente no aplica la seguridad por ti: define cómo hablan clientes y servidores, y el resto es tu responsabilidad.

### Los riesgos principales en 2026

**1. Prompt injection y tool poisoning.** El agente trata todo lo que hay en su contexto como confiable: descripciones de tools, esquemas de parámetros y los datos que devuelven las tools. Quien pueda plantar instrucciones en cualquiera de esos puntos puede dirigir el agente. El tool poisoning es el filo afilado: instrucciones maliciosas ocultas en la descripción o esquema de una tool que el modelo lee y el usuario normalmente no. Controles: tratar descripciones y salidas de tools como entrada no confiable; inspeccionar el esquema completo antes de aprobar un servidor; poner la lista de tools en un paso de aprobación humana; mostrar la llamada completa en lugar de un resumen amigable; mantener servidores sensibles aislados de los de propósito general.

**2. Autorización y el "confused deputy".** Aquí es donde el protocolo se movió más. Los servidores MCP ahora se tratan como resource servers OAuth 2.0, y la guía se ha asentado en OAuth 2.1, PKCE y tokens ligados a una audiencia específica. El riesgo objetivo es el confused deputy: un servidor actuando con sus propios privilegios amplios en nombre de un usuario que no los tiene, o un proxy al que se puede engañar para que entregue a un atacante un código de autorización válido. Controles: adoptar el modelo actual —OAuth 2.1 con PKCE, consentimiento por cliente, coincidencia estricta de redirect-URI y tokens ligados a audiencia, de modo que un token emitido para un servidor no pueda reutilizarse contra otro—; poner un gateway consciente de la identidad delante de cada servidor y rechazar cualquier llamada que no lleve un token válido ligado a audiencia. Azure API Management puede validar tokens de Microsoft Entra y comprobar emisor, audiencia y expiración antes de que la petición alcance una tool.

**3. Acceso sobredimensionado y agregación de credenciales.** Un único servidor MCP suele guardar credenciales de varios sistemas a la vez y pedir scopes más amplios de lo que necesita (acceso completo al buzón donde bastaría read-only). Un solo servidor comprometido, o un token filtrado, se convierte en vía de brecha de cada sistema que toca. Controles: aplicar mínimo privilegio por recurso (scopes OAuth estrechos frente a wildcards; tokens de vida corta frente a secretos de vida larga); dar a cada agente una identidad gobernable, como Microsoft Entra Agent ID, para aplicar política a toda una clase de agentes o apagarlos en una sola operación.

**4. Cadena de suministro y "rug pulls".** Un servidor MCP nunca es sólo el servidor: es el servidor, sus dependencias y la infraestructura donde corre, y cada uno es una vía de entrada. Un paquete typo-squatted, una dependencia comprometida o un cambio de propiedad tras la misma URL pueden volver hostil un servidor de confianza. También conocido como ataque "rug pull": un servidor se comporta bien mientras se revisa, gana aprobación y luego cambia cuando agentes y workflows ya dependen de él. Controles: la aprobación no puede ser un evento único; construir un registro Secure By Design y registrar cada servidor en un catálogo de diseño para tener una línea base known-good; fijar definiciones de tools y alertar ante drift como tripwire para rug pulls; enrutar todo por un gateway que re-compruebe identidad y política en cada llamada. Azure API Center inventaría APIs y servidores MCP, y el OWASP MCP Top 10 mapeado a controles de Azure alinea los riesgos.

**5. Shadow MCP.** Es el shadow IT de la era de la IA. Un desarrollador levanta un servidor para desbloquear una demo, un equipo conecta un agente a cualquier endpoint a mano y nadie lo registra ni verifica. No puedes gobernar, parchear ni revocar lo que no ves. Controles: empezar por visibilidad de lo que existe y un gateway de runtime por el que todo enrute. El GSA AI Gateway ayuda a aflorar los servidores shadow no registrados.

**6. Command injection y sandbox escape.** Muchos servidores MCP corren localmente y hablan por stdin/stdout, lanzando subprocesos y tocando el sistema de ficheros. Si un servidor pasa entrada sin sanear a un shell o a una ruta de fichero, tienes command injection o path traversal, una de las mayores clases de vulnerabilidades MCP reportadas este año. Controles: sandboxear servidores locales en contenedores con sólo el acceso a ficheros y red que necesitan, y bloquear tráfico saliente por defecto; validar y sanear cada entrada y salida; nunca pasar comandos shell crudos o rutas sin sanear; mantener servidores y SDKs parcheados.

### Cierre

MCP no ha cambiado qué es la buena seguridad, sólo dónde aplicarla. Los riesgos que más importan ahora están en la cadena de suministro, en la identidad y en servidores que nadie verificó, y los controles que los abordan son los que ya conoces: identidad fuerte, mínimo privilegio, un gateway delante de cada servidor, sandboxing para servidores locales y una alerta cuando cambia una tool aprobada.
