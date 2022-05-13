import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image


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


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def predict(img):
    model = keras.models.load_model(os.path.join("app", "static", "my_model_2.h5"))
    img = tf.keras.utils.load_img(img, target_size=(80, 80))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names = ['AllerDisplay', 'Aller_Bd', 'Aller_BdIt', 'Aller_It', 'Aller_Lt', 
    'Aller_LtIt', 'Aller_Rg', 'Amatic-Bold', 'AmaticSC-Regular', 'BEBAS___', 
    'Capture_it', 'Capture_it_2', 'CaviarDreams', 'CaviarDreams_BoldItalic', 
    'CaviarDreams_Italic', 'Caviar_Dreams_Bold', 'DroidSans', 'DroidSans-Bold',
    'FFF_Tusj', 'Lato-Black', 'Lato-BlackItalic', 'Lato-Bold', 'Lato-BoldItalic',
    'Lato-Hairline', 'Lato-HairlineItalic', 'Lato-Heavy', 'Lato-HeavyItalic', 
    'Lato-Italic', 'Lato-Light', 'Lato-LightItalic', 'Lato-Medium', 
    'Lato-MediumItalic', 'Lato-Regular', 'Lato-Semibold', 'Lato-SemiboldItalic',
    'Lato-Thin', 'Lato-ThinItalic', 'OpenSans-Bold', 'OpenSans-BoldItalic', 
    'OpenSans-ExtraBold', 'OpenSans-ExtraBoldItalic', 'OpenSans-Italic', 
    'OpenSans-Light', 'OpenSans-LightItalic', 'OpenSans-Regular', 
    'OpenSans-Semibold', 'OpenSans-SemiboldItalic', 'Pacifico', 'Raleway-Black', 
    'Raleway-BlackItalic', 'Raleway-Bold', 'Raleway-BoldItalic', 
    'Raleway-ExtraBold', 'Raleway-ExtraBoldItalic', 'Raleway-ExtraLight', 
    'Raleway-ExtraLightItalic', 'Raleway-Italic', 'Raleway-Light', 
    'Raleway-LightItalic', 'Raleway-Medium', 'Raleway-MediumItalic', 
    'Raleway-Regular', 'Raleway-SemiBold', 'Raleway-SemiBoldItalic', 
    'Raleway-Thin', 'Raleway-ThinItalic', 'Roboto-Black', 'Roboto-BlackItalic', 
    'Roboto-Bold', 'Roboto-BoldItalic', 'Roboto-Italic', 'Roboto-Light', 
    'Roboto-LightItalic', 'Roboto-Medium', 'Roboto-MediumItalic', 'Roboto-Regular', 
    'Roboto-Thin', 'Roboto-ThinItalic', 'RobotoCondensed-Bold', 
    'RobotoCondensed-BoldItalic', 'RobotoCondensed-Italic', 'RobotoCondensed-Light', 
    'RobotoCondensed-LightItalic', 'RobotoCondensed-Regular', 'SEASRN__', 
    'Sansation-Bold', 'Sansation-BoldItalic', 'Sansation-Italic', 'Sansation-Light', 
    'Sansation-LightItalic', 'Sansation-Regular', 'Walkway_Black', 'Walkway_Bold', 
    'Walkway_Oblique', 'Walkway_Oblique_Black', 'Walkway_Oblique_Bold', 
    'Walkway_Oblique_SemiBold', 'Walkway_Oblique_UltraBold', 'Walkway_SemiBold', 
    'Walkway_UltraBold']
    
    print(
        f"This image most likely belongs to {class_names[np.argmax(score)]} with a {100 * np.max(score):.2f} percent confidence."
    )