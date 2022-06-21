import os
import imghdr
import tensorflow as tf
from tensorflow import keras
import numpy as np
from app.utils.class_names import class_names
from PIL import Image

model = keras.models.load_model(os.path.join("app", "static", "top_model.h5"))

def predict(filename: str, model=model) -> tuple:
    """
    Predict font
    :param filename: name of an image file with text
    :param model: Deep Neural Network model
    :return: prediction result with the highest confidence, and top six results
    """   
    with Image.open(os.path.join("app", "static", "uploads", filename)) as im:
        im.show()
    img = tf.keras.utils.load_img(
                                os.path.join("app", "static", "uploads", filename), 
                                target_size=(105, 105))
    img_array: list = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    max_result: str = class_names[np.argmax(score, axis=-1)]
    print(f"This image most likely belongs to {max_result} \
            with a {100 * np.max(score):.2f} percent confidence.")

    ind: list = np.argpartition(score, -6)[-6:]
    top_six: list = []    
    
    print("Top three:")
    for i in ind:
        top_six.append(class_names[i])
        print(class_names[i], score[i].numpy())
    return (max_result, top_six)

def validate_image(stream) -> str:
    """Use file bytes to validate if the image format is the same as its extension """
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return ("." + format)