#Overlays Grid over input file
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image



# Open image file
image = Image.open('Fits_pixelated.png')
my_dpi=300.


plt.grid(True,axis='both' )	
plt.imshow(image, origin='lower', extent = (0, 8, 0, 8))
plt.imsave('Fits_pixelated_Grid.png', image, origin = 'lower', vmax = 3, cmap = plt.cm.inferno)
plt.show()
