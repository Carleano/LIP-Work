from astropy.io import fits	
from skimage import img_as_float
import numpy as np
import matplotlib.pyplot as plt
import image_slicer
from PIL import Image
from skimage.filters import scharr, prewitt, roberts, sobel

fits_file = 'aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits'
image=fits.getdata(fits_file)
percent_thresh = 0.025	
fltr_image1 = scharr(image)# Applies  filter to image

thresh = np.where(fltr_image1 <= percent_thresh * fltr_image1.max()) #Threshold the filter 
fltr_image1[thresh] = 0

fltr_image2 = prewitt(image)# Applies  filter to image

thresh = np.where(fltr_image2 <= percent_thresh * fltr_image2.max()) #Threshold the filter 
fltr_image2[thresh] = 0

fltr_image3 = sobel(image)# Applies  filter to image

thresh = np.where(fltr_image3 <= percent_thresh * fltr_image3.max()) #Threshold the filter 
fltr_image3[thresh] = 0

fltr_image4 = roberts(image)# Applies  filter to image

thresh = np.where(fltr_image4 <= percent_thresh * fltr_image4.max()) #Threshold the filter 
fltr_image4[thresh] = 0

fig, ax = plt.subplots(nrows=2, ncols=4, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[1,0].imshow(fltr_image1,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,0].set_title('Roberts Edge Detection')
ax[0,0].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,1].imshow(fltr_image2,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,1].set_title('Sobel Edge Detection')
ax[0,1].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,2].imshow(fltr_image3,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,2].set_title('Scharr Edge Detection')
ax[0,2].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,3].imshow(fltr_image4,vmin=0.1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,3].set_title('Prewitt Edge Detection')
ax[0,3].imshow(image,vmin=0.1,vmax=3.5,cmap=plt.cm.inferno)

#for a in ax:
#    a.axis('off')

plt.tight_layout()
plt.show()