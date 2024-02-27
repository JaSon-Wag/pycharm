import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

# 设置图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)
# 准备数据
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 27, 24, 22, 18, 15]

# 绘图
plt.plot(x, y)
# 设置x轴的刻度
plt.xticks(range(2, 25, 1))
plt.yticks(range(min(y),max(y)+1))
# 保存图片
plt.savefig('./sig_size.png')

# 展示
plt.show()
