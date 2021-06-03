"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
source_folder is the folder which contains images which you want to copy to destination_folder with different name(random name)
Note1: destination folder is created while the script is running
Note2: you can also adjust the "threshold" below to make copy of those many no.of images """

from PIL import Image 
import argparse
import random
import os
from random import random

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
    help="path to input image file") #images folder
ap.add_argument("-d", "--destination", type=str, default="",
    help="path to input image file") #images folder
args = vars(ap.parse_args())
images = args["image"]
dest = args["destination"]
os.mkdir(dest)

threshold=50 #limit on images to rename
count=0
for fl in os.listdir(images):
    if fl == ".DS_Store" or fl == "_DS_Store":
        print("stupid files")
    else:
        count=count+1
        if count<=threshold:
            image0 = os.path.join(images,fl)
            Image1 = Image.open(image0)
            val= str(random())
            val_int=val[2:]
            Image1.save(str(dest) + "/" + "ren_" +str(val_int)+ ".jpg")
        else:
            exit()

 
