d = {1001: '李梅', 1002: '王华', 1003: '张峰'}
print(d)

# 向字典中添加元素
d[1004] = '张丽丽'  # 直接使用赋值运算符向字典中添加元素
print(d)

# 获取字典中所有的key
keys = d.keys()
print(keys)  # dict_keys([1001, 1002, 1003, 1004])

print(list(keys))
print(tuple(keys))

# 将字典中的数据转成key-value的形式，以元组的方式展现
lst = list(d.items())
print(lst)

d = dict(lst)
print(d)

# 使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008, '不存在'))

# 随机删除
print(d.popitem())
print(d)

# 清空字典中所有的元素
d.clear()
print(d)

print(bool(d))  # 空字典的bool值为False
