s = 'HelloWorld'
s1 = s[0:5:2]  # 索引从0开始,到5结束(不包含5),步长为2
print(s1)

# 省略开始位置，start默认为0
print(s[:5:1])
# 胜利开始位置start，省略步长step
print(s[:5:])
# 省略结束位置，stop默认序列的最后一个元素
print(s[0::1])

print(s[5::])  # 省略结束和步长
print(s[5:])  # 省略结束和步长

#省略开始位置和结束位置
print(s[::2])

# 步长step负数，逆序
print(s[::-1])
print(s[-1:-11:-1])