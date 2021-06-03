#Script to resize the images

import os
import argparse
import dlib
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
	help="path to input image file")
args = vars(ap.parse_args())


images = args["image"]	

path=os.getcwd()

for fl in os.listdir(images):
	print(fl)
	if fl == ".DS_Store" or fl == "_DS_Store":
		print(fl)
		print("stupid files")

	else:
		images2 = os.path.join(images,fl)	
		frame = cv2.imread(images2)
		try:	
			fl2 = fl.split(".")[0]
			cv_interpolation = cv2.INTER_LANCZOS4
			cropped = cv2.resize(frame, dsize=(224,224), interpolation=cv_interpolation)
			extention= os.path.splitext(fl)[-1]

			cv2.imwrite( str(images) + "/" + str(fl2) + extention,cropped)

		except:
		 	print("gip")
		 	continue




			

		
