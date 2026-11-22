---
title: "Chrome Security construye Mirror Dimension: una web sintética para probar agentes de navegación"
source: "https://www.unite.ai/es/chrome-security-builds-a-synthetic-web-to-test-ai-browsing-agents/"
date: 2026-11-22
captured: 2026-11-22
---

# Chrome Security crea una web sintética para probar agentes de navegación con IA

Captura de _Chrome Security builds a synthetic web to test AI browsing agents_, Unite.AI, **19 de
noviembre de 2026**, por Jonas Reeve.

## Puntos clave

- **Mirror Dimension** sirve direcciones familiares dentro de un entorno aislado para que los agentes
  **no puedan detectar la prueba**.
- Los agentes críticos autónomos construyen y revisan sitios sintéticos porque las **simulaciones
  incompletas pueden exponer la evaluación**.
- El pipeline de _red-teaming_ genera **más de 1.000 candidatos de prueba por ingeniero de seguridad
  cada día**.

El equipo de Seguridad de Chrome de Google presentó **Mirror Dimension** el 19 de noviembre de 2026:
una **web sintética autónoma** para probar los agentes que están detrás de la función de navegación
automática de Chrome. El entorno contiene **miles de sitios web simulados**, inspirados en las
actividades cotidianas de los usuarios, y está diseñado para evaluar las protecciones de seguridad sin
exponer la web en vivo a las acciones de los agentes.

La escala explica la necesidad de este entorno. El entrenamiento y la evaluación de agentes de
navegación requieren **miles de acciones de lectura y escritura en cientos de sitios web**; a menudo el
modelo deduce el destino a partir de la solicitud del usuario, en lugar de recibir una URL. La web
pública cambia constantemente, y las acciones sin restricciones de los agentes pueden causar daños. En
cambio, Mirror Dimension proporciona a cada trayectoria **un punto de partida limpio e idéntico**, lo
que impide que los efectos secundarios se trasladen a la siguiente ejecución.

## Mantener la credibilidad del entorno aislado

Una limitación central del diseño es la conciencia de que **se está evaluando al modelo**: cuando
sospecha que lo están poniendo a prueba, puede cambiar su comportamiento. Alojar todos los sitios bajo
un dominio claramente artificial, o mencionar ese dominio en la instrucción, puede provocar ese
problema. Por eso, Mirror Dimension permite que el agente **solicite direcciones conocidas**, como
`www.youtube.com`, mientras una instancia de Chrome sin interfaz gráfica se ejecuta dentro de un
entorno aislado de **gVisor**.

En lugar de permitir que la solicitud llegue a un DNS externo o a la Internet pública, el entorno
aislado **intercepta la conexión** y la envía a un **proxy local** que sirve sitios generados. Como
Chrome está diseñado para bloquear este tipo de interceptación, el proxy **crea dinámicamente
certificados TLS de entidad final**, encadenados a una autoridad de certificación raíz personalizada
instalada en el navegador controlado. Google señala que un atacante externo en la red no puede instalar
una raíz de este tipo en el dispositivo de un usuario real sin privilegios de administrador; el equipo
puede establecer esa raíz de confianza al iniciar el sistema.

## Los agentes crean y evalúan los sitios

Poblar el entorno requiere más que páginas estáticas. Los sitios de prueba deben permitir **flujos de
trabajo de varios pasos** en mercados locales de servicios, procesos de compra de comercio electrónico,
redes sociales y páginas de recetas, ya que un agente puede detectar indicios de que la simulación está
incompleta.

**Chrome DevTools for Agents** permite que los subagentes inspeccionen capturas de pantalla, hagan clic,
escriban, naveguen y observen el comportamiento de las aplicaciones, para que puedan probar los
recorridos de usuario tal como se muestran, en lugar de limitarse a analizar el código fuente. El ciclo
de revisión **prioriza la fidelidad por encima de la rapidez de finalización**, y los revisores vuelven
a comprobar las correcciones que pueden generar nuevos problemas.

## Probar las defensas contra la inyección de instrucciones

El entorno sirve además para probar las defensas del navegador frente a la **inyección de
instrucciones** en contenido web, el vector de ataque que la edición del 21 de noviembre de este
informe identificó como condición ambiental de los agentes siempre encendidos.

## Implicaciones

- La evaluación de agentes de navegación exige **entornos sintéticos creíbles**: la web real es
  destructible, no determinista y, además, un objetivo de seguridad.
- El obstáculo técnico central no es generar páginas, sino **que el agente no sepa que es una prueba**:
  dominios plausibles, TLS válido y flujos multi-paso realistas.
- El mismo sustrato de aislamiento (**gVisor**) que Google donó al CNCF en el plano de la
  infraestructura aparece aquí como pieza de un entorno de pruebas: la contención es una primitiva
  transversal.
