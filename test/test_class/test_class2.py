#coding=utf-8
# @Author: wjn

class foo:
    def Bar(self,arg):
        print(self,self.name,self.age,arg)

f = foo()
print(f)
# f.Bar(2)
f.name = 'wjn'
f.age = 18
f.Bar(6)