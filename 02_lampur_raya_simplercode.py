#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Lampu Raya
#---------------------

import time
from machine import Pin

# Declare LED pins
LED0 = Pin(0, Pin.OUT)
LED1 = Pin(1, Pin.OUT)
LED2 = Pin(2, Pin.OUT)
LED3 = Pin(3, Pin.OUT)
LED4 = Pin(4, Pin.OUT)
LED5 = Pin(5, Pin.OUT)
LED6 = Pin(6, Pin.OUT)
LED7 = Pin(7, Pin.OUT)

while True:

    # Turn ON LEDs from 0 to 7
    LED0.on()
    time.sleep(0.1)
    LED1.on()
    time.sleep(0.1)
    LED2.on()
    time.sleep(0.1)
    LED3.on()
    time.sleep(0.1)
    LED4.on()
    time.sleep(0.1)
    LED5.on()
    time.sleep(0.1)
    LED6.on()
    time.sleep(0.1)
    LED7.on()
    time.sleep(0.1)

    # Turn OFF LEDs from 0 to 7
    LED0.off()
    time.sleep(0.1)
    LED1.off()
    time.sleep(0.1)
    LED2.off()
    time.sleep(0.1)
    LED3.off()
    time.sleep(0.1)
    LED4.off()
    time.sleep(0.1)
    LED5.off()
    time.sleep(0.1)
    LED6.off()
    time.sleep(0.1)
    LED7.off()
    time.sleep(0.1)

    # Turn ON LEDs from 7 to 0
    LED7.on()
    time.sleep(0.1)
    LED6.on()
    time.sleep(0.1)
    LED5.on()
    time.sleep(0.1)
    LED4.on()
    time.sleep(0.1)
    LED3.on()
    time.sleep(0.1)
    LED2.on()
    time.sleep(0.1)
    LED1.on()
    time.sleep(0.1)
    LED0.on()
    time.sleep(0.1)

    # Turn OFF LEDs from 7 to 0
    LED7.off()
    time.sleep(0.1)
    LED6.off()
    time.sleep(0.1)
    LED5.off()
    time.sleep(0.1)
    LED4.off()
    time.sleep(0.1)
    LED3.off()
    time.sleep(0.1)
    LED2.off()
    time.sleep(0.1)
    LED1.off()
    time.sleep(0.1)
    LED0.off()
    time.sleep(0.1)
