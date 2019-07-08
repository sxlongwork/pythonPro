import socket

def main():

    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    localaddr = ('', 3054)
    udp_sock.bind(localaddr)

    while True:
        data = udp_sock.recvfrom(1024)
        print(data[0].decode('gbk'))


    udp_sock.close()


if __name__ == '__main__':
    main()
'''
1.创捷套接字
2.接收数据
localaddr = ('', 3055)
bind(localaddr)     # 绑定一个端口，当发送方给我发消息时就可以使用固定的端口
recv_data = recvfrom(1024)  # 接收1024个字节
recv_data是一个元组，第一个元素时发送过来的消息(字节)，需要decode('xx')转换显示，第二个元素时一个元组，包含发送方ip和port
3.关闭套接字
close()
'''