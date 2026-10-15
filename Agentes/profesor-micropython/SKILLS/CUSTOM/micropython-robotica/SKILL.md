---
name: micropython-robotica
description: Conocimiento de dominio para robots OnStage en MicroPython (ESP32 y Raspberry Pi Pico) — pines, PWM, motores con driver, servos, sensores, tiempo sin bloquear, coreografía por cues, sincronización de 3 robots, seguridad eléctrica y ruta de aprendizaje. Usar al explicar cualquiera de estos temas o al revisar código de robots.
---

# MicroPython para robots OnStage

Referencia para explicar. No es código para pegar en los robots de Luka: los fragmentos son ilustrativos y se verifican con `context7-docs`.

## Qué es OnStage

Categoría de presentación artística: los robots actúan una obra (música, historia, personajes) de forma autónoma. Se valora la sincronía, la interacción con el entorno y que el equipo entienda su robot. **El reglamento de la edición manda**: duración, autonomía, interacción y uso de IA se confirman ahí, no aquí.

## Ruta de aprendizaje

| Paso | Tema | Señal de que lo domina |
|------|------|------------------------|
| 1 | REPL, `Pin` de salida, parpadeo | Cambia el patrón sin ayuda |
| 2 | `Pin` de entrada, `PULL_UP`, botón de arranque | Explica por qué el botón lee 1 suelto |
| 3 | `PWM`: motor DC con driver, velocidad -100..100 | Escribe `vel(v)` y frena en `finally` |
| 4 | Servos (50 Hz, pulso 0.5–2.5 ms) | Calcula el `duty_u16` de 90° |
| 5 | Tiempo sin bloquear: `ticks_ms`, `ticks_diff` | Hace dos cosas a la vez sin `sleep` largo |
| 6 | Sensores: ultrasónico, línea, sonido | Lee, filtra y decide |
| 7 | Coreografía como lista de cues | Ajusta la obra cambiando números, no lógica |
| 8 | Máquina de estados | Dibuja sus estados y transiciones |
| 9 | Sincronizar 3 robots | Los tres arrancan con el mismo `t0` |
| 10 | Robustez: `main.py`, parada segura, baterías, ensayos | El robot arranca solo y frena si algo falla |

## Conceptos clave

**Pines.** `Pin(n, Pin.OUT)` / `Pin(n, Pin.IN, Pin.PULL_UP)`. En ESP32 el LED interno suele ser el 2 y el botón BOOT el 0; en Pico el LED es `Pin("LED")`. Los pines 6–11 del ESP32 son de la flash: no usarlos.

**PWM.** `PWM(Pin(n), freq=1000)` para motores, `freq=50` para servos. `duty_u16(0..65535)` existe en ESP32 y rp2.

**Motor DC.** Nunca directo al pin: siempre con driver (TB6612FNG, L298N, DRV8833). Dos pines de dirección + uno PWM por motor. Tierras comunes entre placa, driver y batería.

**Servo.** Pulso de ~500 µs (0°) a ~2500 µs (180°) en un periodo de 20 ms. `duty = pulso_us * 65535 // 20000`. Alimentar servos desde la batería, no desde el 3.3 V de la placa.

**Tiempo.** `time.sleep_ms` congela todo. Para reaccionar mientras actúa: guardar `t0 = time.ticks_ms()` y comparar con `time.ticks_diff(time.ticks_ms(), t0)`. Nunca restar ticks directamente (se desbordan).

**Coreografía por cues.** Lista de `(ms_desde_t0, acción, parámetros)` recorrida por un bucle que no bloquea. Separa la obra (datos) del motor que la ejecuta (lógica). Se puede probar en el PC con un reloj falso.

**Máquina de estados.** `ESPERANDO → ACTUANDO → REACCIONANDO → ACTUANDO → FIN`, más `PARADA` desde cualquier estado. Una variable de estado y un `if/elif` por estado en el bucle.

**Sincronización.**
| Método | Placa | Comentario |
|--------|-------|-----------|
| ESP-NOW: el líder envía "GO" en broadcast | ESP32 | Sin router, milisegundos. Repetir el envío 3–5 veces; el seguidor toma el primero. |
| Señal común (sonido, luz) | Cualquiera | Calibrar en el lugar. |
| Un botón por robot | Cualquiera | Desfase visible de cientos de ms. |
ESP-NOW no existe en la Pico. Con Pico W, alternativa por WiFi/UDP o señal física.

**Arranque seguro.** `main.py` espera un botón antes de moverse, y todo va dentro de `try/finally` que apaga motores.

## Seguridad eléctrica (avisar siempre)

- ESP32 y Pico son de **3.3 V**. El `echo` del HC-SR04 da 5 V: divisor de voltaje o sensor de 3.3 V.
- Motores y servos con su propia alimentación; tierras unidas.
- Desconectar la batería de motores antes de cablear.
- Si una placa se calienta o huele, desconectar y revisar el cableado.

## Errores típicos

| Síntoma | Causa probable |
|---------|----------------|
| `ImportError: no module named 'threading'` | Código de Python de PC |
| El robot arranca al conectarlo por USB | `main.py` sin espera de botón |
| El motor no gira pero el LED sí | Driver sin alimentación, tierras separadas o pin STBY apagado (TB6612) |
| El servo tiembla | Alimentación insuficiente o duty mal calculado |
| El ultrasónico devuelve basura | Sin timeout en `time_pulse_us` o lecturas demasiado seguidas |
| Los robots se desfasan | Cada uno usa su propio `t0` o hay `sleep` largos en el bucle |
| Funciona en Thonny y no al encender | Archivo no guardado como `main.py` en la placa |
