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

for i in range(10):
    sleep(1)
    link = '/home/pi/Desktop/image' + str(i) + '.jpg'
    camera.capture(link)



camera.stop_preview()

#record video:
camera.start_preview()
#camera.framerate = 15

camera.start_recording('/home/pi/Desktop/video.h264')
sleep(60)
camera.stop_recording()
camera.stop_preview()



#you can set this stuff:
camera.shutter_speed
camera.iso = 100

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()



#using the button to take photo:

from picamera import PiCamera
from time import sleep
from gpiozero import Button


button = Button(4)
camera = PiCamera()


camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/Desktop/image3.jpg')
camera.stop_preview()

x = camera.capture()

from io import BytesIO


my_stream = BytesIO()
camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)


camera.capture(my_stream, 'jpeg')


img = load_img('/home/pi/Desktop/image3.jpg', target_size=(150, 200, 3))

preds = model.predict(image)

#write preds on the image:


#open image:
!xdg-open image3.jpg




#capture frame by pushing button:
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/Desktop/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break





import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.input(4)



while True:
    input_state = GPIO.input(4)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
