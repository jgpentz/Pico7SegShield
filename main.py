from machine import Pin
from utime import sleep
from max7219 import *

pin = Pin("LED", Pin.OUT)

# Create a max7219 device and run the display test
max = Max7219()
max.max7219_write(REG_MAX7219_DISP_TEST, 1)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
