---
title: "La memoria del agente como responsabilidad: HEAMS, Ledger, MemUse, GrepMem y RAG in a Trenchcoat"
source: "https://arxiv.org/abs/2611.20144"
date: 2026-11-21
captured: 2026-11-21
---

# La memoria del agente como responsabilidad (ola de papers de noviembre de 2026)

Captura compuesta de cinco trabajos publicados en arXiv entre el 1 y el 17 de noviembre de 2026,
más `MemFolder` (2611.26427) y `GrepMem` (2611.25123). En conjunto forman la crítica más dura que ha
recibido la memoria de agentes: **los benchmarks de resultado no ven lo que la memoria hace**.

## 1. HEAMS: Holistic Evaluation of Agent Memory Systems (arXiv:2611.20144, 15-nov-2026)

Autores: Chirag Goel, Jacob Lavoie, Amirhossein Naghshzan, Jordan Bannister, Marzia Nouri, Mehar
Bhatia, Matt Harris, Siva Reddy, Arsène Fansi Tchango, Gaétan Marceau Caron.

> Memory systems allow AI agents to persist information across interactions, making them more
> personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored
> information can be disclosed in inappropriate contexts, resist correction or deletion, be retained
> beyond what users desire, or be poisoned to influence later agent behaviour. Yet memory systems are
> typically evaluated on task performance and efficiency alone. We argue that a memory system should
> instead be understood as the **custodian of its user's persistent information**, with
> responsibilities that extend beyond helping an agent complete its tasks, and that it should be
> evaluated holistically against all such responsibilities.

HEAMS es un framework de código abierto que: (1) enuncia las responsabilidades de la memoria como
desiderata de comportamiento explícitos que abarcan **rendimiento, eficiencia, seguridad, privacidad y
soberanía del usuario**; (2) monta un conjunto de benchmarks que cubre esos desiderata y reconoce los
huecos que quedan; (3) desarrolla **MilaMem**, un sistema de memoria prototipo, más una **capa de
gobierno que puede envolver cualquier sistema de memoria**; (4) compara sistemas de memoria en toda la
suite.

Hallazgo central: **ningún sistema de memoria lidera todos los benchmarks de rendimiento, y las
puntuaciones altas de rendimiento pueden coexistir con puntuaciones malas de privacidad, soberanía del
usuario y seguridad**. La gobernanza influye fuertemente en los resultados: las políticas de recuerdo
reducen la divulgación inapropiada a costa de la utilidad, mientras que las políticas de recuerdo y de
retención mejoran la resistencia al envenenamiento.

## 2. LEDGER: Auditable Agent Memory Under Change (arXiv:2611.20927)

> Agent memory systems are mostly evaluated on fixed histories, and only their final answers are
> scored. In real use, facts change, sources differ in reliability, and users ask the agent to forget
> things.

Ledger propone que un modelo de lenguaje **proponga hechos** y que **reglas explícitas decidan** qué
valor está vigente, en qué fuente confiar y qué borrar. Cada hecho conserva su fuente y el **periodo
en el que fue válido**. `Ledger+Ep` añade una búsqueda sobre los turnos de conversación en bruto para
las preguntas que el ledger no cubre, y **limpia esos turnos al borrar**. Se evalúa contra no-memoria,
reproducción de historial completo, recuperación sobre transcripciones y Mem0, con el mismo modelo y
el mismo prompt, sobre una carga sintética multi-sesión de agente de código y un subconjunto de 210
preguntas de LongMemEval; se puntúa tanto **la evidencia que la memoria entrega al modelo** como la
respuesta.

Tres preguntas de investigación: (RQ1) cómo de bien el sistema mantiene valores obsoletos,
contaminados y borrados fuera de la evidencia; (RQ2) cómo de bien respeta la precedencia de fuentes;
(RQ3) cómo de bien cumple el borrado.

## 3. RAG in a Trenchcoat (arXiv:2611.22179, 17-nov-2026)

Autores: Jingyu Liu, Zongze Li, Zach Xu, Zhanhui Zhou, Tahseen Rabbani, Dawn Song, Ce Zhang.

> Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on
> top of retrieval-augmented generation. However, we found that **almost none of those primitives earn
> their cost** in our tested memory benchmarks.

`BRIDGE` —memoria RAG deliberadamente mínima con notas de observación encadenadas, recuperación híbrida
BM25 + coseno y renderizado cronológico— **alcanza paridad dentro del intervalo de confianza bootstrap
con el SOTA previo** en LongMemEval-S y BEAM, y supera al mejor baseline de memoria en EverMemBench por
**5,7–6,3 puntos** con el mismo lector. Corre a **~5–7 K tokens de prompt por consulta**, con una sola
llamada al LLM por ingesta y por consulta.

> We argue that this parity is itself the result: standard benchmarks score **what memory retrieves**,
> not **what memory enables when the agent acts**.

Para medir lo segundo introducen cinco sondas adversariales (Rule Application ±, Pattern Induction
Style / Procedural, Dynamic Multiturn) juzgadas en tiempo de generación por una cadena de verificación
cruzada entre proveedores, donde cada consulta solo puede resolverse aplicando una regla o patrón
recordado que la consulta nunca menciona. Resultado: **ninguna arquitectura gana universalmente**; los
extractores de hechos atómicos (LangMem) ganan en aplicación de reglas, mientras que la memoria de
resúmenes por bloque (BRIDGE) gana en inducción de patrones. El resultado se sostiene en cuatro
dominios, tres jueces y tres familias de lectores.

## 4. MemUse: Delivered, Not Used (arXiv:2611.01718, 1-nov-2026)

Changran Xu, Zeju Li, Qiang Xu (CUHK). Evalúa la memoria **en su punto de uso**, dentro de
trayectorias registradas: cada entrega de memoria se compara con lo que el agente ya podía ver y se
sigue a través de las acciones posteriores y sus consecuencias. Un juez agéntico puntúa relevancia,
exactitud, novedad, influencia y efecto observado de cada entrada entregada.

> On 8,000 SWE-bench Verified episodes from three memory systems, **resolve rates stay within 0.4
> percentage points of a no-memory baseline**, yet MemUse shows that most delivered entries were
> irrelevant, most relevant entries went unused, and in two systems most deliveries restated content
> the agent could still see. It also surfaces effects that outcomes hide: **23.2% of episodes with
> beneficial memory use still failed**, and **5 of 16 with harmful use still succeeded**.

Cifra adicional del cuerpo del paper: entre el **51 % y el 80 %** de las entradas relevantes quedaron
sin usar en cada sistema.

## 5. GrepMem: Forget Freely, Grep Later (arXiv:2611.25123)

Memoria **sin índice y sin pérdida**: un log de texto plano **append-only** con la historia completa
del agente más una herramienta de búsqueda por expresiones regulares (`grep_history`) para el recuerdo
a demanda. No requiere embeddings, índice de recuperación, extracción de memoria ni modelos
adicionales. Se entrena Qwen3.5-9B con RL bajo cinco estrategias de gestión de contexto y se evalúa en
sesiones de investigación con múltiples preguntas, recuerdo en flujo largo y QA sobre trayectorias.

> On ContextBench, GrepMem uses only **29% as many tokens as MemGPT** while achieving substantially
> higher accuracy on Log Triage.

Queda en la frontera de Pareto precisión-coste en las cinco tareas.

## 6. MemFolder (arXiv:2611.26427)

Plegado de memoria guiado por estructura, en dos componentes que comparten grupos de memoria:
`RecordFolder` ancla menciones de entidades, selecciona anclas representativas y complementarias y
combina afinidad semántica y de entidad con encadenamiento temporal para consolidar registros;
`ContextFolder` codifica los registros originales en texto compacto y revisa la codificación con
retroalimentación de verificación cuando no se recuperan hechos clave. Sobre Mem0, `RecordFolder`
**retiene el 99,0 % del rendimiento medio original con un 50 % menos de registros**, superando al
mejor baseline en 1,9 puntos de retención.
