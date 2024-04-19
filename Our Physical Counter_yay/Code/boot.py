import busio  # type: ignore
import board #type:ignore
import digitalio #type:ignore
import storage #type:ignore
import time #type:ignore
import code #type:ignore

switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
if switch.value == False:
    storage.remount("/", readonly=switch.value)


time.sleep(4)
