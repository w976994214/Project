# 导入相关包
import re
# 查找数字
# r表示字符串不转译
p = re.compile(r'\d+')
# 在字符串one12twothree33456four78中进行查找，按照规则p指定的正则进行查找
# 参数3， 6表士在字符串中查找的范围
m = p.match('one12twothree33456four78', 3, 20)
print(m)
print(m[0])
print(m.start(0))