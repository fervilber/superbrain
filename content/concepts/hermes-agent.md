# Hermes Agent: El Agente Autónomo con Bucle de Aprendizaje

Hermes Agent es más que un simple asistente; es un **agente autónomo** diseñado para mejorar con el tiempo. A diferencia de copilotos de código integrados en IDEs, Hermes es independiente de la plataforma y está diseñado para residir en infraestructuras remotas (como VPS o clústeres GPU).

## Funcionalidades Clave

1.  **Bucle de Aprendizaje Integrado:** Crea habilidades (skills) de forma autónoma basándose en la experiencia, mejora estas habilidades durante el uso y refina su modelo interno de usuario en cada sesión.
2.  **Persistencia:** Construye una memoria profunda a lo largo de las sesiones, permitiéndole entender preferencias y contextos de trabajo sin necesidad de recordar constantemente al usuario.
3.  **Independencia de Entorno:** No está atado a tu laptop. Puede ejecutarse en una infraestructura en la nube (como Daytona o Modal) y ser controlado desde dispositivos como Telegram, permitiendo una operatividad continua.
4.  **Despliegue Flexible:** Soporta Linux, macOS, WSL2, Windows nativo y Android (via Termux), facilitando la gestión de tareas desde cualquier lugar.

## Cómo empezar

Tras instalar mediante `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` (en sistemas tipo Unix), el comando principal para inicializar el entorno es:

```bash
hermes setup --portal
```

Este comando realiza el OAuth necesario para habilitar herramientas críticas como búsqueda web, generación de imágenes, síntesis de voz (TTS) y el gateway de herramientas.

---

_Fuente: Documentación Oficial de Hermes Agent (Julio 2026)._
