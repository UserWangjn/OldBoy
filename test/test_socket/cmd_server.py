#coding=utf-8
# @Author: wjn

import socket
import subprocess
import time

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)

conn,addr = sk.accept()
print(conn)
while 1:
    recv = str(conn.recv(1024),'utf8')
    if not recv:
        conn.close()
        conn, addr = sk.accept()
        print(conn)
        continue
    obj = subprocess.Popen(recv, shell=True, stdout=subprocess.PIPE)
    cmd_result = obj.stdout.read()
    print(cmd_result)
    result_len = len(str(cmd_result,'utf8'))
    print(result_len)
    conn.sendall(bytes(str(result_len),'utf8'))
    time.sleep(1)
    conn.sendall(cmd_result)