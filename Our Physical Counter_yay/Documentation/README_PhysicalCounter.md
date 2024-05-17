<p align="center">
  <b>The Physical Counter</b><br>
  <a>Logan & Emma</a>
</p>

---
## Table of Contents
* [Intro](#Introduction)
* [Materials](#List-of-Materials)
* [Important](#Important-Links)
* [Operating Instructions](#Operating-Instructions)


---

### Introduction

<img src="https://github.com/hheisig51/Multi-Use-Trails/assets/71342159/c9510029-bf4e-48e2-b448-e285bddba955" width="400" height="400">

We decided to make a physical counter of our own to better understand how they work. In short, a counter for data collection should involve a sensor, a way to power the device overall, a way to collect and/or display the data, and a way to reset the data on the counter. 

Following this, here's a list of our essentials for a counter:
- Sensor: Ultrasonic Sensor (HC-SR04 (5V))
- Microcontroller: Raspberry Pi Pico
- Powering device: using USB connection from Pico to Computer.
- A way to collect and/or display the data: LCD w/ backpack that shows the 'Sensor count'.
- A way to reset the data: a pushbutton that resets data when pushed.

---

### List of Materials
|Name |Quantity |
|--- | --- |
| LCD w/ I2C Backpack | 1 |
| #72 x 3/8" Socket Head Cap Screws | 6 |
| #4-40 x 5/8" Socket Head Cap Screws | 10 |
| Pushbutton | 2 |
| Rasberry Pi Pico | 1 |
| Micro USB to USB cord | 1 |
| 9v Power Supply Box (six 1.5volt batteries needed) | 1 |
| Switch | 1 |
| Ultrasonic Sensor (HC-SR04 (needs 5 volts)) | 1 |
| Wires | 14 Total (if no component already has wires soldered onto it) |
| Breadboard | 1 |
| Wood Sheet (cut CAD drawing provided above w/ laser cutter) | 1 |

---

### Important Links

Additional Updates:
[https://github.com/hheisig51/Multi-Use-Trails/blob/main/Our%20Physical%20Counter/Code/Documentation/UpdatesForPhysicalCounter.md
](https://github.com/hheisig51/Multi-Use-Trails/blob/main/Our%20Physical%20Counter/Code/Documentation/UpdatesForPhysicalCounter.md)

Link to CAD: 
[https://cvilleschools.onshape.com/documents/2fb32092faf015ebcf5fdffe/w/bc45d2d27e870d15d7a95540/e/304623c3b142e96e0f089fb8
](https://cvilleschools.onshape.com/documents/2fb32092faf015ebcf5fdffe/w/bc45d2d27e870d15d7a95540/e/304623c3b142e96e0f089fb8)

Link to Code:
[https://github.com/hheisig51/Multi-Use-Trails/blob/main/Our%20Physical%20Counter/Code/MainCodeForCounter.py
](https://github.com/hheisig51/Multi-Use-Trails/blob/main/Our%20Physical%20Counter/Code/MainCodeForCounter.py)

---

### Wiring Diagram

<img src="https://github.com/hheisig51/Multi-Use-Trails/assets/71342159/ef41d745-08f2-44da-bb5d-06930be7f529" width="655" height="362">

*Note: The program I am using is TinkerCad. It is limited in components. Thus, I have written pins to the correct connection.*

### Pico Pinouts

<img src="https://github.com/hheisig51/Multi-Use-Trails/assets/71342159/e9c71b26-78bb-44f9-b2a1-392d663888fc" width="550" height="500">


###  Operating Instructions

**General:**

Step 1: Power the device. Make sure the Switch is flipped to the Data Mode.

Step 2: Wave your hand or any object parallel to the box's sensor. The count should go up internally and be displayed on the LCD.

Step 3 a: Press the reset button to reset data.

Step 3 b: Looking at data requires the box to be unpowered by disconnecting USB plug and 9 volt power supply. After this, flip the switch to Code Mode, plug the power back in, and go to the .CSV file to see the data.

**Additional:**

If you want to see prints, make sure everything is powered correctly. This means the MicroUSB to USB is plugged into the Pico and Computer. The external power supply must be connected properly as well. That means all ground wires are connected in some way on the breadboard. Additionally, make sure the switch is flipped to code mode for the board to be seen when plugged into a computer. I can loosely recommend Mu for reading print statements.

