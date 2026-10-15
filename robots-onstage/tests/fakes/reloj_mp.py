"""Reloj virtual con la API de tiempo de MicroPython (ticks_ms, sleep_ms, ...).

En las pruebas nada espera de verdad: sleep_ms avanza el reloj al instante,
así una coreografía de 2 minutos se prueba en milisegundos.
"""


class RelojVirtual:
    def __init__(self):
        self.us = 0

    @property
    def ms(self):
        return self.us // 1000

    def avanzar(self, ms):
        self.us += int(ms * 1000)


_actual = RelojVirtual()


def usar(reloj):
    global _actual
    _actual = reloj


# Funciones con la misma firma que en MicroPython. Delegan en el reloj actual,
# así funcionan aunque el módulo probado haga `from time import ticks_ms`.
def ticks_ms():
    return _actual.ms


def ticks_us():
    return _actual.us


def ticks_diff(nuevo, viejo):
    return nuevo - viejo


def ticks_add(ticks, delta):
    return ticks + delta


def sleep_ms(ms):
    _actual.avanzar(ms)


def sleep_us(us):
    _actual.us += int(us)


def sleep(s):
    _actual.avanzar(s * 1000)


NOMBRES = ("ticks_ms", "ticks_us", "ticks_diff", "ticks_add", "sleep_ms", "sleep_us", "sleep")
