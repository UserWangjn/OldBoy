#coding=utf-8
# @Author: wjn

class Person:

    @property
    def per(self):

        return 1

    @per.setter
    def per(self,val):
        print(val)

    @per.deleter
    def per(self):
        print('delteeeee')

p = Person()
p.per

p.per = 3

del p.per

