#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Send Data to ThingSpeak
#---------------------
import time
import network
import urequests
from machine import Pin, ADC, reset

# WiFi and Blynk Configuration
WIFI_SSID = "YOUR_WIFI_SSID"        # Replace with your WiFi SSID
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"  # Replace with your WiFi password
BLYNK_AUTH_TOKEN = "YOUR_BLYNK_TOKEN"  # Replace with your Blynk auth token

# Hardware Setup
# Built-in LED on Raspberry Pi Pico W (GPIO 25 - "LED")
led = Pin("LED", Pin.OUT)
led.off()  # Initially off

# Built-in temperature sensor (ADC channel 4)
temp_sensor = ADC(4)

def read_temperature():
    """Read temperature from Pico W built-in sensor"""
    # Read raw ADC value
    raw_value = temp_sensor.read_u16()
    
    # Convert to voltage (3.3V reference, 16-bit ADC)
    voltage = raw_value * 3.3 / 65535
    
    # Convert to temperature in Celsius
    # Pico W temperature sensor: Temp = 27 - (voltage - 0.706) / 0.001721
    temperature = 27 - (voltage - 0.706) / 0.001721
    
    return round(temperature, 1)

# Blynk API Functions
def write_virtual_pin(token, pin, value):
    """Send data to Blynk virtual pin"""
    try:
        api_url = f"https://blynk.cloud/external/api/update?token={token}&{pin}={value}"
        response = urequests.get(api_url)
        if response.status_code == 200:
            print(f"{pin} updated: {value}")
        else:
            print(f"Failed to update {pin}: {response.status_code}")
        response.close()
    except Exception as e:
        print(f"Write error: {e}")

def read_virtual_pin(token, pin):
    """Read data from Blynk virtual pin"""
    try:
        api_url = f"https://blynk.cloud/external/api/get?token={token}&{pin}"
        response = urequests.get(api_url)
        if response.status_code == 200:
            value = response.text.strip()
            response.close()
            return value
        else:
            print(f"Failed to read {pin}: {response.status_code}")
            response.close()
            return "0"
    except Exception as e:
        print(f"Read error: {e}")
        return "0"

# WiFi Connection
def connect_wifi():
    """Connect to WiFi network"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to WiFi '{WIFI_SSID}' ...", end="")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1
        
        if wlan.isconnected():
            print(f"\nWiFi Connected!")
            print(f"IP Address: {wlan.ifconfig()[0]}")
            
            # Blink LED 3 times to indicate successful connection
            for i in range(3):
                led.on()
                time.sleep(0.2)
                led.off()
                time.sleep(0.2)
            
            return True
        else:
            print(f"\n!! Failed to connect to WiFi !!")
            return False
    
    return True

# Main Program
print("Initializing Blynk IoT with Temperature Sensor...")
print("=" * 50)

# Connect to WiFi
if not connect_wifi():
    print("WiFi connection failed. Restarting in 5 seconds...")
    time.sleep(5)
    reset()

print("Temperature Sensor: Built-in ADC4")
print("LED Control: Built-in LED (GPIO 'LED')")
print("Blynk Virtual Pins:")
print("- V0: LED Switch (read)")
print("- V1: Temperature (write)")
print("=" * 50)
print("Starting main loop...")

# Main Loop
last_temp_update = 0
temp_interval = 10  # Send temperature every 10 seconds

while True:
    try:
        # Check WiFi connection
        wlan = network.WLAN(network.STA_IF)
        if not wlan.isconnected():
            print("WiFi disconnected. Reconnecting...")
            if not connect_wifi():
                print("Reconnection failed. Restarting...")
                time.sleep(3)
                reset()
        
        current_time = time.time()
        
        # Read LED switch state from Blynk Virtual Pin V0
        led_state = read_virtual_pin(BLYNK_AUTH_TOKEN, "V0")
        
        # Control built-in LED based on Blynk switch
        if led_state == "1":
            led.on()
            print("LED: ON")
        else:
            led.off()
            print("LED: OFF")
        
        # Send temperature reading every 10 seconds
        if current_time - last_temp_update >= temp_interval:
            temperature = read_temperature()
            write_virtual_pin(BLYNK_AUTH_TOKEN, "V1", temperature)
            print(f"Temperature: {temperature}°C")
            last_temp_update = current_time
        
        # Wait before next cycle
        time.sleep(2)
        
    except OSError as e:
        print(f"Connection error: {e}")
        print("Restarting in 5 seconds...")
        time.sleep(5)
        reset()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
        led.off()
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Restarting in 5 seconds...")
        time.sleep(5)
        reset()