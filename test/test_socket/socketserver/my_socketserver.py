#coding=utf-8
# @Author: wjn

import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('服务端启动....')
        while 1:
            conn = self.request
            print(self.client_address)
            while 1:
                client_data = conn.recv(1024)
                print(str(client_data,'utf8'))
                server_response = input('>>>')
                conn.sendall(bytes(server_response,'utf8'))
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(
        ('127.0.0.1',8091),MyServer)
    server.serve_forever()