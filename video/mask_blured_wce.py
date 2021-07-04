# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:30:42 2019

@author: ABSBIN
"""

#!/usr/bin/python3

import os

from PIL import Image
from PIL import ImageFilter
import random

OUTPUT_DIR = 'out'


def process(file,mask):
# Print out some file information
	image = Image.open(file)	
	# Apply BoxBlur Filter
	boxImage = image.filter(ImageFilter.BoxBlur(14.5+random.randint(-0,6)))
	image = Image.composite(boxImage, mask, mask.convert('L'))
	file_name, file_ext = os.path.splitext(file)
	output_file_name = 'blured_'+os.path.basename(file_name)  + '.jpg'
	output_file_path = os.path.join(os.getcwd(), OUTPUT_DIR, output_file_name)
	#print("Saving image to " + output_file_path)
	image.convert('RGB').save(output_file_path)

	

def main():
    image_exts = [ '.jpg', '.jpeg', '.png' ]
    input_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(os.getcwd(), 'out')	
	# Create output directory, if not present
    mask=Image.open(os.getcwd()+'\\mask_wce322.png')
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
            process(file_path,mask)
		

if __name__ == '__main__':
    main()