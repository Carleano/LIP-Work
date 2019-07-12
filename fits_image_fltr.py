#show the filtered fits images compared to the original
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
import numpy as np
import matplotlib.pyplot as plt
import image_slicer
from PIL import Image
from skimage.filters import scharr, prewitt, roberts, sobel

fits_file = 'aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits'
image=fits.getdata(fits_file)
edge_roberts = roberts(image)
edge_sobel = sobel(image)
edge_scharr = scharr(image)
edge_prewitt = prewitt(image)

fig, ax = plt.subplots(nrows=2, ncols=4, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[1,0].imshow(edge_roberts,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,0].set_title('Roberts Edge Detection')
ax[0,0].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,1].imshow(edge_sobel,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,1].set_title('Sobel Edge Detection')
ax[0,1].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,2].imshow(edge_scharr,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,2].set_title('Scharr Edge Detection')
ax[0,2].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,3].imshow(edge_prewitt,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,3].set_title('Prewitt Edge Detection')
ax[0,3].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[0,3].set_title('Original')
ax[0,2].set_title('Original')
ax[0,1].set_title('Original')
ax[0,0].set_title('Original')

plt.tight_layout()
plt.show()
