#coding=utf-8
# @Author: wjn

class Car:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def __call__(self, *args, **kwargs):
        print('call..')

    def __int__(self):
        return 3

    def __str__(self):
        return 'wjn'

c = Car('qqq',18)
c()
ret = int(c)
print(ret)
print(c)