import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

pin_numbers = [25, 24, 23, 18, 12, 16, 20, 13, 19, 26, 17, 27, 22]
GPIO.setup(pin_numbers, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(25, 1)

GPIO.input(25)

#checking all the inputs:
[GPIO.input(pin) for pin in pin_numbers]

#changing the inputs multiple pins at a time:
GPIO.output(pin_numbers[1:],[0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])

#generate random 0-1's for input to pins except pin 25:
while True:
    time.sleep(0.2)
    random_input = np.random.randint(0, 2, len(pin_numbers) - 1)
    GPIO.output(pin_numbers[1:], random_input.tolist())


inputs = np.ones(13, dtype = "int").tolist()
i = 1

#flick it:
while True:

    inputs[i:i+3] = [0, 1, 1]
    GPIO.output(pin_numbers, inputs)
    time.sleep(0.1)
    inputs[i:i+3] = [1, 0, 0]
    GPIO.output(pin_numbers, inputs)

    i = i + 3
    i = i%12
