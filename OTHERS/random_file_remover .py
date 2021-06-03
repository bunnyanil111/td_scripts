"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder -n threshold
i)source_folder is the folder from which you want to move images
ii)destination_folder is to where you want to move your images
iii)threshold is the no.of images you want to move from source_folder to destination_folder
Note: destination folder is created while the script is running """

import os
import random
import argparse
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_folder", type=str, default="",
	help="path to input image_folder")
ap.add_argument("-d", "--destination", type=str, default="",
	help="path to input image_folder")
ap.add_argument("-n", "--number of images", type=int, default="",
	help="path to input image_folder")
args = vars(ap.parse_args())
dest=args["destination"]
os.mkdir(dest)

for i in range(args["number of images"]):
	filename = random.choice(os.listdir(args["image_folder"]))
	path = os.path.join(args["image_folder"], filename)
	shutil.move(path,dest)
