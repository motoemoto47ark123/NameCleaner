import os

path = "replace this with the dir of the files"
for filename in os.listdir(path):
    original_name, ext = os.path.splitext(filename)
    if "Copy of " in original_name:
        new_name = original_name.replace("replace this with what you want to remove from the name of the files ", "")
        os.rename(os.path.join(path, filename), os.path.join(path, new_name + ext))
