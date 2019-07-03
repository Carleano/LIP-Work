def avg_val_pic(img, numtiles,reshape_x,reshape_y): #input img as string
	from skimage import io, img_as_float
	import numpy as np
	import image_slicer
	from PIL import Image
	import matplotlib.pyplot as plt
	
	
	numtiles=numtiles
	imag = Image.open(img)
	image = img_as_float(imag)
	tiles = image_slicer.slice(img, numtiles, save=False)
	tile_lngth = len(np.array(tiles[0].image)) # Length of tile 1 array
	strg_arr = np.zeros((numtiles), dtype=np.uint16)  # storage array of zeros
	
	for f,tile in enumerate(tiles): 
		tl_img = tile.image
		pixels = (np.mean(tl_img))	# take avg pix value from sliced images
		strg_arr[f] = pixels 		# sets all values in empty array to mean of the tile???
	
	strg_arr = strg_arr.reshape(reshape_x, reshape_y)
	plt.imshow(strg_arr, origin='lower') #vmin=strg_arr.min(), vmax=strg_arr.max())
	plt.show()
	#img.save('avg_val_pic', img)
#avg_val_pic('imggrid.png',9604,98,98)