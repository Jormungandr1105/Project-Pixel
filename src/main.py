#!/usr/bin/python3

from PIL import Image
import os
import ImageP

def process(pixels):
	pass


if __name__ == '__main__':
	image0 = "../images/starry_night.jpg"
	image1 = "../images/son_of_man.jpg"
	image2 = "../images/windows.jpg"
	image3 = "../images/einstein.jpg"
	image4 = "../images/dark_side.jpg"
	processor = ImageP.ImageP(image1)
	processor.pixel_reduce(16)
	processor.modify_file_from_array(4)