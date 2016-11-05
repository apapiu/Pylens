
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline


from keras.preprocessing.image import load_img
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split


from keras.models import Sequential
from keras.layers import Dense, Dropout, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import adam
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils.np_utils import to_categorical




os.chdir("/Users/alexpapiu/Documents/Data/Pi_Imaging/ISBI2016_ISIC_Part3_Training_Data")

labels = pd.read_csv("/Users/alexpapiu/Documents/Data/Pi_Imaging/ISBI2016_ISIC_Part3_Training_GroundTruth.csv", header = None)
labels

img_paths

img_paths = os.listdir()[1:]


imgs = []
for path in img_paths:
    img = load_img(path, target_size=(150, 200, 3))
    img = np.array(img).transpose(2,0,1)
    imgs.append(img)

imgs = np.array(imgs)
imgs.shape

np.save("images", imgs)

#checking if it works.
plt.imshow(imgs[1].transpose(1,2,0))

target_enc = LabelEncoder()
y = target_enc.fit_transform(labels[1])

X_tr, X_val, y_tr, y_val = train_test_split(imgs, y, stratify = y)

X_tr = X_tr/255.0
X_val = X_val/255.0

X_tr

X_tr.shape



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


model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

fracs = pd.Series(y_tr).value_counts()
fracs = fracs/np.sum(fracs)
fracs

model.fit(X_tr, y_tr, validation_data = (X_val, y_val), nb_epoch = 5, batch_size = 32)



model.predict(X_val)
