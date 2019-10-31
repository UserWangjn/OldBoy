#coding=utf-8
# @Author: wjn

import socket

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)

while 1:
    inp = input('>>>')
    cmd_result = bytes()
    if inp == 'exit':
        sk.close()
        break
    sk.sendall(bytes(inp,'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    print(result_len)

    # print(str(cmd_result_reg,'utf8'))
    while len(str(cmd_result,'utf8')) != result_len:
        cmd_result_reg = sk.recv(1024)
        cmd_result += cmd_result_reg
    print(str(cmd_result,'utf8'))