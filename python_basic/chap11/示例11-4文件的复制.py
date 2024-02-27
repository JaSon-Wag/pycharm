def copy(src, new_path):
    # 文件的复制就是边读边写的操作
    # (1)打开源文件
    file1 = open(src, 'rb')
    # (2)打开目标文件
    file2 = open(new_path, 'wb')
    # (3)开始复制，边读边写
    s = file1.read()  # 源文件读取所有
    file2.write(s)  # 向目标文件写入所有
    # (4)关闭
    file2.close()
    file1.close()


if __name__ == '__main__':
    src = '../chap10/Google.png'  # . 表示的是当前目录
    new_path = './copy_Google.png'  # .. 表示的是上级目录
    copy(src, new_path)
    print('文件复制完毕！')
