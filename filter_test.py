#Shows original images and the images log Scaled side by side
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt

from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
 
 
#Original data 
inact_image = fits.getdata('aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits')    
active_image = fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')
#Log Scale the images
log_inct = np.log10(fits.getdata('aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits'))
log_actv = np.log10(fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits'))

#Setup Subplot figure for images
fig, ax = plt.subplots(nrows=2,ncols=2, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0,0].imshow(inact_image,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[0,0].set_title('Original Inactive')

ax[1,0].imshow(active_image,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1,0].set_title('Orignal Active')

ax[0,1].imshow(log_inct,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[0,1].set_title('Base 10 inactive')

ax[1,1].imshow(log_actv,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1,1].set_title('Base 10 Active')



plt.tight_layout()
plt.show()
