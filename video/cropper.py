# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 00:30:42 2019

@author: ABSBIN
"""

#!/usr/bin/python3

import os

from PIL import Image

OUTPUT_DIR = 'out'


def process(file):
# Print out some file information
	image = Image.open(file)	
	left_edge_coord=19
	top_edge_coord=19
	right_edge_coord=341
	bottom_edge_coord=341
	cropped_image = image.crop((left_edge_coord, top_edge_coord, right_edge_coord, bottom_edge_coord))
	file_name, file_ext = os.path.splitext(file)
	output_file_name = os.path.basename(file_name) + '_croped' + file_ext
	output_file_path = os.path.join(os.getcwd(), OUTPUT_DIR, output_file_name)
	#print("Saving image to " + output_file_path)
	cropped_image.save(output_file_path)


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