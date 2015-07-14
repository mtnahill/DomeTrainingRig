# coding: utf-8
# UserInput.py contains all the functions involved in retrieving 
# user input from the LCD screen and displaying feedback
#
# Max Basescu
# mbasesc1@jhu.edu

# So we can use the module's concepts of different buttons
# like LCD.SELECT and LCD.UP 
import Adafruit_CharLCD as LCD
import time

# Generic form function that takes <lcd>, the variable containing the display,
# <message>, to prompt the user (note that this should be the bare name of the 
# field being requested, e.g. 'Day'), and <minVal>, the minimum acceptable value
# that the user is allowed to input
def genForm(lcd, message, minVal):

	# Initial variable states
	x = minVal					# Counter internal loop variable
	formVal = minVal

	# Display Input on LCD Screen			
	lcd.clear()					# Clear LCD Screen
	lcd.message(message + ': ' + str(minVal))	# Display message to screen
	msgLength = len(message) + 2			# Find message length including ': '

	# Repeat process until select is pressed
	while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
		lcd.set_cursor(msgLength, 0)		# Set cursor to be after string - awaiting input
	
		# Checks if the up button is pressed, then waits for it to be released
		if lcd.is_pressed(LCD.UP): 	
			while lcd.is_pressed(LCD.UP):
				pass

			# Increases value of x and displays updated val to user
			x = x + 1	
			lcd.message('    ');	
			lcd.set_cursor(msgLength, 0)
			lcd.message(str(x)) 
			time.sleep(0.1)	
		
		# Checks if the down button is pressed, then waits for it to be released
		elif lcd.is_pressed(LCD.DOWN): 	
			while lcd.is_pressed(LCD.DOWN):
				pass

			# Decreases value of x if it will remain above <minVal>,
			# and displays new value of x to user
			x = (x-1) if (x > minVal) else minVal
			lcd.message('    ');	
			lcd.set_cursor(msgLength, 0)
			lcd.message(str(x)) 		
			time.sleep(0.1)			
	
	# Wait for select to be released
	while lcd.is_pressed(LCD.SELECT) == True:
		pass

	formVal = x
	print(message + ' is: ' + str(formVal))		# Prints feedback message to terminal   

	return formVal  
