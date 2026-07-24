# Información técnica sobre Scheduled Tasks (Cron) en Hermes

Hermes Agent permite la gestión de tareas recurrentes o programadas mediante el uso de "cronjobs". Este sistema es fundamental para automatizar flujos de trabajo como la ingesta de noticias o el mantenimiento de repositorios.

## Capacidades de los Cronjobs

- **Programación:** Soporta tanto tareas de una sola ejecución como tareas recurrentes mediante expresiones cron o lenguaje natural.
- **Gestión:** Permite pausar, reanudar, editar, disparar (trigger) y eliminar jobs mediante el uso del tool `cronjob`.
- **Integración:** Se pueden asociar habilidades (skills) específicas a un job, permitiendo que el proceso tenga el contexto necesario.
- **Modos de ejecución:**
  - **Modo Agente:** Crea una sesión nueva con el conjunto de herramientas del agente.
  - **Modo No-Agente:** Ejecución de un script sin involucramiento del LLM, útil para tareas de bajo nivel.
- **Flexibilidad:** Permite la entrega de resultados en el chat, archivos locales o destinos de plataforma configurados.

## Ejemplo de uso técnico

La gestión de estos jobs se realiza principalmente a través del tool `cronjob` dentro de Hermes, facilitando su manejo programático o vía lenguaje natural sin depender estrictamente de CLI manuales.
