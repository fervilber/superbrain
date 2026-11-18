---
title: "Replit Missions: enjambres de agentes con presupuesto fijo que planifican, construyen y prueban hacia un resultado"
source: "https://replit.com/blog/introducing-replit-missions"
date: 2026-11-18
captured: 2026-11-18
---

# Replit Missions (17 de noviembre de 2026)

## Qué es

Replit lanzó **Missions** para ayudar a los equipos a asumir el trabajo complejo para el que no tenían tiempo ni capacidad: ganar más clientes empresariales, mejorar el rendimiento del producto o reemplazar software heredado. El usuario **define el resultado**, y Replit coordina un **enjambre de agentes** que planifica, construye, prueba e itera hacia él **dentro del presupuesto y los límites** que el usuario fija.

## El caso propio de Replit: DataCat

Replit quería traer la monitorización de aplicaciones _in-house_ para reducir costes y ganar control. Dieron a Missions el objetivo de construir **DataCat**, una plataforma personalizable que pudieran correr en su propia infraestructura. En **dos días**, con un presupuesto de **3.000 dólares**, un enjambre de agentes construyó paneles, alertas y trazado de aplicaciones, y luego probó la plataforma contra objetivos medibles de rendimiento y fiabilidad.

Resultados medidos:

- Ante un **bug de base de datos introducido deliberadamente**, DataCat levantó una alerta en **38 segundos**, superando el objetivo de 60 s, y trazó el fallo hasta la consulta exacta y sus logs.
- En una prueba de carga de tres horas, DataCat almacenó **26 millones de registros** de actividad de aplicación y **4,4 millones de entradas de log** sin perder datos, con búsquedas y alertas funcionando.
- **36 comprobaciones** de corrección de datos y **15 comprobaciones** de fiabilidad de alertas pasaron todas.
- En pruebas comparadas de Node.js, la aplicación manejó más peticiones con menos sobrecarga de procesador por monitorización; el agente de DataCat usó menos memoria y sus logs fueron buscables antes.

## Cómo se controla el trabajo

- **Definición del éxito:** durante la configuración, Missions hace preguntas para definir qué cuenta como éxito (¿los pilotos de pago cuentan para los 10 primeros clientes, o se exige contrato anual por encima de un mínimo?).
- **Presupuesto y límites:** el acuerdo de la misión fija el **límite de gasto** y **qué acciones requieren permiso**. Por ejemplo, se puede topar la misión en 1.000 dólares y exigir aprobación antes de que el agente contacte a prospectos, comparta una propuesta, cambie materiales de venta de cara al cliente o haga compromisos de producto. Estos límites permanecen mientras evoluciona el enfoque.
- **Plan, construcción e iteración:** los agentes investigan cuentas objetivo, construyen demos y preparan _outreach_ para aprobación. Los enjambres trabajan en paralelo (un agente investiga compradores mientras otro desarrolla una demo). Tras el _outreach_ aprobado, la misión revisa qué cuentas y mensajes generan conversaciones cualificadas y guía la siguiente ronda.
- **Progreso y verificación:** se elige qué avisos recibir (bloqueos, actualizaciones, estado) y con qué frecuencia. Un **juez de IA independiente** comprueba los resultados contra los criterios de éxito acordados, y los agentes usan su retroalimentación para refinar el trabajo. La misión se marca completada cuando se cumplen los criterios; si se agota el presupuesto, el trabajo se detiene con el resultado sin resolver.

## Por qué los enjambres importan (benchmark)

En 13 tareas de referencia con **NumPy**, los agentes exploraron implementaciones alternativas, optimizaron patrones de acceso a memoria y validaron la corrección automáticamente:

- **Auto (Max):** un solo agente logró aceleraciones de hasta **4×**; un enjambre de **16 agentes** alcanzó **17×**; uno de **32 agentes**, **19×**.
- **Auto (Power):** el mismo patrón, **2×**, **7×** y **9×** respectivamente.

El resultado llamativo es cuánto más lejos llegaron los enjambres: explorar más enfoques en paralelo ayudó a encontrar implementaciones sustancialmente más rápidas.

## Implicación

Missions convierte el enjambre de agentes en un **producto con contrato de gasto y compuerta de aprobación**. La lección no es «los enjambres son más rápidos» —el benchmark lo sugiere— sino que la unidad de delegación pasa de «completa esta tarea» a «persigue este resultado dentro de un presupuesto», con un **juez independiente** como árbitro del éxito. El riesgo que Replit mismo advierte: hay que evaluar el coste total y la fiabilidad del sistema final, y vigilar si los agentes paralelos crean trabajo duplicado, decisiones inconsistentes o costes de uso inesperados.
