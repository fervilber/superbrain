---
title: "FastMCP 4.2 y Skills over MCP (SEP-2640): catálogo de skills del lado del servidor"
source: "https://modelcontextprotocol.info/blog/fastmcp-4-2-skills-over-mcp/"
date: 2026-11-22
captured: 2026-11-22
---

# FastMCP 4.2 y Skills over MCP: qué cambia para tu agente

Captura de _FastMCP 4.2 and Skills over MCP: What Changes for Your Agent_, MCP Community, **17 de
noviembre de 2026**.

**FastMCP 4.2.0**, publicado el **13 de noviembre**, añade un **catálogo de skills del lado del
servidor**. Los equipos pueden mantener una _skill_ junto a las herramientas que describe y dejar que
los clientes la recuperen de ese servidor, en lugar de distribuir una carpeta separada a cada máquina.
Esto ayuda a distribuir cambios; **decidir si cargar y ejecutar esas instrucciones sigue siendo
competencia del host**.

La versión implementa la extensión experimental **Skills over MCP**, asociada a **SEP-2640**. Tres
cosas distintas que no hay que confundir: FastMCP `4.2.0` es una versión de framework,
`io.modelcontextprotocol/skills` es un identificador de extensión, y la revisión del protocolo MCP es
una elección aparte. **Actualizar una no demuestra soporte de las otras.**

## Qué se entrega realmente

Una _skill_ es instrucciones más ficheros de apoyo. Las herramientas MCP describen operaciones
invocables; una skill puede explicar **cuándo y cómo** un agente debe combinar esas operaciones.
Servir los ficheros de instrucciones **no concede por sí mismo permisos de herramienta** ni hace que el
host las ejecute.

| Capa                                        | Qué provee                                                                          | Qué falta por establecer                                                        |
| ------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `Skill` y `SkillCatalogProvider` de FastMCP | Cargar skills autoradas y exponer un catálogo junto a las herramientas del servidor | Qué directorios y ficheros piensas publicar, y quién puede leerlos              |
| `skills/list` y `skills/get`                | Descubrimiento consciente de la extensión y manifiesto de skill                     | Negociación de extensión cliente-servidor, incluidas implementaciones parciales |
| `resources/read`                            | Leer el contenido de las instrucciones y ficheros de apoyo                          | Disponibilidad del fichero, tamaño y consistencia del digest                    |
| `Client.read_skill()` y `to_directory()`    | Verificar una skill obtenida y exportarla a un directorio local                     | Política de instalación local, revisión y ejecución específica del host         |

La versión también expone los ficheros de skill como **recursos ordinarios** para clientes que carecen
de descubrimiento consciente de la extensión. Un `resources/read` exitoso es por tanto evidencia útil
de acceso a ficheros, pero **no demuestra soporte de `skills/list`, descubrimiento automático,
instalación local o ejecución**.

## Antes de adoptar la 4.2

Comprueba primero Python: **FastMCP 4.2 requiere Python 3.11 o superior**. En un entorno de prueba
separado, fija `fastmcp==4.2.0` para que la API que revisas sea la API que ejecutas. No sustituyas el
entorno MCP SDK existente de un host solo para probar la función.

El código de registro del servidor es:

```python
from fastmcp import FastMCP, Skill
from fastmcp.skills.provider import SkillCatalogProvider

skill = Skill.from_directory("skills/deploy")
mcp = FastMCP("Team Skills")
mcp.add_provider(SkillCatalogProvider([skill]))
```

## Implicaciones

- Las _skills_ —el patrón que Hermes Agent popularizó como unidad de conocimiento reutilizable—
  cruzan la frontera del protocolo y pasan a ser **objetos distribuibles por MCP**, con descubrimiento
  y manifiesto propios.
- La separación explícita entre _servir instrucciones_ y _conceder permisos o ejecutar_ es el punto
  clave de seguridad: el catálogo no amplía la superficie de ejecución por sí solo.
- La advertencia de "versión de framework ≠ identificador de extensión ≠ revisión de protocolo"
  anticipa el problema de compatibilidad de una pila MCP que ahora crece por extensiones.
