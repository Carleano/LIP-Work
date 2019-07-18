#Shows log Scaled image and those same images Denoised side by side
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
 
 
#Original data 
active_image = fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')
#Denoise
dnsd_active = denoise_tv_chambolle(active_image, weight=50, multichannel=True)

#Log Scale the images
base_10_dnsd_act = np.log10(dnsd_active)
base_10 = np.log10(active_image)
#Setup Subplot figure for images
fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0].imshow(base_10, vmin=1,vmax=2.95, cmap=plt.cm.inferno )
ax[0].axis('off')
ax[0].set_title('Base 10 Active Sun')
ax[1].imshow(base_dnsd_10_act, vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1].axis('off')
ax[1].set_title('Denoised Base 10 Active Sun')


fig.tight_layout()
plt.show()
