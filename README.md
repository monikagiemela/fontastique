# ![Fontastique logo](/app/static/favicon.ico "Fontastique logo")  FONTASTIQUE | AI POWERED FONT RECOGNITION APP

A web app for font recognition with Tensolflow trained AI model, Flask server-side,
and Javascript front-end combining Dropzone.js, Croppie.js, Bootstrap framework and personalised CSS.

## Project Description

This project is a convolutional neural network trained to classify and recognize
different categories of fonts. I used a dataset of 100 types of fonts to train my model.
Project is implemented in Python with Tensorflow.
The project is broken down into multiple steps:
- Generating training, validation and testing dataset of fonts from the TRDG package
- Loading and preprocessing datasets
- Visualization of samples from the dataset
- Training the Convolutional Neural Network on a dataset
- Testing the model on 5500 images (testing showed over 90% accuracy of the final model)
- Creating a web application with Flask framework
- Using the trained model to predict fonts from new images

## Dataset Description

Dataset for this project was prepared with Text Recognition Data Generator 
[TRDG](https://textrecognitiondatagenerator.readthedocs.io/en/latest/index.html) 
package created by Edouard Belval. This package is a synthetic data generator 
for text recognition.
The package randomly chooses words from a dictionary of a specific language and
generates an image by using font, background, and modifications (skewing, blurring, etc.) 
as specified. For the purpose of this project I modified the script of run.py 
file of the TRDG package, because the packages saves all images together to one
folder, however I needed images with the same type of font to be save on designated
directories titled with a font name. I prepared my dataset of images by runing 
the TRDG package several times in CLI setting different parameters every time 
to create some distortion in the dataset.

All the resulting images were pre-processed by cropping them to 105x105 pixels.
Cropping was done during dataset loading with Tensorflow Keras.


## Files Description

- **training > data_denerator** contains modified Text Recognition Data Generator package.
- **training > FontClassificationModel.py** contains images preprocessing, detasets loading, 
Tensorflow Keras Sequential model.
- **training > model_testing > Classification_report.ipynb** contains Jupyter 
notebook with script that predicts on the 5500 images and creates a 
Scikit-learn classification report.
- **training > model_testing.ipynb** contains Jupyter notebook with script that 
predicts on a single picture.
- **app** folder contains scripts for Flask application

## Installation

- Packages required by model training: Tensorflow, Numpy, Pandas, Scikit-learn, Pillow, and tqdm. 
- Packages required bt the app: Flask, Flask-Session, Werkzeug, 

## GPU/CPU Usage

- **FontClassificationModel.py** script uses GPU for model training.
- **app** scripts use CPU for single image prediction.