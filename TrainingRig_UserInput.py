# coding: utf-8
# Takes the input of:
# Rat Number
# Training Day

# Pressing the up button increases the number 0-9
# Pressing select moves the number to the next digit place.  

#!/usr/bin/python
# Example using a character LCD plate.
import math
import time
import serial # new
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Set backlight color to Blue
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

print("Press Ctrl-C to quit.")

# Testing code
while False:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(button[0]):
			# Button is pressed, change the message and backlight.
			lcd.clear()
			lcd.message(button[1])
			lcd.set_color(button[2][0], button[2][1], button[2][2])

# Start Laps Input.

# Set Variables
x = 0 						# Counter internal loop variable
laps_str = ('Enter Laps:')
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
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(laps_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 1) else 1	# Decreases internal variable
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(laps_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == TRUE:
	pass

laps = x if (x > 0) else 1
print("Entered Number of Laps is:")		# Prints String to Terminal
print(laps)        				# Prints the number of laps to the Terminal

# End of Laps Input

##################################################
# Start Rat Number Input			# RAT NUMBER INPUT
x = 0						# Define internal variable
rat_num_str = ("Rat Number:")			# Define string to request user input 
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
		lcd.message('   ')		# Clear variable before printing new one
		lcd.set_cursor(rat_num_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('   ')		# Clear variable before printing new one
		lcd.set_cursor(rat_num_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == TRUE:
	pass

rat_num = x
print("Rat Number is:")				# Prints String to Terminal
print(rat_num)        				# Prints internal variable to the Terminal

# End of Rat Number Input

##################################################

# Start Training Day Input			# TRAINING DAY INPUT
x = 0						# Define internal variable
date_str = ("Training Day:")			# Define string to request user input 
date = 0					# Define array to store rat number

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(date_str)				# Request User Input
date_str_length = len(date_str) 		# Find Length of user input request string
lcd.set_cursor(date_str_length,0) 			# Set Cursor to be after string - awaiting input

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(date_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(date_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(date_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == TRUE:
	pass

date = x
print("Training Date is:")			# Prints String to Terminal
print(date)       				# Prints internal variable to the Terminal

# End of Training Date Input

##################################################

x = 0
degrees_str = ("Enter Degrees:")
degrees = 0;

# Display Input on LCD Screen			
lcd.clear()					# Clear LCD Screen
lcd.message(degrees_str)			# Request User Input
degrees_str_length = len(degrees_str) 		# Find Length of user input request string
lcd.set_cursor(degrees_str_length,0) 			# Set Cursor to be after string - awaiting input

# Repeat process until select is pressed
while lcd.is_pressed(LCD.SELECT) == False:  	# Waits for User to Press Select
	lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string - awaiting input

	if lcd.is_pressed(LCD.UP): 		# While up button is pressed but not released
		while lcd.is_pressed(LCD.UP):
			pass
        	x = x + 1			# Increases internal Variable	
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing
        
	elif lcd.is_pressed(LCD.DOWN): 		# While down button is pressed but not released
		while lcd.is_pressed(LCD.DOWN):
			pass
        	x = (x-1) if (x > 0) else 0	# Decreases internal variable
		lcd.message('   ');		# Clear variable before printing new one
		lcd.set_cursor(degrees_str_length+1,0)	# Set Cursor to be after string
		lcd.message(str(x)) 		# Prints internal variable on LCD Screen
		time.sleep(0.1)			# Crappy debouncing

# Wait for select to be released
while lcd.is_pressed(LCD.SELECT) == TRUE:
	pass

degrees = x
print("Degree interval is:")			# Prints String to Terminal
print(degrees)       				# Prints internal variable to the Terminal

# Below here is all from Dr. Madhav's code
			
last_received = ''
buffer = ''

if __name__ ==  '__main__':
    rat = input("Enter rat number: ")
    day = input("Enter training day: ")

    fileName = time.strftime("%y%m%d")
    f = open(fileName + "_rat"+str(rat) + "_day"+ str(day) + "_training.dat",'w')

    f.write('\nglobal | rat=%d,day=%d\n' % (rat,day))
    f.write('\nglobal | year=%s,month=%s,date=%s,hour=%s,min=%s,sec=%s\n' % (time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))

    lap = 0; 
    ser = serial.Serial('/dev/tty.usbserial-A600aeCg',9600)
    print("Starting run...\n")

    run = 1;
    while run:
        # last_received = ser.readline()
        buffer += ser.read(ser.inWaiting()).decode('ascii','ignore') 

        if '\n' in buffer:
            last_received, buffer = buffer.split('\n')[-2:]
            f.write(last_received+"\n")

        if 'global' in last_received:
            print(last_received+"\n")
            
        if 'theta=' in last_received:
            theta = int(last_received.split('theta=')[1])
            nlap = math.floor(theta/8192);
            if nlap>lap:
                lap = nlap;
                print("Lap %d\n" % lap)

        if last_received=='#':
            f.close();
            run = 0;
# End Dr. Madhav Code


