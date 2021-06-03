"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
Note: destination folder is created while the script is running """

from PIL import Image 
import argparse
import random
import os
import copy
from random import random
from time import sleep
import cv2 
import numpy as np 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
    help="path to input image file") 
ap.add_argument("-d", "--destination", type=str, default="",
    help="path to input image file") 

args = vars(ap.parse_args())
images = args["image"]
dest_folder = args["destination"]
os.mkdir(dest_folder)
# print("Target images: ",res)

for fl in os.listdir(images):
	an=os.path.join(images,fl)

	if an == ".DS_Store" or an == "_DS_Store":
		print("stupid files")
	else:
		cap = cv2.imread(an)
		hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
		lower_red = np.array([30,150,50]) 
		upper_red = np.array([255,255,180])
		mask = cv2.inRange(hsv, lower_red, upper_red)
		res = cv2.bitwise_and(cap,cap, mask= mask)
		edges = cv2.Canny(cap,100,200)
		Image1copy=edges.copy()
		value = random()
		fullpath = os.path.join(dest_folder,str(fl))
		print(fullpath)
		cv2.imwrite(fullpath,Image1copy)











