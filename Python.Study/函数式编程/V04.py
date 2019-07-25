"""
利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他字母小写的规范的名字，例如：['AMDAAA', 'MAdada', 'dadaad']
利用landba函数
"""

ls = ['AMDAAA', 'MAdada', 'dadaad']

new_ls = map(lambda x: x.lower().capitalize(), ls)
print(list(new_ls))