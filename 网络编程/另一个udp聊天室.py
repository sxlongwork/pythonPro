import socket


def send_msg(send_sock, send_ip, send_port):
    """发送数据方法"""
    send_data = input("我\n")
    send_sock.sendto(send_data.encode('gbk'), (send_ip, send_port))


def recv_msg(recv_sock):
    """接收数据方法"""
    recv_data = recv_sock.recvfrom(1024)
    send_user = str(recv_data[1]) + "\n"
    print(send_user, recv_data[0].decode('gbk'))



def main():
    """聊天室主方法"""

    # 创建socket套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ('', 3055)
    udp_socket.bind(localaddr)

    send_ip = input("请输入接收方的ip:")
    send_port = int(input("请输入接收方的port:"))

    while True:
        # 接收数据
        recv_msg(udp_socket)

        # 发送数据
        send_msg(udp_socket, send_ip, send_port)



    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()