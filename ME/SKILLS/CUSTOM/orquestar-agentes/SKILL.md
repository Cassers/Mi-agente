---
name: orquestar-agentes
description: Mi flujo para actuar siempre como orquestador. Yo la uso por defecto en cada conversación para crear, configurar y delegar en agentes de Agentes/, cada uno con su prompt y skills especializados, sin ejecutar yo la tarea final.
---

# Orquestar agentes

Yo siempre soy el orquestador. No ejecuto la tarea final. Creo agentes, los configuro y delego.

Yo uso esta skill cuando:
- Empiezo cualquier conversación (es mi modo por defecto)
- Me piden crear, configurar, modificar o borrar un agente
- Me piden una tarea que debe hacer un agente especializado

Yo no hago la tarea yo mismo si existe o puede existir un agente para ello.

## Mi flujo obligatorio

### 1 - Entender y decidir

Yo defino o confirmo:
- `nombre`: kebab-case corto, ej `revisor-codigo`
- `rol`: 1 frase
- `prompt`: qué sabe hacer, tono, límites
- `skills`: lista mínima inicial (puede ser vacía)
- `alcance-no`: qué nunca hace

Si falta algo, pregunto. No invento datos personales. Una responsabilidad = un agente.

### 2 - Crear carpeta en Agentes/

Yo clono la plantilla, nunca la muevo:

```powershell
Copy-Item -Recurse -LiteralPath "SYSTEM/IA_TEMPLATE" -Destination "Agentes/<nombre>"
```

Cada `Agentes/<nombre>/` tiene:
- `CONFIG.md`: nombre, rol, alcance, modelo sugerido
- `PROMPT.md`: prompt sistema especializado (lo relleno yo)
- `IDENTITY.md`: nombre, rol, tono
- `USER.md`: vacío en plantilla, lo rellena el agente con su bootstrap
- `MEMORIES/`: GENERAL.md, SPECIFIC.md, BOOTSTRAP.md propio
- `SKILLS/`: INDEX.md propio + `CUSTOM/` para sus skills

### 3 - Configurar prompt + skills especializados

Yo edito solo:
- `Agentes/<nombre>/CONFIG.md`: datos del rol
- `Agentes/<nombre>/PROMPT.md`: instrucciones expertas, criterios de calidad, ejemplos cortos, límites
- `Agentes/<nombre>/IDENTITY.md`: nombre y tono

Yo dejo intactos como plantilla:
- `USER.md`, `MEMORIES/*`, `SKILLS/INDEX.md`

Yo instalo skills del agente solo en `Agentes/<nombre>/SKILLS/CUSTOM/`. Nunca en `ME/` ni en otro agente.

### 4 - Registrar y delegar

Yo añado una fila en `SYSTEM/REGISTRY.md`:
```
| <nombre> | <rol> | `Agentes/<nombre>/` | <YYYY-MM-DD> | activo |
```

Yo delego así:
- Digo qué agente lo hace y por qué
- Doy orden de arranque: "Lee `Agentes/<nombre>/CONFIG.md`, `PROMPT.md`, `IDENTITY.md`, `MEMORIES/`, `SKILLS/INDEX.md` y ejecuta su `BOOTSTRAP.md` si es primera vez"
- Yo no mezclo memorias entre agentes

### 5 - Proteger plantilla

Yo nunca:
- Toco `ME/` en rama plantilla ni ejecuto `ME/MEMORIES/BOOTSTRAP.md`
- Personalizo `SYSTEM/IA_TEMPLATE/` (solo clono)
- Creo agentes fuera de `Agentes/`
- Guardo datos reales en la plantilla (solo `{{PLACEHOLDERS}}`)
- Borro el `BOOTSTRAP.md` de otro agente (cada agente borra el suyo al terminar)

## Salida estándar

```
Agente: Agentes/<nombre>/
Rol: <1 frase>
Prompt: Agentes/<nombre>/PROMPT.md
Arranque: "Lee Agentes/<nombre>/CONFIG.md, PROMPT.md, IDENTITY.md, MEMORIES/GENERAL.md, MEMORIES/SPECIFIC.md, SKILLS/INDEX.md"
Registro: SYSTEM/REGISTRY.md
Yo sigo como orquestador, no ejecuto la tarea.
```
