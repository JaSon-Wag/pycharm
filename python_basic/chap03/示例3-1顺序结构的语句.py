# 赋值运算符的顺序 从右到左
name = '张三'
age = 20
a = b = c = 100
a, b, c, d = 'room'  # 分解赋值
print(a)
print(b)
print(c)
print(d)

print('--------------输入输出 顺序结构-----------------')
name = input('请输入您的姓名:')
age = eval(input('请输入您的年龄:'))
luck_number = eval((input('请输入您的幸运数字:')))
print('姓名:', name)
print('年龄', age)
print('幸运数字', luck_number)