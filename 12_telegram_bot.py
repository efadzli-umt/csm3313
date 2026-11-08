#---------------------
# FSKM UMT
# CSM3313 IoT
# MicroPython with Pico W lesson by Cikgu Fadzli
# Telegram Bot Integration
#---------------------

# -------------------------------------------------------
# HOW TO CREATE AND CONFIGURE A TELEGRAM BOT
# -------------------------------------------------------
# Step 1: Open Telegram and search for @BotFather.
# Step 2: Start a chat with @BotFather and send /newbot.
# Step 3: Enter a name for your bot (e.g., Siti IoT Bot).
# Step 4: Enter a unique username ending with "bot"
#         (e.g., siti123_iot_bot).
# Step 5: BotFather will provide a Bot API Token.
#         Copy this token.
# Step 6: Search for your newly created bot in Telegram.
#         Press START and send a message (e.g., Hello).
# Step 7: Open the following URL in your web browser:
#         https://api.telegram.org/bot<TOKEN>/getUpdates
#         Replace <TOKEN> with your actual Bot API Token.
# Step 8: Find "chat": {"id": ...} in the JSON response.
#         Copy the chat ID (that is your Telegram Chat ID).
# Step 9: Update TELEGRAM_BOT_TOKEN and
#         TELEGRAM_CHAT_ID in the code below.
# Step 10: Update your WiFi SSID and password.
# Step 11: Run the program using Thonny IDE.
#          You should receive messages from your bot!
#
# IMPORTANT:
# - Keep your Bot API Token private.
# - Do not share code containing your actual token.
# - If getUpdates returns an empty result, send another
#   message to your bot and refresh the browser.
# -------------------------------------------------------

import time
import network
import urequests
import json
from machine import Pin

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"     # Replace with your WiFi SSID
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"  # Replace with your WiFi password

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_ID"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

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

# URL encoding function for special characters
def url_encode(text):
    """Simple URL encoding for common characters"""
    replacements = {
        ' ': '%20',
        '\n': '%0A',
        '📡': '%F0%9F%93%A1',
        '🕐': '%F0%9F%95%90',
        '🌐': '%F0%9F%8C%90',
        '📶': '%F0%9F%93%B6',
        '🔋': '%F0%9F%94%8B',
        '🤖': '%F0%9F%A4%96',
        '🔴': '%F0%9F%94%B4',
        '#': '%23',
        ':': '%3A',
        '!': '%21'
    }
    
    for char, encoded in replacements.items():
        text = text.replace(char, encoded)
    
    return text

# Function to send message to Telegram
def send_telegram_message(message):
    try:
        # URL encode the message for special characters
        encoded_message = url_encode(message)
        
        # Use GET request with URL parameters (more reliable with MicroPython)
        url = f"{TELEGRAM_API_URL}?chat_id={TELEGRAM_CHAT_ID}&text={encoded_message}"
        
        response = urequests.get(url)
        
        if response.status_code == 200:
            print(f"Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            try:
                error_response = response.json()
                print(f"Error details: {error_response}")
            except:
                print(f"Response text: {response.text}")
        response.close()
    except Exception as e:
        print(f"Error sending message: {e}")

# Send initial message
print("Starting Telegram bot messages...")
send_telegram_message("🔴 Pico W is now connected and ready!")

# Counter for messages
message_count = 0
start_time = time.time()

# Main loop - send message every 10 seconds
while True:
    try:
        message_count += 1
        current_time = time.time() - start_time
        
        # Create message with device info
        message = f"""📡 Pico W Status Update #{message_count}
        
🕐 Uptime: {current_time:.1f} seconds
🌐 IP: {wlan.ifconfig()[0]}
📶 WiFi: {WIFI_SSID}
🔋 Status: Running normally

Hello from your IoT device! 🤖"""
        
        send_telegram_message(message)
        
        print(f"Waiting 10 seconds before next message...")
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("Program stopped by user")
        send_telegram_message("🔴 Pico W disconnected - Program stopped")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        time.sleep(5)  # Wait before retrying
