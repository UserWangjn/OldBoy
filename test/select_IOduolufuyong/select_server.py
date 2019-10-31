#coding=utf-8
# @Author: wjn

import socket
import select
import time

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(3)
sk2 = socket.socket()
sk2.bind(('127.0.0.1',8090))
sk2.listen(3)

while 1:
    r,w,e = select.select([sk,sk2],[],[])
    print('rrr')
    for i in r:
        conn,addr = i.accept()
        print(conn)
        print(addr)

        conn.sendall('hello'.encode('utf8'))
        # time.sleep(1)
        # data = conn.recv(1024)
        # print(data.decode('utf8'))
    # print(r)