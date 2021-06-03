import numpy as np
import argparse
import cv2
import random
from random import random
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
    help="path to input image file") 

args = vars(ap.parse_args())
images = args["image"]
image_path_output = 'output'
# print(os.listdir(images))
for fl in os.listdir(images):
  image0=os.path.join(images,fl)
  print(fl)
  if fl == ".DS_Store" or fl == "_DS_Store":
    print("stupid files")
  else:
    image = cv2.imread(image0)
    kernel = np.ones((12,12), np.uint8)
    img_erosion = cv2.erode(image, kernel, iterations=12)
    img_dilation = cv2.dilate(image, kernel, iterations=1)
    value = random()
    # cv2.imwrite(str(image_path_output) + "/" +str(value)+ ".jpg",img_dilation)
    cv2.imwrite(str(image_path_output) + "/"+fl,img_dilation)





