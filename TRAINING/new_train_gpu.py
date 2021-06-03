"""README
To train the model:
 i)Import architectures.py script
 ii)Set the required architecture for the model 
 iii)Adjust all the hyperparameters
Finally run the script as:
python3 script_name.py """

import tensorflow as tf
import architectures
import os
import keras
from alt_model_checkpoint.keras import AltModelCheckpoint
from keras.utils import multi_gpu_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

img_width = 224
img_height = 224
train_data_dir = '/home/vishwam/mountpoint/ss/pan/voter_cloth_dataset2/train'
valid_data_dir = '/home/vishwam/mountpoint/ss/pan/voter_cloth_dataset2/test'
batch_size = 64
checkpoints_filepath="weights-improvement-{epoch:02d}-{val_accuracy:.2f}.hdf5"
input_shape = (img_height, img_width, 3)

datagen = keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)

train_generator = datagen.flow_from_directory(directory=train_data_dir,target_size=(img_height,img_width),classes=['real','fake'],class_mode='binary',batch_size=batch_size,interpolation='lanczos')

validation_generator = datagen.flow_from_directory(directory=valid_data_dir,target_size=(img_height,img_width),classes=['real','fake'],class_mode='binary',batch_size=1,interpolation='lanczos')

model = architectures.Faceliveness()
# print(model.summary())

# adam =keras.optimizers.Adam(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
adam =keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
gpu_model = multi_gpu_model(model,2)
#architecture.compile(loss='binary_crossentropy',optimizer=optimizer , metrics=['accuracy'])
gpu_model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#checkpoint = keras.callbacks.callbacks.ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
early_stopping = keras.callbacks.callbacks.EarlyStopping(monitor='val_accuracy', min_delta=0, patience=6, verbose=0, mode='max', baseline=None, restore_best_weights=True)
alt_checkpoint = AltModelCheckpoint(checkpoints_filepath, model, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callback_list = [early_stopping, alt_checkpoint]
training = gpu_model.fit_generator(generator=train_generator, steps_per_epoch=421,epochs=18,validation_data=validation_generator,validation_steps=3000,callbacks = callback_list)
#training = model.fit_generator(generator=train_generator, steps_per_epoch=,epochs=10,validation_data=validation_generator,validation_steps=)


model.save('votermodels_generated_test/voter_paste2_6_0.h5')




