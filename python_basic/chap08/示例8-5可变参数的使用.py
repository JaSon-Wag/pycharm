# 个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)


fun(10, 20, 30, 40)
fun(10)

fun([11, 22, 33, 44])  # 实际上传递的是一个参数
# 在调用时，参数前加一个*，将列表进行解包
fun(*[11, 22, 33, 44])

print('-' * 50)


# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key, '--------', value)


fun2(name='wjs', age=25, height=176)

d = {'name': 'wjs', 'age': 25, 'height': 176}
# fun2(d)  # TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)  # 解包操作
