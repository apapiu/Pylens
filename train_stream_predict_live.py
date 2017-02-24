import numpy as np
import time

from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

from keras.models import Sequential, Model
from keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input
from keras.preprocessing.image import ImageDataGenerator

#be in '/home/pi/Documents'


model = Sequential()
model.add(MaxPooling2D((4,4), input_shape = (3, 150, 200)))
model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dense(1, activation = "sigmoid"))

model.compile(loss = "binary_crossentropy",
              optimizer = "adam",
              metrics = ["accuracy"])

model.summary()


#getting data from directory:
datagen = ImageDataGenerator(rescale=1./255)
train_generator = datagen.flow_from_directory(
        'Images',  # this is the target directory
        target_size=(150, 200),
        batch_size=12,
        class_mode='binary')

model.fit_generator(
        train_generator,
        samples_per_epoch=100,
        nb_epoch=3)



#predicting live:


from picamera import PiCamera
from time import sleep
from gpiozero import Button
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

camera = PiCamera()
camera.start_preview()

camera.vflip = True


#button:
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

    #answer = "fingers" if pred > 0.35 else "no fingers"

    camera.annotate_text=answer


    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    draw.text((10, 10), answer , 'white', font)
    img.save('/home/pi/Desktop/image3.jpg')
    button.close()




#STREAM:

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream

stream = BytesIO()
camera = PiCamera()
camera.start_preview()

while True:
    stream = BytesIO()
    camera.capture(stream, format='jpeg', resize=(200, 150))

    print("pic taken")

    stream.seek(0)

    image = Image.open(stream)
    #a weird bug I have to do this twice
    sm_img = np.array(image)
    sm_img = np.array(image)
    sm_img = sm_img/255.0
    draw = ImageDraw.Draw(image)


    sm_img = sm_img.transpose(2,0,1)

    print(sm_img.mean())
    sm_img = np.expand_dims(sm_img,0)



    pred = model.predict(sm_img)
    pred = pred[0][0]

    #answer = 'probability is ' + str(pred)
    answer = "fingers" if pred > 0.35 else "no fingers"

    if answer == "fingers":
        new_input(np.random.randint(2, size = 12).tolist())


    camera.annotate_text=answer

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    draw.text((10, 10), answer , 'white', font)


    time.sleep(0.33)
