#coding=utf-8
# @Author: wjn

import socket
import os

sk = socket.socket()
address=('127.0.0.1',8000)
sk.connect(address)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

inp = input('>>>').strip() # post|test.png
cmd,path = inp.split('|')
source_path = os.path.join(BASE_DIR,path)
filename = os.path.basename(source_path)
filesize = os.stat(source_path).st_size
file_info = '%s|%s|%s'%(cmd,filename,filesize)
sk.sendall(bytes(file_info,'utf8'))

has_sent = 0
with open(source_path,'rb') as f:
    while has_sent != filesize:
        data = f.read(1024)
        print(data)
        sk.sendall(data)
        has_sent += len(data)

print('上传成功')

sk.close()