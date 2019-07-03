import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
import matplotlib.image as mpimg
import image_slicer as imgslcr
from PIL import Image

img = '2019_06_14__00_00_06_62__SDO_AIA_AIA_131.png'



def img_slcr(input,tiles):# function to slice image
	pxl_strg = imgslcr.slice(input, tiles)
	
	#image = imgslcr.join(pxl_strg) ## joins image back together

	image.save('grd_image.png')

img_slcr(img, 100)

