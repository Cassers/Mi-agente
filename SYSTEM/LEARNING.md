# Mejora basada en experiencia

“Aprender” aquí significa mejorar instrucciones, ejemplos y pruebas reutilizables. No cambia pesos del modelo, no implica autoentrenamiento, ni garantiza memoria entre sesiones.

## Ciclo

1. **Observar:** describir un fallo o mejora con evidencia verificable y contexto mínimo.
2. **Generalizar:** separar el procedimiento reutilizable de datos personales y particularidades del caso.
3. **Proponer:** cambio pequeño a una instrucción o skill, motivo y efecto esperado. No cambiar autorizaciones ni políticas.
4. **Probar:** comparar versión anterior y propuesta con el mismo caso anonimizado, un caso normal y un caso límite. Definir de antemano qué cuenta como mejora y comprobar regresiones.
5. **Revisar:** distinguir hipótesis de resultado probado. Buscar revisión independiente cuando esté disponible; declarar si fue autoevaluación.
6. **Versionar:** en un destino autorizado, registrar versión, fecha, resumen de evidencia, pruebas, limitaciones y versión previa. Publicar en este repo solo cambios genéricos pedidos y revisados.
7. **Revertir:** si empeora calidad o rompe límites, volver a la última versión validada y registrar el motivo. No borrar evidencia útil de forma irreversible.

## Ficha vacía de cambio

- Componente / versión anterior / versión propuesta:
- Problema observado:
- Evidencia anonimizada y procedencia:
- Cambio y resultado esperado:
- Casos y criterios de prueba:
- Resultado y posibles regresiones:
- Revisión y limitaciones:
- Destino autorizado / decisión:
- Versión para revertir:

No hay mejoras validadas registradas todavía. No persistir datos del usuario en el starter público ni tratar feedback aislado como permiso permanente.
