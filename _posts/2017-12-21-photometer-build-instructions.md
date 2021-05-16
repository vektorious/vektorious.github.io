---
layout: post
title: Test Tube Photometer
description: Building Instructions
date: 2017-12-21
author: Alex Kutschera
twitter_text: 'Test Tube Photometer'
category: research
---
<img align="right" src="https://raw.githubusercontent.com/vektorious/test_tube_photometer/master/pictures/cell_cover_fused.png" style="width: 500px ;" hspace="20" vspace="20"/>

This is the second part of the complete test tube photometer building instructions: The building and wiring instructions.
But if you want you can go back to the [the shopping list](https://alexanderkutschera.com/2017/12/09/photometer-shopping-list.html). Here you find instructions for building the test tube photometer. If something is not completely clear to you, let us know and we will help you!

### Build the measuring cell ###
- **Assemble the housing**<br>
The housing consists out of two parts, the main body and a sleeve. There are two respective holes in the main body in which you can place the sensor and the LED. Slowly pull the sleeve over the main body with the LED and Sensor pins sticking out (see picture above). Please remember the sensor orientation for the correct wiring of the pins!

- **Wiring**
<img align="right" src="https://raw.githubusercontent.com/vektorious/test_tube_photometer/master/pictures/cell_wiring.jpg" style="width: 500px ;" hspace="20" vspace="20"/><br>
Now you can start and solder wires to the sensor an LED pins. If you have problems soldering the sensor pins with the housing assembled you can remove the sensor, solder the wires and then assemble the housing. But then you might have to use some force to fit the soldered pins through the gaps.
I labeled each wire to make it easier for me to connect them later.<br>
**You should end up with five wires from the sensor:**
  - Power (V, pin 1)
  - Input/Additional Feedback (-In, pin 2)
  - Power/Ground (-V, pin 3)
  - Output (Output, pin 5)
  - Input/Ground (Common, pin 8)

### Connect it to the microcontroller ###
Connect sensor pin 1 to 5V, pin 3 and 8 to ground. Sensor pin is connected to pin 5 with a 1 MΩ resistor in between (see circuit diagram on the right). You can now connect the sensor output (pin 5) to any analog input pin of your microcontroller and you are ready to measure light.
<img align="right" src="https://raw.githubusercontent.com/vektorious/test_tube_photometer/master/pictures/sketch3.png" style="width: 300px ;" hspace="20" vspace="20"/>
Speaking of light, you still have to connect the LED with one of the digital output pins of the microcontroller to switch the light on and off.


Well, that's basically all you need to do to use your test tube photometer. If you like you can connect an LCD display to the microcontroller to display the measured values directly. I connected my photometer to a Raspberry Pi and let them communicate via the serial connection. The microcontroller runs [this script](https://github.com/vektorious/test_tube_photometer/tree/master/Arduino/test_tube_ALK) and sends the data to the Pi which calculates the OD [with this python script](https://github.com/vektorious/test_tube_photometer/blob/master/python_scripts/dataStream_wo.py) and writes everything to a .csv file.

### That's it! If you have any questions or feedback, don't hesitate to contact me! ####
