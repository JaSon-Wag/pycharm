lst = ['hello', 'world', 'python']
print('原列表', lst, id(lst))

# 增加元素
print('-' * 10, '增加元素', '-' * 10)
lst.append('sql')
print('增加元素之后:', lst, id(lst))

# 使用insert(index,x)在指定的index位置上插入元素x
print('-' * 10, '使用insert', '-' * 10)
lst.insert(1, 100)
print(lst)

# 列表元素的删除操作
print('-' * 10, '列表元素的删除操作', '-' * 10)
lst.remove('world')
print('删除元素之后的列表:', lst, id(lst))

# 使用pop(index)根据索引将元素取出，然后再删除
print('-' * 10, '使用pop', '-' * 10)
print(lst.pop(1))
print(lst)

# 列表的修改
print('-' * 10, '列表的修改', '-' * 10)
lst[1] = 'mysql'
print(lst)

# 列表的拷贝，将生成一个新的列表对象
print('-' * 10, '列表的拷贝', '-' * 10)
new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))

# 列表的反向
print('-' * 10, '列表的反向', '-' * 10)
lst.reverse()  # 在原列表上进行
print(lst)

# 清除列表中所有的元素clear()
print('-' * 10, '清除列表中所有的元素clear', '-' * 10)
lst.clear()
print(lst, id(lst))
