import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))  # 获取保留字的个数

true = '真'
# True = '真' # True是python中的保留字,报错

# 标识符 字母、下划线和数字

# 变量的定义
luck_number = 8

my_name = 'JaSonWag'  # 字符串类型的变量
print('luck_number的数据类型是：', type(luck_number))  # <class 'int'>
print(my_name, '的幸运数字是：', luck_number)

# Python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number = '北京欢迎你'
print('luck_number的数据类型是：', type(luck_number))  # <class 'str'>

# 在Python中允许多个变量指向同一个值
no = number = 1024
print(no, number)
print(id(no))  # id()查看对象的内存地址的 1683728529648
print(id(number))  # 1683728529648

# Python中常量定义
Pi = 3.1415926  # 变量
PI = 3.1415926  # 常量

# 整数类型
num = 987  # 默认是十进制，表示整数
num2 = 0b1010101  # 使用二进制表示整数
num3 = 0o765  # 使用八进制表示整数
num4 = 0x87ABF  # 使用十六进制表示整数
print(num)
print(num2)  # 85
print(num3)  # 501
print(num4)  # 555711

# 浮点类型
height = 187.6
print(height)
print(type(height))  # type()查看height这个变量的数据类型 <class 'float'>

x = 10
y = 10.0
print('x的数据类型:', type(x))  # <class 'int'>
print('y的数据类型:', type(y))  # <class 'float'>

x = 1.99E1413
print('科学计数法:', x, 'x的数据类型:', type(x))  # <class 'float'>

print(0.1 + 0.2)  # 0.30000000000000004
print(round(0.1 + 0.2, 1))  # 0.3

# 虚数的表达
x = 123+456j
print('实数部分:', x.real)  # 123.0
print('虚数部分:', x.imag)  # 456.0

# 字符串类型的使用
city = '天津'
address = "天津市宝坻区香江大街3号"
print(city)
print(address)
# 多行字符串
info = '''地址:天津市宝坻区香江大街3号
    收件人:...
    手机号:...
'''
info2 = """地址:天津市宝坻区香江大街3号
    收件人:...
    手机号:...
"""
print(info)
print('-----------------------------------')
print(info2)

# 转义字符 \n \t \' \" \\
print('北京\n欢迎你')  # \n换行
print('hellooooo')
print('hello\toooo')  # \t制表符，8个字符包括符号前面的

# 原字符，使转义字符失效的符号r或R
print(r'北\n京\n欢\n迎\n你')
print(R'北\n京\n欢\n迎\n你')

# 索引
s = 'HELLOWORLD'
print(s[0], s[-10])  # ->方向 0 1 2 ...,<-方向 -1 -2 -3
print('北京欢迎你'[4])  # 获取字符串中索引为4
print('北京欢迎你'[-1])

# 切片
print(s[2:7])  # 从2开始到7结束不包含7 正向递增
print(s[-8:-3])  # 反向递增
print(s[:5])  # 默认N从0开始
print(s[5:])  # M 默认是切到字符串的结尾

# 字符串类型的操作
x = '2022年'
y = '北京冬奥会'
print(x+y)  # 连接连个字符串
print(x*10)  # 对x这个字符串的内容复制10次
print(10*x)

print('北京' in y)  # 判断在y字符串中是否存在北京 True
print('上海' in y)  # False

# 布尔类型
x = True
print(x)
print(type(x))
print(x+10)  # 11 -->1+10
print(False+10)  # 10 -->0+10

print('-----------------------------------')
print(bool(18))  # True 非0
print(bool(0), bool(0.0))  # False False

print(bool('北京欢迎你'))  # True 非空字符串
print(bool(''))  # False
print(bool(False))  # False
print(bool(None))  # False

# 数据类型的转换
x = 10
y = 3
z = x/y
print(z, type(z))  # 隐式转换
# float类型转成int类型，只保留整数部分
print('float类型转成int类型', int(3.14))
print('float类型转成int类型', int(3.9))
print('float类型转成int类型', int(-3.14))
print('float类型转成int类型', int(-3.9))
# int类型转成float类型
print('int类型转成float类型', float(10))
# str类型转成int类型
print('str类型转成int类型', int('100')+int('200'))

# chr()\ord()
print(ord('王'))  # 王在Unicode表中对应的整数值
print(chr(29579))  # 29579整数在Unicode表中对应的字符是什么

# 进制之间的转换
print('十进制转成十六进制:', hex(29578))
print('十进制转成八进制:', oct(29578))
print('十进制转成二进制:', bin(29578))

# eval函数的使用
s = '3.14+3'
print(s, type(s))
x = eval(s)
print(x, type(x))
# eval函数经常与input函数一起使用，用于获取用户输入的数值
age = eval(input('请输入的您的年龄:'))
print(age, type(age))

height = eval(input('请输入您的身高:'))
print(height, type(height))

hello = '北京欢迎你'
print(hello)
print(eval('hello'))

# 算术运算符
print('加法:', 1+1)
print('减法:', 1-1)
print('乘法:', 2*3)
print('除法:', 10/2)
print('整除:', 10//3)
print('取余:', 10 % 3)
print('幂运算:', 2**4)  # 2*2*2*2

# 赋值运算符
x = 20
y = 10
x = x+y
print(x)  # 30
x += y  # 40
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
print(type(x))
x %= 2
print(x)
z = 3
y //= z
print(y)
y **= 2
print(y)
# 链式赋值
a = b = c = 100
print(a, b, c)
# 系列解包赋值
a, b = 10, 20
print(a, b)
print('---------------如何交换两个变量的值--------------')
a, b = b, a
print(a, b)

# 比较运算符
print('98大于90嘛？', 98 > 90)
print('98小于90嘛？', 98 < 90)
print('98等于90嘛？', 98 == 90)
print('98不等于90嘛？', 98 != 90)
print('98大于等于98嘛？', 98 >= 98)
print('98小于等于98嘛？', 98 <= 98)

# 逻辑运算符
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not False)  # True
print(not True)  # False
print(not (8 > 7))  # False

print('按位与运算:', 12 & 8)
print('按位或运算:', 4 | 8)
print('按位异或运算:', 31 ^ 32)  # 相同为1，不同为0
print('按位取反运算:', ~123)

print('左移位:', 2 << 2)  # 8 左移2位 2*2*2
print('右移位:', 8 >> 2)  # 2 右移2位 8//2//2



