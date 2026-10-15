---
name: context7-docs
description: Consulta documentación actual de MicroPython y sus herramientas (machine, time, espnow, network, mpremote, esptool, mpy-cross, pytest) con Context7 antes de afirmar firmas, parámetros, flags o comportamientos. Usar siempre que la respuesta dependa de una API o comando, aunque creas saberlo.
license: MIT
metadata:
  adaptada-de: "upstash/context7 — skills/find-docs (MIT, Copyright (c) 2021 Upstash, Inc.)"
---

# Context7: documentación actual

Mi memoria de APIs puede estar desactualizada o mezclar Python de PC con MicroPython. Antes de afirmar cómo funciona una función, un parámetro o un flag, lo verifico aquí.

## Dos formas de usarlo

1. **MCP (preferida si está activa):** herramientas `resolve-library-id` y `query-docs` del servidor `context7` (configurado en `opencode.json`).
2. **CLI (siempre funciona):** con pnpm, sin instalar nada global.

```bash
pnpm dlx ctx7@latest library <nombre> "<pregunta>"
pnpm dlx ctx7@latest docs <libraryId> "<pregunta>"
```

## IDs que ya conozco

| Tema | Library ID | Notas |
|------|-----------|-------|
| MicroPython (núcleo, `machine`, `time`, `espnow`, `network`, mpremote) | `/micropython/micropython` | El principal. Reputación alta. |
| Docs web de MicroPython | `/websites/micropython_en` | Respaldo si el anterior no trae la página. |

Si el ID cambia o no aparece, resuelvo de nuevo con `library`. Para cualquier otra herramienta (esptool, pytest, Thonny, Wokwi), siempre `library` primero.

## Flujo

1. **Resolver** (salvo que ya tenga el ID): `pnpm dlx ctx7@latest library MicroPython "PWM duty_u16 en ESP32"`.
2. **Consultar** un solo tema por consulta: `pnpm dlx ctx7@latest docs /micropython/micropython "machine.PWM duty_u16 y freq en ESP32"`.
3. **Usar**: respondo con lo que dice la documentación y cito la función exacta. Si la doc distingue por puerto (esp32, rp2), lo digo.
4. **Probar en la placa** cuando la doc no sea concluyente: doy una línea para el REPL, por ejemplo `from machine import PWM; help(PWM)`.

Máximo 3 consultas por pregunta. Si no aparece, uso lo mejor que encontré y aviso que no está verificado.

## Buenas consultas

| Calidad | Ejemplo |
|---------|---------|
| Buena | `"machine.time_pulse_us timeout y valores de retorno"` |
| Buena | `"espnow ESPNow recv timeout_ms broadcast add_peer"` |
| Buena | `"mpremote cp copiar archivo a la placa como main.py"` |
| Mala (vaga) | `"pines"` |
| Mala (muchos temas) | `"PWM y servos y wifi y espnow"` |

Nunca pongo en la consulta claves, contraseñas, datos personales ni código privado completo.

## Errores

- **Cuota agotada** ("quota exceeded"): le digo a Luka que Context7 llegó al límite, que puede autenticarse con `pnpm dlx ctx7@latest login` o una `CONTEXT7_API_KEY`, y si no, respondo avisando que no pude verificar.
- **Sin internet:** lo digo y propongo verificar en el REPL con `help()` y `dir()`.
- Nunca caigo en mi memoria en silencio: siempre digo cuándo no verifiqué.

## Errores comunes

- Los IDs llevan `/` al inicio: `/micropython/micropython`.
- `docs` sin un ID válido falla: primero `library`.
- Python de PC no es MicroPython: `threading`, `numpy`, `requests` no existen. Si la doc que encuentro es de CPython, no sirve.
