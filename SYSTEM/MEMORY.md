# Memorias en archivos y contexto por agente

El coordinador y cada agente pueden usar una configuración análoga en una **copia privada autorizada**:

| Coordinador | Agente | Propósito |
| --- | --- | --- |
| ME/CONFIG.md | Agentes/<nombre>/CONFIG.md | Alcance, herramientas, destino y versión |
| ME/PROMPT.md | Agentes/<nombre>/PROMPT.md | Instrucciones de trabajo |
| ME/IDENTITY.md | Agentes/<nombre>/IDENTITY.md | Rol e identidad de la definición |
| ME/USER.md | Agentes/<nombre>/USER.md | Contexto mínimo autorizado |
| ME/MEMORIES/GENERAL.md | Agentes/<nombre>/MEMORIES/GENERAL.md | Hechos estables necesarios |
| ME/MEMORIES/SPECIFIC.md | Agentes/<nombre>/MEMORIES/SPECIFIC.md | Índice a archivos por tema |
| ME/SKILLS/INDEX.md | Agentes/<nombre>/SKILLS/INDEX.md | Índice de habilidades pertinentes |
| ME/SKILLS/CUSTOM/ | Agentes/<nombre>/SKILLS/CUSTOM/ | Procedimientos propios |

## Lectura y escritura

Cargar CONFIG, PROMPT, GENERAL y los índices pertinentes; abrir solo las memorias temáticas y skills necesarias. Mantener GENERAL breve. Cada nota temática debe indicar hecho o inferencia, fuente, fecha, contexto, vigencia y acciones pendientes. Corregir información obsoleta y evitar duplicados. No conservar secretos; minimizar información personal.

Antes de escribir, comprobar destino privado, permisos y necesidad. Si no existe persistencia disponible, explicar que el contexto puede perderse entre sesiones y entregar un resumen exportable si se solicita. Un archivo en GitHub no se sincroniza automáticamente con la memoria o catálogo de skills de una plataforma.

No compartir memoria completa entre agentes: transferir un resumen mínimo pertinente y autorizado. El coordinador integra aprendizajes generales sin copiar datos privados entre tareas. La plantilla pública permanece vacía.

## Límites reales

Las carpetas y skills separan **organización y contexto**, no crean un sandbox de permisos. No configuran MCP independientes ni conexiones separadas por agente. Las herramientas y credenciales son las que la plataforma realmente proporciona; cada acción sigue sus permisos. Una instrucción “solo usa estos archivos” no prueba aislamiento técnico.

El arranque no crea conexiones, claves, cuentas ni permisos nuevos. Separar conexiones requiere soporte real de la plataforma y autorización específica; no se emula mediante Markdown.
