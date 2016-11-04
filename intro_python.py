#raspberry pi python:

#~~~~~~~~~~~~~~~
#input - output:
#~~~~~~~~~~~~~~~


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

#1 means output is on
GPIO.output(23, 1)

for i in range(100):
    GPIO.output(23, i%2 == 0)
    GPIO.output(18, i%3 == 0)
    time.sleep(1)


#using button:
GPIO.setup(18, GPIO.IN)

#controlling input:
GPIO.input(18) #this is zero if

while True:
    if GPIO.input(18) == False:
        print("Button Pressed")
        time.sleep(3)
    else:
        print("Push me!")

#using light sensor:

GPIO.setup(16, GPIO.IN)

GPIO.inout(16)

#~~~~~~~~~~~~~
#camera stuff:
#~~~~~~~~~~~~~

from picamera import PiCamera
from time import sleep

camera = PiCamera()

#take a pics 5 secs after starting preview:
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
