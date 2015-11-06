# coding: utf-8
#!/usr/bin/python

# Max Basescu
# mbasesc1@jhu.edu
# 
# This script takes user specified details containing:
# Laps - the number of laps to run the program for
# Rat number - the current rat's identification number
# Training day - the current day of training
# dTheta0 - the initial angle interval between feedings
# dTheta1 - the final angle interval between feedings
#
# Across the trial, the angle interval between feedings is
# transitioned linearly from dTheta0 to dTheta1 with 
# +- 20deg randomness

import math
import csv
import time
import random
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import UserInput as UINPUT

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()
lcd.show_cursor(True)

# Setup GPIO pins for motor pulsing and encoder reading
motorPin = 17
ledPin = 18
buttonPin = 25 
encoderPinA = 22
encoderPinB = 23
GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(encoderPinA, GPIO.IN)
GPIO.setup(encoderPinB, GPIO.IN)

# Set backlight color to blue
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

# Initialization of current angle, count
count = 0

# Number of encoder readings per revolution
countsPerLap = 4096

# Duration of motor per feeding
pulseDur = 1500 # ms

# Triggered by an interrupt from the button, this function
# starts the motor and logs the event
def buttonPress(ch):
	try:
		global f, buttonFeedStart, buttonIsFeeding
		
		# Only do stuff if we're not already pulsing
		if tCurr - buttonFeedStart > pulseDur:
			f.write('event | time={},manFeed=1\n'.format(tCurr))
			GPIO.output(motorPin, True)
			GPIO.output(ledPin, True)
			buttonFeedStart = tCurr
			buttonIsFeeding = True

	except:
		pass

# Triggered by an edge on pin A, this function modifies
# the value of count according to the encoder state
def readEncoderA(ch):
	global count
	
	# Grab readings from the pins
	aState = GPIO.input(encoderPinA)
	bState = GPIO.input(encoderPinB)

	# Look for rising edge on A
	if aState == True:
		# Check direction of encoder turning
		if bState == False:
			count -= 1 # CW
		else:
			count += 1 # CCW

	# There's a falling edge on A
	else:
		# Check direction of encoder turning
		if bState == True:
			count -= 1 # CW
		else:
			count += 1 # CCW

# Triggered by an edge on pin B, this function modifies
# the value of count according to the encoder state
def readEncoderB(ch):
	global count
	
	# Grab readings from the pins
	aState = GPIO.input(encoderPinA)
	bState = GPIO.input(encoderPinB)

	# Look for rising edge on B
	if bState == True:
		# Check direction of encoder turning
		if aState == True:
			count -= 1 # CW
		else:
			count += 1 # CCW

	# There's a falling edge on B
	else:
		# Check direction of encoder turning
		if aState == False:
			count -= 1 # CW
		else:
			count += 1 # CCW


# Attach interrupts
GPIO.add_event_detect(encoderPinA, GPIO.BOTH, callback = readEncoderA)
GPIO.add_event_detect(encoderPinB, GPIO.BOTH, callback = readEncoderB)
GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = buttonPress, bouncetime = pulseDur)

# Converts encoder counts to degrees
def toDeg(cnt):
	return float(cnt) / countsPerLap * 360

# Converts degrees to encoder counts
def toCnt(deg):
	return int(float(deg) / 360 * countsPerLap)

print("Press Ctrl-C to quit.")

# Default string values
lapsStr = "0    "
ratStr = "0    "
dayStr = "0    "
dTheta0Str = "0    "
dTheta1Str = "0    "

# Loading previous entries from params file
paramsFile = 'params.csv'
try:
	pFile = open(paramsFile, 'r+')
	params = next(csv.reader(pFile, delimiter=','))
	lapsStr = params[0]
	ratStr = params[1]
	dayStr = params[2]
	dTheta0Str = params[3]
	dTheta1Str = params[4]
except:
	pFile = open(paramsFile, 'w') # Create the file

# Gets various fields from user (third argument specifies minimum input accepted)
laps = UINPUT.genForm(lcd, 'Laps', lapsStr, 1)
print('# of Laps: ' + str(laps))
goal = laps * 360 # Converting laps into goal degrees
ratNum = UINPUT.genForm(lcd, 'Rat Num', ratStr, 0)
print('Rat Num: ' + str(ratNum))
day = UINPUT.genForm(lcd, 'Day', dayStr, 0)
print('Day: ' + str(day))
dTheta0 = UINPUT.genForm(lcd, 'dTheta0', dTheta0Str, 0)
print('dTheta0: ' + str(dTheta0))
dTheta1 = UINPUT.genForm(lcd, 'dTheta1', dTheta1Str, 0)
print('dTheta1: ' + str(dTheta1))

