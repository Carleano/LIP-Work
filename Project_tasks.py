#Rescales image and then normalizes array of pixels from minimun 0 to maximum 1
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt 

 

ninety_four_image=fits.getdata('aia.lev1.94A_2012-07-11T01_17_13.13Z.image_lev1.fits')
ninety_four_image[ninety_four_image <= 0] = .000000001
log_org = np.log10(ninety_four_image)
print(log_org)
def rebin(arr, new_shape):
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)
log_org = rebin(log_org, (8,8))
print(log_org)
log_org = np.subtract(-1*log_org,log_org.min())
log_org = np.divide(log_org,log_org.max())
print(log_org)
plt.imshow(log_org,origin='lower', vmax=3, cmap=plt.cm.magma)
plt.show()

