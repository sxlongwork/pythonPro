import socket


def main():

    # 1 创建套接字
    tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 绑定端口
    localaddr = ('', 8090)
    tcp_server_sock.bind(localaddr)

    # 3 开启监听
    tcp_server_sock.listen(625)

    # 4 接受连接
    new_sock, addr = tcp_server_sock.accept()

    while True:
        # 5 接收数据和发送数据
        data = new_sock.recv(1024)
        print(data.decode('gbk'))

        send_data = input("请输入要发送的数据:")
        new_sock.send(send_data.encode('gbk'))

    # 6 关闭套接字
    new_sock.close()
    tcp_server_sock.close()


if __name__ == '__main__':
    main()