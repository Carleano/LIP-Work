#Shows the Thresholds and filters the FITS images also log scales the data in comparison to Active original 
from astropy.io import fits	
from skimage import img_as_float
import numpy as np
import matplotlib.pyplot as plt
import image_slicer
from PIL import Image
from skimage.filters import scharr, prewitt, roberts, sobel

fits_file = 'aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits'
pure_data = fits.getdata(fits_file)
image=np.log10(fits.getdata(fits_file))#Log scales the data
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

#Set up figure
fig, ax = plt.subplots(nrows=2, ncols=4, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[1,0].imshow(fltr_image1,vmin=1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,0].set_title('Scharr Edge Detection, Thresholded, Base10 Log')
ax[0,0].imshow(pure_data,vmin=1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,1].imshow(fltr_image2,vmin=1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,1].set_title('Prewitt Edge Detection, Thresholded, Base10 Log')
ax[0,1].imshow(pure_data,vmin=1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,2].imshow(fltr_image3,vmin=1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,2].set_title('Sobel Edge Detection, Thresholded, Base10 Log')
ax[0,2].imshow(pure_data,vmin=1,vmax=3.5,cmap=plt.cm.inferno)
ax[1,3].imshow(fltr_image4,vmin=1,vmax=3.5, cmap=plt.cm.inferno)
ax[1,3].set_title('Roberts Edge Detection, Thresholded, Base10 Log')
ax[0,3].imshow(pure_data,vmin=1,vmax=3.5,cmap=plt.cm.inferno)
ax[0,3].set_title('Original')
ax[0,2].set_title('Original')
ax[0,1].set_title('Original')
ax[0,0].set_title('Original')

plt.tight_layout()
plt.show()
