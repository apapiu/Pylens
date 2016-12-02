#getting images:

from time import sleep
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (150, 200)
camera.start_preview()

def get_and_save_images(classnum = 1):
    for i in range(50):
        sleep(0.5)
        name = str(classnum) + "img" + str(i) + ".jpg"
        camera.capture(name)
