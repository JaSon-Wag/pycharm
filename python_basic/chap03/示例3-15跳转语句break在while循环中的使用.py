s = 0
i = 1
while i < 11:
    s += i
    if s > 20:
        print('累加和大于20的当前数是:', i)
        break
    i += 1

print('-' * 20)
i = 0
while i < 3:
    user_name = input('请输入用户名: ')
    pwd = input('请输入密码:')
    if user_name == 'wjs' and pwd == '123456':
        print('系统正在登陆中，请稍后...')
        break
    else:
        if i < 2:
            print('用户名或密码不正确，您还有', 2 - i, '次机会')
    i += 1
else:  # while else 流程正常结束执行
    print('三次均输入错误！')
