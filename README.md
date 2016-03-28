![Altax](https://altax.net/images/altax.png "Altax")

# pyIRCamera

Python Module that talks to a Wiimote IR camera connected to an I2C bus.

## What is a PixArt?

This device is a 128x96 monochrome camera with built-in image processing. The camera looks through an infrared pass filter in the remote's plastic casing. The camera's built-in image processing is capable of tracking up to 4 moving objects, and these data are the only data available to the host. Raw pixel data is not available to the host, so the camera cannot be used to take a conventional picture. The built-in processor uses 8x subpixel analysis to provide 1024x768 resolution for the tracked points.

![PixArt camera](https://altax.net/images/pyIRCamera/pixart.jpg "PixArt camera")

This camera is used on the WiiMote controller. 

![Wiimote](https://altax.net/images/pyIRCamera/wiimote.jpg "PixArt camera")

The is lots of technical information about the Wiimote: http://wiibrew.org/wiki/Wiimote#IR_Camera

The sensor used for this library is a very good package made by DFRobot, important links:

* To buy it: http://www.dfrobot.com/index.php?route=product/product&product_id=1088#.VvlgYBIrKso
* Wiki: http://www.dfrobot.com/wiki/index.php/Positioning_ir_camera

![Positioning IR Camera](https://altax.net/images/pyIRCamera/ircamera.jpg "Positioning IR Camera")

## Why this module?

The only code that is online is for Arduino, its on C. I need to use this sensor with python and a Raspberry Pi. That's the main reason.

# How?

* The first step is to gather all components, the sensor and a computer with I2C port. I'm choosing the RPI, due to the fact that I have one in my desk right now. The sensor is approximately $25 USD
* Connect the sensor to the raspberry pi 
* Activate the raspberry pi I2C port
* Clone this library on the raspberry pi
* Run ```python test-example.py```

## Activate the raspberry pi I2C

* Execute ```sudo raspi-config```
* Go to ```Advanced Options```
* Go to ```I2C``` and enable it, select yes also for the module to be loaded by default on boot
* Reboot
* Install: ```sudo apt-get install python-smbus i2c-tools```
* Add to the modules file ```sudo nano /etc/modules``` the next lines:
```
i2c-bcm2708 
i2c-dev
```
* Edit the file: ```sudo nano /boot/config.txt``` and add this lines:
```
dtparam=i2c1=on
dtparam=i2c_arm=on
```
* Reboot again

## Test the I2C port / Sensor

* With the sensor already connected to the raspberry pi, execute this line: ```sudo i2cdetect -y 1```, if the sensor is connected and working you will see something like this:
```
0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```
* The sensor address is ```0x58```