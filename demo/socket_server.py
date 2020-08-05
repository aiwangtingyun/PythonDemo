
import socket
import threading

clients = {}


def dispose_client(client_socket, address):
    while True:
        # 接收客户端消息
        msg = eval(client_socket.recv(2048).decode('utf-8'))

        # 回显消息
        print('receive ({}) msg : {}'.format(address, msg))

        # 发送消息给客户端
        send_client = clients.get(msg.get('uid', 0), 0)
        if send_client:
            send_client.send(msg.get('msg').encode('utf-8'))

        # 结束标志
        if msg.get('msg') == 'q':
            break

    # 关闭客户端的连接
    print("close client ({}, {})".format(client_socket, address))
    client_socket.close()


def start_server():
    # 创建套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定套接字
    server.bind(("127.0.0.1", 6670))
    # 监听套接字:指定最大连接数
    server.listen(100)
    # 等待客户端连接
    while True:
        client_socket, address = server.accept()

        print('new client : ', address)
        clients[address[1]] = client_socket
        print('all clients : ', clients.keys())

        threading.Thread(target=dispose_client, args=(client_socket, address)).start()


if __name__ == '__main__':
    start_server()
