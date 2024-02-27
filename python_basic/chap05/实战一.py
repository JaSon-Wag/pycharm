# 千年虫
lst = [88, 89, 90, 98, 00, 99]  # 表示的员工的两位数出生年份
print(lst)

# 遍历列表的方式
# for index in range(len(lst)):
#     if str(lst[index]) != '0':
#         lst[index] = '19' + str(lst[index])
#     else:
#         lst[index] = '200' + str(lst[index])
# print('修改后的年份列表', lst)

# 使用enumerate()函数遍历
for index, value in enumerate(lst):
    if str(value) != '0':
        lst[index] = '19' + str(value)
    else:
        lst[index] = '200' + str(value)
print('修改后的年份列表', lst)
