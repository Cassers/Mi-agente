# Prueba de humo: confirma que la placa está viva.
# Uso: mpremote run robots-onstage/pruebas-placa/humo.py
import gc
import sys
import time

from machine import Pin, freq

print("MicroPython", sys.implementation.version, "en", sys.platform)
print("CPU:", freq() // 1000000, "MHz")
gc.collect()
print("RAM libre:", gc.mem_free(), "bytes")

LED = "LED" if sys.platform == "rp2" else 2  # ESP32: pin 2 en la mayoría de placas
led = Pin(LED, Pin.OUT)
for _ in range(6):
    led.value(not led.value())
    time.sleep_ms(150)
led.value(0)

print("OK: placa viva")
