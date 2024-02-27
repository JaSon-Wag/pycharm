t = ('python', 'hello', 'world')
# 根据索引访问元组
print(t[0])

t2 = t[0:3:2]  # 切片操作
print(t2)

# 元组的遍历
for item in t:
    print(item)

# for+range()+len
for i in range(len(t)):
    print(i, t[i])

# 使用enumerate
for index, item in enumerate(t, start=1):
    print(index, item)
