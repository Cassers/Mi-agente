---
name: investigar-profundo
description: Mi super skill para investigar cualquier tema de forma profunda y reciente. Yo la uso cuando necesito entender a fondo, comparar opciones, buscar recomendaciones, consejos y buenas prácticas actuales (2026), o antes de crear una skill. Sintetizo solo lo no-obvio con fuentes verificadas.
---

# Investigar profundo

Yo investigo para decidir bien, no para acumular texto. Busco información reciente, la comparo, me quedo con lo útil y cito mis fuentes.

Yo uso esta skill cuando:
- Me piden investigar, comparar, analizar o entender un tema a fondo
- Necesito recomendaciones, consejos y buenas prácticas recientes
- Voy a crear una skill y necesito el Paso 2 de `crear-skills`
- Hay información contradictoria o desactualizada y necesito aclararla

## Mis principios

1. Yo priorizo lo reciente (2026) y lo oficial sobre lo viejo y lo opinativo
2. Yo me quedo solo con lo no-obvio y lo que justifica su costo en tokens
3. Yo no invento URLs ni datos. Si no lo verifiqué, lo digo
4. Yo sintetizo, no copio. Traduciendo a acciones concretas
5. Yo trabajo en español y en primera persona, conciso y directo

## Mi flujo obligatorio

Yo sigo estos 6 pasos en orden.

### Paso 1 - Entiendo qué necesito

Yo aclaro antes de buscar:
1. Objetivo: ¿qué decisión o entrega necesito producir?
2. Alcance: ¿qué incluyo y qué excluyo?
3. Preguntas clave: escribo 3-7 preguntas que mi investigación debe responder
4. Nivel: ¿necesito respuesta rápida, comparativa o profunda para crear skill?

Si el pedido es ambiguo, propongo mi interpretación en una línea y sigo.

### Paso 2 - Busco amplio

Yo busco en varias direcciones, no con una sola query:
1. Lanzo 3-6 búsquedas distintas: término principal, sinónimos, errores comunes, alternativas, `tema + 2026`, `tema + best practices`
2. Reviso mis skills (`ME/SKILLS/INDEX.md`, `ME/SKILLS/CUSTOM/`) por si ya sé algo
3. Identifico 5-10 fuentes candidatas: docs oficiales, repos, guías reconocidas, skills.sh si aplica
4. Anoto fecha de cada fuente. Descarto lo claramente desactualizado salvo que sea fundamento vigente

### Paso 3 - Profundizo y verifico

Yo abro las fuentes que importan:
1. Hago fetch de las 3-5 fuentes clave (docs oficiales primero)
2. Busco específicamente: recomendaciones, consejos, errores comunes, límites, costos en tokens/tiempo/dinero, requisitos y compatibilidad
3. Comparo: ¿dónde coinciden? ¿dónde se contradicen? ¿qué es específico de 2025-2026?
4. Si algo implica código o comandos, lo verifico ejecutando o revisando archivos locales antes de afirmarlo

Yo no me quedo con el primer resultado. Yo contrasto.

### Paso 4 - Filtro y sintetizo

Yo convierto lo encontrado en conocimiento útil:
1. Elimino lo obvio, lo duplicado y lo que no responde mis preguntas clave
2. Agrupo por: qué es, cuándo usar, cuándo no usar, cómo hacerlo bien, qué evitar
3. Marco qué es opinión vs hecho verificado, y qué tan reciente es
4. Si hay varias opciones, armo tabla comparativa corta: opción, pros, contras, cuándo elegirla

Mi regla: si un párrafo no cambia una decisión, lo borro.

### Paso 5 - Entrego en formato útil

Yo entrego siempre así, conciso:

1. **Resumen** (3-5 líneas): lo que encontré y qué recomiendo
2. **Hallazgos** (5-10 bullets): solo lo no-obvio y reciente, con fecha cuando importa
3. **Recomendaciones** (accionables): qué hacer, qué evitar, en qué orden
4. **Fuentes**: lista con URL real que visité + qué aportó cada una
5. **Siguiente paso**: si vale la pena crear skill, lo propongo con nombre en `ME/SKILLS/CUSTOM/`

Yo adapto el detalle al pedido, pero nunca entrego sin fuentes ni sin recomendación clara.

### Paso 6 - Guardo solo si vale la pena

Yo no guardo investigación por defecto para no ocupar contexto:
- Si fue consulta puntual → no guardo nada, solo respondo
- Si es conocimiento reutilizable → propongo crear o actualizar una skill con mi flujo `crear-skills` (una sola skill o hub, borro el resto)
- Si es sobre la persona o proyecto → lo anoto en `ME/MEMORIES/` según mis reglas, no en la skill

Yo nunca guardo en `.opencode/`, `.claude/`, `.gemini/`, `.antigravity/`, `.cursor/` ni similares. Solo en `ME/SKILLS/CUSTOM/` o `ME/MEMORIES/` según corresponda.

## Ejemplo rápido

Pedido: "investiga autenticación JWT en 2026"
Yo hago:
1. Preguntas: ¿librería vigente? ¿errores comunes? ¿alternativa mejor?
2. Busco: `JWT best practices 2026`, `JWT vs sessions 2026`, `JWT library node 2026`, errores JWT
3. Profundizo en docs oficiales + 2 guías recientes, comparo
4. Sintetizo: refresh rotation, corta expiración, dónde guardar tokens, qué evitar
5. Entrego resumen + recomendaciones + fuentes, propongo skill solo si se repetirá
