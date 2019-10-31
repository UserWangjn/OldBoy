#coding=utf-8
# @Author: wjn

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def show(self):
        return '{0}-{1}'.format(self.name,self.age)


# 反射
obj = Person('wjn',18)
r = getattr(obj,'name')
print(r)
r2 = getattr(obj,'show')
rr = r2()
print(rr)
res = hasattr(obj,'age')
print(res)

setattr(obj,'kkk','vvvalue')
print(obj.kkk)

delattr(obj,'age')
print(hasattr(obj,'age'))