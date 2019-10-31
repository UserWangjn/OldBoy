#coding=utf-8
# @Author: wjn

class Person:

    age = 18

    def __init__(self,n):
        self.name = n

    def show(self):
        print(self.name)

    @staticmethod
    def dd(a,b):
        print(a,b)

# p = Person('wjn')
# p.show()

print(Person.age)
Person.dd(3,5)