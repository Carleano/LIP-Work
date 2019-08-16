#Rescales image and then normalizes array of pixels from minimun 0 to maximum 1
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt 
import matplotlib
 
#Read In image
ninety_four_image=fits.getdata('aia.lev1.94A_2011-06-15T17_00_02.12Z.image_lev1.fits')
#Threshold to avoid nan and -inf values in array when using Log10
ninety_four_image[ninety_four_image <= 0] = .000000001
log_org = np.log10(ninety_four_image)
#Rebin function, method for interpolation is averaging. Returns resized array
def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)
log_org = rebin(log_org, (8,8))#INSERT DESIRED REBIN SIZE HERE
#Normalize data 
log_org = np.subtract(-1*log_org,log_org.min())
log_org = np.divide(log_org,log_org.max())



#plt.figure(figsize = (14,14), tight_layout = True)
#plt.imshow(log_org, origin='lower', vmax=3, cmap=plt.cm.inferno, extent = (0, 8, 0, 8))
#plt.imsave('Fits_pixelated.png', log_org, origin = 'lower', vmax = 3, cmap = plt.cm.inferno)
#plt.show()

