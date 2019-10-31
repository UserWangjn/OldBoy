#coding=utf-8
# @Author: wjn
from test.test_socket.exercise_FTP.config import settings
import pickle
import os
import socketserver

# 登录认证
def login_auth(username,pwd):
    try:
        dp_path = settings.db_path+'/'+username
        ret = pickle.load(open(dp_path,'rb'))
        if pwd == ret:
            return True
        else:
            return False
    except BaseException as e:
        # print(e)
        return False

# 判断接收的文件名是否已经存在
def is_exist_file(username,filename):
    target_path = os.path.join(settings.file_target_path,username,filename)
    ret = os.path.exists(target_path)
    return ret

# 接收文件方法
def recv_file(username,conn,filename,filesize):
    target_path = os.path.join(settings.file_target_path,username,filename)
    recv_data = bytes()
    while len(recv_data) != filesize:
        data = conn.recv(1024)
        recv_data += data

    with open(target_path,'wb') as f:
        f.write(recv_data)
        print('接收完成..接收路径：{0}'.format(target_path))

if __name__ == '__main__':
    ret = login_auth('wjn','123')
    print(ret)