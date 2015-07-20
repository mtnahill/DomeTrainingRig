# coding: utf-8
#!/usr/bin/python

# Max Basescu
# mbasesc1@jhu.edu

import socket
import time
import os
import Adafruit_CharLCD as LCD

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
		pass

	# Wait for select to be released
	while lcd.is_pressed(LCD.SELECT):
		time.sleep(0.1)
	
	# Runs main program
	os.system('sudo python TrainingRig_UserInput.py')

