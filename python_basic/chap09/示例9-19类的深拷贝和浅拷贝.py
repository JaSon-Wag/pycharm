class CPU():
    pass


class Disk():
    pass


class Computer():
    def __init__(self, cpu, disk):
        # 计算机由CPU和硬盘
        self.cpu = cpu
        self.disk = disk


# 创建cpu和disk对象
cpu = CPU()
disk = Disk()
# 创建一个计算机对象
com = Computer(cpu, disk)
# 变量(对象)的赋值
com1 = com
print(com, '子对象的内存地址:', com.cpu, com.disk)
print(com1, '子对象的内存地址:', com1.cpu, com1.disk)

# 类对象的浅拷贝
import copy

com2 = copy.copy(com)  # com2是新产生的对象，com2的子对象，cpu，disk不变
print(com, '子对象的内存地址:', com.cpu, com.disk)
print(com2, '子对象的内存地址:', com2.cpu, com2.disk)

# 类对象的深拷贝
com3 = copy.deepcopy(com)  # com3是新产生的对象，com3的子对象，cpu，disk也会重新创建
print(com, '子对象的内存地址:', com.cpu, com.disk)
print(com3, '子对象的内存地址:', com3.cpu, com3.disk)