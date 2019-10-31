#coding=utf-8
# @Author: wjn

class Foo:

    state = 'y'

    def __init__(self,n,a):
        self.name = n
        self.age = a

    @staticmethod
    def show():
        print('showwww')


obj = Foo('wjn',18)
print(Foo.state)
print(obj.state)

Foo.show()