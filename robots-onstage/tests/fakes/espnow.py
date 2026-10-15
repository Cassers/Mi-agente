"""Falso mínimo de `espnow`: todos los ESPNow de una prueba comparten un mismo aire."""

_aire = []


class ESPNow:
    def __init__(self):
        self._activo = False
        self.peers = []
        self.enviados = []

    def active(self, valor=None):
        if valor is None:
            return self._activo
        self._activo = bool(valor)

    def add_peer(self, mac, *args, **kwargs):
        self.peers.append(bytes(mac))

    def send(self, mac, msg, sync=True):
        if not self._activo:
            raise OSError("ESPNow no está activo")
        dato = msg.encode() if isinstance(msg, str) else bytes(msg)
        self.enviados.append((bytes(mac), dato))
        _aire.append((self, dato))
        return True

    def recv(self, timeout_ms=None):
        for i, (emisor, dato) in enumerate(_aire):
            if emisor is not self:
                del _aire[i]
                return b"\x00" * 6, dato
        return None, None

    def any(self):
        return any(emisor is not self for emisor, _ in _aire)


def _limpiar():
    del _aire[:]
