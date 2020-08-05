
import socket
import threading


def send_to_server(fd):
    # 发送消息给服务端
    while True:
        msg = input("")
        msg_send = str({"uid": 5556, "msg": msg})
        fd.send(msg_send.encode('utf-8'))


def receive_from_server(fd):
    # 接收来自服务端的消息
    while True:
        msg_recv = fd.recv(2048).decode('utf-8')
        print("msg from server : ", msg_recv)
        if not msg_recv:
            break


def start_client():
    # 创建套接字
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.bind(('127.0.0.1', 5557))

    # 连接服务端
    fd.connect(("127.0.0.1", 6670))

    threading.Thread(target=send_to_server, args=(fd,)).start()
    threading.Thread(target=receive_from_server, args=(fd,)).start()


if __name__ == '__main__':
    start_client()
