# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nTvvVrlgakV7F2HDSBKIr3G5umdlplv8
"""

# Commented out IPython magic to ensure Python compatibility.
#Import and install required libraries
import os
import glob
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Flatten, Conv2D,Dense,MaxPooling2D,Dropout,BatchNormalization,Activation 
from PIL import Image
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
## Automate the building of CNN
def convolutional_neural_network_CNN(filter_multiplier=1,num_filters=32,dropout=0.2,dense_size=64,batch_norm=False,image_size=200,num_classes=10):
    model = Sequential()
    #filter_size = [(11,11),(9,9),(7,7),(5,5),(3,3)]
    filter_size = [(3,3),(3,3),(3,3),(3,3),(3,3)]

#*************************************************************LAYER 1**********************************************************************************
    model.add(Conv2D(num_filters, filter_size[0], input_shape=(image_size, image_size, 3), data_format="channels_last"))
    if batch_norm:
        model.add(BatchNormalization())
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    num_filters = int(num_filters * filter_multiplier)
        
 
#*************************************************************LAYER 2**********************************************************************************       
        
    model.add(Conv2D(num_filters, filter_size[1]))
    if batch_norm:
        model.add(BatchNormalization())
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    num_filters = int(num_filters * filter_multiplier)


#*************************************************************LAYER 3**********************************************************************************
    model.add(Conv2D(num_filters, filter_size[2]))
    if batch_norm:
        model.add(BatchNormalization())
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    num_filters = int(num_filters * filter_multiplier)

#*************************************************************LAYER 4**********************************************************************************
    model.add(Conv2D(num_filters, filter_size[3]))
    if batch_norm:
        model.add(BatchNormalization())
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    num_filters = int(num_filters * filter_multiplier)
    

#*************************************************************LAYER 5**********************************************************************************
    model.add(Conv2D(num_filters, filter_size[4]))
    if batch_norm:
        model.add(BatchNormalization())
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Flatten())
    model.add(Dense(dense_size))
    model.add(Dropout(dropout))
    model.add(Activation("relu"))
    model.add(Dense(num_classes))
    model.add(Activation("softmax"))

    return model
## Prepare the dataset for training
def dataset_Training(Dataset_loc="inaturalist_12K", augment_data=False):
    Directory_train= os.path.join(Dataset_loc, "train")
    Directory_test= os.path.join(Dataset_loc, "val")

    if augment_data:
        generator_train=ImageDataGenerator(rescale=1./255,rotation_range=90,zoom_range=0.2,shear_range=0.2,validation_split=0.1,horizontal_flip=True)
    else:
        generator_train=ImageDataGenerator(rescale=1./255, validation_split=0.1)
       
    generator_test = ImageDataGenerator(rescale=1./255)
    train_generate = generator_train.flow_from_directory(Directory_train, target_size=(200, 200), batch_size=32, subset="training",shuffle=True,seed=8700)
    val_generate = generator_train.flow_from_directory(Directory_train, target_size=(200, 200), batch_size=32, subset="validation",shuffle=True,seed=8700)
    test_generate = generator_test.flow_from_directory(Directory_test, target_size=(200, 200), batch_size=32)
    
    return train_generate, val_generate, test_generate;

#Visualise feature maps from the first Conv layer for a test image
def plot_filters(model, test_data, sample_num):
    sub_model = Model(inputs=model.inputs, outputs=model.layers[1].output)
    plt.imshow(test_data[0][0][sample_num])
    plt.axis('off')
    feature_maps = sub_model(test_data[0][0])
    fig, ax = plt.subplots(4, 8, figsize=(12,6))
    for i in range(feature_maps.shape[-1]):
        ax[int(i/8), i%8].imshow(feature_maps[sample_num, :, :, i], cmap='gray')
        ax[int(i/8), i%8].axis('off')
#Display sample test images with their predictions and labels
def plot_test_results(test_data, predictions, labels):
    fig, ax = plt.subplots(nrows=5, ncols=6, figsize=(15,15))
    output_map = {0: 'Amphibia', 1: 'Animalia', 2: 'Arachnida', 3: 'Aves', 4: 'Fungi', 
                  5: 'Insecta', 6: 'Mammalia', 7: 'Mollusca', 8: 'Plantae', 9: 'Reptilia'}
    for i in range(30):
        img = test_data[0][0][i]
        ax[int(i/6), i%6].imshow(img)
        ax[int(i/6), i%6].axis('off')
        ax[int(i/6), i%6].set_aspect('equal')
        ax[int(i/6), i%6].set_title("Predicted: " + output_map[np.argmax(predictions, axis=1)[i]] + "\nLabel: " + output_map[np.argmax(labels, axis=1)[i]])

from sys import argv

if __name__ == "__main__":

    if(len(argv) !=9):
        print("Invalid num of parameters passed ")
        exit()
    filter_multiple=int(argv[1])
    num_filter=int(argv[2])
    dropout=float(argv[3])
    dense_size=int(argv[4])
    if argv[5] == "True":
      batch_normalisation = True
    else:
      batch_normalisation=False
    if argv[6]=="True":
      augment_data=True
    else:
      augment_data=False

    epochs = int(argv[7])
    lr = float(argv[8])
    train_generator, val_generator, test_generator = dataset_Training(augment_data=augment_data)
    model = convolutional_neural_network_CNN(filter_multiplier=filter_multiple,num_filters=num_filter,dropout=dropout,dense_size=dense_size, batch_norm=batch_normalisation)
    model.compile(optimizer=keras.optimizers.Adamax(lr), loss="categorical_crossentropy", metrics="categorical_accuracy")
    model.fit(train_generator, epochs=epochs, validation_data=val_generator)

    print("Evaluating Our Model:")
    y=model.evaluate(test_generator, batch_size=32)
    print(y)
    predictions = model(test_generator[0][0])
    plot_test_results(test_generator, predictions, test_generator[0][1])
    sample_num =16
    plot_filters(model, test_generator, sample_num)
    #wandb.log({"Test_accuracy":y[1]})
    model.save("Best_model.h5")

    """
    README Part-A - Q1 --------------------------------------------------------------------
        
      To compile the file with command line arguments write in following format in terminal :-

    !python3 filename filter_multiplier,num_filters dropout dense_size  batch_normalisation
    Example:
     !python3 q1.py 2 32 0.27 1331 True True 1 0.0007

    
    """