
import socket

def main():
    '''socket udp编程'''

    # 创建套接字
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 发送数据，udp.sock(发送内容, (对方IP, 对方port))
        send_data = input("pls input content you want to send:")

        if send_data == 'exit':
            break

        udp_sock.sendto(send_data.encode('utf-8'),('192.168.31.202', 2425))


    # 关闭套接字
    udp_sock.close()









if __name__ == '__main__':
    main();