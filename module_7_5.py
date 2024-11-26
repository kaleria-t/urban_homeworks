import os
import time
from time import localtime

#directory = '.'
directory = os.getcwd()
for root, dirs, files in os.walk(directory):

    for file in files:

        filepath = os.path.join(root, file)

        filetime_os = os.path.getmtime(filepath)
        filetime_time = time.strftime('%d.%m.%Y', time.localtime(filetime_os))

        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        
        print(f'Файл: {file}, путь: {filepath}, размер: {filesize} байт, '
              f'время изменения: {filetime_time}, родительская директория: {parent_dir}')
