#Shows original images and Highlights edge and active regions in images
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
 

#Original data

active_image = fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')

#Log Scale the images
base_10_actv = np.log10(active_image)

#Rebin Image
def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)
rbnd_base_10_actv = rebin(base_10_actv,(512,512))



#Setup Subplot figure for images
fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0].imshow(active_image, origin='lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[0].axis('off')
ax[0].set_title('Orignal')
ax[1].imshow(rbnd_base_10_actv,origin='lower', vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1].axis('off')
ax[1].set_title('Base 10, Rebinned Active Sun')


fig.tight_layout()
plt.show()
