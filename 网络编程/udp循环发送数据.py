import socket

def main():
    "udp socket test"

    # 创建套接字
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        # 发送数据
        # sock.sendto("bhello dear.",(ip, port))
        # sock.sendto(b"hello python", ('192.168.31.131',8080))
        send_data = input("pls input the content you want to send:")

        if send_data == 'exit':
            break

        sock.sendto(send_data.encode('utf-8'),('192.168.39.21', 8080))

    # 关闭套接字
    sock.close()


if __name__ == '__main__':
    main();

'''
1.创建套接字
AF_INET 指的是ipv4
SOCK_DGRAM 指的是UDP
2.发送数据
sendto(要发送的数据字节, (接收方ip, 接收方port))
要发送的数据组要encode('xx')编码为字节才能发送
3.关闭套接字
close()

'''