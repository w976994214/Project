"""
统计当前目录下每个文件类型和文件数量

思路
打开当前文件夹
获取当前文件夹下所有文件
处理当前文件夹下可能有文件夹的情况
统计
"""

import os

# 获取当前文件夹下面所有文件
all_files = os.listdir(os.curdir)  # os.curdit表示当前目录
type_dict = dict()

for each_file in all_files:
    # 如果说我们的each_file是文件夹
    if os.path.isdir(each_file):
        type_dict.setdefault("文件夹", 0)
        type_dict["文件夹"] += 1
    else:
        # 如果不是文件夹而是文件，统计我们的文件
        ext = os.path.splitext(each_file)[1] # 获取文件夹的后缀
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict:
    print("该文件夹下面有类型为{}的文件{}个".format(each_type, type_dict[each_type]))