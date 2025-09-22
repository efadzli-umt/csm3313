#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# WiFi Connection
#---------------------
import time
import network
from machine import Pin

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"     # Replace with your WiFi SSID
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"  # Replace with your WiFi password

# Initialize WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting to WiFi '{}' ... ".format(WIFI_SSID), end="")

# Connect to WiFi
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
    print(".", end="")

print("connected!")
print()

# Print network information
config = wlan.ifconfig()
print("Pico W IP address: ", config[0])
print("Subnet mask: ", config[1])
print("Gateway: ", config[2])
print("DNS server: ", config[3])
print()
