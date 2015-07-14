# coding: utf-8
#!/usr/bin/python

# Takes user inputted details 
import math
import time
import RPi.GPIO as GPIO
import serial
import Adafruit_CharLCD as LCD
import UserInput as UINPUT

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Setup GPIO pins for motor pulsing and encoder reading
motorPin = 11
encoderPinA = 13
encoderPinB = 15
buttonPin = 16
GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(encoderPinA, GPIO.IN)
GPIO.setup(encoderPinB, GPIO.IN)
GPIO.setup(buttonPin, GPIO.IN)

# Set backlight color to Blue
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

# Sends a pulse to the motor for duration 'dur'
def pulseMotor(dur):
	GPIO.output(motorPin, True)
	time.sleep(dur)
	GPIO.output(motorPin, False)
	return

print("Press Ctrl-C to quit.")

# Start Laps Input.

# Set Variables
x = 0 						# Counter internal loop variable
laps_str = ('Laps:')
laps = 1

# Display Input on LCD Screen			# LAPS INPUT
lcd.clear()					# Clear LCD Screen
lcd.message(laps_str)				# Request User Input
laps_str_length = len(laps_str) 		# Find Length of user input request string

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(laps_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(laps_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 1) else 1	# Decreases internal variable
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(laps_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == True:
	pass

laps = x if (x > 0) else 1
print("Entered Number of Laps is:")		# Prints String to Terminal
print(laps)        				# Prints the number of laps to the Terminal

# End of Laps Input

##################################################

# Start Rat Number Input			# RAT NUMBER INPUT
x = 0						# Define internal variable
rat_num_str = ("Rat Num:")			# Define string to request user input 
rat_num = 0		

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(rat_num_str)			# Request User Input
rat_num_str_length = len(rat_num_str) 		# Find Length of user input request string
lcd.set_cursor(rat_num_str_length,0) 		# Set Cursor to be after string - awaiting input

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(rat_num_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('    ')		# Clear variable before printing new one
		lcd.set_cursor(rat_num_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('    ')		# Clear variable before printing new one
		lcd.set_cursor(rat_num_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == True:
	pass

rat_num = x
print("Rat Number is:")				# Prints String to Terminal
print(rat_num)        				# Prints internal variable to the Terminal

# End of Rat Number Input

##################################################

# Start Training Day Input			# TRAINING DAY INPUT
x = 0						# Define internal variable
day_str = ("Day:")				# Define string to request user input 
day = 0					

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(day_str)				# Request User Input
day_str_length = len(day_str) 			# Find Length of user input request string
lcd.set_cursor(day_str_length,0) 		# Set Cursor to be after string - awaiting input

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(day_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(day_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(day_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == True:
	pass

day = x
print("Training Date is:")			# Prints String to Terminal
print(day)       				# Prints internal variable to the Terminal

# End of Training Day Input

##################################################

# Get dTheta0

# Set variables
x = 0
degrees_str = ("dTheta0:")
dTheta0 = 0;

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(degrees_str)			# Request User Input
degrees_str_length = len(degrees_str) 		# Find Length of user input request string
lcd.set_cursor(degrees_str_length,0) 		# Set Cursor to be after string - awaiting input

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == True:
	pass

dTheta0 = x
print("dTheta0 is:")				# Prints String to Terminal
print(dTheta0)       				# Prints internal variable to the Terminal

# Get dTheta1

# Set variables
x = 0
degrees_str = ("dTheta1:")
dTheta1 = 0;

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(degrees_str)			# Request User Input
degrees_str_length = len(degrees_str) 		# Find Length of user input request string
lcd.set_cursor(degrees_str_length,0) 		# Set Cursor to be after string - awaiting input


# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('    ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == True:
	pass

dTheta1 = x
print("dTheta1 is:")				# Prints String to Terminal
print(dTheta1)       				# Prints internal variable to the Terminal

# End user input

##################################################

# Number of encoder readings per revolution
thetaLap = 8192

# Duration of motor per feeding
pulseDur = 2

# Converts values in degrees into values compatible with encoder readings, and prints info
f.write('\nglobal | dTheta0={},dTheta1={},pulseDur={},goal={}'.format(dTheta0, dTheta1, pulseDur, goal))

dTheta0 *= thetaLap / 360
dTheta1 *= thetaLap / 360
goal *= thetaLap

# Local base path to log folder
logBase = 'logs/'

# Opening file
fName = logBase + time.strftime("%y%m%d") + "_rat" + str(rat_num) + "_day" + str(day) + "_training.dat"
f = open(fName, "a")

# Writes general trial info including timestamp
f.write('\nglobal | rat={},day={}\n'.format(rat_num,day))
f.write('\nglobal | year={},month={},date={},hour={},min={},sec={}\n'.format(time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))

# Sets initial current lap and angle of last drop
currLap = 0
angPrev = 0
pulseDur = 2 # Seconds


# Begin running actual training program:

# Until the rat has run the specified number of laps
#while absTheta < goal
#
#	angle = 0 # TEMP, replace with real input 
#	
#	# If the current angle is within three degrees of the target angle
#	if math.fmod(angle, dTheta0) <= 3 && abs(angPrev - angle) > dTheta0/2
#		# Store the previous angle
#		angPrev = angle
#
#		# Send a 2 second pulse to the motor
#		pulseMotor(pulseDur)
#		
#	 # currLap = math.floor(angle / thetaLap)
	

f.close()

