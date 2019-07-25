import re

title = u'<div>name</div><div>age</div>'

p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())