#coding=utf-8
# @Author: wjn

import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8090))

while 1:
    inp = input('>>>')
    sk.sendall(inp.encode('utf8'))
    data = sk.recv(1024)
    print(data.decode('utf8'))