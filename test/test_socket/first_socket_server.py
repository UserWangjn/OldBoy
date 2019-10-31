#coding=utf-8
# @Author: wjn

import socket

# Socket函数使用的格式为：socket(family,type[,protocol])
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
'''
Family参数    描述
socket.AF_UNIX
只能够用于单一的Unix系统进程间通信

socket.AF_INET
服务器之间网络通信

socket.AF_INET6
IPv6
'''
'''
Type参数  描述

socket.SOCK_STREAM
流式socket , 当使用TCP时选择此参数

socket.SOCK_DGRAM
数据报式socket ,当使用UDP时选择此参数

socket.SOCK_RAW
原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，
SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由
用户构造IP头。
'''

address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)
conn,addr = sk.accept()
while 1:
    try:
        data = conn.recv(1024)  # 阻塞
    except Exception:
        break
    print('....',str(data,'utf8'))
    if not data:
        conn.close()
        conn, addr = sk.accept()
        continue
    inp = input('>>>')
    conn.send(bytes(inp,'utf8')) # 发送

sk.close()