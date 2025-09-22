#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# LDR Sensor
#---------------------
import time
from machine import ADC

ldr = ADC(0)  # Using ADC0 (GPIO26)           
R = 10000     # ohm resistance value

def get_voltage(raw):
    return (raw * 3.3) / 65535  # MicroPython ADC uses 65535 as max value

def rtolux(rawval):
    vout = get_voltage(rawval)
    RLDR = (vout * R) / (3.3 - vout)
    lux = 500 / (RLDR / 1000)  # Conversion resistance to lumen
    return lux
    
while True:
    raw = ldr.read_u16()  # Read 16-bit value (0-65535)
    volts = get_voltage(raw)
    luxval = rtolux(raw)
    print("raw = {:5d} volts = {:.2f} light = {:.2f}".format(raw, volts, luxval))
    time.sleep(1)