#!/usr/bin/python
# coding: utf-8

# Max Basescu
# mbasesc1@jhu.edu

import socket
import time
import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

motorPin = 17

os.chdir('/home/pi/DomeTrainingRig/')

while True:
	# Initialize motor pin
	GPIO.setup(motorPin, GPIO.OUT)
	
	# Initialize the LCD using the pins
	lcd = LCD.Adafruit_CharLCDPlate()
	lcd.show_cursor(False)

	# Set backlight color to blue
	lcd.set_color(0.0, 0.0, 1.0)
	lcd.clear()

	# Get ip
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	ipAdd = s.getsockname()[0]

	welcomeMsg = 'Welcome!\nDOWN for help'
	lcd.message(welcomeMsg)

	# Wait for select to be pressed
	while not lcd.is_pressed(LCD.SELECT):
		# If left is pressed
		if lcd.is_pressed(LCD.LEFT):
			ipMsg = 'IP:\n{}'.format(ipAdd)
			lcd.clear()
			lcd.set_color(1.0, 1.0, 0.0)
			lcd.message(ipMsg)

			while not (lcd.is_pressed(LCD.UP) or lcd.is_pressed(LCD.DOWN) or lcd.is_pressed(LCD.LEFT) or lcd.is_pressed(LCD.RIGHT) or lcd.is_pressed(LCD.SELECT)):
				pass;
			
			lcd.clear()
			lcd.set_color(0.0, 0.0, 1.0)
			lcd.message(welcomeMsg)
	
		# If down is pressed
		elif lcd.is_pressed(LCD.DOWN):
			helpMsg = ' UP:Prime RT:Off\nSEL:Start LT:IP'
			lcd.clear()
			lcd.set_color(0.0, 1.0, 0.0)
			lcd.message(helpMsg)
			
			while not (lcd.is_pressed(LCD.UP) or lcd.is_pressed(LCD.DOWN) or lcd.is_pressed(LCD.LEFT) or lcd.is_pressed(LCD.RIGHT) or lcd.is_pressed(LCD.SELECT)):
				pass;
			
			lcd.clear()
			lcd.set_color(0.0, 0.0, 1.0)
			lcd.message(welcomeMsg)

		# If up is pressed
		elif lcd.is_pressed(LCD.UP):
			while lcd.is_pressed(LCD.UP):
				time.sleep(0.1)

			# Prime the lines until up is pressed again
			GPIO.output(motorPin, True)
			lcd.clear()
			lcd.set_color(0.0, 1.0, 1.0)
			lcd.message('Priming motor...\n')
			while not lcd.is_pressed(LCD.UP):
				time.sleep(0.05)

			while lcd.is_pressed(LCD.UP):
				time.sleep(0.1)

			# Turn off motor
			GPIO.output(motorPin, False)
			lcd.clear()
			lcd.set_color(0.0, 0.0, 1.0)
			lcd.message(welcomeMsg)

		# Shutdown if right is pressed	
		elif lcd.is_pressed(LCD.RIGHT):
			while lcd.is_pressed(LCD.RIGHT):
				time.sleep(0.1)
			
			# Prompt for confirmation of shutdown
			lcd.clear()
			lcd.set_color(1.0, 0.0, 0.0)
			lcd.message('Are you sure?\nUP=yes, DOWN=no')

			while not lcd.is_pressed(LCD.UP) and not lcd.is_pressed(LCD.DOWN):
				pass
			
			# Up means yes
			if lcd.is_pressed(LCD.UP):
				lcd.clear()
				lcd.message('Shutting down...\n')
				os.system('shutdown -h now')
			
			# Down means cancel
			else:
				while lcd.is_pressed(LCD.DOWN):
					time.sleep(0.1)
				lcd.clear()
				lcd.set_color(0.0, 0.0, 1.0)
				lcd.message(welcomeMsg)

	# Wait for select to be released
	while lcd.is_pressed(LCD.SELECT):
		time.sleep(0.1)
	
	# Runs main program
	os.system('./TrainingProg')

