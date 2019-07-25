"""
回数：从左向右或从右向左读都是一样的数，例如12321，999。使用filter()函数
利用lambda函数
"""
ls = range(1000)
output = filter(lambda x: str(x)[0] == str(x)[len(str(x))-1], ls)

print(list(output))
 
