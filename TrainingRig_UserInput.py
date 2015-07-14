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

# Gets laps from the user with a minimum of 1 lap
laps = UINPUT.genForm(lcd, 'Laps', 1)
goal = laps * 360

# Gets rat number from the user with a minimum number of 0
ratNum = UINPUT.genForm(lcd, 'Rat Num', 0)

# Gets training day from the user with a minimum value of 0
day = UINPUT.genForm(lcd, 'Day', 0)

# Gets dTheta0 from the user with a minimum value of 0
dTheta0 = UINPUT.genForm(lcd, 'dTheta0', 0)

# Gets dTheta1 from the user with a minimum value of 0
dTheta1 = UINPUT.genForm(lcd, 'dTheta1', 0)

# Number of encoder readings per revolution
thetaLap = 8192

# Duration of motor per feeding
pulseDur = 2

# Local base path to log folder
logBase = 'logs/'

# Opens log file
fName = logBase + time.strftime("%y%m%d") + "_rat" + str(ratNum) + "_day" + str(day) + "_training.dat"
f = open(fName, "a")

# Prints info, then converts values in degrees into values compatible with encoder readings
f.write('\nglobal | dTheta0={},dTheta1={},pulseDur={},goal={}'.format(dTheta0, dTheta1, pulseDur, goal))
dTheta0 *= thetaLap / 360
dTheta1 *= thetaLap / 360
goal *= thetaLap

# Writes general trial info including timestamp
f.write('\nglobal | rat={},day={}\n'.format(ratNum,day))
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

