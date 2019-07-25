"""
编写一个程序，接收用户输入的内容，并保存为新的文件
如果用户单独输入:W
表示文件保存退出
"""
file_name = input("请用户输入文件名：")


def file_write(file_name):
    f = open(file_name, "w")
    print("请输入内容，:W代表结束")
    while True:
        write_something = input()
        if write_something != ":W":
            f.write("{0}\n".format(write_something))
        else:
            break
    f.close()


file_write(file_name)

