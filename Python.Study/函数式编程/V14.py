"""
计算当前文件夹下面所有文件的大小
打开当前文件夹
获取当前文件名称
获取文件大小
组成字典形式返回
"""

import os

all_file = os.listdir(os.curdir)

list_files = dict()

for each_file in all_file:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        list_files[each_file] = file_size

for k, v in list_files.items():
    print("文件名称为{}，大小是{}".format(k, v))
