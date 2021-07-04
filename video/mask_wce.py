# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:30:42 2019

@author: ABSBIN
"""

#!/usr/bin/python3

import os
import numpy as np
from PIL import Image
from PIL import ImageFilter


OUTPUT_DIR = 'out'


def process1(file):
# Print out some file information
	image = Image.open(file)
	
	thresh = 2
	
	image = image.convert('L').point(lambda x : 255 if x > thresh else 0, mode='1')


	# Apply BoxBlur Filter
	file_name, file_ext = os.path.splitext(file)
	output_file_name = os.path.basename(file_name) + '.jpg'
	output_file_path = os.path.join(os.getcwd(), OUTPUT_DIR, output_file_name)
	#print("Saving image to " + output_file_path)
	image.save(output_file_path)
	#jpg_image.save(output_file_path)

	
def process(file):
	image = Image.open(file)
	gray = image.convert('L')

	# Let numpy do the heavy lifting for converting pixels to pure black or white
	bw = np.asarray(gray).copy()
	thresh = 1
	# Pixel range is 0...255, 256/2 = 128
	bw[bw < thresh] = 0    # Black
	bw[bw >= thresh] = 255 # White

	# Now we put it back in Pillow/PIL land
	imfile = Image.fromarray(bw)
	imfile.save("result_bw.png")

def main():
    image_exts = [ '.jpg', '.jpeg', '.png' ]
    input_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(os.getcwd(), 'out')

    # Create output directory, if not present
    
    # Iterate over working directory
    for file in os.listdir(input_dir):
        try:
            os.stat(output_dir)
        except:
            os.mkdir(output_dir)
        file_path = os.path.join(input_dir, file)
        file_name, file_ext = os.path.splitext(file_path)
		# Check if file is an image file
        if file_ext not in image_exts:
            print("Skipping " + file + " (not an image file)")
            continue
        else:
            print( file )
            process(file_path)
		

if __name__ == '__main__':
    main()