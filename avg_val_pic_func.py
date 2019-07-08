def avg_val_pic(img, numtiles,reshape_x,reshape_y): #input img as string
	from skimage import img_as_float
	import numpy as np
	import matplotlib.pyplot as plt
	import image_slicer
	from PIL import Image
	from skimage.filters import sobel
	
	
	
	imag = Image.open(img)
	image = sobel(img_as_float(imag))# Applies Sobel filter to image
	if (image >= 0.9*image).any() : 0
	tiles = image_slicer.slice(img, numtiles, save=False)# Tiles the images into numtiles
	strg_arr = np.zeros((numtiles), dtype=np.uint16)  # storage array of zeros
	
	for f,tile in enumerate(tiles): 
		tl_img = tile.image
		pixels = (np.sum(tl_img))	# take sum pix value from sliced images
		strg_arr[f] = pixels 		# sets all values in empty array to mean of the tile
	
	strg_arr = strg_arr.reshape(reshape_x, reshape_y)
	#plt.imshow(strg_arr, origin='lower', vmin=strg_arr.std(), vmax=strg_arr.max())##show new image
	#plt.show()
