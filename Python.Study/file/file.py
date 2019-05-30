# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟

# 让程序暂停，可以使用time下的sleep函数
import time

with open(r'test01.txt', 'r',encoding='UTF-8-sig') as f:
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    lines = f.readlines()  # 读取全部内容
    for line in lines:
        line = line.strip()
        print(line)
        strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep参数单位是秒
        time.sleep(1)
        strChar = f.read(3)
# 作业：
# 解释以下运行结果，为什么不是每行三个字符