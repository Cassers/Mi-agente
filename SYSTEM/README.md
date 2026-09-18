# SYSTEM/README.md

_Plantilla multi-agente. No personalizar aquí. No ejecutar bootstrap madre._

## Estructura

```
./ME/                        <- plantilla madre, intacta, no tocar
./ME/SKILLS/CUSTOM/orquestar-agentes/SKILL.md  <- yo siempre soy orquestador (skill)
./SYSTEM/
  ORCHESTRATOR.md            <- puntero a la skill
  PROTOCOL.md                <- resumen operativo
  REGISTRY.md                <- índice de agentes
  IA_TEMPLATE/               <- se clona para cada agente
    CONFIG.md
    PROMPT.md                <- prompt especializado
    IDENTITY.md
    USER.md
    MEMORIES/GENERAL.md
    MEMORIES/SPECIFIC.md
    MEMORIES/BOOTSTRAP.md
    SKILLS/INDEX.md
./Agentes/
  README.md                  <- los agentes viven aquí: ./Agentes/<nombre>/
  <nombre>/                  <- clon con prompt + skills propios
```

## Reglas

1. `ME/` no se personaliza en esta rama.
2. `IA_TEMPLATE/` no se personaliza, solo se clona.
3. Cada `Agentes/<nombre>/` tiene prompt y skills aislados.
4. Solo el orquestador crea carpetas en `Agentes/`.
