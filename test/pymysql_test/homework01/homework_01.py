#coding=utf-8
# @Author: wjn

import pymysql




conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                       passwd='12345678',db='homework01',charset='utf8')
cursor = conn.cursor()

cursor.execute()