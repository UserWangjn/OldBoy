#coding=utf-8
# @Author: wjn

import test_main

while True:
    choice = input('选择进入哪个页面:')
    ret = hasattr(test_main,choice)
    if ret == True:
        res = getattr(test_main,choice)
        res()
    else:
        print('404,找不到页面')