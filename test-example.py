#!/usr/bin/env python

"""test-example.py: Test script that uses the pyIRcam module and shows the coordinates of the 4 IR objects seeing by the sensor. """

"""
Requirements:

- Positioning IR camera (http://www.dfrobot.com/wiki/index.php/Positioning_ir_camera), or PixArt WiiMote camera
- Raspberry Pi (or any computer with python capabilities and exposed I2C port)

"""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2016 Altax.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyIRcam import pyIRcam
from time import sleep,time

update_rate = 0.01 # 100hz update rate

camera = pyIRcam() # Sensor initialization

while True:
	current = time() # Counters for loop
	elapsed = 0

	camera.getPositions() # Update found IR objects
	
	if camera.positions['found']: # If an IR object is found, print the information
		print "Object 1: %d, %d | Object 2: %d, %d | Object 3: %d, %d | Object 4: %d, %d" % (camera.positions['1'][0],camera.positions['1'][1],camera.positions['2'][0],camera.positions['2'][1],camera.positions['3'][0],camera.positions['3'][1],camera.positions['4'][0],camera.positions['4'][1])
	
	while elapsed < update_rate:
		elapsed = time() - current # Wait until the loop completes, perfect update_rate loop