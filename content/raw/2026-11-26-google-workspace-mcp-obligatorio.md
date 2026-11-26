---
title: "Google Workspace MCP: servidores GA, ruta MCP obligatoria desde febrero de 2027 y tarifas desde abril"
source: "Google Workspace Updates / Dataconomy / Arthat / The Agent Stack / aiagentnews.io"
date: 2026-11-24
captured: 2026-11-26T20:05:00+01:00
---

# Google convierte MCP en la única puerta a Workspace (y le pone precio)

URL: https://arthat.ai/blog/ai-today-2026-11-26
URL: https://the-agent.beehiiv.com/p/agent-stack-2026-11-26
URL: https://aiagentnews.io/
URL: https://agentnewsdaily.com/brief/2026-11-26

## El anuncio (24 de noviembre de 2026)

Google ha hecho **generalmente disponibles** sus servidores MCP alojados de Workspace, junto con una CLI oficial de Workspace. El despliegue llega a todos los dominios a lo largo de dos semanas. Los servidores cubren ocho productos: Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat y Tasks. **Keep aparece como «coming soon»**, por lo que no conviene planificar sobre él todavía.

La línea que más importa para quien construye: _los agentes de IA y herramientas de acceso similares deben usar MCP para llegar a los datos de Workspace en lugar de llamar directamente a las API REST de Workspace_, con **aplicación técnica a partir del 1 de febrero de 2027**.

> Lectura cuidadosa antes de alarmarse: Google no dice que las API REST se apaguen. Dice que, para los agentes, la ruta MCP pasa a ser la obligatoria, y el reloj es real. Desde el 1 de febrero de 2027, los agentes que llamen directamente a las API REST de Workspace quedarán sujetos a las cuotas del tier gratuito.

## El plano de administración

La segunda mitad del anuncio es la consola de administración, que es lo que realmente importará a los equipos de operaciones:

- Bajo **Seguridad > Controles de API**, un administrador puede gestionar qué herramientas de IA externas y qué servidores MCP entran.
- Se pueden fijar **reglas human-in-the-loop** para que un usuario tenga que confirmar una acción sensible, como leer un fichero externo o compartir datos.
- Existe un **registro de auditoría** de lo que hizo cada agente y de lo que aprobó el usuario.
- Las reglas de **Data Loss Prevention (DLP)** existentes pasan a aplicarse por sí solas a la actividad de los agentes.
- Un nuevo **Workspace AI Tools Addendum** prohíbe a los agentes hacer scraping de las API y acumular datos derivados de ellas.

## El detalle de facturación

El acceso se divide en dos tiers:

- **Standard**: gratuito, con límites de tasa publicados.
- **Scaled**: para uso intensivo.

Google afirma que **más del 99 % de los desarrolladores activos** operan hoy dentro del tier Standard sin coste. A partir del **1 de abril de 2027**, los proyectos en el tier Scaled solo pagan por el uso que supere una franquicia diaria gratuita que Google aún no ha dimensionado. Las tarifas arrancan por las API de Gmail, Calendar y Drive y los servidores MCP de Workspace.

Según la página de precios de Google para desarrolladores, el tier gratuito se limita a **5.000 peticiones MCP al día por proyecto y por producto**, y las tarifas del tier de pago van de **0,10 a 0,50 USD por 1.000 peticiones**.

## Caveats honestos

Ese «99 %» es la única cifra que Google publicó. No hay precio cerrado, ni importe de franquicia, y las políticas finas de agentes se prometen «en los próximos meses» en lugar de estar ya enviadas. La historia de gobernanza debe juzgarse por lo que está vivo: los servidores, la CLI, el requisito de febrero y los controles de administración.

## Otro dato: Zapier y el coste de las llamadas MCP

**Zapier está eximiendo del coste de tarea las llamadas MCP hasta el mediodía (hora del Este) del 5 de enero de 2027.** La oferta cubre Zapier MCP, que permite a clientes de IA como Claude, ChatGPT y Cursor ejecutar acciones sobre más de 9.000 aplicaciones.

## Qué hacer

Si se opera cualquier agente contra Workspace: empezar ya la migración a MCP y no esperar al primer trimestre. Marcar los clientes OAuth del agente con el nuevo ajuste «AI-powered agent», pilotar los servidores en un sandbox y activar la regla human-in-the-loop para todo lo que envíe o comparta.
