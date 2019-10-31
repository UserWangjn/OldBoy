#coding=utf-8
# @Author: wjn

import threading
import random
import time

class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = random.randint(0,100)
            print('生产者',self.name,':Append'+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L) == 0:
                lock_con.wait()
            print('消费者',self.name,':Delete'+str(L[0]),L)
            del L[0]
            lock_con.release()
            time.sleep(0.25)


if __name__ == '__main__':
    L = []
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    lock_con = threading.Condition()
    for t in threads:
        t.start()
    for t in threads:
        t.join()