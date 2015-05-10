import sys
import time
import RPi.GPIO as GPIO

#Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#Define GPIO signals to use physical pins 11,15,16,18
#GPIO 17, GPIO 22, GPIO 23, GPIO 24
StepPins = [17, 22, 23, 24]

#Set all pins as output
for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

#Define advanced sequence as shown in manufacturers datasheet
Seq = [[1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]]

StepCount = len(Seq)-1
#Set to 1 or 2 for clockwise
#Set to -1 or -2 for counter-clockwise
StepDir = 2

#Read wait time from command line
if len(sys.argv)>1:
    WaitTime=int(sys.argv[1])/float(1000)
else:
    WaitTime=10/float(1000)

#Initialise variables
StepCounter = 0

print "Press and enter 0 to spin the motor clockwise"
print "Press and enter 1 to spin the motor counter-clockwise"
user_input = input("Please enter something here: ")
#Still need to make a fix for when a user enters
#anything with a non-numeric char
while user_input != 1 and user_input != 0:
    user_input = input("Please enter a value of either 0 or 1: ")

#Start main loop
if user_input == 0:
    while True:
        for pin in range(0,4):
            xpin = StepPins[pin]
            print StepCounter
            print pin
            if Seq[StepCounter][pin] != 0:
                #print " Step %i Enable %i" %(StepCounter,xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += StepDir

        #If we reach the end of the sequence start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter=StepCount

        #Wait before moving on
        time.sleep(WaitTime)
elif user_input == 1:
     while True:
        for pin in range(0,4):
            xpin = StepPins[pin]
            print StepCounter
            print pin
            if Seq[StepCounter][pin] != 0:
                #print " Step %i Enable %i" %(StepCounter,xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter -= StepDir

        #If we reach the end of the sequence start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter=StepCount

        #Wait before moving on
        time.sleep(WaitTime)