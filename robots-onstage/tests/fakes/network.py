"""Falso mínimo de `network` (solo lo que ESP-NOW necesita)."""

STA_IF = 0
AP_IF = 1


class WLAN:
    def __init__(self, interfaz=STA_IF):
        self.interfaz = interfaz
        self._activo = False

    def active(self, valor=None):
        if valor is None:
            return self._activo
        self._activo = bool(valor)

    def disconnect(self):
        pass

    def config(self, *args, **kwargs):
        if args == ("mac",):
            return b"\x24\x0a\xc4\x00\x00\x01"
