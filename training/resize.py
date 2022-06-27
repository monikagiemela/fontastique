import os
from PIL import Image

def resize(folder):
    """
    Resize files recursively.
    Used with trgd (Text Generator) package.
    """
    for path, _, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(path, filename)
            img = Image.open(filepath)
            img.thumbnail((105,105))
            img.save(filepath)

resize(os.path.join("app", "static", "output"))