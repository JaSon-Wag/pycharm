s = 'helloWorld'
# in 的使用
print('e在helloWorld中存在嘛?', ('e' in s))
print('v在helloWorld中存在嘛?', ('v' in s))

# not in 的使用
print('e在helloWorld中不存在嘛?', ('e' not in s))
print('v在helloWorld中不存在嘛?', ('v' not in s))

# 序列的内置函数的使用
print('len()', len(s))
print('max()', max(s))
print('min()', min(s))

# 序列对象的方法，使用序列的名称，打点调用
print('s.index()', s.index('o'))  # o在s中第一次出现的索引的位置
print('s.count()', s.count('o'))  # o在s中出现的次数
