---
name: crear-skills
description: Mi flujo para crear una skill nueva. Yo la uso cuando enfrento una actividad nueva sin skill, quiero consolidar conocimiento, o me piden crear o mejorar una skill. Busco skills relacionadas, investigo a fondo con info reciente, creo una sola skill o skill hub, borro el resto y guardo solo en ME/SKILLS/CUSTOM.
---

# Crear skills

Yo creo skills para no repetir trabajo y para no ocupar mi contexto con cosas obvias. Solo guardo lo que realmente necesito y en un solo lugar.

Mi regla: cada vez que voy a hacer algo, lo hago con una skill, sin importar lo que sea. Si no tengo skill, la creo primero y luego la uso. Así documento y aprendo de cada cosa que hago.

Yo uso esta skill cuando:
- Me enfrento a una actividad nueva de la cual no tengo una skill
- Aunque ya sepa resolverla, igual la documento como skill
- Me piden crear, consolidar o limpiar skills

Yo no uso el flujo original de `skill-creator` de SKILLS.SH para el proceso. Solo lo consulto como referencia de formato (qué lleva un SKILL.md, qué son scripts, references, assets).

## Mi flujo obligatorio

Yo sigo estos 5 pasos en orden, sin saltarme ninguno.

### Paso 1 - Busco todas las skills relacionadas que encuentro

Yo primero busco, nunca creo a ciegas:
1. Reviso mi `ME/SKILLS/INDEX.md` y mi carpeta `ME/SKILLS/CUSTOM/`
2. Uso mi skill `find-skills`: ejecuto `npx skills find [query]` con varias queries (término principal, sinónimos, categoría)
3. Reviso https://skills.sh/ si necesito más contexto
4. Anoto qué encontré: nombre, qué cubre, qué le falta

Si ya existe una skill que cubre el tema, no creo una duplicada. La mejoro o la uso como base.

### Paso 2 - Investigo de forma profunda y reciente

Yo uso mi skill `investigar-profundo` para este paso. Yo investigo el tema a fondo antes de escribir:
1. Busco documentación oficial y guías actuales (uso el año actual, 2026)
2. Busco recomendaciones, consejos, errores comunes y buenas prácticas recientes
3. Comparo lo que dicen las skills encontradas vs lo que dice la documentación actual
4. Me quedo solo con lo no-obvio y lo que justifica su costo en tokens: yo ya soy capaz, no necesito explicaciones básicas

Yo no copio todo. Yo sintetizo.

### Paso 3 - Creo una sola skill, o una skill hub

Con toda la información, yo decido un solo formato:

- **Una sola skill**: si el tema es cohesivo y cabe en un `SKILL.md` de menos de 500 líneas. Todo va ahí.
- **Skill hub**: si el tema es amplio o tiene variantes. Creo un `SKILL.md` índice corto que redirige:
  - a `references/*.md` por variante o dominio
  - o a otras skills de `ME/SKILLS/CUSTOM/` que ya existen

Estructura que yo creo:
```
ME/SKILLS/CUSTOM/<nombre-skill>/
├── SKILL.md (obligatorio, en primera persona, español, conciso)
├── references/ (opcional, solo si SKILL.md supera ~200 líneas o hay variantes)
└── scripts/ (opcional, solo si repito el mismo código o necesito determinismo)
```

Yo no creo `README.md`, `CHANGELOG.md`, `INSTALLATION_GUIDE.md` ni archivos auxiliares. Solo lo esencial para hacer el trabajo.

Yo escribo el `SKILL.md` con:
- frontmatter con `name` y `description` claros (qué hace + cuándo usarla)
- instrucciones en primera persona, en infinitivo/imperativo conciso
- ejemplos cortos, no explicaciones largas

### Paso 4 - Borro el resto

Yo no dejo duplicados ni borradores:
1. Borro las skills temporales que descargué solo para investigar
2. Borro borradores, copias y versiones viejas
3. Si creé un hub, dejo solo el hub + las skills finales a las que redirige
4. Verifico que en `ME/SKILLS/CUSTOM/` solo quede lo que realmente uso

Mi regla: una responsabilidad = una skill. Si hay dos que hacen lo mismo, me quedo con una.

### Paso 5 - Guardo solo en la carpeta de skills

Yo guardo mis skills únicamente en:
- `ME/SKILLS/CUSTOM/<nombre-skill>/SKILL.md`

Yo nunca guardo skills en carpetas de herramientas para no ocupar contexto global:
- Nunca en `.opencode/`, `.claude/`, `.gemini/`, `.antigravity/`, `.cursor/`, ni similares
- Nunca duplico la misma skill en dos rutas

Después de crear o borrar, yo actualizo `ME/SKILLS/INDEX.md` con la entrada nueva y quito las que borré.

## Ejemplo de decisión

- Tema "revisar PRs en este repo" → una sola skill `ME/SKILLS/CUSTOM/revisar-prs/SKILL.md`
- Tema "desarrollo frontend" (react, testing, deploy, docs) → skill hub `ME/SKILLS/CUSTOM/frontend/SKILL.md` que redirige a `references/react.md`, `references/testing.md`, o a otras skills CUSTOM existentes. Borro el resto.
