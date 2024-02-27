def happy_birthday(name, age):
    print('祝' + name + '生日快乐!')
    print(str(age) + '岁生日快乐!')


# 关键字传参
happy_birthday(age=18, name='wjs')
# happy_birthday(age=18, name1='wjs')  # TypeError: happy_birthday() got an unexpected keyword argument 'name1'

# 同时使用位置传参和关键字传参
happy_birthday('wjs', age=18)

# 位置传参应该在关键字传参之前
# happy_birthday(name='wjs', 18)  # SyntaxError: positional argument follows keyword argument
