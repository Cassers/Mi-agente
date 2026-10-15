# robots-onstage

Código de los 3 robots autónomos para la competencia OnStage. **El código de los robots lo escribe Luka**; los agentes de IA preparan el entorno, las pruebas y enseñan.

¿Primera vez? Abre `intro.html` en el navegador: explica en una página quién hace qué y cómo es un día de trabajo.

## Estructura

```
robots-onstage/
├── ficha-robots.md        # hardware real: placa, pines, sensores (llenar primero)
├── ejercicios/            # ejercicios de las clases
├── lib/                   # código compartido entre robots (motores, guion, sync)
├── robot1/ robot2/ robot3/# main.py de cada robot
├── tests/                 # pruebas en el PC (pytest)
│   └── fakes/             # imitaciones de machine, time, espnow para el PC
├── pruebas-placa/         # pruebas cortas que corren en la placa real
├── diagramas/             # diagramas Archify del profesor
├── tools/verificar.py     # sintaxis MicroPython + pruebas, en un comando
└── requirements-dev.txt   # herramientas del PC
```

## Empezar

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r robots-onstage/requirements-dev.txt
mpremote connect list              # ¿aparece la placa?
mpremote run robots-onstage/pruebas-placa/humo.py
python robots-onstage/tools/verificar.py
```

¿Algo falla? En opencode, cambia al agente `entorno` y cuéntale qué pasó.

## Día a día

| Quiero… | Comando |
|---------|---------|
| Probar todo antes de un commit | `python robots-onstage/tools/verificar.py` |
| Correr un archivo en la placa sin guardarlo | `mpremote run robots-onstage/ejercicios/01_parpadeo.py` |
| Abrir la consola de la placa | `mpremote repl` (salir: `Ctrl+]`) |
| Subir el programa de un robot | `mpremote cp robots-onstage/robot1/main.py :main.py` |
| Guardar el avance | `git add -A && git commit -m "qué funciona ahora"` |

## Los agentes (opencode)

| Agente | Para qué | Cómo |
|--------|----------|------|
| `profesor` 🎭 | Entender conceptos, pistas cuando te atascas, revisar tu código, diagramas | `Tab` hasta `profesor`, o `@profesor` |
| `entorno` 🔧 | Instalar, flashear, subir código, correr pruebas | `Tab` hasta `entorno`, o `@entorno` |

El profesor no te escribe la solución: te da pistas por niveles. Si de verdad la necesitas, escribe "muéstrame la solución" y te la explica línea por línea.

## Escribir una prueba

```python
# robots-onstage/tests/test_motores.py
def test_motor_frena(pines):
    import motores                       # robots-onstage/lib/motores.py
    m = motores.Motor(26, 27, 25)
    m.vel(60)
    assert pines.pwm(25).porcentaje == 60
    m.vel(0)
    assert pines.pwm(25).duty == 0
```

Fixtures disponibles: `reloj` (tiempo virtual: `reloj.avanzar(500)`) y `pines` (`pines.pin(2).value()`, `pines.pwm(25).duty`, `pines.programar_pulsos(580)`).
