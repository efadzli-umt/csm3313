#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Piezo Buzzer Music
#---------------------
from machine import Pin, PWM
import time
import math

# Define pin connected to piezo buzzer.
BUZZER_PIN = Pin(18, Pin.OUT)
buzzer = PWM(BUZZER_PIN)

# Define a list of tones/music notes to play.
TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494,  # B4
              523 ] # C5

def play_tone(frequency, duration):
    """Play a tone at given frequency for specified duration"""
    if frequency > 0:
        buzzer.freq(int(frequency))
        buzzer.duty_u16(32768)  # 50% duty cycle
    else:
        buzzer.duty_u16(0)  # Silent
    time.sleep(duration)
    buzzer.duty_u16(0)  # Turn off sound

def playtones():
    for i in range(len(TONE_FREQ)):
        play_tone(TONE_FREQ[i], 0.5)
    for i in range(len(TONE_FREQ)-1, -1, -1):
        play_tone(TONE_FREQ[i], 0.5)

def testtones():
    for f in (262, 294, 330, 349, 392, 440, 494, 523):
        play_tone(f, 0.25)
    time.sleep(1)

def sintones():
    y = 180
    w = 1000
    z = 100
    for x in range(y):
        sinVal = (math.sin(x*(3.1412/y)))
        f = z+(sinVal*w)
        print(f)
        play_tone(f, 0.015)
        
def simpletone():
    play_tone(261, 0.1)
    play_tone(392, 0.15)

while True:
    sintones()
    time.sleep(1)
    testtones()
    time.sleep(1)
    playtones()
    time.sleep(1)
    simpletone()
    time.sleep(1)