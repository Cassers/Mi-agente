# Arranque portable

## 1. Confirmar intención y versión

Si el usuario solo comparte una URL, preguntar si quiere revisión o adopción. Si ya pidió usar el kit, no volver a preguntar lo mismo. Resolver la rama `dots-multiagents` y registrar el commit leído en el informe de configuración; no asumir que la rama principal contiene esta adaptación.

Leer README, AGENTS y los documentos SYSTEM enlazados, incluido SYSTEM/MEMORY.md. No descargar todo, ejecutar scripts ni instalar skills como parte de este arranque.

## 2. Comprobar capacidades reales

Comprobar lectura de repositorio, herramientas de delegación, acceso a fuentes y escritura/persistencia autorizada. No solicitar accesos que no sean necesarios para la tarea actual. No inferir una herramienta por una mención en Markdown.

- Multiagente disponible: mapear coordinador y tareas a herramientas nativas.
- Sin multiagente: resolver secuencialmente con los mismos criterios de calidad.
- Sin persistencia: conservar solo el contexto de sesión y explicar la limitación.
- Sin acceso al repositorio: solicitar los archivos necesarios.

## 3. Adoptar sin sobrescribir

Conservar nombre, contexto y preferencias existentes del asistente. No iniciar una entrevista de identidad ni suponer que la memoria está vacía. Consultar el registro; un registro vacío no exige crear especialistas preventivamente.

Las plantillas `ME/` y `SYSTEM/IA_TEMPLATE/` permanecen genéricas en el repositorio público. Solo una solicitud concreta con destino autorizado permite crear una copia de trabajo o persistir configuración; leer el kit no autoriza commits, publicaciones ni cambios de cuenta.

## 4. Respuesta de arranque

Informar brevemente:
- Rama y commit leídos.
- Guía adoptada y objetivo actual, si existe.
- Delegación real o ejecución secuencial.
- Persistencia disponible, destino autorizado o limitación.
- Siguiente paso y cualquier permiso estrictamente necesario.

No decir “instalado”, “configurado permanentemente” o “agentes activos” sin comprobarlo. Si no hay una tarea, quedar listo para recibirla sin activar ejemplos.

## Comprobación de aceptación

- URL sola: pregunta por intención, no instalación.
- Petición explícita: adopta la guía compatible sin pedir autorización repetida.
- Sin herramientas: informa la limitación y ofrece modo secuencial.
- Sin destino privado: no escribe datos personales en GitHub.
- Registro vacío: no inventa especialistas ni ejecuciones.
- Ejemplo enlazado: no se activa durante el arranque.
