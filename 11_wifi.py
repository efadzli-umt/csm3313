#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Lesson 11: WiFi Connection (Raspberry Pi Pico W)
# Last update: 9 Nov 2026
#---------------------

import time
import network

# WiFi Configuration - update these values
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
CONNECTION_TIMEOUT = 15  # seconds

# Initialize WiFi interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Display the Pico W's MAC address
mac = wlan.config("mac")
mac_address = ":".join("{:02X}".format(byte) for byte in mac)
print("Pico W MAC address:", mac_address)

# Connect to WiFi (unless already connected)
if not wlan.isconnected():
    print("Connecting to WiFi '{}'...".format(WIFI_SSID), end="")

    try:
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        start_time = time.ticks_ms()

        while not wlan.isconnected():
            if wlan.status() < 0:
                break

            if time.ticks_diff(time.ticks_ms(), start_time) >= CONNECTION_TIMEOUT * 1000:
                break

            print(".", end="")
            time.sleep(1)

    except OSError as error:
        print("\nWiFi error:", error)

# Display connection status and network information
if wlan.isconnected():
    print("\nWiFi connected successfully!")

    config = wlan.ifconfig()
    print("IP address :", config[0])
    print("Subnet mask:", config[1])
    print("Gateway    :", config[2])
    print("DNS server :", config[3])

else:
    print("\nWiFi connection failed or timed out.")
    print("WiFi status code:", wlan.status())
    print("Check the SSID, password, and 2.4 GHz WiFi availability.")
