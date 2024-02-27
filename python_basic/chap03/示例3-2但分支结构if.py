number = eval(input('请输入您的6位中奖号码:'))
# 使用if语句
if number == 987654:
    print('恭喜，你中奖了！')

if number != 987654:
    print('你未中本期大奖！')

print('-'*40)

n = 98
if n % 2:
    print(n, '是奇数')
if not n % 2:
    print(n, '是偶数')

print('-'*20, '判断一个字符串是否是空字符串', '-'*20)
x = input('请输入一个字符串:')
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')

print('-'*20, '表达式可以是一个单纯的布尔类型变量', '-'*20)
flag = eval(input('请输入一个布尔类型的值(True/False):'))
if flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')
