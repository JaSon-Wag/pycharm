# (1)创建字典
d = {10: 'cat', 20: 'dog', 30: 'pet', 20: 'zoo'}
print(d)  # key值相同时，value的值进行了覆盖

# (2)zip函数创建
lst1 = [10, 20, 30, 40]
lst2 = ['cat', 'dog', 'pet', 'zoo', 'car']
zipObj = zip(lst1, lst2)
print(zipObj)  # <zip object at 0x0000021B4BB87E00>
d = dict(zipObj)
print(d)  # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d = dict(cat=10, dog=20)
print(d)

t = (10, 20, 30)
print({t: 10})  # t是key，10是value，元组是可以作为字典中的key

# lst = [10, 20, 30]
# print({lst: 10})  # TypeError: unhashable type: 'list'

# 字典属于序列
print('最大值:', max(d))
print('最小值:', min(d))
print('len:', len(d))

# 字典的删除
del d
