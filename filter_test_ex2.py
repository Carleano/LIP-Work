#Shows original images and the rebinned and log scaled side by side
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt

from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
 
 
#Original data 
inact_image = fits.getdata('aia.lev1.171A_2012-07-11T01_17_11.34Z.image_lev1.fits')    
active_image = fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')

#Log Scale the images
log_inct = np.log10(inact_image)
log_actv = np.log10(active_image)
#Rebin Array to new shape that is arr arg is divisible by
def rebin(arr, new_shape):
	
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)
Rbnd_base_act = rebin(log_actv,(512,512))
Rbnd_base_inact =  rebin(log_inct,(512,512))

#Setup Subplot figure for images
fig, ax = plt.subplots(nrows=2,ncols=2, 
                       figsize=(20, 10))

ax[0,0].imshow(inact_image,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[0,0].set_title('Original 171 Active')

ax[1,0].imshow(active_image,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1,0].set_title('Orignal  94 Active')

ax[0,1].imshow(Rbnd_base_inact,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[0,1].set_title('Rebinned Base 10 171 active')

ax[1,1].imshow(Rbnd_base_act,origin = 'lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1,1].set_title('Rebinned Base 10 94 Active')



plt.tight_layout()
plt.show()
