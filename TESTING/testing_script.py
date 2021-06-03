
"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder
Note: destination folder is created while the script is running """

import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
import csv
import tensorflow as tf
import shutil  
import random


ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='',help='path')
ap.add_argument('-m','--model',type=str,default='',help='path')
ap.add_argument('-d','--destination', type=str, default='true',
 help="path to destination folder")
args=vars(ap.parse_args())

dest = args["destination"]
image_path=args['image']
os.mkdir(dest)
def preprocessing_img(img_path):
    #Converting the image to tensor
    img = tf.keras.preprocessing.image.load_img(img_path,target_size=(224, 224),interpolation = "lanczos")
    #this function Loads the image and resizes it to the specified size using PIL(Nearest Neighbour)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    #this function converts the image to numpy Array
    img_array = np.expand_dims(img_array, axis=0)
    #(1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_array /= 255.
    #the numpy array are normalized between 0 and 1
    return img_array


ran_val=random.random()
str_ran_value=str(ran_val)

an = args["model"]
model = tf.keras.models.load_model(an)
images=os.listdir(image_path)
fi=open(str_ran_value,"x")
a=[]
count_of_total_images=0
count_of__FP =0
for each_image in images:
    count_of_total_images+=1    
    try:
        img_path = os.path.join(image_path,each_image)
        new_image = preprocessing_img(img_path)
        pred = model.predict(new_image)
        print(each_image , pred)
        if pred[0][0]<0.5:
            a.append(each_image)                            
        else:
            continue

    except:
        print(each_image)
        continue
for i in a:
    s=str(i)
    fi.write(s)
    fi.write(os.linesep)
fi.close()
src=image_path
fil=open(str_ran_value)
lines = fil.readlines()
for file_name in lines:
    count_of__FP+=1
    try:        
        source=src+'/'+file_name
        val=shutil.move(source[:-1], dest)
    except:
        continue

fil.close()
rem_data=(count_of_total_images-count_of__FP)
print("text file created is:",str_ran_value)
print("total images processed are:",count_of_total_images)
print("total TN's or FN's are:",rem_data)
print("total FP's or TP's are/total images moved to destination are:",count_of__FP)

#finding accuracies
print("choose accuracies acc to your data")
fake_acc=(rem_data/(rem_data+count_of__FP))*100
print("If the tested data is fake then FAKE ACCURACY is :",fake_acc)


real_acc=(count_of__FP/(rem_data+count_of__FP))*100
print("if the tested data is real then REAL ACCURACY is :",real_acc)


