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

fig, ax = plt.subplots(ncols=4, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0].imshow(edge_roberts,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1].set_title('Sobel Edge Detection')

ax[2].imshow(edge_scharr,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[2].set_title('Scharr Edge Detection')

ax[3].imshow(edge_prewitt,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[3].set_title('Prewitt Edge Detection')


for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()