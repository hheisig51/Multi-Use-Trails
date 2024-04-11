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
    with open("/dataCollected.txt", "a") as fp:
        while True:
            countToSend = code.countValue
            fp.write('{0:f}\n'.format(countToSend))
            fp.flush()
            time.sleep(1)
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