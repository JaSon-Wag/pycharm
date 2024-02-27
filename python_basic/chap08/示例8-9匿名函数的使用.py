def calc(a, b):
    return a + b


print(calc(10, 20))

# 匿名函数
s = lambda a, b: a + b  # s表示一个匿名函数
print(type(s))
print(s(10, 20))

#
print('-' * 50)
lst = [10, 20, 30, 40]
for i in range(len(lst)):
    print(lst[i])
print()

print('-' * 50)
for i in range(len(lst)):
    result = lambda x: x[i]  # 根据索引取值
    print(result(lst))  # lst是实际参数

#
print('-' * 50)
student_scores = [
    {'name': '陈美美', 'score': 98},
    {'name': '王一一', 'score': 95},
    {'name': '张天乐', 'score': 100},
    {'name': '白雪儿', 'score': 65}
]
# 对列表进行排序，按字典中的成绩排序
student_scores.sort(key=lambda x: x.get('score'), reverse=True)
print(student_scores)
