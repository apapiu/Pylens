# ssh pi@172.27.29.162
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPinHI = 25 # Broadcom pin 23 (P1 pin 16)
ledPinR1 = 24 # Broadcom pin 23 (P1 pin 16)
ledPinG1 = 23 # Broadcom pin 23 (P1 pin 16)
ledPinB1 = 18 # Broadcom pin 23 (P1 pin 16)

ledPinR2 = 12 # Broadcom pin 23 (P1 pin 16)
ledPinG2 = 16 # Broadcom pin 23 (P1 pin 16)
ledPinB2 = 20 # Broadcom pin 23 (P1 pin 16)

ledPinR3 = 13 # Broadcom pin 23 (P1 pin 16)
ledPinG3 = 19 # Broadcom pin 23 (P1 pin 16)
ledPinB3 = 26 # Broadcom pin 23 (P1 pin 16)

ledPinR4 = 17 # Broadcom pin 23 (P1 pin 16)
ledPinG4 = 27 # Broadcom pin 23 (P1 pin 16)
ledPinB4 = 22 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPinR1, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinG1, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinB1, GPIO.OUT) # LED pin set as output

GPIO.setup(ledPinR2, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinG2, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinB2, GPIO.OUT) # LED pin set as output

GPIO.setup(ledPinR3, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinG3, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinB3, GPIO.OUT) # LED pin set as output

GPIO.setup(ledPinR4, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinG4, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPinB4, GPIO.OUT) # LED pin set as output

GPIO.setup(ledPinHI, GPIO.OUT) # LED pin set as output

GPIO.output(ledPinHI, GPIO.HIGH);


numTrials = 10;

for x in range(0, numTrials):
    GPIO.output(ledPinR1, GPIO.LOW);
    GPIO.output(ledPinG1, GPIO.LOW);
    GPIO.output(ledPinB1, GPIO.LOW);
    time.sleep(0.1)  # Delay for 1 second
    camera.capture('/home/pi/Desktop/image1.jpg');
    GPIO.output(ledPinR1, GPIO.HIGH);
    GPIO.output(ledPinG1, GPIO.HIGH);
    GPIO.output(ledPinB1, GPIO.HIGH);
    
    GPIO.output(ledPinR2, GPIO.LOW);
    GPIO.output(ledPinG2, GPIO.LOW);
    GPIO.output(ledPinB2, GPIO.LOW);
    time.sleep(0.1)  # Delay for 1 second
    camera.capture('/home/pi/Desktop/image2.jpg');
    GPIO.output(ledPinR2, GPIO.HIGH);
    GPIO.output(ledPinG2, GPIO.HIGH);
    GPIO.output(ledPinB2, GPIO.HIGH);
    
    GPIO.output(ledPinR3, GPIO.LOW);
    GPIO.output(ledPinG3, GPIO.LOW);
    GPIO.output(ledPinB3, GPIO.LOW);
    time.sleep(0.1)  # Delay for 1 second
    camera.capture('/home/pi/Desktop/image3.jpg');
    GPIO.output(ledPinR3, GPIO.HIGH);
    GPIO.output(ledPinG3, GPIO.HIGH);
    GPIO.output(ledPinB3, GPIO.HIGH);
    
    GPIO.output(ledPinR4, GPIO.LOW);
    GPIO.output(ledPinG4, GPIO.LOW);
    GPIO.output(ledPinB4, GPIO.LOW);
    time.sleep(0.1)  # Delay for 1 second
    camera.capture('/home/pi/Desktop/image4.jpg');
    GPIO.output(ledPinR4, GPIO.HIGH);
    GPIO.output(ledPinG4, GPIO.HIGH);
    GPIO.output(ledPinB4, GPIO.HIGH);
    

