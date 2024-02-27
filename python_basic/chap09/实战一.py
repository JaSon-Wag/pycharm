class Circle:
    def __init__(self, r):
        self.r = r

    # 计算面积的方法
    def get_area(self):
        return 3.14 * pow(self.r, 2)

    # 计算周长的方法
    def get_perimeter(self):
        return 3.14 * 2 * self.r


r = eval(input('请输入圆的半径:'))
# 创建对象
cir = Circle(r)
area = cir.get_area()  # 调用计算面积的方法
print('圆的面积为:', area)
perimeter = cir.get_perimeter()  # 调用计算周长的方法
print('圆的周长为', perimeter)
