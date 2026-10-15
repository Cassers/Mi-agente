---
name: configurar-entorno
description: Preparar el PC de Luka y sus placas para el proyecto robots-onstage — Python, git, venv, mpremote, esptool, mpy-cross, pytest; flashear MicroPython en ESP32 o Pico; detectar el puerto; subir código y dejar main.py arrancando solo. Usar en la primera sesión, al cambiar de PC o al llegar una placa nueva.
---

# Configurar el entorno

Todo comando se explica en una frase antes de correrlo. Borrar o flashear una placa requiere confirmación explícita de Luka.

## 1. Diagnóstico

```bash
python --version        # o python3; se necesita 3.9+
git --version
```

Anoto en `Agentes/entorno-micropython/MEMORIES/` el sistema operativo, la versión de Python y el comando correcto (`python` o `python3`, `py` en Windows).

Si falta algo:
| SO | Python | git |
|----|--------|-----|
| Windows | `winget install Python.Python.3.12` | `winget install Git.Git` |
| macOS | `brew install python` | `xcode-select --install` o `brew install git` |
| Linux (Debian/Ubuntu) | `sudo apt install python3 python3-venv` | `sudo apt install git` |

## 2. Entorno virtual y herramientas

Desde la raíz del repo:

```bash
python -m venv .venv
# Activar: Windows → .venv\Scripts\activate   macOS/Linux → source .venv/bin/activate
pip install -r robots-onstage/requirements-dev.txt
```

`requirements-dev.txt` trae mpremote, esptool, mpy-cross y pytest. `.venv/` ya está en `.gitignore`.

## 3. Driver USB (solo si la placa no aparece)

Muchas ESP32 usan CP210x o CH340. Si `mpremote connect list` no muestra nada con la placa conectada:
- Probar otro cable (muchos solo cargan, no transmiten datos).
- Windows/macOS: instalar el driver CP210x (Silicon Labs) o CH340 (WCH) según el chip junto al USB.
- Linux: agregar el usuario al grupo `dialout` y volver a iniciar sesión.

## 4. Detectar la placa

```bash
mpremote connect list
```

Anoto el puerto (`COM3`, `/dev/ttyUSB0`, `/dev/cu.usbserial-...`) y el chip en `robots-onstage/ficha-robots.md`.

## 5. Flashear MicroPython

Antes de flashear, verifico con `context7-docs` los flags actuales de esptool y el offset de la placa: cambian entre versiones y modelos.

**ESP32** (firmware estable desde micropython.org/download, por ejemplo `ESP32_GENERIC`):
```bash
esptool --chip esp32 --port <PUERTO> erase-flash
esptool --chip esp32 --port <PUERTO> --baud 460800 write-flash 0x1000 <firmware>.bin
```
- ESP32-S3 / C3 usan offset `0x0` y `--chip esp32s3` / `esp32c3`.
- Versiones viejas de esptool usan `esptool.py` y `erase_flash` / `write_flash`.
- Si se queda en "Connecting...", mantener presionado BOOT al empezar.

**Raspberry Pi Pico / Pico W**: mantener BOOTSEL al conectar, aparece la unidad `RPI-RP2`, copiar el `.uf2` de micropython.org. Se reinicia sola.

**Plan B**: Thonny → Herramientas → Opciones → Intérprete → Instalar o actualizar MicroPython.

## 6. Comprobar

```bash
mpremote repl            # Enter → aparece >>>   (salir: Ctrl+])
```
Dentro: `import sys; print(sys.implementation, sys.platform)`.

Luego la prueba de humo: `mpremote run robots-onstage/pruebas-placa/humo.py`.

## 7. Subir código a un robot

```bash
mpremote cp -r robots-onstage/lib :                    # librerías compartidas (si hay)
mpremote cp robots-onstage/robot1/main.py :main.py     # el programa del robot
mpremote reset
```
Con varios robots conectados: `mpremote connect <PUERTO> cp ...`. Antes de subir, siempre `python robots-onstage/tools/verificar.py`.

## 8. git

```bash
git config --global user.name "Luka ..."     # si no está configurado
git config --global user.email "..."
git add -A && git commit -m "entorno: herramientas instaladas y placa flasheada"
```
Commits pequeños, uno por avance que funcione.

## Problemas frecuentes

| Problema | Solución |
|----------|----------|
| `could not enter raw repl` | Otro programa tiene el puerto (Thonny abierto) o `main.py` está en un bucle: Ctrl+C en `mpremote repl` y reintentar |
| `Permission denied` en Linux | Grupo `dialout` |
| La placa se reinicia al mover motores | Caída de voltaje: alimentar motores aparte |
| `mpremote` no se encuentra | El venv no está activado |

Cada problema nuevo y su solución los agrego aquí en el momento.
