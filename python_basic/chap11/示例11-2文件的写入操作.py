def my_write(s):
    # (1)(创建)打开文件
    file = open('b.txt', 'a', encoding='utf-8')
    # (2)写入内容
    file.write(s)
    file.write('\n')
    # (3)关闭文件
    file.close()


def my_write_lst(file, lst):
    # (1)(创建)打开文件
    f = open(file, 'a', encoding='utf-8')
    # (2)操作文件
    f.writelines(lst)
    # (3)关闭
    f.close()


if __name__ == '__main__':
    # my_write('伟大的中国梦')
    # my_write('北京欢迎您')

    # 准备数据
    lst = ['姓名\t', '年龄\t', '成绩\n', '张三\t', '30\t', '98\t']
    my_write_lst('c.txt', lst)
