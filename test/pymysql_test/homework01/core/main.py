#coding=utf-8
# @Author: wjn

import pymysql
import time

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def show_menu():
    menu = '''1.登录
    2.注册
    3.退出(暂不支持)
    '''
    print(menu)

def login():

    while 1:
        username = input('用户名>>>:').strip()
        password = input('密码>>>:').strip()
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                               passwd='12345678',db='homework01',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select * from sys_user where user_name = %s and "
                       "passwd = %s and is_locked = '0'",(username,password))
        ret = cursor.fetchone()
        cursor.close()
        conn.close()

        if ret == None:
            print('用户名/密码错误，请重新输入！')
        else:
            username = ret[3]
            user_data['is_authenticated'] = True
            # print(user_data['account_id'])
            break

    print('{0}登录成功！'.format(username))
    if user_data['is_authenticated'] == True:
        sys_menu(username)


def sys_menu(username):
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                           passwd='12345678',db='homework01',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select user_auth from sys_auth where user_name=%s',
                   (username))
    ret = cursor.fetchone()
    menu_list = ret['user_auth']
    menu_list = menu_list.split('|')
    for menu_code in menu_list:
        cursor.execute('select menu_name from sys_menu where menu_code = %s'
                       ,(menu_code))
        ret = cursor.fetchone()
        menu_name = ret['menu_name']
        print(menu_name)

def register():
    while 1:
        username = input('新建用户名>>>:').strip()
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                               passwd='12345678',db='homework01',charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('select login_name from sys_user where login_name = %s',
                       (username))
        ret = cursor.fetchone()
        if ret == None:
            password = input('密码>>>:').strip()
            try:
                cursor.execute('insert into sys_user(user_name,passwd,'
                               'login_name) values(%s,%s,%s)',(username,
                                password,username))
                conn.commit()
                cursor.close()
                conn.close()
                print('用户创建成功！')
                break
            except BaseException as e:
                print('用户创建失败！%s' %e)
        else:
            print('该用户名已存在，请重新输入!')

def exit():
    pass

def home():
    show_menu()
    menu_dic = {
        '1':login,
        '2':register,
        '3':exit
    }
    user_option = input('>>>:').strip()
    if user_option in menu_dic:
       menu_dic[user_option]()
       # (1, 'admin', '123', 'admin', '1', datetime.datetime(2019, 10, 20, 12, 19, 21), '0')



if __name__ == '__main__':
    home()