"""Falso mínimo de `machine` para probar la lógica de los robots en el PC.

Imita solo lo que usan los ejercicios: Pin, PWM y time_pulse_us.
Si un módulo necesita algo más, se agrega aquí (es infraestructura de pruebas).
"""

_pines = {}
_pwms = {}
_pulsos = []


def _id(pin):
    return pin.id if isinstance(pin, Pin) else pin


class Pin:
    IN = 1
    OUT = 3
    OPEN_DRAIN = 7
    PULL_DOWN = 1
    PULL_UP = 2
    IRQ_RISING = 1
    IRQ_FALLING = 2

    def __init__(self, id, mode=-1, pull=-1, value=None):
        self.id = id
        self._irq = None
        self.init(mode, pull, value)
        _pines[id] = self

    def init(self, mode=-1, pull=-1, value=None):
        self.mode = mode
        self.pull = pull
        self._valor = 1 if pull == Pin.PULL_UP else 0
        if value is not None:
            self._valor = 1 if value else 0

    def value(self, x=None):
        if x is None:
            return self._valor
        self._valor = 1 if x else 0

    def __call__(self, x=None):
        return self.value(x)

    def on(self):
        self._valor = 1

    def off(self):
        self._valor = 0

    def irq(self, handler=None, trigger=IRQ_FALLING | IRQ_RISING):
        self._irq = (handler, trigger)

    # --- solo para pruebas ---
    def simular(self, valor):
        """Cambia el valor como si viniera de afuera (botón, sensor) y dispara la IRQ."""
        anterior, self._valor = self._valor, 1 if valor else 0
        if self._irq and self._irq[0] and anterior != self._valor:
            flanco = Pin.IRQ_RISING if self._valor else Pin.IRQ_FALLING
            if self._irq[1] & flanco:
                self._irq[0](self)

    def __repr__(self):
        return "Pin({})".format(self.id)


class PWM:
    def __init__(self, dest, freq=None, duty_u16=None, duty_ns=None):
        self.pin = dest if isinstance(dest, Pin) else Pin(dest)
        self._freq = 0
        self._duty = 0
        self.activo = True
        if freq is not None:
            self.freq(freq)
        if duty_u16 is not None:
            self.duty_u16(duty_u16)
        if duty_ns is not None:
            self.duty_ns(duty_ns)
        _pwms[self.pin.id] = self

    def freq(self, valor=None):
        if valor is None:
            return self._freq
        self._freq = int(valor)

    def duty_u16(self, valor=None):
        if valor is None:
            return self._duty
        valor = int(valor)
        if not 0 <= valor <= 65535:
            raise ValueError("duty_u16 debe estar entre 0 y 65535, llegó {}".format(valor))
        self._duty = valor

    def duty_ns(self, valor=None):
        periodo_ns = 1000000000 // self._freq if self._freq else 0
        if valor is None:
            return self._duty * periodo_ns // 65535 if periodo_ns else 0
        if not periodo_ns:
            raise ValueError("define freq antes de duty_ns")
        self.duty_u16(int(valor) * 65535 // periodo_ns)

    def deinit(self):
        self._duty = 0
        self.activo = False

    # --- solo para pruebas ---
    @property
    def duty(self):
        return self._duty

    @property
    def porcentaje(self):
        return round(self._duty * 100 / 65535)


def time_pulse_us(pin, nivel, timeout_us=1000000):
    """Devuelve el siguiente pulso programado con programar_pulsos(); -1 si no hay (timeout)."""
    return _pulsos.pop(0) if _pulsos else -1


def freq(valor=None):
    return 240000000 if valor is None else None


def reset():
    raise SystemExit("machine.reset() llamado")


# --- solo para pruebas ---
def programar_pulsos(*valores):
    """Encola duraciones en µs que devolverá time_pulse_us (ej. 580 ≈ 10 cm)."""
    _pulsos.extend(valores)


def _limpiar():
    _pines.clear()
    _pwms.clear()
    del _pulsos[:]
