# gratings.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-500, 501, 1)

X, Y = np.meshgrid(x, x)

wavelength = 200
angle = np.pi / 9 # pi/9 radians = 20 degree
print(np.degrees(angle))
print(angle * (180/np.pi))
grating = np.sin(
    2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / wavelength
)

plt.set_cmap("gray")
plt.imshow(grating)
plt.show()