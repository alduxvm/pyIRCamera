#!/usr/bin/env python

"""pyIRcam.py: Module that talks to PixArt camera connected to the I2C bus. """

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

import smbus
from time import sleep

class pyIRcam:
	""""Class that handles the sensor communication"""
	def __init__(self):
		self.sensorAddress = 0x58 # Check before to be sure its the correct address
		#self.rate = rate
		self.device = smbus.SMBus(1)
		self.positions = {'found':False,'1':[0,0],'2':[0,0],'3':[0,0],'4':[0,0]}
		# Initialization of the IR sensor
		self.initCMDs = [0x30, 0x01, 0x30, 0x08, 0x06, 0x90, 0x08, 0xC0, 0x1A, 0x40, 0x33, 0x33]
		for i,j in zip(self.initCMDs[0::2], self.initCMDs[1::2]):
			self.device.write_byte_data(self.sensorAddress, i, j)
			sleep(0.01)

	def getPositions(self):
		self.device.write_byte(self.sensorAddress, 0x36)
		data = self.device.read_i2c_block_data(self.sensorAddress, 0x36, 16)
		x = [0x00]*4
		y = [0x00]*4
		i=0
		for j in xrange(1,11,3):
			x[i]=data[j]+((data[j+2] & 0x30) << 4)
			y[i]=data[j+1]+((data[j+2] & 0xC0) << 2)
			i+=1
		i=0
		for j in ('1','2','3','4'):
			self.positions[j][0]=x[i]
			self.positions[j][1]=y[i]
			i+=1
