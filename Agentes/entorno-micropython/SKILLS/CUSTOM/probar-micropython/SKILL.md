---
name: probar-micropython
description: Probar código MicroPython del proyecto robots-onstage en 3 niveles — sintaxis con mpy-cross, lógica en el PC con pytest y falsos de machine/time, y humo en la placa con mpremote. Usar antes de cada commit, antes de subir a un robot y cuando algo falla.
---

# Probar MicroPython

Un solo comando cubre los niveles 1 y 2:

```bash
python robots-onstage/tools/verificar.py
```

## Nivel 1 — Sintaxis MicroPython (mpy-cross)

`verificar.py` compila cada `.py` de `ejercicios/`, `robot*/`, `lib/` y `pruebas-placa/` con el compilador real de MicroPython. Atrapa sintaxis que en el PC funciona y en la placa no. No ejecuta nada, así que no detecta errores de lógica ni módulos inexistentes.

## Nivel 2 — Lógica en el PC (pytest + falsos)

`robots-onstage/tests/fakes/` imita lo justo de MicroPython para correr la lógica en el PC:

| Falso | Qué imita | Para qué sirve en una prueba |
|-------|-----------|------------------------------|
| `machine.Pin` | `value()`, `on()`, `off()`, modos, `PULL_UP` | Leer qué pines quedaron prendidos; simular un botón con `pin.simular(0)` |
| `machine.PWM` | `freq()`, `duty_u16()`, `deinit()` | Comprobar velocidad de motores y ángulo de servos |
| `machine.time_pulse_us` | Devuelve lo que la prueba programe | Simular el sensor ultrasónico |
| `time.ticks_ms`, `ticks_diff`, `sleep_ms`… | Reloj virtual controlado por la fixture `reloj` | Probar coreografías de 2 minutos en milisegundos |

`tests/conftest.py` instala los falsos antes de cada prueba y agrega `lib/`, `ejercicios/` y `robot*/` al path.

Patrón de prueba (Luka escribe las suyas en `tests/test_<tema>.py`):

```python
def test_motor_frena_al_final(reloj, pines):
    import motores                      # su módulo en lib/
    m = motores.Motor(26, 27, 25)
    m.vel(60)
    assert pines.pwm(25).duty == 39321  # 60 % de 65535
    m.vel(0)
    assert pines.pwm(25).duty == 0
```

Reglas:
- Las pruebas de los ejercicios las escribe Luka; yo le muestro el patrón y le ayudo a correrlas.
- Probar lógica (cálculos, cues, estados), no el hardware. Si una prueba necesita demasiados falsos, la lógica está demasiado mezclada con el hardware: sugerir separarla (y derivar la explicación a `profesor-micropython`).
- Si un módulo usa algo que los falsos no imitan, amplío `tests/fakes/` (infraestructura, es mi alcance) y lo anoto aquí.

## Nivel 3 — Humo en la placa (mpremote)

```bash
mpremote run robots-onstage/pruebas-placa/humo.py          # placa viva, LED, info
mpremote run robots-onstage/pruebas-placa/<prueba>.py      # pruebas de hardware cortas
```

- `mpremote run` ejecuta sin guardar en la placa: no pisa `main.py`.
- Pruebas de motores: robot levantado (ruedas al aire) y siempre con `try/finally` que frena.
- Cada prueba de placa dura menos de 10 s e imprime `OK` o `FALLA: <motivo>`.

## Opcional — Simulador Wokwi

Para probar sin la placa a mano: wokwi.com permite simular ESP32 o Pico con MicroPython, LEDs, servos y sensores en el navegador. Útil para ensayar ejercicios; no reemplaza la prueba en el robot real.

## Antes de cada commit

1. `python robots-onstage/tools/verificar.py` → todo verde.
2. Si cambió algo de hardware: nivel 3 en la placa.
3. `git add -A && git commit -m "<qué funciona ahora>"`.

## Leer fallos

- `mpy-cross` → error con archivo y línea: es sintaxis, ir a esa línea.
- pytest → leer el `assert` que falló y el valor real; explicar a Luka qué esperaba la prueba y qué pasó.
- En placa → copiar el Traceback completo. `ImportError` suele ser un archivo no subido o una librería de PC.
