#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# LCD Display with Temperature Sensor
#--------------------
# References:
# [1] https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython
# Additional Library:
# 1. lcd_api.py from [1]
# 2. pico_i2c_lcd.py from [1]
#---------------------
from machine import Pin, SoftI2C, ADC
import time
# Needs these 2 libraries - make sure they're MicroPython compatible
# Upload them to the 'lib' folder (lowercase)
from pico_i2c_lcd import I2cLcd

# Initialize I2C for LCD
i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
address = 0x27
display = I2cLcd(i2c, address, 2, 16)

# Initialize temperature sensor (ADC channel 4 on Pico)
sensor_temp = ADC(4)

while True:
    # Read temperature from built-in sensor
    reading = sensor_temp.read_u16() * (3.3 / 65535)
    # Convert to temperature in Celsius using Pico's formula
    temperature = 27 - (reading - 0.706) / 0.001721
    
    # Display on LCD
    display.clear()
    display.move_to(0, 0)
    display.putstr("Temp(C) = {:0.2f}".format(temperature))
    time.sleep(2)