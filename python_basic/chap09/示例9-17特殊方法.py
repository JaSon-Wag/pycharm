a = 10
b = 20
print(dir(a))
print(a + b)  # 执行加法运算
print(a.__add__(b))
print(a.__sub__(b))  # 执行减法运算
print(f'{a}<{b}吗？', a.__lt__(b))
print(f'{a}<={b}吗？', a.__le__(b))
print(f'{a}=={b}吗？', a.__eq__(b))
print(f'{a}>{b}吗？', a.__gt__(b))
print(f'{a}>={b}吗？', a.__ge__(b))
print(f'{a}!={b}吗？', a.__ne__(b))

print('-' * 50)
print(a.__mul__(b))  # 乘法
print(a.__truediv__(b))  # 除法
print(a.__mod__(b))  # 取余
print(a.__floordiv__(b))  # 整除
print(a.__pow__(2))  # 幂
