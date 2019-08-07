#Generates highlighted bins in image and also creates sound files for each one. Because they are in the same for loop, the sound file and highlighted bin are guaranteed to be the same.
from moviepy.video.io.ffmpeg_tools import ffmpeg_movie_from_frames
import numpy as np
from astropy.io import fits	
import matplotlib.pyplot as plt 
from IPython.display import Audio
import os
import math
from scipy.io.wavfile import read, write
from scipy.signal import argrelextrema
from IPython.display import Audio
import warnings
import librosa
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
log_org = rebin(log_org, (8,8))
#Normalize data 
log_org = np.subtract(-1*log_org,log_org.min())
log_org = np.divide(log_org,log_org.max())
#print(log_org)

bin_arr = np.zeros([64, 64])
cnt = 0
framerate = 44100
t = np.linspace(0,5,framerate*5)
a_value=0
scaled_data = np.empty((0, 220500))
for val in np.nditer(log_org):
	val = val * -1
	bin_arr[cnt] = log_org.reshape(64)
	bin_arr[cnt, cnt] = val
	cnt = cnt + 1
	volume = val
	data = (np.sin(2*np.pi*220*.01*t)*np.exp(a_value*t)  + np.sin(2*np.pi*224*t)*np.exp(a_value*t))
	max_data=np.max(data)
	min_data=np.min(data)
	if np.abs(min_data) >= max_data:
		max_data=np.abs(min_data)
	data=data/max_data
	scaled_data = np.append(scaled_data, [volume*data], axis = 0)
	#librosa.output.write_wav('sonified_pixels_' + str(cnt) + '.wav', scaled_data, sr=framerate, norm=False)
bin_arr = bin_arr.reshape(64, 8, 8)
scaled_data = scaled_data.reshape(14112000)
#librosa.output.write_wav('sonified_pixels_movie.wav', scaled_data, sr=framerate, norm=False)#rate=framerate, autoplay=True, normalize=False)

mvie.ffmpeg_tools.ffmpeg_movie_from_frames(filename='8x8_movie', folder='movie_clips', fps=.2, digits=6)

#for cnt in range (64):
#	plt.imsave('movie_clips' + str(cnt) + '.png',bin_arr[cnt],  origin = 'lower', vmax = 3, cmap = plt.cm.inferno)
