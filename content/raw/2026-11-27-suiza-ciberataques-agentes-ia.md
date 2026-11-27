---
title: "Suiza confirma cinco ciberataques con agentes de IA: cuatro exitosos, tres contra infraestructura crítica"
source: "The Hacker News / BACS (OFCS suizo) / CSIRT Italia / NCSC UK / AI Agent Store"
date: 2026-11-25
captured: 2026-11-27T20:10:00+01:00
---

# Suiza confirma ciberataques asistidos por agentes de IA

URL: https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html
URL: https://www.bacs.admin.ch/en/26-ki-agenten-1-en
URL: https://csirt.regione.toscana.it/impiego-di-agenti-di-ia-in-campagne-di-compromissione-automatizzate-bl01-261123-csirt-ita/
URL: https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks
URL: https://aiagentstore.ai/ai-agent-news/daily/2026-11-27

## La noticia

Atacantes que usan agentes de IA han comprometido sistemas informáticos de organizaciones suizas en cuatro de cinco ataques confirmados, los primeros casos de este tipo en el país, según declaró ayer la agencia de ciberseguridad nacional. Tres de los ataques se dirigieron contra operadores de infraestructura crítica y dos de ellos tuvieron éxito, sin que se reportaran perturbaciones mayores. No se han nombrado las víctimas y no se sabe quién está detrás de los ataques.

Florian Schütz, director del Centro Nacional de Ciberseguridad de Suiza (NCSC, por sus siglas en inglés, dependiente de la Oficina Federal de Ciberseguridad —BACS—), dio las cifras en una entrevista con la emisora pública SRF. Los cinco casos se reportaron en días recientes. Entre las organizaciones afectadas había pequeñas y medianas empresas, que se presentaron voluntariamente.

El primer aviso de la agencia, un boletín de seguridad publicado el martes, decía que los agentes habían comprometido los sistemas de TI de las víctimas en todos los casos conocidos en ese momento. Ni el aviso ni la entrevista retransmitida ayer explican por qué cambió el recuento.

«Estos casos representan un cambio en el panorama de amenazas cibernéticas», dice el aviso. Los operadores atacados pertenecen a al menos dos sectores. Suministro eléctrico, agua potable y telecomunicaciones son ejemplos de lo que Suiza considera infraestructura crítica.

## Frameworks ofensivos agénticos

Los ataques involucran lo que la agencia suiza llama _agentic offensive frameworks_: agentes de IA que encuentran debilidades de seguridad y ejecutan ataques por su cuenta. Su aviso nombra **ARTEX** y **CyberStrikeAI** como ejemplos de agentes accesibles por internet, no como las herramientas usadas en los cinco casos.

Los agentes se usan a menudo para escanear vulnerabilidades conocidas y sin parchear y pueden lanzar muchos ataques en paralelo, dice la agencia. Cuando las defensas responden, los agentes cambian de método, dejando a las empresas mucho menos tiempo para detectar la intrusión y responder. El número de herramientas de ataque con IA accesibles libremente en línea casi se ha duplicado desde octubre, según la agencia. La cifra cuenta herramientas disponibles, no ataques ni víctimas.

Raphael Reischuk, cofundador del Instituto Nacional de Pruebas de Ciberseguridad de Suiza, espera una ola de ataques mayor y dice que las empresas subestiman el riesgo.

## El patrón se repite en Italia y el Reino Unido

El equipo nacional de respuesta a incidentes de Italia, **CSIRT Italia**, describió campañas de compromiso masivo en un boletín oficial esta semana. En los casos que observó de primera mano, agentes autónomos dirigidos por IA irrumpieron en un gran número de sistemas en unas pocas horas.

Los agentes adaptan sus acciones en segundos, se ejecutan en paralelo sin intervención humana y encadenan vulnerabilidades, configuraciones erróneas y credenciales comprometidas, dice el boletín. Nombra **ARTEX**, **CyberStrikeAI**, **PentAGI** y **DeepSeek Harness**, un agente de código abierto cuyo _Red Team Mode_ usa un prompt incorporado para saltarse los límites de seguridad del modelo subyacente.

Cada acción, por sí sola, parece tráfico normal de usuario o de API. La detección depende del contexto: de dónde vienen las peticiones, con qué frecuencia llegan, cuántos datos se mueven y en qué orden suceden las cosas.

El **NCSC británico** reportó el mismo patrón en una guía de la agencia esta semana. «Desde septiembre de 2026, el NCSC ha visto un aumento marcado en los ciberataques asistidos por IA», dice. Algunos incidentes causaron caídas en servicios expuestos a internet, y otros dieron a los atacantes un punto de apoyo para actividad posterior dirigida por agentes. Las debilidades son viejas: credenciales comprometidas en repositorios de código, infraestructura como código mal configurada, autenticación por defecto o ausente y debilidades en las APIs. Lo que ha cambiado es la velocidad, la persistencia y el bajo coste de los ataques, dice la agencia británica. Los frameworks también son ruidosos, lo que los hace más fáciles de detectar.

La **Comisión Europea** ya ha sido golpeada. Atacantes que usaban ARTEX irrumpieron en sus sistemas de recursos humanos, reembolso médico y traducción, según confirmó la Comisión, en una intrusión anterior detectada por primera vez el 22 de octubre.

## Qué deberían hacer los defensores

El consejo común más fuerte de las tres agencias es reducir el tiempo del que disponen los atacantes. Sus recomendaciones se solapan:

- Instalar actualizaciones de seguridad críticas en sistemas expuestos a internet en las 24 horas siguientes a su publicación (Suiza), y parchear primero las fallas que ya se están explotando (Italia).
- Desconectar o aislar sistemas expuestos a internet que no puedan parchearse rápido (Italia).
- Reducir lo que es alcanzable desde internet, usando geo-bloqueo, listas de permitidos y autenticación delante de los servicios (Suiza, Reino Unido).
- Exigir MFA o passkeys en todo lo alcanzable desde internet, y conceder los privilegios mínimos que funcionen (Suiza).
- Vigilar comportamiento y volúmenes de datos inusuales (Suiza), y correlacionar registros: la actividad de agentes aparece como ráfagas de peticiones y tasas de error altas (Reino Unido).
- Poner desafíos de bot en endpoints de alto valor y usar señuelos como _honeytokens_ para atrapar y frenar a los agentes (Reino Unido).
- Cargar los feeds de indicadores publicados por Italia en las herramientas de monitorización, teniendo en cuenta que los indicadores cambian rápido y solo son válidos para sus marcos temporales declarados (Italia).
