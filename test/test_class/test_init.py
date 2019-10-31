#coding=utf-8
# @Author: wjn

class Person:
    # 构造方法
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def show_info(self):
        print(self.n,self.a)
# 把属性封装到wjn这个对象k0
wjn = Person('wangjianing',18)
wxe = Person('wangxiaoer',33)

wjn.show_info()
wxe.show_info()