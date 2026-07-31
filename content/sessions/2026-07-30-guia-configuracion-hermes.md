---
title: Informe-2026-07-30
date: 2026-07-30
tags: [hermes, configuración, agentes]
---
# Informe-2026-07-30: Guía de configuración y optimización de Hermes Agent

Este informe resume los puntos clave para el uso eficiente de Hermes Agent, extraído de la documentación técnica revisada.

## 1. Instalación y Seguridad
Hermes Agent se instala vía script de terminal (`hermes setup`). Dada su capacidad de control del sistema (Computer Use), es vital aislarlo en un contenedor Docker o VPS dedicado para evitar riesgos.

## 2. Optimización Económica
Para evitar costes excesivos en la API:
- **Uso de comandos efímeros**: Activar/desactivar MCP servers según necesidad.
- **Enrutamiento inteligente**: Utilizar routers como el de Open Router para derivar tareas simples a modelos baratos.
- **Compresión de historial**: Ejecutar el comando `compress` regularmente para limpiar el contexto sin perder lo esencial.
- **Límites duros**: Configurar `hard stop` y límites de turnos (ej. 60 en lugar de 150) para evitar bucles.

## 3. Control y Memoria
- **Control por voz**: Utilizar los sistemas TTS nativos para interfaces manos libres.
- **Memoria Hinign**: La base de datos local Hinign permite al agente recordar hechos críticos sin consultar la API, mejorando la precisión y reduciendo el consumo de tokens.

## 4. Gestión de Subagentes
El sistema permite la creación de subagentes con perfiles específicos (como "Agente Hugo") y la organización mediante un Kanban integrado (Triaje, Por hacer, En progreso, Hecho).

---
*Este conocimiento fue procesado a partir de la documentación técnica y las sesiones de usuario el 30 de julio de 2026.*
