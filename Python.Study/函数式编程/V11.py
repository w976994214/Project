"""
当用户输入文件名和行数的时候,用户随意输入需要显示的行数
2:3
:3
:
使用以上表示其实行数
"""

file_name = input("请输入文件名：")
line_num = input("请输入文件起始行号")


def print_line(file_name, line_num):
    f = open(file_name)

    begin, end = line_num.split(":")

    if begin == "":
        begin = "1"
    if end == "":
        end = "-1"

    begin = int(begin) - 1
    end = int(end)

    lines = end - begin

    # 消耗掉begin之前的行数

    for i in range(begin):
        f.readline()

    if lines < 0:
        print(f.read)
    else:
        for j in range(lines):
            print(f.readline())

    f.close()

print_line(file_name,line_num)
