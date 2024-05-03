# Notes: Using CircuitPython and Rasberry-Pi-Pico.
# Note 2/26/2024: try using a hotspot opposed to using the LoRa wifi stuff

from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface  # type: ignore
from CircuitPython_LCD.lcd.lcd import LCD, CursorMode  # type: ignore
import time  # type:ignore
import board  # type:ignore
import adafruit_hcsr04  # type:ignore
import busio  # type: ignore
import digitalio  # type: ignore
from digitalio import DigitalInOut  # type: ignore
import storage  # type: ignore

### - Sensor - ###
debounce_Sensor = False
countValue = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP14, echo_pin=board.GP15)
# Most accurate to ~55cm, past that doesn't seem accurate.

### - LCD - ###
# https://github.com/dhalbert/CircuitPython_LCD
# when downloading, the name of the folder was "CircuitPython_LCD-main", change that name of the folder and make sure it matches the above name.

# http://www.penguintutor.com/electronics/pico-lcd
# Make sure to have at least 5v for LCD. Use battery pack or use VBUS. Note: VBUS has no volts when the pico's USB is unplugged.

i2c_address = 0x27  # check the i2c address of your specific device
i2c_bus_0 = busio.I2C(board.GP11, board.GP10)  # make sure to check (SLC, SCA)
interface = I2CPCF8574Interface(i2c_bus_0, i2c_address)
# change the num based on that LCD's rows and cols
lcd = LCD(interface, num_rows=2, num_cols=16)

# lcd.clear() # do this each time you want to write something new on the LCD, if you don't text will overlap
# lcd.print("Here I am")
######


resetButton = digitalio.DigitalInOut(board.GP16)  # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.UP
resetButtonWasPressed = False


switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

###time.sleep(4)

lcd.clear()
lcd.print("Sensor count: " + str(countValue))
print("code.py is running!")


while True:
    ##print(switch.value)
    
    if resetButton.value == False:
        if resetButtonWasPressed == False:
            resetButtonWasPressed = True
            print("Reset button pressed!")
            countValue = 0
            countValueAsString = str(countValue)
            ##lcd.clear()
            ##lcd.print("Sensor count: " + countValueAsString)

    elif resetButton.value == True:
        if resetButtonWasPressed == True:
            resetButtonWasPressed = False
            # print("Test button 2")

    try:
        ##print(sonar)
        distanceFromSensor = sonar.distance
        ##print((distanceFromSensor))

        if distanceFromSensor >= 5 and distanceFromSensor <= 66:  # This is the range we want to collect data from
            ##print("mid range, add to count")
            if debounce_Sensor == False:
                # print("took input")
                debounce_Sensor = True
                countValue += 1
                countValueAsString = str(countValue)
                print(countValueAsString)
                ##lcd.clear()
                ##lcd.print("Sensor count: " + countValueAsString)
                
                try:
                    with open("/data.csv", "a") as datalog:
                        time.sleep(1)
                        time_elapsed = time.monotonic()
                        countToSend = countValue
                        datalog.write(f"{time_elapsed},{countToSend}\n")
                        datalog.flush()
                        lcd.clear()
                        lcd.print("Wrote to file!")
                        print("wrote to file!")
                        
                except Exception as error_2:
                    print("Couldn't write to file!")
                    ##print(error_2)
                    lcd.clear()
                    lcd.print(str(error_2))

    except Exception as error_1:
        ##print("Retrying!")
        print(error_1)
        if str(error_1) == "Timed out":
            if debounce_Sensor == True:
                debounce_Sensor = False
                
        pass

    time.sleep(0.02)
