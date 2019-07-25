import re
#  I 表示忽略掉大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m = p.match("i am really love wangxiaojing")
print(m)

print(m.group(0))
print(m.start(0))
print(m.end(0))

print(m.group(1))
print(m.start(1))
print(m.end(1))

print(m.group(2))
print(m.start(2))
print(m.end(2))

print(m.groups())