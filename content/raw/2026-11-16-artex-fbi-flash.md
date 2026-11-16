---
title: "FBI FLASH-20261113-001: Threat Overview of ARTEX Autonomous Penetration Testing Framework"
source: "https://www.ic3.gov/CSA/2026/261113.pdf"
date: 2026-11-16
captured: 2026-11-16
---

# FBI FLASH-20261113-001 — ARTEX (13 de noviembre de 2026)

Fuente primaria: Federal Bureau of Investigation, FLASH-20261113-001, TLP:CLEAR, 13 de noviembre de 2026. Capturado el 2026-11-16. Texto completo en la caché de extracción: `/home/vilber/.hermes/cache/web/www.ic3.gov-43bf988e7f.md`.

## Summary (verbatim)

> The Federal Bureau of Investigation (FBI) is releasing this FLASH to highlight the tactics, techniques, and procedures (TTPs) and indicators of compromise (IOCs) associated with the ARTEX autonomous penetration testing framework. ARTEX is an open-source, large language model (LLM)-driven agentic platform that threat actors have weaponized to automate multiple phases of cyber intrusions at machine speed, from reconnaissance through data exfiltration. Since at least August 2026, a variety of malicious cyber actors have used ARTEX to conduct campaigns targeting organizations globally across multiple sectors, including financial services, government, technology, defense, semiconductor, energy, healthcare, manufacturing, telecommunications, and legal industries. ARTEX significantly reduces the time required to chain attack techniques, with some intrusions progressing from initial targeting to privileged access in under three hours. The framework enables threat actors with minimal technical expertise to conduct complex, multi-target operations simultaneously, fundamentally accelerating attack velocity and expanding operational scale. Notable campaigns include financially motivated attacks against South Korean financial institutions resulting in exfiltration of personal information from approximately 67,000 individuals, and a supply chain compromise affecting ConnectWise Cloud Backup customers that enabled access to more than 2,250 downstream tenants.

## Threat (verbatim, extractos)

> ARTEX is an autonomous, multi-agent penetration testing platform written in Go. The framework translates high-level tactical goals described in natural language into actionable machine commands executed by specialized super intelligence (SI) agents, requiring minimal human interaction beyond initial objective setting. ARTEX does not include its own SI model but integrates with external LLM providers, including frontier models (Anthropic Claude, OpenAI GPT) and open-source or Chinese-origin models (DeepSeek, GLM, Grok, Kimi). Analysis of attacker-controlled ARTEX instances shows Chinese models are most prevalent, with DeepSeek Flash family models dominating usage due to their balance of capabilities, relatively low cost, and lack of observable guardrails when framed for penetration testing.

> Originally released on GitHub by developer "Autumn-27" in July 2026, ARTEX gained rapid adoption, reaching an estimated 1,500–2,000 GitHub stars within 10 weeks. The developer stated the tool was intended for authorized security testing within defined scopes and made the repository unavailable on October 8, 2026, following reports of threat actor abuse. Despite this action, ARTEX remains widely accessible through independent routes and mirrors on code-sharing platforms. Following public disclosure of malicious usage, the original ARTEX developer removed the GitHub repository in October 2026. However, the framework continues to proliferate through community forks, localized variations, archived copies, and a commercial version (ARTEX PRO), ensuring continued availability to threat actors. As of early November 2026, researchers identified over 1,600 publicly exposed ARTEX console instances, with total deployments likely significantly higher when including systems behind firewalls or in private networks.

## Observed Capabilities and Potential Uses (verbatim)

> - **Accelerated Multi-Target Operations:** SI agents provide automation for the time-consuming phases of enumeration and exploitation; small threat groups can run concurrent intrusion campaigns at a scale previously unavailable to them.
> - **Exploitation of Overlooked Attack Surfaces:** ARTEX excels at identifying and exploiting peripheral systems receiving less security attention than flagship applications, including partner and supplier portals, mobile backends, employee applications, sales-support systems, legacy services, third-party integrations, and applications created across different business units.
> - **Supply Chain Compromise:** Agents have demonstrated capability to identify and exploit supply chain attack vectors, including modifying iOS application distribution infrastructure via exposed cloud credentials. Autonomous agents can systematically map trust relationships between organizations. By identifying and compromising weaker third-party vendors, CI/CD pipelines, or integrated software providers, attackers can leverage ARTEX to pivot from a peripheral supplier directly into high-value upstream enterprise networks.
> - **Reduced Barrier to Entry:** ARTEX lowers technical barriers for conducting complex intrusions, enabling threat actors with minimal expertise to execute sophisticated campaigns.
> - **Compressed Detection Window:** ARTEX generates high volumes of forensically noisy traffic that may trigger alerts, but attack speed provides limited time for coordinated defender response before objective completion.

## Observed TTPs mapped to MITRE ATT&CK (verbatim, extractos)

