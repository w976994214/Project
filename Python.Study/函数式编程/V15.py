"""
用户输入文件名以及开始搜索的路径，搜索该文件是否存在，如果遇到文件夹则进入文件夹继续搜索

思路
接收用户输入的文件名和搜索路径
判断是不是文件夹，进入该文件夹继续搜索，循环调用函数实现
"""

import os

start_dir = input("请输入开始目录")
target = input("请输入要查找的文件名")


def search_file(start_dir, target):
    os.chdir(start_dir)  # 进入要查找的目录

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + "\\" + each_file)
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)


search_file(start_dir, target)
