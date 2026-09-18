# Agentes — dónde viven los agentes

_Carpeta gestionada solo por el orquestador con la skill `orquestar-agentes`._

- No crear carpetas a mano. Pedirme: "crea un agente para X".
- Cada agente es un clon de `SYSTEM/IA_TEMPLATE/`: `Agentes/<nombre>/` con su `CONFIG.md`, `PROMPT.md`, `IDENTITY.md`, `USER.md`, `MEMORIES/` y `SKILLS/` propios.
- En plantilla esta carpeta está vacía (a propósito).

Ejemplo (no crear hasta pedirlo):

```
Agentes/ejemplo-coder/CONFIG.md
Agentes/ejemplo-coder/PROMPT.md
Agentes/ejemplo-coder/IDENTITY.md
Agentes/ejemplo-coder/MEMORIES/...
Agentes/ejemplo-coder/SKILLS/CUSTOM/...
```
