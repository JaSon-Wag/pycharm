import re  # 导入

patter = '\d\.\d+'  # +限定符，\d 0-9数字出现一次或多次
s = 'I study Python 3.9 every day Python2.7 I love you'  # 待匹配字符串
s2 = '4.10 Python I study every day'
s3 = 'I study Python every day'
lst = re.findall(patter, s)
lst2 = re.findall(patter, s2)
lst3 = re.findall(patter, s3)
print(lst)
print(lst2)
print(lst3)
