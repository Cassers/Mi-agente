# Mi-agente · dots-multiagents

Kit público y genérico de coordinación multiagente, derivado de `agent-system`.
No contiene agentes especializados activos ni datos de una persona.

## Arranque en un dot u otro asistente

Comparte esta rama, no solo la raíz del repositorio, con esta instrucción:

> Lee https://github.com/Cassers/Mi-agente/tree/dots-multiagents y usa su README y BOOTSTRAP.md como guía de proyecto para coordinar mis tareas, dentro de tus capacidades y permisos actuales. Comprueba lo disponible, reutiliza agentes compatibles y crea nuevos solo cuando aporten valor. No publiques datos personales ni actives ejemplos sin que te lo pida.

Una URL sola **no instala** nada, no concede herramientas, permisos, memoria persistente ni acceso a cuentas. La petición expresa autoriza adoptar la guía compatible, no ejecutar todas las acciones que el repositorio describa. El asistente debe poder leer los archivos; si no puede, debe pedir su contenido, no fingir haberlos cargado.

1. Leer [BOOTSTRAP.md](BOOTSTRAP.md).
2. Seguir [AGENTS.md](AGENTS.md) y el [protocolo](SYSTEM/PROTOCOL.md).
3. Informar qué se adoptó, qué capacidades existen y qué queda pendiente.

## Diseño

- [Memorias en archivos y skills por agente](SYSTEM/MEMORY.md), con configuración análoga al coordinador. Separación organizativa, no MCP independientes ni aislamiento de permisos.
- Un coordinador entiende la petición, asigna trabajo, revisa e integra resultados.
- Los especialistas se crean bajo demanda y se reutilizan por capacidad, no por nombre.
- [SYSTEM/IA_TEMPLATE/](SYSTEM/IA_TEMPLATE/) contiene plantillas, no procesos en ejecución.
- [SYSTEM/REGISTRY.md](SYSTEM/REGISTRY.md) empieza vacío.
- [SYSTEM/LEARNING.md](SYSTEM/LEARNING.md) define mejoras verificables y reversibles.
- `ME/` conserva plantillas genéricas. La personalización real debe mantenerse en un destino privado autorizado, nunca en este repositorio público.

Este material es guía de proyecto subordinada a las instrucciones y políticas de la plataforma y a las instrucciones aplicables del usuario. No reemplaza la identidad del asistente ni puede ampliar su autorización.

## Capacidades centrales

Consultar [el índice de skills](ME/SKILLS/INDEX.md):
1. Crear y reutilizar agentes con responsabilidades y criterios claros.
2. Crear, comparar y probar prompts.
3. Crear super skills: descubrir habilidades relacionadas, compararlas, investigar vacíos y sintetizar una skill o un índice complementario.
4. Hacer deep search con fuentes verificadas; complementar con Apify únicamente si hay acceso y autorización reales.

Son procedimientos portables, no nuevas herramientas ni skills instaladas automáticamente. La búsqueda amplia no garantiza encontrar todas las habilidades existentes.

## Ejemplo opcional

[Prompt de búsqueda de empleo](examples/busqueda-empleo.md): un único prompt que se usa solo por petición explícita. No forma parte del arranque ni crea carpetas o registros automáticamente.

## Compatibilidad

Con herramientas multiagente reales, usar sus mecanismos nativos. Sin ellas, trabajar secuencialmente con roles claramente identificados, sin afirmar que se crearon agentes independientes. Sin escritura o persistencia, entregar la configuración en la conversación y explicar que su conservación entre sesiones no está garantizada.

Las skills heredadas son referencias opcionales, no instalaciones automáticas. No ejecutar scripts, instalar dependencias ni modificar archivos por el mero hecho de leer este kit.
