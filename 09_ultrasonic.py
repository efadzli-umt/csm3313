#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# HC-SR04 Ultrasonic Distance Sensor
#---------------------
# Required library:
# 1. hcsr04.py - Place this file in the same directory or in /lib folder
#---------------------
import time
from hcsr04 import HCSR04

# Initialize the HC-SR04 sensor
# trigger_pin=7 (GPIO7), echo_pin=6 (GPIO6)
sonar = HCSR04(trigger_pin=7, echo_pin=6)


while True:
    try:
        distance = sonar.distance_cm()
        print("Distance: {:.2f} cm".format(distance))
    except OSError as e:
        print("Retrying! Error:", e)
    time.sleep(0.1)