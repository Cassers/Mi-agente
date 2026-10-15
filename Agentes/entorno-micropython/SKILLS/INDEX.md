# SKILLS/INDEX.md — Entorno MicroPython

_Aquí van las habilidades de este agente, aisladas de otros agentes._

Antes de iniciar una actividad reviso si ya existe una habilidad que pueda ayudarme.

Mi regla: cada vez que voy a hacer algo, lo hago con una skill. Si no tengo skill, la creo primero en `Agentes/entorno-micropython/SKILLS/CUSTOM/` y luego la uso.

## CUSTOM

- [configurar-entorno](./CUSTOM/configurar-entorno/SKILL.md) "Instalar herramientas, flashear MicroPython, detectar puertos y subir código / la uso en la primera sesión y cada vez que llega una placa nueva"
- [probar-micropython](./CUSTOM/probar-micropython/SKILL.md) "Pruebas en 3 niveles (sintaxis, lógica en PC, humo en placa) / la uso antes de cada commit y cuando algo falla"
- [context7-docs](./CUSTOM/context7-docs/SKILL.md) "Documentación actual / la uso antes de dar un comando, flag o API que pueda haber cambiado (adaptada de upstash/context7 find-docs, MIT)"

## Notas

- Una responsabilidad = una skill.
- Nunca guardo skills fuera de `Agentes/entorno-micropython/SKILLS/`.
- Nunca leo skills de otro agente salvo que el orquestador lo autorice.
