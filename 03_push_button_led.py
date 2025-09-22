#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Push Button LED
#---------------------
import time
from machine import Pin

led = Pin(0, Pin.OUT)

switch = Pin(20, Pin.IN, Pin.PULL_UP)

def blinkled():
    print("Blink LED GP0")
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)

def ledoff():
    led.off()
    print("Turn OFF LED GP0")

while True:
    if switch.value() == 0:  # Button pressed (pull-up means pressed = 0)
        blinkled()
    else:
        ledoff()
    time.sleep(1)