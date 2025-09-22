#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# PIR Motion Sensor with Buzzer Alarm
#---------------------
import time
from machine import Pin, PWM

# Define pin connected to piezo buzzer
BUZZER_PIN = Pin(18, Pin.OUT)
buzzer = PWM(BUZZER_PIN)

# PIR sensor pin
pir = Pin(7, Pin.IN)

def play_tone(frequency, duration):
    """Play a tone at given frequency for specified duration"""
    if frequency > 0:
        buzzer.freq(int(frequency))
        buzzer.duty_u16(32768)  # 50% duty cycle
        time.sleep(duration)
        buzzer.duty_u16(0)  # Turn off sound
    else:
        buzzer.duty_u16(0)  # Silent

def simpletone():
    for i in range(5):
        play_tone(261, 0.1)  # C4 note
        play_tone(392, 0.15) # G4 note

def offtone():
    buzzer.duty_u16(0)  # Turn off buzzer

while True:
    if pir.value() == 1:  # Motion detected
        print("Motion detected! Playing alarm...")
        simpletone()
    else:
        print("No motion detected")
        offtone()
        
    time.sleep(1)