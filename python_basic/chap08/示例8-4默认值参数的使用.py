def happy_birthday(name='wjs', age=18):
    print('祝' + name + '生日快乐!')
    print(str(age) + '岁生日快乐!')


# 调用
happy_birthday()  # 不用传参

happy_birthday('wsj')  # 位置传参
happy_birthday(age=25)

# 19传给了name
# happy_birthday(25)  # TypeError: can only concatenate str (not "int") to str
