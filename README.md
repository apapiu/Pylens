# archhacks
Project for the Archhacks competition by [Jon Bumstead](http://www.jrbums.com/) and [Alexandru Papiu](http://apapiu.github.io/)

### Statement:
The Goal of this project was to construct an imaging device that could be used in low resource settings. 

Despite the millions of people that suffer from some form of eye impairment, there are only a few low-cost
diagnostic tools available for identifying eye disorders. We therefore developed PyLens, a portable low-cost
microscopy system capable of screening for eye disease, profiling the ocular surface, and measuring
differential changes in oxy- and deoxygenated hemoglobin in the eye.

The PyLens uses a Raspberry Pi under the hood and this allows machine learning algorithms to be embedded onto the device and be used real-time to predict and diagnose diseases. We've managed to make some basic deep learning algortihms run on the Pi. These basic Convolutional Nets are able to distinguish between basic hand gestures. The hope is that with adequate datasets one could train the PyLens to classify eye defects and skin lesions using convolutional neural networks. 

The PyLens is constructed with a Raspberry Pi, four individually addressable LEDs, low-lost optics, and 3D
printed optomechanical components. It also only costs around $130 and requires no smart phone to operate.
By acquiring images with different angles of illumination, the PyLens is capable of acquiring 3D reconstructions
of the ocular surface. In addition, the PyLens can also perform spectral imaging of the eye. Due to the
wavelength dependent absorption of light by hemoglobin, the PyLens can measure relative changes in oxy-
and deoxy-hemoglobin. Both these features in combination with machine learning algorithms available
developed with our system, give the PyLens a unique capability in diagnosing eye impairment, specifically in
low resource settings.



### The Pylens:
![](https://github.com/apapiu/Pylens/blob/master/images/img1.jpg)

### Eye Image taken with the PyLens:
![](https://github.com/apapiu/Pylens/blob/master/images/img2.jpg)

