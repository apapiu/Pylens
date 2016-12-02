import matplotlib.pyplot as plt

%matplotlib inline

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from keras.preprocessing.image import load_img



img = plt.imread("/Users/alexpapiu/Downloads/images/923.jpg")

img = load_img("/Users/alexpapiu/Downloads/images/923.jpg")

draw = ImageDraw.Draw(img)

draw.font

plt.imshow(img)



myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)

draw.text((10, 10),"Sample Text",(255,255,255), font = myfont)

draw.text((50, 50),"Sample Text","white")

myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)

plt.imshow(img)



font = ImageFont.truetype("arial.ttf", 10)



#add a plot to image:
import matplotlib.pyplot as plt
im = plt.imread("/Users/alexpapiu/Downloads/images/923.jpg")
implot = plt.imshow(im)
plt.scatter([10], [20])
plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)
plt.


import numpy as np

im = plt.imread("/Users/alexpapiu/Downloads/images/923.jpg")
implot = plt.imshow(im)
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, x=[30, 40], y=[50, 60], align='center', alpha=0.5)
