lst = [4, 56, 3, 78, 40, 56, 89]
print('原列表:', lst)

# 排序
asc_lst = sorted(lst)
print('升序:', asc_lst)
print('原列表:', lst)

# 降序
desc_lst = sorted(lst, reverse=True)
print('降序:', desc_lst)
print('原列表:', lst)

print('-------------------------------------')
lst2 = ['banana', 'apple', 'Cat', 'Orange']
print('原列表:', lst2)

# 升序
new_lst2 = sorted(lst2, key=str.lower)
print('升序', new_lst2)  # 忽略大小写
print('原列表:', lst2)
