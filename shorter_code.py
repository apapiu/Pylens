import RPi.GPIO as GPIO
import time
import numpy as np
import picamera
from gpiozero import Button


GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# the 12 led pins
pin_numbers = [25, 24, 23, 18, 12, 16, 20, 13, 19, 26, 17, 27, 22]
n = (len(pin_numbers) - 1)

GPIO.setup(pin_numbers, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(25, 1)

camera = picamera.PiCamera()
camera.start_preview()

#checking all the inputs:
def check_inputs():
    return [GPIO.input(pin) for pin in pin_numbers]

#changing the inputs:
def new_input(inputs):
    GPIO.output(pin_numbers[1:],inputs)

#do it by ordering:
def new_input_order(*args):
    inputs = n*[1]
    for i in args:
        inputs[i] = 0
    new_input(inputs)

def reset_lights():
    new_input(n*[1]) #* is shortcut for repeat [1] n times here

#flick it:
def one_flick(save_image = False, sleep_time = 0.3, name = None):
    i = 0
    inputs = n*[1]
    while i < 12:
        inputs[i:i+3] = [0, 0, 0]
        new_input(inputs)

        if save_image:
            path = '/home/pi/Pictures/3Dbaby/{0}{1}.jpg'.format(name, i/3)
            camera.capture(path)

        time.sleep(sleep_time)
        inputs[i:i+3] = [1, 1, 1]
        new_input(inputs)
        i = i + 3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#random:
while True:
    new_input(np.random.randint(2, size = 12).tolist())
    time.sleep(0.5)



while True:
    one_flick()


#save images with different names:

while True:


    try:
        camera = picamera.PiCamera()
        camera.start_preview()
    except:
        pass
    name = input("what name should i give it?")
    button = Button(4)
    button.wait_for_press()
    one_flick(name = name, save_image = True)
    button.close()
    camera.close()
