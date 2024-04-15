import busio  # type: ignore
from CircuitPython_LCD.lcd.lcd import LCD, CursorMode  # type: ignore
from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
i2c_address = 0x27 # check the i2c address of your specific device
i2c_bus_0 = busio.I2C(board.GP11, board.GP10) # make sure to check (SLC, SCA)
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=2, num_cols=16) # change the num based on that LCD's rows and cols
lcd.clear()
lcd.print("boot.py running!")
print("boot.py is running!")



# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
# SPDX-License-Identifier: MIT

## Note: boot.py only runs on first boot of the device, not if you re-load the serial console with ctrl+D or if you save a file. You must EJECT the USB drive, then physically press the reset button!

"""CircuitPython Essentials Storage logging boot.py file"""
import board #type:ignore
import digitalio #type:ignore
import storage #type:ignore
import time #type:ignore

## The code.py script/module:
import code #type:ignore

# For Gemma M0, Trinket M0, Metro M0/M4 Express, ItsyBitsy M0/M4 Express
switch = digitalio.DigitalInOut(board.GP0)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", readonly=switch.value)

print("test A")

try:
   with open("/data.csv", "a") as datalog:
        while True:
            time.sleep(1)

            time_elapsed = time.monotonic()
            countToSend = code.countValue

            all_data_to_send =  f“{time_elapsed},{countToSend}\n”
            
            datalog.write(all_data_to_send)
            datalog.flush()

            lcd.clear()
            lcd.print(".csv file updated with data!")

except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.5  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.25  # ...blink the LED faster!
    while True:
        time.sleep(delay)
        print("test B")
        if switch.value == True:
            print("switch, True")
        
        if switch.value == False:
            print("switch, False")
