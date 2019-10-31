#coding=utf-8
# @Author: wjn

import socket

sk = socket.socket()
ip_port = ('127.0.0.1',8091)
sk.connect(ip_port)
print('客户端启动：')

while 1:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.sendall(bytes(inp,'utf8'))
    server_response = sk.recv(1024)
    print(str(server_response,'utf8'))

sk.close()