#coding=utf-8
# @Author: wjn
# @Time: 2019-08-13 22:43

import json

with open('data.txt','r') as f:
    data = f.read()

print(json.loads(data))