#coding=utf-8
# @Author: wjn

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                       passwd='12345678',db='test_import_database',charset='utf8')

# 创建游标    # cursor=pymysql.cursors.DictCursor 是fetchall得到的结果
# 是字典形式。默认是列表形式
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行sql，并返回受影响行数
# ret = cursor.execute('insert into class(caption) values ("测试一班")')
# print(ret)

# 提交
# conn.commit()

cursor.execute('select * from student where sid in (1,2,3)')
# result = cursor.fetchone()
result = cursor.fetchall()
print(result)
r = result[0][3]
print(r)
# 关闭游标
cursor.close()

# 关闭连接
conn.close()
