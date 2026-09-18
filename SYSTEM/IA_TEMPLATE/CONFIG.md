# CONFIG.md — {{NOMBRE_AGENTE}}

_Plantilla. La rellena el orquestador al clonar. Este agente no toca ME/ ni otros agentes._

- **nombre:** `{{nombre-agente}}`
- **rol:** {{rol en 1 frase}}
- **alcance sí:** {{qué sí hace}}
- **alcance no:** {{qué no hace}}
- **modelo sugerido:** {{opcional}}
- **carpeta:** `Agentes/{{nombre-agente}}/`
- **prompt:** `Agentes/{{nombre-agente}}/PROMPT.md`

## Arranque

Para activar este agente, leer en orden:

1. `Agentes/{{nombre-agente}}/CONFIG.md`
2. `Agentes/{{nombre-agente}}/PROMPT.md`
3. `Agentes/{{nombre-agente}}/IDENTITY.md`
4. `Agentes/{{nombre-agente}}/USER.md`
5. `Agentes/{{nombre-agente}}/MEMORIES/GENERAL.md`
6. `Agentes/{{nombre-agente}}/MEMORIES/SPECIFIC.md`
7. `Agentes/{{nombre-agente}}/SKILLS/INDEX.md`
8. Ejecutar su `MEMORIES/BOOTSTRAP.md` (propio, aislado)

## Límites

- Solo lee/escribe dentro de `Agentes/{{nombre-agente}}/`.
- Si necesita una skill nueva, la crea en `Agentes/{{nombre-agente}}/SKILLS/CUSTOM/`.
- Si necesita memoria nueva, la guarda en `Agentes/{{nombre-agente}}/MEMORIES/`.
