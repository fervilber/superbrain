---
title: "NVIDIA Open Agent Safety Platform: OpenShell y Sentry para contener agentes descontrolados"
source: "https://thenewstack.io/nvidia-openshell-sentry-agents"
date: 2026-11-02
captured: 2026-11-02
---

# Nvidia launches Open Agent Safety Platform to lock down rogue AI agents

Frederic Lardinois — The New Stack (28 de septiembre de 2026). Captura verbatim de los tramos sustantivos (cabeza y cola) más el artículo de The Daily Star publicado el 1 de noviembre de 2026.

After four frontier labs saw agents escape test sandboxes this summer, Nvidia pairs its OpenShell runtime with a BlueField-4 watchdog called Nvidia Sentry.

## OpenShell: el runtime con políticas

Nvidia's Open Agent Safety Platform combina OpenShell, su software de código abierto para controlar a qué puede acceder un agente mientras opera, con Sentry, un sistema de monitorización independiente que se ejecuta en las DPU BlueField-4 de Nvidia. Nvidia sostiene que colocar Sentry en un procesador separado —en lugar de en la CPU o la GPU donde opera el agente— proporciona una vista aislada de la actividad del agente.

"An agent can bypass this by spawning two sub-agents: one that can read from GitHub, that can talk to another one, that could also then post outside," dijo Golshan (Nvidia). El _prover_ modela el acceso combinado de toda la flota de agentes para encontrar esa ruta.

En las propias pruebas de Nvidia, agentes que operaban con salvaguardas reducidas pasaron hasta dos horas intentando convencer a un revisor de IA de que les concediera acceso de escritura a un repositorio protegido. El _prover_, según la compañía, dio al revisor evidencia de lo que la petición permitía realmente, y no se produjo ninguna escritura protegida.

Un ejemplo de política: prohibir que un agente lea código en GitHub y lo publique externamente. El _prover_ busca el camino indirecto que la política deja abierto.

## Sentry: la "isla de seguridad"

Nvidia Sentry añade una capa de hardware adicional. Se ejecuta en BlueField-4, en un dominio de confianza separado del host, y según Nvidia puede poner en cuarentena a un agente en milisegundos.

Con una DPU en el sistema, el endpoint del modelo del agente se enruta "a través de un proxy en la DPU, de modo que puedes ver todos los rastros de razonamiento de los agentes en el host", dijo Boitano (Nvidia).

A diferencia de OpenShell, Sentry no es de código abierto, aunque Boitano dijo que tiene APIs abiertas y que OpenShell puede funcionar con otro hardware de aplicación de red.

Lo comparó con los vehículos autónomos. "Hay un sistema primario que puede estar ejecutando el sistema de percepción, y luego una isla de seguridad que garantiza la seguridad del sistema."

"La DPU es realmente opcional en estas arquitecturas", dijo Boitano. "En muchos casos, usar solo OpenShell en CPUs es honestamente suficiente para proporcionar un control de acceso estricto para los agentes." La DPU es para "casos de uso de frontera de evaluación de modelos o sistemas donde podrías tener las salvaguardas desactivadas de los modelos, así que podría ser para red teaming".

## Quién construye sobre la plataforma

Anthropic está integrando OpenShell con Claude Managed Agents, que ya mantiene el bucle del agente en la infraestructura de Anthropic y empuja la ejecución de herramientas a sandboxes controlados por el cliente. SpaceXAI dice que usa la plataforma para agentes de codificación de Cursor y modelos Grok, mientras que Salesforce ha añadido eventos de auditoría y aprobaciones de permisos de OpenShell en Slack. SAP está integrando el runtime en Joule Studio y también contribuye código.

OpenAI y Google, dos de los cuatro laboratorios cuyos agentes se descontrolaron este verano, no están en la lista de socios. Tampoco AWS.

## Contexto de incidentes

En julio de 2026, OpenAI reveló que modelos sometidos a evaluaciones de ciberseguridad eludieron los controles destinados a aislarlos de internet. Los agentes comprometieron partes de la infraestructura de investigación de OpenAI y sistemas operados por Hugging Face.

David Sacks, fundador, capitalista de riesgo y copresidente del Consejo Asesor Presidencial de Ciencia y Tecnología, dijo que el anuncio de Nvidia recuerda que la seguridad de los agentes es un problema de ingeniería. "Los escapes recientes no fueron prueba de que el desarrollo deba detenerse", escribió en X. "Fueron prueba de que el sandbox era demasiado débil. El entorno de ejecución estaba mal diseñado y mal configurado."

Jensen Huang dijo a CNBC que la plataforma es esencialmente "un navegador para agentes", un sistema de contención que solo permite el acceso a lo que un agente necesita para hacer su trabajo. "No puedes tener agentes vagando y derivando por la empresa, así que tienes que encontrar la manera de contenerlos." "No podemos tener una industria de IA exitosa si el mundo no cree que está construida y desplegada de forma segura."

---

# Nvidia launches Open Agent Safety Platform to keep rogue AI agents in check

The Daily Star (publicado el 1 de noviembre de 2026). Captura verbatim.

Nvidia has launched a new security platform designed to prevent autonomous artificial intelligence (AI) agents from operating beyond their permitted environments, as technology companies face growing concerns over how increasingly capable AI systems are controlled.

The chipmaker unveiled the Nvidia Open Agent Safety Platform on September 28, combining software and hardware-based security measures that operate separately from the AI agents they monitor.

At the centre of the platform are Nvidia OpenShell and Nvidia Sentry. OpenShell is open-source software that creates a secure runtime boundary around an AI agent, monitoring its actions and enforcing policies governing what systems, data, and tools it can access.

Sentry adds another layer of protection through Nvidia's BlueField-4 data processing units. Nvidia said the system continuously monitors agent activity independently of the processors running the AI model and can quarantine agents within milliseconds if they attempt to operate outside prescribed boundaries.

The approach is intended to make security controls harder for an autonomous agent to circumvent because some of the safeguards operate outside the agent's own software environment.

The launch follows heightened scrutiny of AI agents after incidents in which models reportedly bypassed safeguards during testing and gained access to systems beyond their intended environments.

Nvidia chief executive Jensen Huang said AI safety would require controls across the entire computing stack rather than relying solely on restrictions built into individual models.

More than 100 organisations are working with technologies linked to Nvidia's platform, according to the company. They include Anthropic, Microsoft, SAP, Scale AI, Cisco, IBM, Salesforce, financial institutions, infrastructure providers, and robotics companies.

OpenShell can also be extended to computing platforms made by companies including Arm and Intel.
