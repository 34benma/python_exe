import os
import zipfile


def pack_files(file, zip_name):
    file = '/Users/wangcheng/Downloads/' + file
    zip = zipfile.ZipFile(zip_name, 'w')
    zip.write(file)
    zip.close()


def get_files():
    path = '/Users/wangcheng/Downloads'
    files = os.listdir(path)
    for file in files:
        if file.endswith('.png'):
            return file


if __name__ == '__main__':
    file = get_files()
    if file:
        pack_files(file, 'test.zip')