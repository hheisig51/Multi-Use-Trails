List of Additional Updates for the Physical Counter we made.


3/21/2024:
- Updated main readme 
- Notes on the counter:
     - Data Saving --> When unplugging the pico, the data resets. Emma suggested writing the data to a file.
     - Sensor Sensitivity --> The sensor seems sensitive yet also not sensitive enough. I'll need to play around with the numbers.
     - Method of Powering --> Right now the sensor is powered by USB to the computer. We should power it with a battery instead.
     - Annoyances with Assembly --> The process of putting the box together was quite annoying. I could try making more things friction fit or try another method. Maybe out of the scope of this project.
 
Week of 4/8/2024:
- Monday: This week I'm learning about about storage on the Pico. Getting data to save seems to be quite complicated, more than I thought it'd be.
     - [https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage](https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage)
- Thursday: Last class I broke the pico trying to write to a file. So, this class, I fixed the pico with help from Emma and Mr. Miller. I've made a Code folder, Lib folder, and have added other files to this in case anything else happens. If something happens, it should no longer take an entire class period to fix it.
- Friday: going through this: https://docs.google.com/document/d/1RtqWXy4P9aIcJqrYk6g71_IP663rZxrHkY_nHGh0bgs/edit

Week of 4/15/2024:
- Monday: I've gotten data mode and code mode switching to work. The issue now is getting the pico's drive to show up when being plugged in/booted. The solution to this seems to be flash_nuking the pico, reinstalling the .uf2 file, and putting back in code & library files.
   - Notes: counter should only be able to count data in data mode. Confirm the counter is in dataMode when collecting data. The 'as open .cvs' thing should make a file by itself. Will test more next class.

Week of 4/22/2024:
- Tuesday: I have a new Pico but it doesn't have a Boot Select button for resetting the board. And, I might've fried the Pico. The drive is not showing up when the board is plugged in. The Code or wiring could be wrong, not sure what currently. I have an LED that should tell me when the Pico is in Code or Data mode.
- 4/26/2024: I have another Pico, this one works fine. Writing to the csv file still doesn't work, but I learned more about the Ultra Sonic Sensor. When an object is at an angle, that can deflect the sonar pulse and thus the code will timeout and not count that as a count for the data. This is a limitation of the Ultra Sonic Sensor.

Week of 4/29/2024:
- Friday: We finanally got the counter to work with writing code to the .csv file. Note to self: don't import code.py from boot.py and make sure to use 4.5 volts not 9 volts. The sensor can only take so many volts. Code files are updated.

![image](https://github.com/hheisig51/Multi-Use-Trails/assets/71342159/9d2351d0-24a3-49f0-81ef-91741d75d4cc)
