import sys
import imageio
import numpy as np
import cv2

# defines the number of bins for pixel values of each type {r,g,b}
num_bins=16

# size of values in each bin
range_per_bin=256/num_bins

#frame chosen every k frames
sampling_rate=int(sys.argv[2])

#manual function to generate a 3D tensor representing histogram
def generate_histogram(frame):
	histogram=np.zeros(num_bins,num_bins,num_bins)
	for row in range(len(frame)):
		for row in range(len(frame[row])):
			r,g,b=frame[row][col]
			histogram[r/num_bins][g/num_bins][b/num_bins]+=1;
	return histogram

def main():
	video=imageio.get_reader(sys.argv[1]);

	#manually generated histogram
	color_histogram=[generate_histogram(video.get_data(i*sampling_rate)) for i in range(len(video)/sampling_rate)]

	#opencv: generates 3 histograms corresponding to each channel for each frame
	channels=['b','g','r']
	hist=[]
	for i,col in enumerate(channels):
		hist.append([cv2.calcHist(video.get_data(j*sampling_rate),[i],None,[num_bins],[0,256]) for j in range(len(video)/sampling_rate)])



if __name__ == '__main__':
	main()