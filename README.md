# IoT individual project


## Overview

I have created a system that has the capability of measuring the soil moisture of a plant and also water it if necessary. It is a useful tool for people who want to monitor the status of their apartment plants and would like to see in real time how much water they are pouring.

## Schema
![schema_1_bb](https://github.com/ATchibo/IoT-Proiect-Individual/assets/44547421/d5bbeeab-4f70-41f4-854b-3b5abdf0ed22)
* built with Fritzng
* the motor is a replacement for my water pump
* the moisture sensor I used is not the same model as the one pictured here but it works the same
* the screen is not the real screen; in reality, my touchscreen connects to the Raspberry Pi via a 5V pin, a ground and a DSI cable.

## Components

- Raspberry Pi 4B with a power supply (https://www.optimusdigital.ro/ro/placi-raspberry-pi/8617-raspberry-pi-4-model-b-4gb-765756931182.html)
- 32GB or more MicroSD card
- 7 inch DSI capacitive touchscreen LCD (https://www.waveshare.com/wiki/7inch_DSI_LCD) - comes with all necessary cables included
- Breadboard (https://cleste.ro/breadboard-830-puncte-mb-102-mb102.html)
- A MCP3008 Analog to Digital converter (https://ro.farnell.com/microchip/mcp3008-i-p/10bit-adc-2-7v-8ch-spi-16dip/dp/1627174)
- a moisture sensor (https://www.optimusdigital.ro/ro/senzori-senzori-de-umiditate/12803-senzor-de-umiditate-a-solului.html?search_query=senzor+umiditate&results=87)
- a Mosfet relay (https://www.sigmanortec.ro/Modul-IRF520-p141724639)
- a 9V battery with terminal connector (https://cleste.ro/suport-baterie-de-9v-cu-capac.html, https://cleste.ro/baterie-alcalina-varta-industrial-9v.html)
- a water pump (https://www.sigmanortec.ro/Pompa-Apa-Aer-cu-diafragma-6-12V-R385-p190556176)
- two small hoses 
- 7 DuPont male-male wires (https://cleste.ro/10-x-fire-dupont-tata-tata-10cm.html)
- 7 DuPont male-female wires (https://cleste.ro/10xfire-dupont-mama-tata-20cm.html)
- 1 DuPont female-female wire (https://cleste.ro/10-x-fire-dupont-mama-mama-10cm.html)

## Setup and Build Plan

1. We use two male-female cables to link a 5V pin and a ground pin from the Raspberry to the breadboard
2. We take the ADC and place it on the breadboard like in the schema above
3. We use the appropiate cables (4 male-male, 4 male-female) to connect the Raspberry to the ADC
4. We take the moisture sensor and connect its pins to 5V, ground and the pin of the ADC corresponding to channel 1 (the second one on the left)
5. We link the ground pin of the Mosfet to the ground of the Raspberry and we link the Signal pin to the corresponding GPIO pin from the Raspberry
6. We connect the water pump and the battery to the Mosfet, then attach the hoses to the pump
7. In the end, to complete the hardware setup, we also connect the touchscreen to the Raspberry
8. We need to put Raspberry Pi OS on our MicroSD card, which will be inserted in our Raspberry Pi
9. After we boot in Raspberry Pi OS, we need to clone this repository on our Raspberry Pi (make sure you have Python3, git setup is not mandatory but recommended)
10. We enter the project folder and run "python3 main.py", then the app should launch shortly
11. Place one tube in a water tank and in the flower pot put the other tube and the moisture sensor
12. Enjoy!

## Using the app

In the home screen we see a bottom navigation bar. If we go to the last section (Watering options) you have the option to press a button to chech the current moisture, as well as to press a button to trigger the on/off operation of the pump.
