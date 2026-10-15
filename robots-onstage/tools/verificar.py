#!/usr/bin/env python3
"""Verifica el proyecto antes de subirlo a un robot o hacer commit.

1. Sintaxis MicroPython: compila cada .py con mpy-cross (el compilador real).
2. Lógica en el PC: corre pytest con los falsos de tests/fakes/.

Uso (desde la raíz del repo, con el venv activado):
    python robots-onstage/tools/verificar.py
"""
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def carpetas_de_codigo():
    fijas = [RAIZ / "ejercicios", RAIZ / "lib", RAIZ / "pruebas-placa"]
    return [c for c in fijas + sorted(RAIZ.glob("robot*")) if c.is_dir()]


def archivos_py():
    return sorted(f for c in carpetas_de_codigo() for f in c.rglob("*.py"))


def verificar_sintaxis():
    print("== 1. Sintaxis MicroPython (mpy-cross)")
    try:
        import mpy_cross  # noqa: F401
    except ImportError:
        print("   Falta mpy-cross: pip install -r robots-onstage/requirements-dev.txt")
        return False

    archivos = archivos_py()
    if not archivos:
        print("   (todavía no hay archivos .py)")
        return True

    errores = 0
    with tempfile.TemporaryDirectory() as tmp:
        for archivo in archivos:
            salida = Path(tmp) / (archivo.stem + ".mpy")
            r = subprocess.run(
                [sys.executable, "-m", "mpy_cross", "-o", str(salida), str(archivo)],
                capture_output=True,
                text=True,
            )
            nombre = archivo.relative_to(RAIZ)
            if r.returncode == 0:
                print("   ok    {}".format(nombre))
            else:
                errores += 1
                print("   FALLA {}".format(nombre))
                print("         " + (r.stderr or r.stdout).strip().replace("\n", "\n         "))
    return errores == 0


def verificar_logica():
    print("== 2. Lógica en el PC (pytest)")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", str(RAIZ / "tests")])
    # 5 = no se encontraron pruebas: no es un error
    return r.returncode in (0, 5)


def main():
    sys.stdout.reconfigure(line_buffering=True)  # que pytest no se adelante en la salida
    sintaxis_ok = verificar_sintaxis()
    logica_ok = verificar_logica()
    print()
    if sintaxis_ok and logica_ok:
        print("TODO OK. Puedes hacer commit o subirlo a la placa.")
        return 0
    print("Hay fallas. Lee el primer error de arriba y empieza por ahí.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
