# coding: utf-8
#!/usr/bin/python

# Takes user inputted details 
import math
import time
import random
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import UserInput as UINPUT

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()
lcd.show_cursor(True)

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

# Initialization of current angle, theta
theta = 0

# Number of encoder readings per revolution
thetaLap = 8192

# Triggered by an interrupt from pin A, this function modifies
# the value of theta according to the encoder state
def readEncoderA(ch):
	global theta
	
	# Check direction of encoder turning
	if GPIO.input(encoderPinB) == False:
		theta += 1 #CW

# Triggered by an interrupt from pin B, this function modifies
# the value of theta according to the encoder state
def readEncoderB(ch):
	global theta

	# Check direction of encoder turning 
	if GPIO.input(encoderPinA) == False:
		theta -= 1 # CCW

# Converts encoder angle to degrees
def toDeg(ang):
	return ang / thetaLap * 360

# Converts degrees to encoder angle
def toEnc(ang):
	return ang / 360 * thetaLap

# Attach rising edge interrupts to pins A and B
GPIO.add_event_detect(encoderPinA, GPIO.RISING, callback=readEncoderA)
GPIO.add_event_detect(encoderPinB, GPIO.RISING, callback=readEncoderB)

print("Press Ctrl-C to quit.")

# Gets various fields from user (third argument specifies minimum input accepted)
laps = UINPUT.genForm(lcd, 'Laps', 1)
print('# of Laps: ' + str(laps))
goal = laps * 360 # Converting laps into goal degrees
ratNum = UINPUT.genForm(lcd, 'Rat Num', 0)
print('Rat Num: ' + str(ratNum))
day = UINPUT.genForm(lcd, 'Day', 0)
print('Day: ' + str(day))
dTheta0 = UINPUT.genForm(lcd, 'dTheta0', 0)
print('dTheta0: ' + str(dTheta0))
dTheta1 = UINPUT.genForm(lcd, 'dTheta1', 0)
print('dTheta1: ' + str(dTheta1))

lcd.clear()

# Stop showing cursor on screen
lcd.show_cursor(False)

# Duration of motor per feeding
pulseDur = 2000 # ms

# Local base path to log folder
logBase = 'logs/'

# Opens log file
fName = logBase + time.strftime("%y%m%d") + "_rat" + str(ratNum) + "_day" + str(day) + "_training.dat"
f = open(fName, "a")

# Prints info, then converts values in degrees into values compatible with encoder readings
f.write('\nglobal | dTheta0={},dTheta1={},pulseDur={},goal={}'.format(dTheta0, dTheta1, pulseDur, goal))
dTheta0 = toEnc(dTheta0)
dTheta1 = toEnc(dTheta1)
goal *= thetaLap

# Writes general trial info including timestamp
f.write('\nglobal | rat={},day={}\n'.format(ratNum,day))
f.write('\nglobal | year={},month={},date={},hour={},min={},sec={}\n'.format(time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))

# Begin running actual training program:
isFeeding = False # Whether or not the motor is currently pulsing
feedStart = 0 # Contains the time at which the motor was started
nextFeedAng = 0 # Stores next angle at which to begin feeding
tInit = time.time() # Establish offset time

# Until the rat has run the specified number of laps
while theta < goal:
	tCurr = int(math.floor((time.time() - tInit) * 1000)) # Grabs current time in milliseconds
	print('data | time={},theta={}\n'.format(tCurr, theta))
	
	# Arrived at feeding location
	if not isFeeding and theta >= nextFeedAng:
		feedStart = tCurr
		isFeeding = True
		
		# Begin pulsing motor
		GPIO.output(ledPin, True)
		GPIO.output(motorPin, True)

		# Write enable to log
		f.write('event | time={},feed=1\n'.format(tCurr))

	# End of feeding period
	elif isFeeding and tCurr - feedStart >= pulseDur:
		# Stop pulsing motor
		GPIO.output(ledPin, False)
		GPIO.output(motorPin, False)

		# Calculate current interval between feedings and next feed angle
		dTheta = dTheta0 + (dTheta1 - dTheta0) * theta / goal
		nextFeedAng = theta + dTheta + random.randint(-455, 455)
	
		# Write disable to log
		f.write('event | time={},feed=0\n'.format(tCurr))	

	time.sleep(0.01) # Wait 10 ms

# Update time and write end of session to file
tCurr = int(math.floor((time.time() - tInit) * 1000))
f.write('event | time={},goal=1\n#\n', tCurr)

f.close()

