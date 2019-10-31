#coding=utf-8
# @Author: wjn
import socket
from test.test_socket.exercise_FTP.config import settings
import os

def my_client():
    sk = socket.socket()
    address = ('127.0.0.1',8091)
    sk.connect(address)
    print('客户端启动...')

    while 1:
        username = input('请输入用户名>>>')
        sk.sendall(bytes(username,'utf8'))
        pwd = input('请输入密码>>>')
        sk.sendall(bytes(pwd,'utf8'))
        # 接收登录是否成功标识
        login_flag = str(sk.recv(1024),'utf8')
        print(login_flag)
        if login_flag == 'True':
            while 1:
                inp = input('请输入指令>>>').strip()      #post|test.png
                if 'post' in inp:      # 目前没有写get指令的逻辑
                    # 指令是post或者get为文件传输
                    cmd ,path = inp.split('|')
                    source_path = os.path.join(settings.file_source_path,path)
                    filename = os.path.basename(source_path)
                    filesize = os.stat(source_path).st_size
                    fileinfo = '{0}|{1}|{2}'.format(cmd,filename,filesize)
                    # 发送文件信息        post|test.png|12732134
                    sk.sendall(bytes(fileinfo,'utf8'))

                    # 接收服务器返回的文件是否已经存在
                    is_exist_file = str(sk.recv(1024),'utf8')
                    # 如果文件已经存在，就不再传输
                    if is_exist_file == 'True':
                        print('文件名已经存在，不能重复传输')
                    else:
                        has_send = 0
                        with open(source_path,'rb') as f:
                            while has_send != filesize:
                                data = f.read(1024)
                                # print(data)
                                sk.sendall(data)
                                has_send += len(data)
                        print('上传成功')
                else:
                    # 指令不存在post或者get，则为shell命令
                    sk.sendall(bytes(inp,'utf8'))
                    result_len = int(str(sk.recv(1024),'utf8'))
                    print(result_len)
                    cmd_result = bytes()
                    while len(str(cmd_result,'utf8')) != result_len:
                        cmd_result_reg = sk.recv(1024)
                        # print(len(cmd_result_reg))
                        cmd_result += cmd_result_reg
                    print(str(cmd_result,'utf8'))
        else:
            print('用户名、密码输入错误，请重新输入')
    sk.close()