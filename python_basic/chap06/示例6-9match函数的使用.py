import re  # 导入

patter = '\d\.\d+'  # +限定符，\d 0-9数字出现一次或多次
s = 'I study Python 3.8 every day'  # 待匹配字符串
match = re.match(patter, s, re.I)
print(match)  # None
s2 = '3.9Python I study every day'
match2 = re.match(patter, s2, )
print(match2)  # <re.Match object; span=(0, 3), match='3.9'>

print('匹配值的起始位置:', match2.start())
print('匹配值的结束位置:', match2.end())
print('匹配区间的位置元素:', match2.span())
print('待匹配的字符串:', match2.string)
print('匹配的数据:', match2.group())
