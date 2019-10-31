#coding=utf-8
# @Author: wjn

class Car:
    def __init__(self):
        self.name = 123
        self.__age = 18

class Benz(Car):
    def __init__(self,game):
        self.game = game
        self.__gage = 22
        super(Benz,self).__init__()
    def show(self):
        print(self.game,self.__gage,self.name)

benz = Benz('smart')
benz.show()