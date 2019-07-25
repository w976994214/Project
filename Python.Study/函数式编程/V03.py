"""
假设，用一组tuple来表示学生的名字和成i，L=[("Bob", 75), ("Adan", 92), ("Bart", 92), ("Linda", 22)]，用sorted()对上述列表按照名字排序
"""
L = [("Bob", 75), ("Adan", 92), ("Bart", 92), ("Linda", 22)]


def by_name(t):
    t = sorted(t[0], key=str.lower)
    return t


L2 = sorted(L, key=by_name)
print(L2)


def by_score(n):
    n = sorted(range(n[1]), key=abs)
    return n

L3 = sorted(L, key=by_score)
print(L3)
