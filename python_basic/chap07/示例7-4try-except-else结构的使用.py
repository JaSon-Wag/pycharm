try:
    num1 = int(input('请输入一个整数:'))
    num2 = int(input('请输入另一个整数:'))
    result = num1 / num2
except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print('不能将字符串转成整数')
else:  # 程序正常执行结束，执行else语句
    print('结果:', result)