# Write new parameters to file
pFile.seek(0)
pFile.write('{:<5},{:<5},{:<5},{:<5},{:<5}'.format(str(laps), str(ratNum), str(day), str(dTheta0), str(dTheta1)))
pFile.close()

# Clear display and set color to red for trial
lcd.clear()
lcd.set_color(1.0, 0.0, 0.0)
lcd.message('Press select\nto cancel')

# Stop showing cursor on screen
lcd.show_cursor(False)

# Local base path to log folder
logBase = 'logs/'

# Opens log file
fName = logBase + time.strftime("%y%m%d") + "_rat" + str(ratNum) + "_day" + str(day) + "_training.dat"
f = open(fName, "a")

# Prints info, then converts values in degrees into values compatible with encoder readings
f.write('\nglobal | dTheta0={},dTheta1={},pulseDur={},goal={}\n'.format(dTheta0, dTheta1, pulseDur, goal))
dTheta0 = toCnt(dTheta0)
dTheta1 = toCnt(dTheta1)
goal = toCnt(goal)

# Writes general trial info including timestamp
f.write('global | rat={},day={}\n'.format(ratNum,day))
f.write('global | year={},month={},date={},hour={},min={},sec={}\n\n'.format(time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))

# Begin running actual training program:

# Variable initialization
count = 0 # Zero out count
isFeeding = False # Whether or not the motor is currently pulsing
feedStart = 0 # Contains the time at which the motor was started
buttonFeedStart = 0 # Contains the time at which the button was pressed
buttonIsFeeding = False # Whether or not there is a button pulse going
nextFeedAng = 0 # Stores next angle at which to begin feeding
tInit = time.time() # Establish offset time

# Until the rat has run the specified number of laps
tDispNext = 0
tDispIncr = 1000
while count < goal:
	tCurr = int(math.floor((time.time() - tInit) * 1000)) # Grabs current time in milliseconds
	f.write('data | time={},theta={}\n'.format(tCurr, toDeg(count)))
	
	if tCurr>tDispNext:
		lcd.clear()
		statusMsg = 'Laps: {:.2}/{:d}\nSEL to cancel'.format(float(toDeg(count))/360,laps);
		lcd.message(statusMsg)
		tDispNext += tDispIncr
	

	# If the user decides to end the trial early
	if lcd.is_pressed(LCD.SELECT):
		while lcd.is_pressed(LCD.SELECT):
			time.sleep(0.1)

		f.write('event | time={},end=manual\n'.format(tCurr))
		break

	# If we're at the end of a button pulse
	if tCurr - buttonFeedStart >= pulseDur and buttonIsFeeding == True:
		buttonIsFeeding = False

		# Stop pulsing motor
		GPIO.output(motorPin, False)
		GPIO.output(ledPin, False)

		# Write disable to log
		f.write('event | time={},manFeed=0\n'.format(tCurr))	
	
	# Arrived at feeding location
	if not isFeeding and count >= nextFeedAng:
		feedStart = tCurr
		isFeeding = True
		
		# Begin pulsing motor
		GPIO.output(ledPin, True)
		GPIO.output(motorPin, True)

		# Write enable to log
		f.write('event | time={},feed=1\n'.format(tCurr))

	# End of feeding period
	elif isFeeding and tCurr - feedStart >= pulseDur:
		isFeeding = False

		# Stop pulsing motor
		GPIO.output(ledPin, False)
		GPIO.output(motorPin, False)

		# Calculate current interval between feedings and next feed angle
		dTheta = dTheta0 + (dTheta1 - dTheta0) * count / goal
		nextFeedAng = count + dTheta + random.randint(-math.floor(dTheta/2),math.floor(dTheta/2))
	
		# Write disable to log
		f.write('event | time={},feed=0\n'.format(tCurr))	

	time.sleep(0.01) # Wait 10 ms

# Update time and write end of session to file
tCurr = int(math.floor((time.time() - tInit) * 1000))
f.write('event | time={},goal=1\n#\n'.format(tCurr))

# Turn motor off if it's on
GPIO.output(motorPin, False)
GPIO.output(ledPin, False)
GPIO.cleanup()
f.close()
exit(0)
