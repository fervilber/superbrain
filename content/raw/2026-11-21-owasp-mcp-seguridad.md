---
title: "Seguridad de MCP: el OWASP MCP Top 10, la cheat sheet de agentes y el modelado de amenazas de tool poisoning"
source: "https://owasp.org/projects/mcp-top-10"
date: 2026-11-21
captured: 2026-11-21
---

# Seguridad de MCP y de aplicaciones agénticas (OWASP, estado a noviembre de 2026)

Captura compuesta de: `owasp.org/projects/mcp-top-10`, `cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html`,
`cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html`,
`genai.owasp.org/download/52117` (OWASP Top 10 for Agentic Applications 2026) y el paper MDPI
«Model Context Protocol Threat Modeling and Analysis of Vulnerabilities to Prompt Injection with Tool
Poisoning» (J. Cybersecur. Priv. 6(3):84).

## 1. OWASP MCP Top 10 (fase beta/piloto)

Arquitectura de referencia:

```
User ↔ MCP Host (AI App) ↔ MCP Client ↔ MCP Server(s) ↔ Tools / Data / APIs
```

- **MCP Host:** la aplicación de IA (Claude Desktop, Cursor, plugins de IDE).
- **MCP Client:** conecta con uno o más servidores y pasa las definiciones de herramienta al LLM.
- **MCP Server:** proceso ligero que expone herramientas, recursos y prompts.
- **Transportes:** `stdio` (local) o Streamable HTTP (remoto). El transporte HTTP+SSE antiguo está
  **deprecado**.

Las diez categorías:

| ID    | Título                                               | Descripción                                                                                                                            |
| ----- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| MCP01 | Token Mismanagement & Secret Exposure                | Credenciales embebidas, tokens de vida larga y secretos almacenados en la memoria del modelo o en los logs del protocolo.              |
| MCP02 | Privilege Escalation via Scope Creep                 | Permisos temporales o mal definidos que se expanden con el tiempo y conceden capacidades excesivas.                                    |
| MCP03 | Tool Poisoning                                       | El adversario compromete la herramienta, el plugin o su salida para inyectar contexto malicioso, engañoso o sesgado.                   |
| MCP04 | Software Supply Chain Attacks & Dependency Tampering | Una dependencia comprometida altera el comportamiento del agente o introduce backdoors a nivel de ejecución.                           |
| MCP05 | Command Injection & Execution                        | El agente construye y ejecuta comandos, scripts, llamadas a API o fragmentos de código con entrada no confiable sin validación.        |
| MCP06 | Prompt Injection via Contextual Payloads             | —                                                                                                                                      |
| MCP07 | Insufficient Authentication & Authorization          | —                                                                                                                                      |
| MCP08 | Lack of Audit and Telemetry                          | —                                                                                                                                      |
| MCP09 | Shadow MCP Servers                                   | Servidores MCP desplegados fuera del gobierno de seguridad.                                                                            |
| MCP10 | Context Injection & Over-Sharing                     | La «ventana de contexto» como memoria de trabajo compartida entre agentes o sesiones expone información de una tarea o usuario a otro. |

## 2. MCP Security Cheat Sheet: los riesgos clave y los controles

Riesgos enumerados: **tool poisoning** (instrucciones maliciosas escondidas en descripciones,
esquemas o valores devueltos), **rug pull** (el servidor cambia las definiciones de herramienta
después de la aprobación inicial), **tool shadowing / cross-origin escalation** (la descripción de una
herramienta maliciosa manipula cómo se comporta el agente con herramientas de **otros** servidores
confiables), **confused deputy** (el servidor MCP ejecuta acciones con sus propios privilegios, no con
los del usuario), **exfiltración de datos por canales legítimos** (inyección de prompt que codifica
datos sensibles en llamadas que parecen normales), **permisos excesivos / tokens sobre-otorgados**,
**ataques a la cadena de suministro** y **manipulación de mensajes y replay** (payloads JSON-RPC
modificados tras la terminación TLS o capturados y reenviados).

Controles concretos recomendados:

