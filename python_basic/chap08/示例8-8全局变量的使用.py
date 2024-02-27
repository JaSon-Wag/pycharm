a = 100  # 全局变量


def calc(x, y):
    return a + x + y


print(a)
print(calc(10, 20))  # 130
print('-' * 50)


def calc2(x, y):
    a = 200  # 局部变量，局部变量的名称和全局变量的名称相同
    return a + x + y


print(calc2(10, 20))  # 230
print(a)

print('-' * 50)


def calc3(x, y):
    global s  # s是在函数中定义的变量，但是使用了global关键字声明，这个变量s变成了全局变量
    s = 300
    return s + x + y


print(calc3(10, 20))
print(s)
