---
title: "MCP sin estado para integración empresarial: qué cambia en despliegue, estado de negocio y control de acceso"
source: "https://www.techtarget.com/news/stateless-mcp-a-new-era-for-enterprise-ai-integration/874933/"
date: 2026-11-18
captured: 2026-11-18
---

# Stateless MCP: una nueva era para la integración de IA empresarial (TechTarget, 17 de noviembre de 2026)

## El problema de fiabilidad

Cuando un agente de IA empresarial envía una petición a un sistema empresarial, la operación puede tener éxito aunque la conexión se corte antes de que la respuesta llegue al agente. Sin embargo, el agente **no puede determinar si reintentar** la petición, porque hacerlo podría repetir una acción ya completada. Es uno de los retos de fiabilidad que enfrentan las organizaciones al usar MCP para conectar aplicaciones de IA a servicios empresariales.

Los cambios recientes en la especificación de MCP **eliminan las sesiones a nivel de protocolo**, facilitando la distribución de peticiones entre servidores. Los equipos empresariales siguen necesitando mantener **estado de negocio**, **aplicar controles de acceso**, **recuperarse de operaciones interrumpidas** y **monitorizar la actividad** entre servicios.

## MCP sin estado cambia el despliegue de servidores

- En versiones anteriores, los servidores emitían un **identificador de sesión** y lo usaban para reconocer peticiones posteriores. Los despliegues que mantenían estado en memoria tenían que **enrutar las llamadas siguientes a la misma instancia** o compartir ese estado entre servidores. Un fallo del servidor podía interrumpir una interacción en curso.
- El cambio **elimina ese mecanismo de sesión**. Cada petición incluye la información necesaria para procesarla, de modo que el tráfico puede moverse a **otra instancia**. Esto facilita añadir capacidad, reemplazar servidores caídos y usar infraestructura _serverless_.
- Los procesos de negocio **siguen necesitando recordar** qué pasó entre llamadas. Ejemplo: si un agente prepara una orden de compra, la herramienta MCP puede **guardar un borrador en el ERP y devolver un número de referencia**; las peticiones posteriores usan ese número para recuperar y actualizar el borrador, **aunque las reciba un servidor MCP distinto**.
- La pregunta práctica es **dónde guardar esa información**: el almacenamiento compartido puede hacer que esos registros estén disponibles entre instancias. Si la organización corre clientes MCP antiguos, es imperativo comprobar la **compatibilidad** antes de cambiar la infraestructura.

## Control de acceso en MCP sin estado

- MCP usa un modelo de autorización basado en **OAuth** para conexiones HTTP protegidas: cada petición incluye un **token de acceso**. El servidor valida el token para confirmar la identidad del llamante, el servicio previsto y los permisos concedidos.
- Esto importa cuando distintos agentes de IA **comparten el mismo entorno MCP**. La información aportada por el cliente —como los detalles de su software— **no prueba identidad ni permiso**. Si un agente pide acceso a un registro de cliente, el servicio debe **verificar de todos modos** que el usuario o la carga de trabajo que hace la petición tiene permiso para verlo o modificarlo.

## Conclusión

MCP sin estado facilita desplegar y escalar servidores que conectan apps de IA a sistemas de negocio. Antes de migrar, las organizaciones deben **evaluar clientes dependientes de sesión, entender dónde se guarda el estado de negocio, probar el comportamiento de reintento y asegurar que la monitorización rastrea cada transacción**.

## Implicación

Este artículo pone nombre al problema operativo que la especificación `2026-07-28` dejó abierto: quitar las sesiones **resuelve el escalado y traslada el problema al estado de negocio**. La referencia al borrador en el ERP con número de referencia es la respuesta pragmática: el protocolo se vuelve _stateless_, pero la aplicación reintroduce estado donde le corresponde. Y el aviso sobre OAuth es la lección de seguridad de la semana: **un token demuestra acceso, no autorización para esta acción concreta** —exactamente el hueco que Proof intenta cerrar con x401.
