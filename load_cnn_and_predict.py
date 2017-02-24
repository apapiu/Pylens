


import numpy as np


from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

from keras.models import Sequential, Model
from keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input


model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', border_mode="same",input_shape = (3, 150, 200)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))


model.add(Convolution2D(32, 3, 3, activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))


model.add(Convolution2D(32, 3, 3, activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))


model.add(Convolution2D(32, 3, 3, activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))


model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(1, activation = "sigmoid"))



#get an image:

model.load_weights("/home/pi/ArchhacksImaging/basic_weights")



from picamera import PiCamera
from time import sleep
from gpiozero import Button
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

camera = PiCamera()
camera.start_preview()

camera.vflip = True



while True:

    button = Button(4)

    camera.start_preview()

    button.wait_for_press()
    camera.capture('/home/pi/Desktop/image3.jpg')
    camera.stop_preview()
    img = Image.open('/home/pi/Desktop/image3.jpg')
    draw = ImageDraw.Draw(img)


    sm_img = load_img('/home/pi/Desktop/image3.jpg', target_size = (150, 200, 3))
    sm_img = img_to_array(sm_img)/255.0
    sm_img = np.expand_dims(sm_img,0)
    pred = model.predict(sm_img)
    pred = pred[0][0]

    answer = 'probability is ' + str(pred)

    camera.annotate_text=answer


    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    draw.text((10, 10), answer , 'white', font)
    img.save('/home/pi/Desktop/image3.jpg')
    button.close()

    #sleep(2)




!xdg-open /home/pi/Desktop/image3.jpg
