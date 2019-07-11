#def avg_val_pic(img, numtiles,reshape_x,reshape_y): #input img as string
from astropy.io import fits	
from skimage import img_as_float
import numpy as np
import matplotlib.pyplot as plt
import image_slicer
from PIL import Image
from skimage.filters import scharr, prewitt, roberts, sobel
	
fits_file = 'aia.lev1.94A_2019-06-14T00_00_35.12Z.image_lev1.fits'
img=fits.getdata(fits_file)
numtiles=9604
reshape_x=98
reshape_y=98
percent_thresh = 0.025
	
fltr_image = scharr(img)# Applies  filter to image
thresh = np.where(fltr_image <= percent_thresh * fltr_image.max()) #Threshold the filter 
fltr_image[thresh] = 0

#tl_fltrd_img = Image.fromarray(fltr_image)	
#tiles = image_slicer.slice(, numtiles, save=False)# Tiles the image into numtiles
#strg_arr = np.zeros((numtiles), dtype=np.uint16)  # storage array of zeros
	
#for f,tile in enumerate(tiles): 
#		tl_img = tile.image
#		pixels = (np.sum(tl_img))	# take sum pix value from sliced images
#		strg_arr[f] = pixels 		# sets all values in empty array to mean of the tile
	
#strg_arr = strg_arr.reshape(reshape_x, reshape_y)
#plt.imshow(strg_arr, origin='lower', vmin=strg_arr.std(), vmax=strg_arr.max(), cmap='cividis')	
plt.imshow(fltr_image, origin = 'lower', vmin=0.1,vmax=3.5, cmap='inferno')
plt.show()
