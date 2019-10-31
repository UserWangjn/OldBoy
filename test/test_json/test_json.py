#coding=utf-8
# @Author: wjn
# @Time: 2019-08-13 22:31

import json

dic = {'name':'wjn','age':18,'job':'IT'}

data = json.dumps(dic)

with open('data.txt','w') as f:
    f.write(data)