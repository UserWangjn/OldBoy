#coding=utf-8
# @Author: wjn
'''
    作为server端启动入口
'''

from test.test_socket.exercise_FTP.src.service import server_service
import socketserver

def execute():
    server = socketserver.ThreadingTCPServer(
        ('127.0.0.1',8091),server_service.MyServer)
    server.serve_forever()

if __name__ == '__main__':
    execute()