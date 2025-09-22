#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# External LED blink
#---------------------
import time
from machine import Pin

led = Pin(0, Pin.OUT)

while True:
    led.on()   # Turn LED on
    time.sleep(0.5)
    led.off()  # Turn LED off
    time.sleep(1)