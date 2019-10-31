#coding=utf-8
# @Author: wjn

class Bar():
    def foo(self,name):
        print(name)
        return 3

f = Bar()
a = f.foo('wjn')
print(a)