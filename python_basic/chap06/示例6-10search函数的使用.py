import re  # 导入

patter = '\d\.\d+'  # +限定符，\d 0-9数字出现一次或多次
s = 'I study Python 3.9 every day Python2.7 I love you'  # 待匹配字符串
match = re.search(patter, s)
s2 = '4.10Python I study every day'
match2 = re.search(patter, s2)
print(match)
print(match2)

print(match.group())
print(match2.group())
