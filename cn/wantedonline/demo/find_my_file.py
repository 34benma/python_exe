import os

path = '/Users/wangcheng/Documents/Arduino/libraries'
files = os.listdir(path)

for f in files:
    if 'read' in f and f.endswith('.txt'):
        print('Found it: ' + f)
