import skimage as ski
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

%matplotlib inline

os.chdir("/Users/alexpapiu/Documents/Data/NSFW/Pictures/")

name = "alex_pen"

img0 = plt.imread("{0}0.0.jpg".format(name))
img1 = plt.imread("{0}1.0.jpg".format(name))
img2 = plt.imread("{0}2.0.jpg".format(name))
img3 = plt.imread("{0}3.0.jpg".format(name))

plt.imshow(img3)


img = [img0, img1, img2, img3]

images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in img]
images = np.array(images)

images.shape

plt.imshow(images.mean(0), cmap = "viridis")


plt.imshow(images[0], cmap = "viridis")

plt.imshow(images.max(0) - images.mean(0), cmap = "viridis")


plt.imshow(images[0])


import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])



data = [go.Surface(z=img[0])]

data

layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90)
)
fig = go.Figure(data=data)

py.iplot(fig, filename='elevations-3d-surface')
