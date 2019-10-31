#coding=utf-8
# @Author: wjn

import socketserver

obj = socketserver.ThreadingTCPServer(1,2)
obj.server_forever()