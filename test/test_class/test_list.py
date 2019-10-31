#coding=utf-8
# @Author: wjn


'''
class Foo:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def __getitem__(self, item):
        return item+10

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)


li = Foo('wjn',18)
r = li[5]
print(r)
li[10] = 'qwe'
del li[9]
'''

class Foo:

    def __init__(self,n,a):
        self.name = n
        self.age = a
    def __iter__(self):
        return iter([88,66,99])

li = Foo('wjn',18)
for i in li:
    print(i)