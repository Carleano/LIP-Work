#shows original images and sobel filter side by side
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
from skimage import feature
from skimage.feature import greycomatrix, greycoprops
import matplotlib.image as mpimg

img1 = '2019_06_14__00_00_06_62__SDO_AIA_AIA_131.png'
img2 = '2019_06_14__00_00_09_63__SDO_AIA_AIA_211.png'
img3 = '2019_06_14__00_00_12_63__SDO_AIA_AIA_335.png'
img4 = '2019_06_14__00_00_21_35__SDO_AIA_AIA_171.png'
img5 = '2019_06_14__00_00_28_84__SDO_AIA_AIA_193.png'
img6 = '2019_06_14__00_00_29_13__SDO_AIA_AIA_304.png'
img7 = '2019_06_14__00_00_35_12__SDO_AIA_AIA_94.png'

#Reads the images
img1 = mpimg.imread(img1)
img2 = mpimg.imread(img2)
img3 = mpimg.imread(img3)
img4 = mpimg.imread(img4)
img5 = mpimg.imread(img5) 
img6 = mpimg.imread(img6)
img7 = mpimg.imread(img7)

#List of read images
images = [img1, img2, img3, img4, img5, img6, img7]

cols = 7
rows = 2

fig, ax = plt.subplots(rows, cols, sharex = True, sharey = True, figsize = (18,9))

for k in range(len(images)):
	edg_fltr = sobel(images[k])
	ax[0, k-1].imshow(images[k], cmap=plt.cm.viridis)
	ax[0, k-1].set_title('Sobel Filtered Images')
	ax[1,k].imshow(edg_fltr, cmap=plt.cm.viridis)
	ax[1,k].set_title('Original Images')	
#plt.tight_layout()
plt.show()
