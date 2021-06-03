"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
Note: destination folder is created while the script is running """

import cv2
import numpy as np
# import scipy.ndimage
from skimage.util import random_noise
import os
import random
from random import shuffle
# import skimage.util
import argparse

#from deff import pepper,salt_pepper,gauss,speckle,salt,poisson

# Load the image
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
        gauss = random_noise(img, mode='gaussian', seed=None, clip=True)
        poisson = random_noise(img, mode='poisson')
        s_p = salt_pepper(img, 0.001)
        gauss = np.array(255*gauss, dtype = 'uint8')
        poisson = np.array(255*poisson, dtype = 'uint8')
        # salt_img=salt(img)
        # cv2.imwrite( str(outPath) + "/" + "salt" +image_path,salt_img)
        # pepper_img=pepper(img)
        # speckle_img=speckle(img)
        # cv2.imwrite( str(outPath) + "/" + "speckle" +image_path,speckle_img)
        # cv2.imwrite( str(outPath) + "/" + "pepper" +image_path,pepper_img)
        cv2.imwrite( str(outPath) + "/" + "gauss" +image_path,gauss)
        cv2.imwrite( str(outPath) + "/" + "poisson" +image_path,poisson)
        cv2.imwrite( str(outPath) + "/" + "salt_pepper" +image_path,s_p)



# def salt(image):
#       row,col,ch = image.shape
#       s_vs_p = 0.5
#       amount = 0.001
#       out = np.copy(image)

#       num_salt = np.ceil(amount * image.size * s_vs_p)
#       coords = [np.random.randint(0, i - 1, int(num_salt))
#               for i in image.shape]
#       out[coords] = 1
#       return out

# def pepper(image):
#       row,col,ch = image.shape
#       s_vs_p = 0.5
#       amount = 0.001
#       out = np.copy(image)

#       num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
#       coords = [np.random.randint(0, i - 1, int(num_pepper))
#               for i in image.shape]
#       out[coords] = 0
#       return out

# def speckle(image):
#       row,col,ch = image.shape
#       gauss = np.random.randn(row,col,ch)
#       gauss = gauss.reshape(row,col,ch)        
#       speckle = image + image * gauss
#       return speckle
def salt_pepper(image,prob):
    
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

if __name__ == '__main__':
    main()
