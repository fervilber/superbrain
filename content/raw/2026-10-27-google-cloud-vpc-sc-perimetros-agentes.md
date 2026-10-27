---
title: "Google Cloud VPC Service Controls: perímetros heredados por carpeta, endpoints PSC y service patterns para agentes"
source: "https://blog.ogwilliam.com/post/gcp-vpc-service-controls-scalable-perimeters"
author: "William OGOU (citando el blog de Google Cloud, Pratik Bhangale, 16 de octubre de 2026)"
date: 2026-10-16
captured: 2026-10-27
---

# Captura: VPC-SC con perímetros escalables (contexto técnico)

Los agentes autónomos de IA actúan como identidades no humanas (NHI) de alta velocidad, consultando APIs y moviendo datos entre proyectos de Google Cloud mucho más rápido que operadores humanos. Mientras IAM Deny y las Organization Policies gobiernan _quién_ puede actuar y _cómo_ se configuran los recursos, **VPC Service Controls (VPC-SC)** aplica el perímetro de datos a nivel de servicio, de modo que credenciales robadas, bindings IAM mal configurados o agentes comprometidos no puedan exfiltrar datos fuera de la frontera.

Históricamente, operar VPC-SC a escala empresarial significaba mantener listas frágiles proyecto por proyecto, chocar con las cuotas de atributos de ingress/egress y pasar días depurando denegaciones `Request is prohibited by organization's policy`. El 16 de octubre de 2026 Google Cloud destacó cinco capacidades de VPC-SC —sin coste adicional— que alinean los perímetros directamente con la jerarquía de recursos y la arquitectura de red privada.

## Qué cambió de un vistazo

| Capacidad                                              | Etapa   | Qué resuelve                                                                                                                             |
| ------------------------------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Membership de carpetas en perímetros**               | GA      | Protege automáticamente todos los proyectos y subcarpetas anidadas bajo `folders/FOLDER_ID`.                                             |
| **Carpetas y organizaciones en reglas ingress/egress** | GA      | Reemplaza listas largas de proyectos por `folders/FOLDER_NUMBER` u `organizations/ORG_NUMBER`, evitando agotar la cuota de reglas.       |
| **Endpoints PSC en reglas ingress/egress**             | GA      | Limita el acceso entre perímetros a una regla de reenvío concreta de Private Service Connect (`pscEndpoint`).                            |
| **Service patterns en servicios accesibles por VPC**   | GA      | Permite patrones de URL granulares y cabeceras de restricción de organización sobre `private.googleapis.com` o endpoints PSC `all-apis`. |
| **Guided Violation Remediation**                       | Preview | Propone arreglos de mínimo privilegio (ingress, egress, access level o servicio accesible) en el Violation Analyzer.                     |

## 1. Membership de carpeta en el perímetro

En lugar de actualizar definiciones de perímetro cada vez que una plataforma entrega un proyecto nuevo, ahora se puede adjuntar `folders/FOLDER_ID` directamente a un perímetro (enforcement o dry-run). Cada proyecto hijo y subcarpeta anidada hereda la política del perímetro automáticamente, y mover un proyecto dentro o fuera de una carpeta actualiza su cobertura dinámicamente.

```bash
# Añadir una carpeta a un perímetro en enforcement
gcloud access-context-manager perimeters update prod_data_perimeter \
    --add-resources="folders/789012345678" \
    --policy=POLICY_ID

# Verificar de qué perímetro hereda un proyecto desde su jerarquía de carpetas
gcloud access-context-manager lookup-configured-perimeter \
    --resource="projects/345678901234"
```

El comando de lookup devuelve tanto los bindings explícitos de proyecto como los heredados de carpeta (`restrictedResource` y `restrictedResourceDryRun`).

**Caveat operativo:** al migrar perímetros existentes a nivel de proyecto hacia perímetros por carpeta, hay que esperar a la ventana de **propagación de jerarquía de 48 horas** antes de retirar los bindings explícitos de proyecto, para que las cargas no sufran huecos de cobertura transitorios.

## 2. Carpetas y organizaciones en reglas ingress/egress

Los entornos multi-proyecto y los flujos de trabajo agénticos chocan con frecuencia con los límites de tamaño y atributos de reglas de VPC-SC al autorizar servicios compartidos entre cientos de proyectos. Las reglas ingress/egress ahora aceptan `folders/FOLDER_NUMBER` y `organizations/ORGANIZATION_NUMBER` en los bloques `sources` y en los `resources` destino.

