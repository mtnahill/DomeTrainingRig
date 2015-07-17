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
# <message>, to prompt the user (note that this should be the bare name 
# of the field being requested, e.g. 'Day'), <valStr>, a string containing the previous
# value entered for the field and <minVal>, the minimum value
# returned by the function, even if the user's input is lower
def genForm(lcd, message, valStr, minVal):

	# Initial variable states
	valIndex = 0
	valStr = list(valStr)				# Get a list from the stored string

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

	# Try to convert input into integer
	try:
		formVal = int("".join(valStr)) 
		formVal = formVal if formVal >= minVal else minVal
	except ValueError:
		# Recurse if there was an invalid entry
		print('Invalid entry for ' + message + ': ' + "".join(valStr))
		formVal = genForm(lcd, message, minVal)

	return formVal
