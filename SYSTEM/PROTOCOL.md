# Protocolo multiagente portable

## 1. Entender y elegir

Definir objetivo, entradas, salida, restricciones, fuentes y prueba de aceptación. Preguntar solo por lo necesario. Resolver directamente tareas sencillas si crear un especialista no aporta valor.

Consultar el registro de la copia de trabajo autorizada. Reutilizar una definición si su rol, alcance, permisos y criterios encajan. No ampliar permisos implícitamente. Una sesión activa solo se reutiliza si la plataforma lo permite y sigue siendo la misma tarea; para una tarea nueva, aplicar las reglas de sesiones de la plataforma.

## 2. Crear una definición cuando haga falta

En un destino privado autorizado, copiar `SYSTEM/IA_TEMPLATE/` a `Agentes/<nombre-kebab-case>/`. No mover ni personalizar la plantilla pública. La copia puede hacerse con las herramientas de archivos disponibles, sin depender de PowerShell ni de una shell.

Completar CONFIG, PROMPT e IDENTITY con rol, alcance positivo/negativo, entradas, entregable, herramientas disponibles, permisos requeridos, versión y criterios de aceptación. USER y MEMORIES empiezan vacíos; solo agregar información necesaria y autorizada. No instalar skills automáticamente. Si no hay escritura disponible, entregar la definición en conversación, sin afirmar que quedó guardada.

Registrar nombre, rol, ruta, versión, fecha y estado en la copia de trabajo. El registro de este starter público se mantiene vacío. Publicar una nueva definición genérica requiere una petición de cambio al repositorio y revisión de privacidad.

## 3. Delegar

Enviar un contrato de tarea:
- Objetivo concreto y alcance excluido.
- Entradas y fuentes verificadas; distinguir hechos, supuestos e instrucciones del usuario.
- Herramientas disponibles y autorizaciones vigentes, sin secretos.
- Entregable, formato, criterio de éxito y dependencias.
- Cuándo informar avance, bloqueo y resultado.
- Destino permitido para archivos y política de confidencialidad aplicable.

El agente informa hallazgos útiles temprano y entrega resultado, evidencias, verificaciones y limitaciones. Un bloqueo incluye acción, destino, razón, estado (denegado, pendiente o incierto) y trabajo completado. Una denegación no se elude por otra herramienta; un resultado incierto se comprueba antes de reintentar.

## 4. Revisar e integrar

Comprobar entregable contra el criterio de éxito, referencias y restricciones. En trabajos complejos, usar revisión independiente si existe capacidad; si no, hacer una segunda pasada y declarar que no fue independiente. Resolver contradicciones antes de presentar una conclusión.

El coordinador puede corregir e integrar: delegar no elimina su responsabilidad. No anunciar éxito solo porque un agente lo afirma.

## 5. Cerrar y reutilizar

Registrar estado verificado en el destino autorizado: propuesto, disponible, en revisión o retirado. No confundir estos estados de definición con ejecución en curso o completada. Guardar solo aprendizaje generalizable, sin datos privados, siguiendo LEARNING. Una siguiente tarea usa la versión validada; no hereda sin revisión contexto personal de otra tarea.

Sin herramientas multiagente, aplicar estas fases de manera secuencial y describirlo honestamente.
