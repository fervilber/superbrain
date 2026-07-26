# Resumen Técnico: Automatización y Cron Jobs en Hermes Agent

La documentación oficial subraya la robustez del sistema de tareas programadas (`cronjob` tool) en Hermes Agent. Un aspecto crítico es la seguridad ante cambios de modelo: cuando un cron job se crea sin especificar explícitamente un proveedor o modelo, el agente realiza un "snapshot" de la configuración global.

### Puntos Clave de Seguridad

- **Falla Seguro (Fail-Closed):** Si la configuración global cambia, el job no se ejecuta silenciosamente; se detiene y envía una alerta solicitando una actualización explícita (`cronjob action=update job_id=… provider=… model=…`).
- **Prevención de Costos:** Este mecanismo evita que un agente autónomo herede cambios costosos o inesperados en el modelo de inferencia sin supervisión humana.
- **Flexibilidad:** Permite programar tareas mediante lenguaje natural o expresiones cron, con soporte para "no-agent mode" (scripts puros sin inferencia LLM para máxima eficiencia).

Este diseño subraya el enfoque de Hermes hacia la autonomía segura y la previsibilidad en entornos de producción.
