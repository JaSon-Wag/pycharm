d = {'hello': 10, 'world': 20, 'python': 30}
# 访问字典的元素
# (1)使用d[key]
print(d['hello'])
# (2)d.get(key)
print(d.get('hello'))

# 两者之间有区别，访问字典中没有的key时(1)报错
# print(d['java'])  # KeyError: 'java'
print(d.get('java'))  # None

# 字典的遍历
for item in d.items():
    print(item)  # key和value组成的一个元素

# 使用for循环遍历时，分别获取key，value
for key, value in d.items():
    print(key, '-->', value)
