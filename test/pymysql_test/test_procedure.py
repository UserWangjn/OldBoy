#coding=utf-8
# @Author: wjn

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='12345678',
                       db='test_import_database',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor = conn.cursor()

r1 = cursor.callproc('p11',args=(1,22,3,4))
print(r1)

result1 = cursor.fetchall()
print(result1)

r2 = cursor.execute('select @_p11_0,@_p11_1,@_p11_2,@_p11_3')
print(r2)

result2 = cursor.fetchall()
print(result2)

# 如果有增删改的操作需要加commit
# conn.commit()
cursor.close()
conn.close()