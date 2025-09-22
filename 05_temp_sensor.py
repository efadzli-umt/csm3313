#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Built-in Temperature Sensor
#---------------------
import time
from machine import ADC

# Initialize the built-in temperature sensor (ADC channel 4 on Pico)
sensor_temp = ADC(4)

while True:
    # Read the raw ADC value (0-65535)
    reading = sensor_temp.read_u16() * (3.3 / 65535)
    
    # Convert to temperature in Celsius
    # Pico's temperature sensor formula: T = 27 - (ADC_voltage - 0.706) / 0.001721
    temperature = 27 - (reading - 0.706) / 0.001721
    
    # Format to 2 decimal places
    data = "{:.2f}".format(temperature)
    print("Temperature: ", data, "celsius")
    time.sleep(2)