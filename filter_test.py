import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
    
img=Image.open('2019_06_14__00_00_12_63__SDO_AIA_AIA_335.png')
image = img
edge_roberts = roberts(image)
edge_sobel = sobel(image)
edge_scharr = scharr(image)
edge_prewitt = prewitt(image)

fig, ax = plt.subplots(ncols=4, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0].imshow(edge_roberts, cmap=plt.cm.inferno)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel, cmap=plt.cm.inferno)
ax[1].set_title('Sobel Edge Detection')

ax[2].imshow(edge_scharr, cmap=plt.cm.inferno)
ax[2].set_title('Scharr Edge Detection')

ax[3].imshow(edge_prewitt, cmap=plt.cm.inferno)
ax[3].set_title('Prewitt Edge Detection')


for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()