- **Initial Recon:** mapeo automático de permisos efectivos de credenciales Azure (SAS tokens, Service Principals, Kudu credentials, Storage Account keys) mediante comprobaciones sub-segundo; test blob writes/deletes; ARM deployment validation dry-runs; fuzzing de directorios web con 500+ peticiones; WHOIS asset mapping; escaneo activo de vulnerabilidades; consultas a `api.db-ip[.]com` para geolocalizar a la víctima. Técnicas: T1595, T1580, T1087.004, T1069.003, T1526.
- **Initial Access:** SAML sin firmar, XXE, subida anónima de ficheros, confianza cross-account, credenciales de terceros vía federación B2B, SSRF, contraseñas de administrador hardcoded en bundles SPA de JavaScript, APIs web sin autenticación, RCE por command injection, IDOR, credenciales administrativas débiles, RCE por SSTI, SQL injection, bypass de autenticación, VPN robadas. Técnicas: T1190, T1078, T1133, T1195, T1199, T1606.002, T1552.001.
- **Establish Foothold / Persistence:** web shells JSP y PHP (incl. vía MySQL log poisoning), abuso de Kudu administrative APIs, C2 en servidores Windows internos de bases de datos, RATs open-source (WISP, vshell, AdaptixC2), pares de claves SSH, Elastic IPs, account takeover, credenciales añadidas a OAuth apps existentes. Técnicas: T1505.003, T1078.004, T1098.001, T1574.001, T1036.005, T1105, T1059.
- **Privilege Escalation:** instancias cloud con roles IAM de alto valor, Kerberoasting, SQL injection para volcar credenciales de BD, DCSync para robar la clave krbtgt del dominio, cuentas con `is_admin=true`, resource-based constrained delegation, consultas al metadata service vía XXE, forja de token de administrador usando claves sin rotar.
- **Internal Recon:** PowerShell iterativo contra Domain Controllers; enumeración de más de 110.000 objetos de Active Directory; lectura de contraseñas LAPS; inventario de cobertura de sensores para identificar máquinas Windows sin CrowdStrike Falcon.
- **Lateral Movement:** Pass-the-Ticket, WinRM, Kerberos relay, Pass-the-Hash (bloqueado por protección de endpoint).
- **Collection / Exfiltration Prep:** interrogación de bases SQL backend, lecturas masivas de blobs, boot scripts personalizados vía instancias EC2, salida enviada a endpoints rotativos de webhook.site, lectura de buzones en servidor de correo comprometido, volúmenes nuevos de 100GB para exfiltración.
- **Command and Control:** proxies residenciales, Tor, SOCKS proxies, relays comprometidos, túneles vía Chisel y SoftEther, BLOODALCHEMY comunicando con dominios C2.

## IOCs (extractos, verbatim)

- IPs: `38.244.50[.]120` (ARTEX host, campaña financiera surcoreana), `144.172.64[.]60/99/128` (campaña ConnectWise), `187.15.88[.]186`, `187.15.90[.]217`, `187.15.89[.]186` (Graph API vía apps comprometidas), proxies de la campaña surcoreana (`101.53.80[.]20`, `205.214.59[.]31`, `124.155.252[.]63`, `154.201.79[.]246`, `23.248.249[.]90`, `23.158.220[.]98`, `103.248.148[.]84`, `203.160.133[.]172`, `209.209.85[.]38`), nodos C2 de WISP `199.19.95[.]66/67/68` (Storm-3358), servidores ARTEX `91.92.240[.]238`, `85.11.168[.]45`, `178.16.54[.]129`, `31.77.229[.]35`, C2 `85.11.167[.]52`.
- Dominios: `xcai[.]pro` (revendedor de API LLM, campaña surcoreana).
- Indicadores de red y comportamiento: llamadas salientes a `api.anthropic.com`, `api.deepseek.com`, `open.bigmodel.cn`, `api.x.ai`; peticiones HTTP de alta frecuencia con enumeración secuencial contra endpoints de login/search; transferencias salientes de datos estructurados (nombres, teléfonos, información financiera) por HTTPS a destinos externos no autorizados; web shells `*.aspx` o `*.jsp` en rutas inesperadas.

## Recomendaciones del FBI (extractos, verbatim)

- Reducir la superficie de ataque externa: inventariar todas las aplicaciones expuestas a Internet incluyendo sistemas periféricos; restringir administración cloud, gestión de dispositivos de red, interfaces de publicación (Kudu/SCM), hipervisores y plataformas de backup a redes de confianza; deshabilitar la autenticación básica de publicación donde no se requiera; gobernar la asignación de IPs públicas con revisión de arquitectura antes de exponer interfaces de gestión; mover aplicaciones empresariales detrás de soluciones Zero Trust.
- Preservar evidencia y responder: preservar registros de sign-in de Microsoft Entra, Microsoft Purview Audit, SIEM y telemetría de Microsoft Graph; revisar actividad desde al menos el 1 de octubre de 2026 para lo relacionado con ConnectWise; extender la revisión de service-principal sign-ins; si se confirma actividad sospechosa, que un respondedor autorizado elimine credenciales no autorizadas tras preservar evidencia; mantener deshabilitadas las conexiones de la aplicación ConnectWise afectada hasta instrucciones formales de restauración; no borrar enterprise applications como primera respuesta.

## Información solicitada por el FBI

Infraestructura ARTEX (código/fuentes, capturas del console, ficheros de configuración), logs de autenticación y acceso, actividad de aplicación/API (Microsoft Graph, Entra audit, M365 audit, violaciones de rate limit), indicadores de infraestructura LLM/SI (conexiones salientes a endpoints LLM, software de gateway/revendedor LLM como CLIProxyAPI o New API, anomalías de facturación), actividad cloud y de contenedores (AWS IAM, dry-runs de ARM, test blob write/delete, credenciales Kudu/SCM), y artefactos de explotación/persistencia (web shells, BLOODALCHEMY, RATs WISP/vshell/AdaptixC2).

## Referencias citadas por el FLASH

Akamai (23-oct-2026); Microsoft Security Research & Threat Intelligence (21-oct-2026); Google Threat Intelligence Group (30-oct-2026); Censys (5-nov-2026); Google Threat Intelligence Group y Mandiant (30-oct-2026); CrowdStrike (7-oct-2026); Zscaler ThreatLabz (14-oct-2026); CERT-EU (5-nov-2026); Check Point Research (5-nov-2026); Microsoft Threat Intelligence (nov-2026).
