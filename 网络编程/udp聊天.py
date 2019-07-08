import socket


def send_msg(udp_socket, send_ip, send_port):
    """发送数据"""
    send_data = input("我\n")

    udp_socket.sendto(send_data.encode('gbk'), (send_ip, send_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print('%s\n%s' % (str(recv_data[1]), recv_data[0].decode('gbk')))


def main():
    """主方法"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ('', 3054)
    udp_socket.bind(localaddr)

    send_ip = input("请输入发送方ip:")
    send_port = int(input("请输入发送方port:"))

    while True:

        send_msg(udp_socket, send_ip, send_port)

        recv_msg(udp_socket)

    udp_socket.close()


if __name__ == '__main__':
    main()