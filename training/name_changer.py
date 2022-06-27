import os

def change_name(folder):
    """
    Change names of files recursively.
    Can be used with trgd (Text Generator) package to change name of files generated
    by the trdg to custom names.
    
    :param folder: path to folder that contains subfolders with files
    "
    """
    for path, _, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(path, filename)
            new_filepath = os.path.join(path, "This_is_Fontastique.jpg")
            os.rename(filepath, new_filepath)

change_name(os.path.join("app", "static", "output"))