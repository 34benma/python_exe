import os
import shutil


def scan_file(path):
    files = os.listdir(path)
    for f in files:
        if f.endswith('.zip'):
            return f


def unzip_it(file):
    folder_name = file.split('.')[0]
    target_path = './' + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(file, target_path)


def del_it(file):
    os.remove(file)


while True:
    zip_file = scan_file()
    if zip_file:
        unzip_it(zip_file)
        del_it(zip_file)

