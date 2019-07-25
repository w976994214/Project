"""
回数：从左向右或从右向左读都是一样的数，例如12321，999。使用filter()函数
"""


def equal(a, b):
    return a == b


def is_palindrome(n):
    s = str(n)   # 转换成字符串
    for i in range(len(s)-1):
        if equal(s[i], s[len(s)-i-1]):
            continue
        else:
            return False
    return True


output = filter(is_palindrome, range(1, 10000))
print(list(output))
