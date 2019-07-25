"""
利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他字母小写的规范的名字，例如：['AMDAAA', 'MAdada','dadaad']
"""


def standards(n):
    t = n.lower()
    t = t.capitalize()
    return t


print(list(map(standards, ['AMDAAA', 'MAdada', 'dadaad'])))
