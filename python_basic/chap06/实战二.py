s = 'HelloPython,HelloJava,Hellophp'
world = input('请输入要统计的数据:')
print('{0}在{1}一共出现了{2}'.format(world, s, s.upper().count(world)))
