"""
实现全部替换的功能
打开一个文件
把文件中XXX的字符串替换成SSS
"""

file_name = input("请输入想要替换的文件名")
file_rep_word = input("请输入要替换掉的内容")
file_new_word = input("请输入想要替换成的内容")

def file_replace(file_name, file_rep_word, file_new_word):

    f = open(file_name)
    content = []
    for eachline in f:
        if file_rep_word in eachline:
            eachline = eachline.replace(file_rep_word, file_new_word)
        content.append(eachline)

    decide = input("确定替换请输入Y/N")

    if decide in ["Y", "y"]:
        f_write = open(file_name, "w")
        f_write.write("".join(content))
        f_write.close()



file_replace(file_name, file_rep_word, file_new_word)