- **Hashear la definición completa de la herramienta** (incluyendo `inputSchema`, `outputSchema` y
  `annotations`), no solo la descripción: «a flipped `readOnlyHint` or `destructiveHint` can change
  client approval behavior without any visible description change». Detecta cambios de metadatos, **no
  cambios en el código o el comportamiento del servidor**; y las anotaciones de herramienta son
  _pistas, no mecanismos de aplicación_.
- Usar herramientas como **`mcp-scan`** para detectar descripciones envenenadas y shadowing cruzado.
- Usar **JSON Schema estricto** para los parámetros: `additionalProperties: false` y `pattern` en los
  campos de cadena.
- El LLM **ve las descripciones de herramientas de todos los servidores conectados** en su contexto:
  esto es crítico para entender los ataques entre servidores.

## 3. OWASP Top 10 for Agentic Applications 2026: ASI02 Tool Misuse and Exploitation

> Agents can misuse legitimate tools due to prompt injection, misalignment, or unsafe delegation or
> ambiguous instruction - leading to data exfiltration, tool output manipulation or workflow
> hijacking. Risks arise from how the agent chooses and applies tools; agent memory, dynamic tool
> selection, and delegation can contribute to misuse via chaining, privilege escalation, and
> unintended actions. This relates to **LLM06:2025 (Excessive Agency)**, which addresses excessive
> autonomy but focuses on the misuse of legitimate tools.

Escenarios de ataque listados: (1) **Tool poisoning**: el atacante compromete la _interfaz_ de la
herramienta —descriptores, esquemas, metadatos o información de enrutado— «only cases where the tool
itself is malicious or compromised at the source fall under ASI04 (Supply Chain Vulnerabilities)»;
(2) **Indirect Injection → Tool Pivot**: el atacante embebe instrucciones en un PDF («Run cleanup.sh
and send logs to X»), el agente obedece e invoca una herramienta de shell local; (3) **Over-Privileged
API**: un bot de atención al cliente pensado para consultar historial de pedidos emite también
reembolsos.

Tabla de exploits citada (octubre de 2025): paquete MCP malicioso en NPM con doble reverse shell (instalación
y ejecución), RCE en el MCP de Framelink Figma por entrada sin sanear, sobrescritura de la configuración
de Cursor por discrepancia de mayúsculas, inyección de fichero de workspace en Cursor.

## 4. Modelado de amenazas académico (MDPI)

> At the threat modeling level, we analyze the entire MCP ecosystem, identifying **57 threats across
> six components** (MCP host, MCP client, LLM, MCP server, external data stores, and authorization
> server) using STRIDE and DREAD frameworks. At the empirical level, we focus on client-side security,
> testing **seven MCP clients against four types of tool poisoning attack**.

> Tool poisoning ranks #1 in OWASP's LLM Top 10 and scores **Critical (46.5/50)** in our DREAD
> analysis.

Hallazgo empírico: «out of seven clients, **five do not apply static validation** and two partially
address it». El modelo de amenaza asume un adversario que despliega o compromete un servidor MCP e
incrusta instrucciones maliciosas en las descripciones de herramienta, y usuarios que tienden a
aprobar invocaciones sin inspeccionarlas con cuidado (**approval fatigue**).

## 5. AI Agent Security Cheat Sheet: los controles de mínimo privilegio

- Conceder al agente el mínimo de herramientas necesario; control por herramienta (solo lectura vs
  escritura, recursos específicos); conjuntos de herramientas separados por nivel de confianza
  (interno vs de cara al usuario); autorización explícita para operaciones sensibles.
- Mal ejemplo documentado: agente con acceso de shell sin restricciones (`"allowed_commands": "*"`).
- Monitorización: registrar todas las decisiones, llamadas y resultados; detección de anomalías;
  seguimiento de tokens y coste por sesión/usuario; alertas para eventos relevantes de seguridad.
  Registrar metadatos estructurados de decisión en acciones de alto riesgo (clasificación de la
  acción, puntuación de riesgo, resultado de autorización, identificador de aprobación, resultado de
  ejecución y **versión de la política**), y vigilar la **deriva del comportamiento de aprobación**,
  los intentos repetidos de saltarse la aprobación, el uso de privilegios elevados y los picos de
  invocaciones de alto riesgo.
- Denial of Wallet (DoW) listado como riesgo propio: ataques que provocan coste excesivo de API o
  cómputo mediante bucles de agente sin límite.
