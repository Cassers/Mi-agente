"""Pruebas de la infraestructura de pruebas (los falsos). No prueban código de Luka.

Si alguna falla, el problema está en tests/fakes/, no en los robots.
"""
import time

import pytest


def test_pin_salida_y_boton_con_pull_up(pines):
    from machine import Pin

    led = Pin(2, Pin.OUT)
    led.value(1)
    assert pines.pin(2).value() == 1

    boton = Pin(0, Pin.IN, Pin.PULL_UP)
    assert boton.value() == 1  # suelto
    boton.simular(0)
    assert boton.value() == 0  # presionado


def test_irq_de_boton():
    from machine import Pin

    eventos = []
    boton = Pin(0, Pin.IN, Pin.PULL_UP)
    boton.irq(handler=lambda p: eventos.append(p.value()), trigger=Pin.IRQ_FALLING)
    boton.simular(0)
    boton.simular(1)
    assert eventos == [0]


def test_pwm_valida_rango(pines):
    from machine import PWM, Pin

    motor = PWM(Pin(25), freq=1000)
    motor.duty_u16(32768)
    assert pines.pwm(25).porcentaje == 50
    with pytest.raises(ValueError):
        motor.duty_u16(70000)


def test_servo_con_duty_ns():
    from machine import PWM, Pin

    servo = PWM(Pin(13), freq=50)
    servo.duty_ns(1500000)  # 1.5 ms = centro
    assert servo.duty_u16() == 1500000 * 65535 // 20000000


def test_reloj_virtual_no_espera_de_verdad(reloj):
    inicio = time.ticks_ms()
    time.sleep_ms(120000)  # 2 minutos de obra
    assert time.ticks_diff(time.ticks_ms(), inicio) == 120000
    reloj.avanzar(500)
    assert time.ticks_ms() == 120500


def test_ultrasonico_programado(pines):
    from machine import Pin, time_pulse_us

    pines.programar_pulsos(580)
    assert time_pulse_us(Pin(18, Pin.IN), 1, 30000) / 58 == 10
    assert time_pulse_us(Pin(18, Pin.IN), 1, 30000) == -1  # sin eco: timeout


def test_espnow_lider_y_seguidor():
    import espnow
    import network

    network.WLAN(network.STA_IF).active(True)
    lider, seguidor = espnow.ESPNow(), espnow.ESPNow()
    lider.active(True)
    seguidor.active(True)
    lider.add_peer(b"\xff" * 6)
    lider.send(b"\xff" * 6, b"GO")
    _, msg = seguidor.recv(1000)
    assert msg == b"GO"
    assert seguidor.recv(10) == (None, None)
