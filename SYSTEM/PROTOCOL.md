# PROTOCOL.md — Crear un agente (usa la skill)

_Sigo la skill `orquestar-agentes` al pie de la letra. Resumen operativo._

## 1 — Definir

nombre kebab-case, rol 1 frase, prompt, skills iniciales, alcance-no. Si falta, pregunto.

## 2 — Clonar

```powershell
Copy-Item -Recurse -LiteralPath "SYSTEM/IA_TEMPLATE" -Destination "Agentes/<nombre>"
```

Debe existir: `CONFIG.md`, `PROMPT.md`, `IDENTITY.md`, `USER.md`, `MEMORIES/`, `SKILLS/`.

## 3 — Configurar

Edito solo `CONFIG.md`, `PROMPT.md`, `IDENTITY.md`. Dejo `USER.md`, `MEMORIES/*`, `SKILLS/INDEX.md` como plantilla. Skills del agente solo en `Agentes/<nombre>/SKILLS/CUSTOM/`.

## 4 — Registrar

Fila en `SYSTEM/REGISTRY.md`:
```
| <nombre> | <rol> | `Agentes/<nombre>/` | <YYYY-MM-DD> | activo |
```

## 5 — Verificar

`ME/` intacta, `IA_TEMPLATE/` con placeholders, sin referencias cruzadas, `git status` limpio salvo lo nuevo.
