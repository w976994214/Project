"""
假设，用一组tuple来表示学生的名字和成i，L=[("Bob", 75), ("Adan", 92), ("Bart", 92), ("Linda", 22)]，用sorted()对上述列表按照名字排序
利用lambda函数
"""
L = [("Bob", 75), ("Adan", 92), ("Bart", 92), ("Linda", 22)]

L2 = sorted(L, key=lambda x: sorted(x[0], key=str.lower))
print(L2)

L3 = sorted(L, key=lambda x: x[1], reverse=True)
print(L3)