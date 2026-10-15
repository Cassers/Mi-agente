"""Prepara el PC para correr código de MicroPython con pytest.

- Pone los falsos (machine, espnow, network, micropython) en el path.
- Agrega a `time` las funciones de MicroPython con un reloj virtual.
- Deja importar módulos de lib/, ejercicios/ y robot*/ directamente.
- Cada prueba arranca limpia: pines, reloj y módulos del proyecto se reinician.
"""
import sys
import time
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
FAKES = Path(__file__).resolve().parent / "fakes"

sys.path.insert(0, str(FAKES))
for carpeta in [RAIZ / "lib", RAIZ / "ejercicios"] + sorted(RAIZ.glob("robot*")):
    if carpeta.is_dir():
        sys.path.insert(0, str(carpeta))

import espnow  # noqa: E402  (falso)
import machine  # noqa: E402  (falso)
import reloj_mp  # noqa: E402

_CARPETAS_PROYECTO = tuple(
    str(c) for c in [RAIZ / "lib", RAIZ / "ejercicios"] + sorted(RAIZ.glob("robot*"))
)


def _olvidar_modulos_del_proyecto():
    for nombre, modulo in list(sys.modules.items()):
        archivo = getattr(modulo, "__file__", None) or ""
        if archivo.startswith(_CARPETAS_PROYECTO):
            del sys.modules[nombre]


@pytest.fixture(autouse=True)
def reloj(monkeypatch):
    """Reloj virtual. Úsalo para avanzar el tiempo: reloj.avanzar(500)."""
    nuevo = reloj_mp.RelojVirtual()
    reloj_mp.usar(nuevo)
    for nombre in reloj_mp.NOMBRES:
        monkeypatch.setattr(time, nombre, getattr(reloj_mp, nombre), raising=False)
    monkeypatch.setitem(sys.modules, "utime", time)
    machine._limpiar()
    espnow._limpiar()
    _olvidar_modulos_del_proyecto()
    yield nuevo
    _olvidar_modulos_del_proyecto()


class _Pines:
    """Acceso a lo que el código dejó en los pines: pines.pin(2).value(), pines.pwm(25).duty."""

    def pin(self, id):
        return machine._pines[id]

    def pwm(self, id):
        return machine._pwms[id]

    def programar_pulsos(self, *valores):
        machine.programar_pulsos(*valores)


@pytest.fixture
def pines():
    return _Pines()
