from socket import socket, AF_INET, SOCK_STREAM

# AF_INET用于Internet之间的进程通信
# SOCK_STREAM表示的是用TCP协议编程

# (1)创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)

# (2)绑定IP地址和窗口
ip = '127.0.0.1'  # 等同于local
port = 8888  # 端口的范围
server_socket.bind((ip, port))

# (3)使用listen()开始监听
server_socket.listen(5)
print('服务器已启动!')

# (4)等待客户端的连接
client_socket, client_addr = server_socket.accept()  # 系列解包赋值

# (5)接受来自客户端的数据
data = client_socket.recv(1024)
print('客户端发送过来的数据为:', data.decode('utf-8'))  # 要求客户端发送过来的数据是使用utf-8进行编码的

# (6)关闭socket
server_socket.close()

'''
import socket

# (1)创建socket对象
client_socket = socket.socket()

# (2)IP地址和窗口
ip = '127.0.0.1'  # 等同于local
port = 8888  # 端口的范围
client_socket.connect((ip, port))
print('--------与服务器连接建立成功----------')

# (3)发送数据
client_socket.send('Welcome to python world'.encode('utf-8'))

# (4)关闭
client_socket.close()
print('发送完毕')
'''
