i = 0
while i < 3:
    user_name = input('请输入您的用户名:')
    pwd = input('请输入您的密码:')
    if user_name == 'wjs' and pwd == '123456':
        print('系统正在登录，请稍后！')
        i = 8
    else:
        if i < 2:
            print('用户名和密码不正确，你还有', 2 - i, '次机会!')
        i += 1
if i == 3:
    print('对不起，三次均输入错误!')
