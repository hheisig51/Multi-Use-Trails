import board # type: ignore
import digitalio  # type: ignore
import time # type: ignore
import busio  # type: ignore
from digitalio import DigitalInOut # type: ignore

from CircuitPython_LCD.lcd.lcd import LCD, CursorMode  # type: ignore
from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
# https://github.com/dhalbert/CircuitPython_LCD
# when downloading, the name of the folder was "CircuitPython_LCD-main", change that name of the folder and make sure it matches the above name.

# http://www.penguintutor.com/electronics/pico-lcd 
# Make sure to have at least 5v for LCD. Use battery pack or use VBUS. Note: VBUS has no volts when the pico's USB is unplugged.

i2c_address = 0x27 # check the i2c address of your specific device
i2c_bus_0 = busio.I2C(board.GP11, board.GP10) # make sure to check (SLC, SCA)
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=2, num_cols=16) # change the num based on that LCD's rows and cols

lcd.clear() # do this each time you want to write something new on the LCD, if you don't text will overlap
lcd.print("Here I am")