import re
p = re.compile(r'(\w+) (\w+)')

s = 'hello 123 wang 456 lalala. i love you'

rst = p.sub(r'Hello world', s)
print(rst)