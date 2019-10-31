#coding=utf-8
# @Author: wjn

import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen(5)

rlist = [sk]
while 1:
    r,w,e = select.select(rlist,[],[])
    for obj in r:
        if obj == sk:
            conn,addr = obj.accept()
            print(conn)
            rlist.append(conn)
        else:
            data = obj.recv(1024)
            print(data.decode('utf8'))
            inp = input('回答第{0}位>>>：'.format(rlist.index(obj)))
            obj.sendall(inp.encode('utf8'))
obj.close()