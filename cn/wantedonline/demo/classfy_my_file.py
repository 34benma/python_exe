import os
import shutil

path = '/Users/wangcheng/Downloads/'
files = os.listdir(path)

for f in files:

    folder_name = f.split('.')[-1]
    if not len(folder_name):
        continue
    folder_name = path + folder_name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    shutil.move(path + f, folder_name)
