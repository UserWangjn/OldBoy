#coding=utf-8
# @Author: wjn

import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = ('127.0.0.1',8000)
sk.connect(address)
while 1:
    inp = input('>>>')
    if inp == 'exit':break
    sk.send(bytes(inp,'utf8'))
    data = sk.recv(1024) # 阻塞  接受
    print(str(data,'utf8'))

sk.close()