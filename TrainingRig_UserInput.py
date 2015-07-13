# coding: utf-8
# Takes the input of:
# Rat Number
# Training Day
# Degree interval

#!/usr/bin/python
import math
import time
import RPi.GPIO as GPIO
import serial
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Declare pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Setup GPIO pin for pulsing the motor
motorPin = 11
GPIO.setup(motorPin, GPIO.OUT)

# Set backlight color to Blue
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

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

x = 0
degrees_str = ("Degrees:")
degrees = 0;

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

degrees = x
print("Degree interval is:")			# Prints String to Terminal
print(degrees)       				# Prints internal variable to the Terminal

# Logging setup
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

# Until the rat has run the specified number of laps
while currLap < laps:

	angle = 0 # TEMP, replace with real input 
	
	# If the current angle is within three degrees of the target angle
	if math.fmod(angle, degrees) <= 3 && abs(angPrev - angle) > degrees/2
		# Store the previous angle
		angPrev = angle

		# Send a 2 second pulse to the motor
		pulseMotor(pulseDur)
		
	currLap = math.floor(angle / 8192)
	

	

f.close()


## Below here is all from Dr. Madhav's code
#			
#last_received = ''
#buffer = ''
#
#if __name__ ==  '__main__':
#    rat = input("Enter rat number: ")
#    day = input("Enter training day: ")
#
#    fileName = time.strftime("%y%m%d")
#    f = open(fileName + "_rat"+str(rat) + "_day"+ str(day) + "_training.dat",'w')
#
#    f.write('\nglobal | rat=%d,day=%d\n' % (rat,day))
#    f.write('\nglobal | year=%s,month=%s,date=%s,hour=%s,min=%s,sec=%s\n' % (time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))
#
#    lap = 0; 
#    ser = serial.Serial('/dev/tty.usbserial-A600aeCg',9600)
#    print("Starting run...\n")
#
#    run = 1;
#    while run:
#        # last_received = ser.readline()
#        buffer += ser.read(ser.inWaiting()).decode('ascii','ignore') 
#
#        if '\n' in buffer:
#            last_received, buffer = buffer.split('\n')[-2:]
#            f.write(last_received+"\n")
#
#        if 'global' in last_received:
#            print(last_received+"\n")
#            
#        if 'theta=' in last_received:
#            theta = int(last_received.split('theta=')[1])
#            nlap = math.floor(theta/8192);
#            if nlap>lap:
#                lap = nlap;
#                print("Lap %d\n" % lap)
#
#        if last_received=='#':
#            f.close();
#            run = 0;
#
## End Dr. Madhav Code
#
#
