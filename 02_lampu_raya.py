#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Lampu Raya
#---------------------
import time
from machine import Pin

# LEDs Pinout             
L = []

# To Declare the LEDs as PORT
LEDS = (0, 1, 2, 3, 4, 5, 6, 7)

for i in range(8):
    L.append(Pin(LEDS[i], Pin.OUT))
    L[i].off()  # Initialize LEDs as off
    
while True:
    for j in range(8):
        L[j].on()
        time.sleep(0.1)
    
    for j in range(8):
        L[j].off()
        time.sleep(0.1)
        
    for j in reversed(range(8)):
        L[j].on()
        time.sleep(0.1)
        
    for j in reversed(range(8)):
        L[j].off()
        time.sleep(0.1)
