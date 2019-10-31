#coding=utf-8
# @Author: wjn

import socketserver
import subprocess
from test.test_socket.exercise_FTP.lib import common
from test.test_socket.exercise_FTP.src import socket_server
from test.test_socket.exercise_FTP.config import settings
import time
import os


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('服务端启动...')
        while 1:
            conn = self.request
            print(self.client_address, '已连接')

            # 认证登录的循环
            while 1:
                # 登录认证
                username = str(conn.recv(1024), 'utf8')
                pwd = str(conn.recv(1024), 'utf8')
                # username_md5 = common.create_md5(username)
                # pwd_md5 = common.create_md5(pwd)
                if socket_server.login_auth(username, pwd):
                    # 通知client端登录成功
                    conn.sendall(bytes('True','utf8'))
                    break
                else:
                    # 通知client端密码错误
                    conn.sendall(bytes('False','utf8'))
            while 1:
                recv_data = str(conn.recv(1024), 'utf8')    # post|test.png|12732134
                print(recv_data)
                if 'post' in recv_data:
                    # 收到post指令为客户端向服务器传输文件
                    cmd, filename, filesize = recv_data.split('|')
                    filesize = int(filesize)
                    # 下面接着写接收文件的逻辑
                    # 判断传入的文件名是否已经存在，如果存在就返回客户端不传输
                    is_exist_file = socket_server.is_exist_file(username,filename)
                    if is_exist_file:
                        conn.sendall(bytes('True','utf8'))
                    else:
                        conn.sendall(bytes('False','utf8'))
                        # 如果文件不存在，接收客户端传输的文件
                        socket_server.recv_file(username,conn,filename,filesize)
                elif 'get' in recv_data:
                    # 收到get指令为服务器向客户端传输文件
                    pass
                else:
                    # 如果指令不是post\get，则执行shell命令
                    try:
                        os.chdir(os.path.join(settings.file_target_path,username))
                        obj = subprocess.Popen(recv_data, shell=True, stdout=subprocess.PIPE)
                        cmd_result = obj.stdout.read()
                    except BaseException as e:
                        print(e)
                        cmd_result = 'command not found'
                    print(cmd_result)
                    print(type(cmd_result))     #cmd返回结果为bytes类型
                    # 下面接着写cmd执行后把信息返回给client端的逻辑
                    result_len = len(str(cmd_result,'utf8'))
                    print(result_len)
                    # 给客户端返回结果长度
                    conn.sendall(bytes(str(result_len),'utf8'))
                    time.sleep(1)   # 防止粘包
                    # 给客户端返回shell执行结果
                    conn.sendall(cmd_result)
            conn.close()

