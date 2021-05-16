---
layout: post
title: Test Tube Photometer
date: 2017-12-09
description: Shopping List
author: Alex Kutschera
twitter_text: 'Test Tube Photometer'
category: research
---
<img align="right" src="https://raw.githubusercontent.com/vektorious/test_tube_photometer/master/pictures/sketch.png" style="width: 500px ;" hspace="20" vspace="20"/>
This is the first part of the complete test tube photometer building instructions: The Shopping List.
But if you want you can directly go to the [building and wiring instructions](https://alexanderkutschera.com/2017/12/21/photometer-build-instructions.html).

Here you find a list of all the things you will need to build the test tube photometer, which we describe in our recent [paper](https://link.springer.com/article/10.1007%2Fs00284-017-1370-3). Additionally you will need standard electronics equipment including wires, resistors, breadboard for testing, soldering equipment and maybe some soldering experience.

### What do you need? ###

#### Main components ####
- **Arduino or similar microcontroller**<br>
You need something to read the analog input of the sensors in a measuring routine. We used an [Arduino Mega](https://store.arduino.cc/arduino-mega-adk-rev3) because it has 16 analog inputs.

- **LCD display**<br>
This one is optional but nice if you instantly want to see the measured values. It is useful for easy calibration and for discontinuous measurements with the photometer. You can use any available LCD which works well with the microcontroller. We used a standard HD44780 16x2 LCD Display.

- **Measuring cell**<br>
You obviously need at least one measuring cell to build the photometer but you can add as many as you like! You are just limited by the number of analog inputs on your microcontroller (one measuring cell requires one analog input!). All the components you need to build a measuring cell are listed above.
<br><br>


#### Measuring cell components ####
<img align="right" src="https://raw.githubusercontent.com/vektorious/test_tube_photometer/master/pictures/sketch2.png" style="width: 250px ;" hspace="120" vspace="130"/>
This are the components you need for one measuring cell
- **Housing and housing cover**<br>
We uploaded our 3D models for you at [Github](https://github.com/vektorious/test_tube_photometer/tree/master/3Dfiles). The housing has slots for the LED and the photodiode, which are fixed with the housing cover. If you do not have access to a 3D printer you can find service providers online. We printed it with standard black PLA and we recommend you to use black material, too, because it improves sensitivity of the system significantly. You might have to adjust the parameters of the housing to fit with the test tubes!

- **LED**<br>
It is really important to use a high quality LED because it determines the wavelength you are measuring with. We used a 740 nm LED from [Roithner LaserTechnik](http://www.roithner-laser.com/index.html) (article number: [LED740-01AU](http://www.roithner-laser.com/datasheets/led_div/infrared/led740-series.pdf)). If you prefer to measure at a different wavelength choose your LED accordingly!

- **Photodiode**<br>
This is the heart of the measuring cell. We used an [opt101](http://www.ti.com/lit/ds/symlink/opt101.pdf) from Texas Instruments because it contains an on-chip operational amplifier, and responds to light in the range of 300–1100 nm (linear dependence between 400–800 nm!). We added a 1MΩ external resistor to achieve a DC gain of 2 million volts per ampere to optimize the output voltages.
<br>
