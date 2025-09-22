#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Send Data to ThingSpeak
#---------------------
import time
import network
import urequests
import ujson  # Add JSON support
import random
from machine import Pin, PWM, reset

# WiFi and ThingSpeak Configuration
WIFI_SSID = "YOUR_WIFI_SSID"        # Replace with your WiFi SSID
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"  # Replace with your WiFi password
THINGSPEAK_WRITE_API_KEY = "YOUR_WRITE_API_KEY"  # Replace with your API key

# LED Control Channel Configuration (NEW)
THINGSPEAK_LED_CHANNEL_ID = "YOUR_LED_CONTROL_CHANNEL_ID"    # Replace with LED control channel ID
THINGSPEAK_READ_API_KEY = "YOUR_READ_API_KEY"               # Replace with READ API key (optional)

# ThingSpeak API URL
API_URL = "http://api.thingspeak.com"

# Built-in LED setup (NEW)
builtin_led = Pin("LED", Pin.OUT)  # Built-in LED on Pico W
builtin_led.off()  # Start with LED off

def read_thingspeak_led_control():
    """
    Read LED control value from ThingSpeak channel Field 4
    Returns the field value or None if error
    """
    try:
        # Method 1: Try to get just the field value (without JSON)
        if THINGSPEAK_READ_API_KEY and THINGSPEAK_READ_API_KEY != "YOUR_READ_API_KEY":
            url = f"{API_URL}/channels/{THINGSPEAK_LED_CHANNEL_ID}/fields/4/last?api_key={THINGSPEAK_READ_API_KEY}"
        else:
            url = f"{API_URL}/channels/{THINGSPEAK_LED_CHANNEL_ID}/fields/4/last"
        
        print(f"Reading LED control from channel {THINGSPEAK_LED_CHANNEL_ID}, field 4...")
        response = urequests.get(url)
        
        if response.status_code == 200:
            value = response.text.strip()
            response.close()
            
            # Check if it's JSON (starts with '{') or plain text
            if value.startswith('{'):
                # It's JSON, parse it to get the field4 value
                try:
                    data = ujson.loads(value)
                    field_value = data.get('field4')
                    print(f"Parsed JSON, field4 value: {field_value}")
                    return field_value
                except:
                    print("Failed to parse JSON response")
                    return None
            else:
                # It's plain text field value
                print(f"Plain text response: {value}")
                return value
        else:
            print(f"HTTP Error reading LED control: {response.status_code}")
            response.close()
            return None
    except Exception as e:
        print(f"Error reading LED control: {e}")
        return None

def control_builtin_led(value):
    """Control built-in LED based on value: 1=ON, 0=OFF"""
    try:
        if value == "1" or value == 1:
            builtin_led.on()
            print("Built-in LED: ON")
            play_tone(NOTE_C5, 0.05)  # Quick high tone for ON
            return True
        elif value == "0" or value == 0:
            builtin_led.off()
            print("Built-in LED: OFF")
            play_tone(NOTE_G4, 0.05)  # Quick low tone for OFF
            return True
        else:
            print(f"Invalid LED control value: {value}")
            return False
    except Exception as e:
        print(f"Error controlling built-in LED: {e}")
        return False

# Initialize WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to Wi-Fi
print("Initializing...")
print("Connecting to WiFi '{}' ... ".format(WIFI_SSID), end="")

wlan.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
    print(".", end="")

print("connected!")
config = wlan.ifconfig()
print("IP Address: {}".format(config[0]))

print("\nThingSpeak IoT System Started:")
print("1. Sending sensor data every 20 seconds")
print("2. Checking LED control every 20 seconds")
print("   - Channel ID:", THINGSPEAK_LED_CHANNEL_ID)
print("   - Field 4: 1=LED ON, 0=LED OFF")
print()

while True:
    try:
        # Check WiFi connection
        while not wlan.isconnected():
            print("Reconnecting to WiFi...")
            wlan.connect(WIFI_SSID, WIFI_PASSWORD)
            time.sleep(5)
        
        # 1. Generate and send dummy sensor values (original functionality)
        value1 = round(random.uniform(25, 35), 2)    # Temperature
        value2 = round(random.uniform(75, 90), 2)    # Humidity
        value3 = round(random.uniform(8, 300), 2)    # Light level
        
        # Update ThingSpeak with sensor data
        print("Updating ThingSpeak with sensor data...")
        get_url = API_URL + "/update?api_key=" + THINGSPEAK_WRITE_API_KEY + "&field1=" + str(value1) + "&field2=" + str(value2) + "&field3=" + str(value3)
        
        response = urequests.get(get_url)
        print("Value 1 (Temperature):", value1)
        print("Value 2 (Humidity):", value2)
        print("Value 3 (Light):", value3)
        print("Data Count:", response.text)
        print("Sensor data sent successfully!")
        response.close()
        
        # 2. Read LED control from separate channel (NEW functionality)
        if THINGSPEAK_LED_CHANNEL_ID != "YOUR_LED_CONTROL_CHANNEL_ID":
            print("\nChecking LED control channel...")
            led_control_value = read_thingspeak_led_control()
            
            if led_control_value is not None:
                print(f"LED control value received: {led_control_value}")
                success = control_builtin_led(led_control_value)
                if success:
                    print("LED control applied successfully")
                else:
                    print("LED control failed")
            else:
                print("No LED control data available")
        else:
            print("LED control channel not configured")
    
        time.sleep(20)  # Check both channels every 20 seconds
        print("=" * 50)
        
    except OSError as e:
        print("Network error:", e)
        time.sleep(10)  # Wait before retrying
    except Exception as e:
        print("Unexpected error:", e)
        time.sleep(10)