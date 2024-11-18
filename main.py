from machine import Pin
from utime import sleep
from max7219 import *

pin = Pin("LED", Pin.OUT)

# Create a max7219 device and run the display test
max = Max7219()
max.max7219_write(REG_MAX7219_DISP_TEST, 0) # DEBUG: Set to 1 for display test
max.max7219_write(REG_MAX7219_DECODE_MODE, 0xFF) # Use Code B Font
max.max7219_write(REG_MAX7219_SCAN_LIMIT, 0x7) # Display all digits
max.max7219_write(REG_MAX7219_INTENSITY, 0xF) # Max intensity
max.max7219_write(REG_MAX7219_SHUTDOWN, 1) # Enable normal operation

print("LED starts flashing...")
while True:
    try:
        num = int(input("Enter a number to display..."))
        max.max7219_write(REG_MAX7219_DIG_0, num)
        max.max7219_write(REG_MAX7219_DIG_1, num)
        max.max7219_write(REG_MAX7219_DIG_2, num)
        max.max7219_write(REG_MAX7219_DIG_3, num)
        max.max7219_write(REG_MAX7219_DIG_4, num)
        max.max7219_write(REG_MAX7219_DIG_5, num)
        max.max7219_write(REG_MAX7219_DIG_6, num)
        max.max7219_write(REG_MAX7219_DIG_7, num)
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
