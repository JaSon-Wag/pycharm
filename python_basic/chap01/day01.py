# coding=utf-8
print('Hello Python!')

# 函数print使用
a = 100
b = 50

print(90)
print(a)
print(a*b)

print('北京欢迎你！')
print("北京欢迎你！")
print('''北京欢迎你！''')
print("""北京欢迎你！""")

# 不换行输出
print(a,b,'dfdafadf')

# ASCII码输出
print('b')
print(chr(98))
print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))

# Unicode码输出
print(ord('北'))
print(chr(21271))
print(ord('京'))
print(chr(20140))

# 输出到文件
fp = open('note.txt', 'w')
print('北京欢迎你', file=fp)
fp.close()

# 多条print语句一行输出 end默认'\n'换行
print('Beijing', end='-->')
print('欢迎你')

# 连接符+
print('北京欢迎你' + '2023')

# 输入函数input 获取的都是字符串类型
# x=input('提示语句')
name = input('请输入您的姓名:')
print('我的姓名是:' + name)

# 输入获取的字符型转换为int型
age = input('请输入您的年龄:')
print('我的年龄是:' + age)
# 内置函数转化为int型
age = int(age)
print('我的年龄是:', age)

# 单行注释
# 要求从键盘输入出生年份，要求是4位的年份，举例：1990
year = input('请输入您的出生年份:')

year = input('请输入您的出生年份:')  # 要求从键盘输入出生年份，要求是4位的年份，举例：1990

# 多行注释
'''
版权所有：
文件名：
创建人：
'''

# 中文声明注释，一定要写在第一行，见第一行 coding=utf-8

# 代码缩进
# 类的定义
class Student:
    pass

# 函数的定义
def fun():
    pass

