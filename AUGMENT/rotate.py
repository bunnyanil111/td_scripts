"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
Note: destination folder is created while the script is running """

from scipy import ndimage, misc
import imageio
import argparse
import numpy as np
import os
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', type=str, default='', help='path')
    ap.add_argument('-d', '--destination', type=str, default='', help='path')
    args = vars(ap.parse_args())
    outPath = args["destination"]
    os.mkdir(outPath)
    path = args['image']
    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = imageio.imread(input_path)
        print(image_path)
        List = [0.1,0.3,0.5,0.7]
        for i in List:
            rotate = ndimage.rotate(image_to_rotate,i)
            fullpath = os.path.join(outPath, 'rotate_'+str(i)+'_'+image_path)
            imageio.imwrite(fullpath,rotate)


if __name__ == '__main__':
    main()
