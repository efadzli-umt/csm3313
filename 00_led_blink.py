import machine
import utime

pin = machine.Pin("LED", machine.Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        utime.sleep(0.1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
