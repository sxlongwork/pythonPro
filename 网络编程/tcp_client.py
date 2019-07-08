import socket


def main():

    # 1.创建套接字
    tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.建立连接
    server_ip = input("请输入tcp server的ip:")
    server_port = int(input("请输入tcp server的port:"))
    addr = (server_ip, server_port)
    tcp_client_sock.connect(addr)

    # 3.发送数据
    send_data = input("请输入你要发送的数据:")
    tcp_client_sock.send(send_data.encode('gbk'))

    # 4.关闭套接字
    tcp_client_sock.close()


if __name__ =='__main__':
    main()
