import socket


def send_msg(udp_sock, send_ip,send_port):
    """发送消息方法
    :param udp_sock: 发送数据的套接字
    :param send_ip:  接收方的ip
    :param send_port: 接收方的port
    """
    send_data = input("请输入要发送的数据:")
    udp_sock.sendto(send_data.encode('gbk'),(send_ip ,send_port))


def recv_msg(udp_sock):
    """
    接收数据的方法
    :param udp_sock:  发送数据的套接字
    :return:
    """
    recv_data = udp_sock.recvfrom(1024)
    print(recv_data[1],recv_data[0].decode('gbk'), sep=':')


def main():
    """udp 主方法"""

    # 创建套接字
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    localaddr = ('', 3054)
    udp_sock.bind(localaddr)

    send_ip = input("请输入接收方的ip:")
    send_port = int(input("请输入接收方的port:"))

    # 循环发送数据和接收数据
    while True:

        # 发送数据
        send_msg(udp_sock, send_ip, send_port)

        # 接收数据
        recv_msg(udp_sock)


    # 关闭套接字
    udp_sock.close()


if __name__ == '__main__':
    main()