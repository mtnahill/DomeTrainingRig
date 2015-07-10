#!/usr/bin/python
# Example using a character LCD plate.
import math # for LCD
import time # for LCD
import Adafruit_CharLCD as LCD # for LCD
import RPi.GPIO as GPIO  # Import GPIO pin module
GPIO.setmode(GPIO.BOARD) #set mode of numbering pins

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(0.0, 0.0, 1.0) #set backlight to blue
lcd.clear()

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

laps = 0 #assign a counter for number of laps
degrees = 0 #assign a counter for number of degrees

lcd.message('Enter Laps:')
lcd.set_cursor(0,1)
lcd.message('Enter Degrees:')
lcd.set_cursor(11,0) #move cursor to end of 'Enter Laps' string
lcd.show_cursor(True) #Show cursor
lcd.blink(True) #Make the cursor blink as if waiting for input

print 'Press Ctrl-C to quit.'

lcd.message([laps])
#while True:
	# Loop through each button and check if it is pressed.
#	for button in buttons:
#		if lcd.is_pressed(button[2]):#checks if the up button is pressed
			# Button is pressed, change the message and backlight.
#			counter = counter +1
#			lcd.message(counter) #display counter
#			lcd.message(button[1])
#			lcd.set_color(button[2][0], button[2][1], button[2][2])
#message('Enter Number of Laps')


################################################
# Conversion from Current Arduino Code "training.ino"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)
GPIO.setup(36, GPIO.OUT)


dTheta0 = 30 # Degrees
dTheta1 = 30 # Degrees
feedInterval = 2000 # ms
laps = 250

dTheta = 60
nextFeedTheta = 0
feedStartTime = 0

trialStartFlag = 0
feedingFlag = 0


