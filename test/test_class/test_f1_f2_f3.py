#coding=utf-8
# @Author: wjn

class F1:
    def __init__(self):
        self.name = 123

class F2:
    def __init__(self,a):
        self.ff = a

class F3:
    def __init__(self,b):
        self.dd = b

f1 = F1()
f2 = F2(f1)
f3 = F3(f2)
print(f3.dd)