#coding=utf-8
# @Author: wjn
'''
    作为client端启动入口
'''
from test.test_socket.exercise_FTP.src.service import client_service

def execute():
    client_service.my_client()

if __name__ == '__main__':
    execute()