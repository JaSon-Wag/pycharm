for i in 'hello':
    print(i)
for i in range(1, 11):  # range-> [1,11)
    # print(i)
    if i % 2 == 0:
        print(i, '是偶数')
s = 0
for i in range(1, 11):
    s += i
print('1到10之间的累加和为:', s)

print('-' * 10, '100到999之间的水仙花树', '-' * 10)
# 153 = 3*3*3+5*5*5+1*1*1
for i in range(100, 1000):
    sd = i % 10  # 获取个位数上的数字 153%10-->3
    tens = i // 10 % 10  # 获取十位上的数字 153//10-->15%10-->5
    hundred = i // 100  # 获取百位上的 153//100-->1
    if sd ** 3 + tens ** 3 + hundred ** 3 == i:
        print(i)
