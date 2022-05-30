import os

from flask import render_template
import imghdr

import tensorflow as tf
from tensorflow import keras
import numpy as np

from app.utils.class_names import class_names


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


model = keras.models.load_model(os.path.join("app", "static", "my_model_2_5.h5"))
def predict(filename, model=model) -> tuple:
    """Predict font"""
    img = tf.keras.utils.load_img(os.path.join("app", "static", "uploads", 
                                    filename), target_size=(105, 105))
    img_array: list = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    max_result: str = class_names[np.argmax(score)]
    print(f"This image most likely belongs to {class_names[np.argmax(score)]} \
            with a {100 * np.max(score):.2f} percent confidence.")

    ind: list = np.argpartition(score, -4)[-4:-1]
    top_three: list = []
    
    print("Top three:")
    for i in ind:
        top_three.append(class_names[i])
        print(class_names[i], score[i].numpy())    
    return (max_result, top_three)

def validate_image(stream):
    """Use file bytes to validate if the image format is the same as its extension """
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return ("." + format)