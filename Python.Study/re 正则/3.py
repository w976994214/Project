import re
p = re.compile(r'\d+')

m = p.search('one12twothree33456four78')
print(m.group())

rst = p.findall('one12twothree33456four78')
print(type(rst))
print(rst)