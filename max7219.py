from machine import SPI, Pin

# No-Op Register
REG_MAX7219_NO_OP = 0x0

# Digit registers
REG_MAX7219_DIG_0 = 0x1
REG_MAX7219_DIG_1 = 0x2
REG_MAX7219_DIG_2 = 0x3
REG_MAX7219_DIG_3 = 0x4
REG_MAX7219_DIG_4 = 0x5
REG_MAX7219_DIG_5 = 0x6
REG_MAX7219_DIG_6 = 0x7
REG_MAX7219_DIG_7 = 0x8

#Extra Functions
REG_MAX7219_DECODE_MODE = 0x9
REG_MAX7219_INTENSITY = 0xA
REG_MAX7219_SCAN_LIMIT = 0xB
REG_MAX7219_SHUTDOWN = 0xC
REG_MAX7219_DISP_TEST = 0xF

class Max7219():
    def __init__(self):
        # Create a chip select pin and configure the SPI
        # TODO: Move these initializations up to the user code
        self.max7219_cs = Pin(13, Pin.OUT, value=1)
        self.max7219_spi = SPI(
            1, 
            baudrate=1000000, # Try this with scientific notatoin
            polarity=0,
            phase=0,
            bits=8,
            firstbit=SPI.MSB,
            sck=Pin(10),
            mosi=Pin(11),
        )

    def max7219_write(self, addr: int, data: int) -> int | None:
        if addr < 0 or addr > 15:
            raise Exception(f"there are only 15 addresses (zero indexed), got={addr}")
        if data > 255:
            raise Exception(f"data is only 8 bits (max value is 255), got={data}")

        # Build the 16 bit data packet
        # bits 8-11  addr
        # bits 0-7   data
        tx_data = 0x0000
        tx_data |= addr << 8
        tx_data |= data
        tx_data = tx_data.to_bytes(2, 'big')
        print(tx_data)
        

        # Send the data over SPI``
        try:
            self.max7219_cs(0)
            self.max7219_spi.write(tx_data)
        finally:
            self.max7219_cs(1)

        return 0
