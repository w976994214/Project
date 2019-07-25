"""
当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上
"""
file_name = input("请输入文件名：")
line_num = input("请输入行号")

def file_view(file_name, line_num):
    print("\n文件{0}的前{1}行内容如下".format(file_name, line_num))

    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline())

    f.close()

file_view(file_name, line_num)