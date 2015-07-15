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
# and <message>, to prompt the user (note that this should be the bare name 
# of the field being requested, e.g. 'Day')
def genForm(lcd, message, minVal):

	# Initial variable states
	valIndex = 0
	valStr = list("0    ")				# String with which to display value to user

	# Display Input on LCD Screen			
	lcd.clear()					# Clear LCD Screen
	lcd.message(message + ': ' + "".join(valStr))	# Display message to screen
	msgLength = len(message) + 2			# Find message length including ': '
	cursorPos = msgLength				# Initial position of cursor
	cursorMax = cursorPos + 3			# Allows 4 digit input

	# Repeat process until select is pressed
	while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
		lcd.set_cursor(cursorPos, 0)		# Set cursor to be after string - awaiting input
		
		valIndex = cursorPos - msgLength

		# Checks to see if the left or right buttons are being pressed, and moves cursor if permitted
		if lcd.is_pressed(LCD.RIGHT):
			while lcd.is_pressed(LCD.RIGHT):
				pass
			if cursorPos < cursorMax:
				cursorPos += 1

		elif lcd.is_pressed(LCD.LEFT):
			while lcd.is_pressed(LCD.LEFT):
				pass
			if cursorPos > msgLength:
				cursorPos -= 1

		# Checks if the up button is pressed, then waits for it to be released
		elif lcd.is_pressed(LCD.UP): 	
			while lcd.is_pressed(LCD.UP):
				pass
			
			# Increases value at cursor position if < 9
			if valStr[valIndex] == ' ':
				valStr[valIndex] = '0'
			elif valStr[valIndex] < '9':
				valStr[valIndex] = str(int(valStr[valIndex]) + 1)

			# Displays new message to user
			lcd.set_cursor(msgLength, 0)
			lcd.message("".join(valStr)) 
			time.sleep(0.1)	
		
		# Checks if the down button is pressed, then waits for it to be released
		elif lcd.is_pressed(LCD.DOWN): 	
			while lcd.is_pressed(LCD.DOWN):
				pass

			# Decreases value at cursor position if possible
			if valStr[valIndex] > '0':
				valStr[valIndex] = str(int(valStr[valIndex]) - 1)
			elif valStr[valIndex] == '0' and cursorPos != msgLength:
				valStr[valIndex] = ' '

			# Displays new message to user
			lcd.set_cursor(msgLength, 0)
			lcd.message("".join(valStr)) 		
			time.sleep(0.1)			
	
	# Wait for select to be released
	while lcd.is_pressed(LCD.SELECT) == True:
		pass

	# formVal = x
# 	print(message + ' is: ' + str(formVal))		# Prints feedback message to terminal   

	return valStr 
