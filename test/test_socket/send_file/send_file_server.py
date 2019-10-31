#coding=utf-8
# @Author: wjn

import socket
import os

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)
conn,addr = sk.accept()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_info = conn.recv(1024)
print(file_info)
cmd,filename,filesize = str(file_info,'utf8').split('|')
filesize = int(filesize)

recv_data = bytes()
target_path = os.path.join(BASE_DIR,'dir',filename)
while len(recv_data) != filesize:
    data = conn.recv(1024)
    recv_data += data

with open(target_path, 'wb') as f:
    f.write(recv_data)


conn.close()