#coding=utf-8
# @Author: wjn

# import sys
# print(sys.path)

# import main_func
from main_func import *

class MyTeacher(Teacher):

    def aa(self):
        print('aa')

# t = Teacher('wjn','北京大学',1000)
# ret = t.teacher_info()
# print(ret)
mt = MyTeacher('wjn','北京大学',1000)
mt.aa()
