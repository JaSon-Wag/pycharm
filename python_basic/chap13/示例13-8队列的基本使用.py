from multiprocessing import Queue

if __name__ == '__main__':
    # 创建一个队列
    q = Queue(3)  # 最多可以接收3条信息
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    # 向队列中添加消息
    q.put('hello')
    q.put('world')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    q.put('python')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    print('队列中信息的个数:', q.qsize())

    # 出队
    print(q.get())
    print('队列中信息的个数:', q.qsize())
    # 入队
    q.put_nowait('html')
    # q.put_nowait('sql')  # queue.Full
    # q.put('sql')  # 堆满之后入队不报错，会一直等待，等到队列中有空位置

    # 遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())  # nowait()不等待
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    print('队列中信息的个数:', q.qsize())