**Caveat operativo:** al especificar `egressFrom.sources` hay que fijar `sourceRestriction: SOURCE_RESTRICTION_ENABLED` (si no, VPC-SC ignora el bloque `sources`). Además, especificar una carpeta u organización en reglas ingress/egress permite el acceso de recursos cuyo padre está en ese nodo de jerarquía y que no pueden encerrarse ellos mismos en un perímetro.

## 3. Endpoints PSC en reglas ingress/egress

Las empresas que estandarizan en Private Service Connect —incluidos endpoints propagados entre spokes vía Network Connectivity Center— pueden ahora autorizar tráfico basándose en la regla de reenvío PSC exacta (`pscEndpoint`) en lugar de una red VPC o proyecto amplios.

### Ejemplo YAML (carpetas + endpoint PSC)

```yaml
- title: Allow AI Agents Folder via Dedicated PSC Endpoint
  ingressFrom:
    identities:
      - serviceAccount:agent-runtime@proj.iam.gserviceaccount.com
    sources:
      - resource: folders/112233445566
      - pscEndpoint:
          forwardingRule: //compute.googleapis.com/projects/net-hub-prod/global/forwardingRules/psc-vpcsc-endpoint
  ingressTo:
    operations:
      - serviceName: bigquery.googleapis.com
        methodSelectors:
          - method: google.cloud.bigquery.v2.JobService.InsertJob
    resources:
      - folders/998877665544
```

**Caveats operativos para PSC en VPC-SC:**

- Crear el endpoint PSC usando el bundle de API objetivo **`vpc-sc`** para servicios restringidos.
- Solo se soportan endpoints PSC creados de nuevo; los endpoints legados creados antes de esta función deben recrearse para poder referenciarse en reglas de perímetro.
- Las entradas de `sources` (`resource`, `accessLevel`, `pscEndpoint`) se evalúan como condición **OR** entre sí, y se combinan con **AND** respecto a `identities` / `identityType`.

## 4. Service patterns en servicios accesibles por VPC

Los servicios accesibles clásicos exigen enrutar el tráfico al VIP restringido (`restricted.googleapis.com`), que bloquea todas las APIs de Google no soportadas por VPC-SC. A la inversa, enrutar al VIP privado (`private.googleapis.com`) o a un bundle PSC `all-apis` permite el acceso por defecto a APIs no soportadas, creando una vía de exfiltración si no se vigila.

Los **service patterns** cierran ese hueco en la ruta del VIP privado (`GOOGLE_APIS_VIA_PRIVATE_PATH`). Permiten `RESTRICTED-SERVICES` junto a patrones de URL explícitos (`API_NAME.googleapis.com/*`, `www.googleapis.com/API_NAME/*` o `*.appspot.com/*`) e inyectar cabeceras de restricción de organización (`X-Goog-Allowed-Resources`, `X-GoogApps-Allowed-Domains`) sin desplegar un proxy de egress propio.

```yaml
enableRestriction: true
servicePatternsEnforcementScopes:
  - GOOGLE_APIS_VIA_PRIVATE_PATH
allowedServicePatterns:
  - service: "RESTRICTED-SERVICES"
  - service: "logging.googleapis.com"
  - pattern: "maps.googleapis.com/*"
  - pattern: "appengine.googleapis.com/*"
modifiers:
  - addRequestHeader:
      key: "X-Goog-Allowed-Resources"
      value: "YOUR_BASE64_ORG_RESTRICTION_HEADER"
```

```bash
gcloud access-context-manager perimeters update prod_data_perimeter \
    --set-vpc-accessible-services=vpc_accessible_services.yaml \
    --policy=POLICY_ID
```

**Caveats operativos:**

- Al migrar de `restricted.googleapis.com` a `private.googleapis.com`, aplicar la configuración de service patterns al perímetro **antes** de cambiar DNS y enrutamiento.
- Los modificadores `addRequestHeader` solo adjuntan cabeceras a servicios no soportados y **no** inyectan cabeceras cuando el perímetro está solo en dry-run.

## Fuentes del autor

- Google Cloud Blog: "Modernizing perimeter security: Scalable perimeters with VPC Service Controls" (Pratik Bhangale, 16 de octubre de 2026).
- Documentación: Configure folders in service perimeters; Ingress and egress rules for VPC Service Controls; Configure Private Service Connect endpoints in service perimeters; Limit access by using service patterns; Resolve access denials with remediation suggestions.
