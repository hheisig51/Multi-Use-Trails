## Notes: Using CircuitPython and Rasberry-Pi-Pico.
## Most accurate to ~55cm, past that doesn't seem accurate.

## Note 2/26/2024: try using a hotspot opposed to using the LoRa wifi stuff

import time #type:ignore
import board #type:ignore
import adafruit_hcsr04 #type:ignore
import busio  # type: ignore
import digitalio  # type: ignore
from digitalio import DigitalInOut # type: ignore

debounce_Sensor = False
countValue = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP14, echo_pin=board.GP15)

from CircuitPython_LCDFolder.lcd.lcd import LCD, CursorMode  # type: ignore
from CircuitPython_LCDFolder.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
# http://www.penguintutor.com/electronics/pico-lcd 
# Make sure to have at least 5v. Pico only gives 3 volts. use battery back.
# declare the singleton variable for the default I2C bus:

i2c_address = 0x3f
cols = 16
rows = 2
i2c_bus_0 = busio.I2C(board.GP15, board.GP14) # 1 rn
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
lcd = LCD(interface, num_rows=rows, num_cols=cols)

resetButton = digitalio.DigitalInOut(board.GP10) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.UP 
resetButtonWasPressed = False


while True:

    if resetButton.value == False and resetButtonWasPressed == False:
       resetButtonWasPressed = False
       print("Test 1 button")
    if resetButton.value == True and resetButtonWasPressed == True:
       resetButtonWasPressed = True #backward logic, true = false
       print("Test 2 button")

    try:
        distanceFromSensor = sonar.distance
        ##print((distanceFromSensor,))

        if distanceFromSensor >= 5 and distanceFromSensor <= 50 : ## This is the range we want to collect data from
           ## print("mid range, add to count")
            if debounce_Sensor == False:
                ##print("took input")
                debounce_Sensor = True
                countValue += 1
                print(countValue)

    except RuntimeError:
        ##print("Retrying!")
        if debounce_Sensor == True:
            debounce_Sensor = False
        pass
    time.sleep(0.1)

