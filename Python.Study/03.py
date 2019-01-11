import random
'''
输入一个三位数与程序随机数比较大小
1.如果大于程序随机数，则分别输出这三个数的个位十位百位
2.如果等于程序随机数，则提示中奖，中100分
3.如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字）
'''

num = input("请输入一个三位数字")

random_num = random.randrange(100, 1000)

def line():
    str_num = ''
    for i in range(4):
        num = random.randrange(97, 123)
        str_s = chr(num)
        str_num = str_num + str_s
    for i in range(8):
        num = random.randrange(10)
        str_num = str_num + str(num)
    return(str_num)

if num.isdigit() and 100 <= int(num) <= 999:
    num = int(num)
    if num > random_num :
        tmp = list(str(num))
        print(tmp[0])
        print(tmp[1])
        print(tmp[2])
    elif num == random_num:
        print("你中奖了，加100分")
    else:
        for i in range(10):
            str_line = line()
            with open("str_num.txt", "a") as f:
                f.write(str_line + '\n')
else:
    print("请按照规定输入")