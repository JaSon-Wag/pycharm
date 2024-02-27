# 导入
import random

# 设置随机数的种子
random.seed(10)
print(random.random())
print(random.random())

print('-' * 50)
random.seed(10)
print(random.randint(1, 100))  # [1,100]

for i in range(10):  # [m,n)部长为k，m-->start-->1,n-->stop-->10,k-->step-->3
    print(random.randrange(1, 10, 3))

print(random.uniform(1, 100))  # [a,b]随机小数

lst = [i for i in range(1, 11)]
print(random.choice(lst))  # lst是列表，称为序列

#随机的排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)