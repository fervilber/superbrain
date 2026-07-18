# Hermes Agent: Funcionalidades Técnicas de Persistencia y Loops

Hermes Agent no es un simple chatbot; es un agente autónomo diseñado para la persistencia a largo plazo y la mejora continua. Sus pilares fundamentales permiten una operación autónoma eficiente:

## 1. El Loop de Aprendizaje (Learning Loop)

Hermes no solo ejecuta tareas; crea y refina su propia base de conocimiento procedimental.

- **Creación de Skills:** Tras completar tareas complejas (5+ llamadas de herramientas), el agente debe guardar el flujo exitoso como un "skill" (`~/.hermes/skills/`).
- **Mantenimiento de Skills:** Si un skill falla o es ineficiente, se actualiza mediante `skill_manage`.
- **Evolución:** El modelo no depende de instrucciones estáticas, sino de la experiencia previa almacenada en estos skills.

## 2. Persistencia y Memoria

- **Memoria Duradera:** Facts (hechos) guardados mediante la herramienta `memory` sobreviven a las sesiones. Se inyectan en cada turno para reducir la necesidad de re-steering.
- **Factores de Estabilidad:** La memoria se divide en `user` (preferencias) y `memory` (hechos del entorno/herramientas).
- **Session Search:** FTS5 permite recuperar estados, decisiones y resoluciones de conversaciones pasadas sin contaminar el contexto actual.

## 3. Operación Autónoma y Cron Jobs

Hermes puede operarse como un cron job, permitiendo tareas de fondo sin interacción humana:

- **Seguridad:** Los cron jobs tienen permisos limitados y no pueden interactuar con el usuario.
- **Autonomía:** Debe tomar decisiones inteligentes, evitar preguntas, y resolver bloqueos siguiendo los "pitfalls" definidos en sus skills.
- **Entrega de resultados:** La salida final se entrega directamente al sistema de destino, utilizando marcadores como `[SILENT]` para procesos sin cambios relevantes.

---

_Fuente: Documentación oficial de Hermes Agent (Julio 2026)._
