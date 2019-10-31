#coding=utf-8
# @Author: wjn

import socket

while 1:
    sk = socket.socket()
    sk.connect(('127.0.0.1',8090))

    data = sk.recv(1024)
    print(data.decode('utf8'))
    inp = input('>>>')
    sk.sendall(inp.encode('utf8'))