"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
Note: destination folder is created while the script is running """

import cv2
from scipy import ndimage, misc
import numpy as np
import scipy.ndimage
import argparse
import os
import random
from random import shuffle
import skimage.util
import imageio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', type=str, default='', help='path')
    ap.add_argument('-d', '--destination', type=str, default='', help='path')
    args = vars(ap.parse_args())
    outPath = args["destination"]
    path = args['image']
    os.mkdir(outPath)

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        img = cv2.imread(input_path)
        print(img)

        List = [0.7,0.9]
        for i in List:
            beta=100
            result = cv2.addWeighted(img, i, np.zeros(img.shape, img.dtype),0,beta)
            fullpath = os.path.join(outPath, 'bright_'+str(i)+'_'+image_path)
            imageio.imwrite(fullpath,result)

if __name__ == '__main__':
    main()
