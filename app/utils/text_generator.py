import os

from trdg.generators import GeneratorFromStrings

from PIL import Image 
import PIL 


def text_generator(text="This is Fontastique!"):
    generator = GeneratorFromStrings([text], )

    for img in generator:
        img.save(os.path.join("app", "static", "generated_text", 'text'), "JPEG")