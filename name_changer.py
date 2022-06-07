import os

def change_name(folder):
    """
    Change names of files recursively
    
    Used with trgd (Text Generator) package.
    """
    for path, _, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(path, filename)
            new_filepath = os.path.join(path, "This_is_Fontastique.jpg")
            os.rename(filepath, new_filepath)

change_name(os.path.join("app", "static", "output"))