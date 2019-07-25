"""
编写程序，比较用户输入的两个文件是否相同，如果不同，显示出所有不同处的行号
"""
file1 = input("请输入必要比较的第一个文件名：")
file2 = input("请输入必要比较的第二个文件名：")
open(file1, "r")
open(file2, "r")


def file_compare(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    count = 0
    differ = []

    for line1 in f1:
        line2 = f2.readline()

        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    return differ


differ = file_compare(file1, file2)

if len(differ) == 0:
    print("文件相同")
else:
    print("两个文件有{0}处不同".format(len(differ)))
    for i in differ:
        print("第{0}行不同".format(i))