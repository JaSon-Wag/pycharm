import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# 读取图片
n1 = plt.imread('Google.png')
print(type(n1), n1)  # 数组，三维数组，最高维度表示的是图像的高，次高纬度表示的是图像的宽度，最低维[R,G,B]颜色
plt.imshow(n1)

# 编写一个灰度的公式
n2 = np.array([0.299, 0.587, 0.114])  # 创建数组
# 将数组n1(RGB)颜色值与数组n2(灰度公式固定值)，进行点乘运算
x = np.dot(n1, n2)
# 传入数组，显示灰度
plt.imshow(x, cmap='gray')
# 显示图像
plt.show()
