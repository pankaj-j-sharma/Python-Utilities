#Cell 1
from __future__ import print_function
from builtins import input
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

#Cell 2
image = io.imread('images/img.png')

new_image = np.zeros(image.shape, image.dtype)
alpha = 1 # Simple contrast control
beta = 0   # Simple brightness control

#Cell 3
print(' Enter Values ')
print('-------------------------')
try:
    alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
    beta = int(input('* Enter the beta value [0-100]: '))   ##put alpha as 1.5 & beta as 60
except ValueError:
    print('Error, not a number')
	
#Cell 4
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
fig = plt.figure(figsize = (12,8))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(image)

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(new_image)