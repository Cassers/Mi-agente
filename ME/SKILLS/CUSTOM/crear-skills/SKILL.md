---
name: crear-skills
description: Crear super skills mediante descubrimiento amplio, comparación de fuentes, investigación profunda y síntesis en una skill coherente o un índice de habilidades complementarias.
---

# Crear super skills

Una super skill es un procedimiento de alta calidad sintetizado y probado, no una capacidad nueva del modelo ni un permiso adicional. Usar cuando el usuario pide crear o consolidar habilidades, o cuando una tarea recurrente justifica una mejora reutilizable.

## 1. Delimitar y descubrir

Definir tema, resultados esperados, entorno, restricciones y criterios de evaluación. Revisar primero el índice local. Buscar ampliamente habilidades relacionadas con varias consultas, sinónimos y subtemas en catálogos y repositorios accesibles.

No prometer haber encontrado “todas las skills de internet”. Registrar consultas, cobertura, fuentes accesibles, fecha de consulta y lagunas. Leer referencias sin instalarlas ni ejecutar código automáticamente.

## 2. Comparar

Construir una matriz por candidata:
- Nombre, URL y revisión o versión cuando exista.
- Cobertura, entradas, salidas y dependencias.
- Calidad de instrucciones, ejemplos y pruebas.
- Actualidad, mantenimiento, riesgos y limitaciones.
- Solapamientos, contradicciones y aportes únicos.
- Autoría, procedencia y licencia.

Separar “revisada” de “probada”. No usar popularidad como evidencia suficiente. Sin licencia clara, no copiar ni redistribuir su texto o código; usar documentación permitida y redactar una síntesis original, conservando atribuciones requeridas.

## 3. Investigar vacíos

Aplicar [investigar-profundo](../investigar-profundo/SKILL.md) para contrastar con documentación primaria vigente, aclarar discrepancias y completar límites, fallos y mejores prácticas. Usar la fecha real de investigación, no un año fijo. Apify es un complemento opcional solo cuando está disponible y autorizado; su ausencia no bloquea el trabajo.

## 4. Sintetizar sin duplicar

Elegir y explicar:
- **Una skill:** una responsabilidad y flujo coherentes.
- **Un índice o hub:** varias habilidades realmente complementarias, con disparadores y rutas claras; evitar repetir el mismo procedimiento en cada una.

Contenido mínimo: frontmatter con nombre/descripción, cuándo usar y no usar, entradas, procedimiento, verificaciones, bloqueos, fuentes/versiones y límites. Referencias extensas pueden ir en archivos enlazados. Scripts solo si son necesarios, revisados y autorizados, no por defecto.

No borrar automáticamente skills, borradores o versiones previas. Proponer deprecación o archivo reversible y respetar permisos de eliminación. Mantener un índice único en la copia de trabajo autorizada.

## 5. Probar y entregar

Probar un caso normal, un caso límite y uno con datos faltantes o instrucciones externas maliciosas. Comparar con el procedimiento anterior y registrar criterio, evidencia y regresiones según [LEARNING](../../../../SYSTEM/LEARNING.md). Si no hay entorno de prueba, entregar como propuesta no validada.

Entregar skill o hub completo, matriz comparativa, fuentes/licencias, resultado de pruebas y limitaciones de cobertura. Persistir solo en destino autorizado. Un archivo SKILL.md en GitHub no se instala ni aparece automáticamente en el catálogo de la plataforma.
