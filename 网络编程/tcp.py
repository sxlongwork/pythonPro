import socket


def main():

    server_ip = input("请输入tcp服务端ip:")
    server_port = int(input("请输入tcp服务端port:"))

    while True:

        # 1.创建套接字
        tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2.连接tcp服务器   socket.connect(ip, port)
        tcp_client_sock.connect((server_ip, server_port))

        # 3.发送数据,
        send_data = input("请输入要发送的数据:")
        tcp_client_sock.send(send_data.encode('gbk'))

        # 4.关闭套接字
        tcp_client_sock.close()


if __name__ == '__main__':
    main()

"""
tcp客户端创建流程
1.创建套接字
2.连接tcp服务器(ip, port)
3.发送数据
4.关闭套接字


"""