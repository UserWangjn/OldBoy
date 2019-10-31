#coding=utf-8
# @Author: wjn

import threading
import time

def muisc(func):
    for i in range(2):
        print('Begin listening to %s.  %s'%(func,time.ctime()))
        time.sleep(2)
        print('end listening.   %s'%time.ctime())

def movie(func):
    for i in range(2):
        print('Begin watching at the %s!  %s'%(func,time.ctime()))
        time.sleep(5)
        print('end watching.  %s'%time.ctime())

threads = []
t1 = threading.Thread(target=muisc,args=('晴天',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('教父',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.start()
    print('all over %s' %time.ctime())