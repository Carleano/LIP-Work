#Shows log Scaled image and those same images Denoised side by side
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
from PIL import Image
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
 
 
#Original data 
inact_image = fits.getdata('aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits')    
active_image = fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')

#Log Scale the images
log_inct = np.log10(fits.getdata('aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits'))
log_actv = np.log10(fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits'))
#
Base_10_dnsd = denoise_tv_chambolle(log_actv, weight=50, multichannel=True)

#Setup Subplot figure for images
fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(20, 10))

ax[0].imshow(log_actv, vmin=1,vmax=2.95, cmap=plt.cm.inferno )
ax[0].axis('off')
ax[0].set_title('Base 10 Active Sun')
ax[1].imshow(Base_10_dnsd, vmin=1,vmax=2.95, cmap=plt.cm.inferno)
ax[1].axis('off')
ax[1].set_title('Denoised Base 10 Active Sun')


fig.tight_layout()
plt.show()
