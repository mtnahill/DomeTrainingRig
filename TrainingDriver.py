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
GPIO.setup(motorPin, GPIO.OUT)

os.chdir('/home/pi/DomeTrainingRig/')

while True:

	# Initialize the LCD using the pins
	lcd = LCD.Adafruit_CharLCDPlate()
	lcd.show_cursor(False)

	# Set backlight color to blue
	lcd.set_color(0.0, 0.0, 1.0)
	lcd.clear()

	# Show welcome screen with ip
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	ipAdd = s.getsockname()[0]
	lcd.message('Welcome! IP is:\n{}'.format(ipAdd))

	# Wait for select to be pressed
	while not lcd.is_pressed(LCD.SELECT):
		# If up is pressed
		if lcd.is_pressed(LCD.UP):
			while lcd.is_pressed(LCD.UP):
				time.sleep(0.1)

			# Send a 440 second pulse to prime lines
			GPIO.output(motorPin, True)
			time.sleep(440)
			GPIO.output(motorPin, False)

	# Wait for select to be released
	while lcd.is_pressed(LCD.SELECT):
		time.sleep(0.1)
	
	# Runs main program
	os.system('./TrainingProg')

