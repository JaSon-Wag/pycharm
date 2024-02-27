class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建Person类的对象
per = Person('陈梅梅', 20)  # 创建对象的时候会自动调用__init__()方法
print(per)  # 自动调用了__str__()方法
