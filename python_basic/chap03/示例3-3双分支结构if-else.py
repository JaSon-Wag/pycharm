number = eval(input('请输入您的6位中奖号码:'))

if number == 987654:
    print('恭喜，你中奖了！')
else:
    print('你未中本期大奖！')

print('-'*10, '以上代码可以使用条件表达式进行简化', '-'*10)
result = '恭喜，你中奖了！' if number == 987654 else '您未中本期大奖！'
print(result)
print('恭喜，你中奖了！' if number == 987654 else '您未中本期大奖！')

