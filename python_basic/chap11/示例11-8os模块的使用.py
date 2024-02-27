import os

print('当前的工作路径:', os.getcwd())

lst = os.listdir()
print('当前路径下的所有目录及文件:', lst)
print('指定路径下所有目录及文件:', os.listdir(r'E:\workspace\pycharm\python_basic'))  # r取消转义字符

# 创建目录
# os.mkdir('好好学习')  # FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '好好学习'
# os.makedirs('./aa/bb/cc')
# 删除目录
# os.rmdir('./好好学习')  # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: './好好学习'
# os.removedirs('./aa/bb/cc')

# 改变当前的工作路径
os.chdir('E:\workspace\pycharm\python_basic')  # 再写代码，工作路径就是E:\workspace\pycharm\python_basic
print('当前的工作路径:', os.getcwd())

#遍历目录树
for dirs,dirlst,filelst in os.walk('E:\workspace\pycharm\python_basic'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('-'*50)
