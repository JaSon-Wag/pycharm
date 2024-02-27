# format
print(format(3.14, '20'))  # 数字型默认右对齐
print(format('hello', '20'))  # 字符串默认左对齐
print(format('hello', '*<20'))  # <左对齐，*表示的填充符，20表示显示的宽度
print(format('hello', '*>20'))  # <右对齐，*表示的填充符，20表示显示的宽度
print(format('hello', '*^20'))  # <居中对齐，*表示的填充符，20表示显示的宽度

print(format(3.1415926, '.2f'))  # 3.14
print(format(20, 'b'))  # 二进制
print(format(20, 'o'))  # 八进制
print(format(20, 'X'))  # 十六进制
print(format(20, 'x'))  # 十六进制

print('-' * 50)
print(len('helloworld'))
print(len([10, 20, 30, 40, 50]))

print('-' * 50)
print(id(10))
print(id('helloworld'))
print(type('hello'), type(10))

print(eval('10+30'))
print(eval('10>30'))
