#coding=utf-8
# @Author: wjn
# @Time: 2019-08-17 10:53

import json

# 展示商品列表
def show_shopping_page():
    try:
        with open('../data/product_list.txt','r') as f:
            data = f.read()
        data = json.loads(data)
        for i in data:
            for j in data[i]:
                print('{0}>>>{1}>>>{2}'.format(i,j,data[i][j]))

    except BaseException as e:
        print(e)

def auth(auth_type):
    def login(f):
        def inner():
            if auth_type == 'jingdong':
                username = input('enter your username:')
                passwd = input('enter your password:')

                with open('../data/shopping_user.txt','r') as w:
                    data = w.read()
                data = json.loads(data)
                if username in data:
                    if passwd == data[username]:
                        print('登录成功')
                        f()
                    else:
                        print('密码输入错误')
            elif auth_type == 'weixin':
                print('调用微信用户名、密码验证')
        return inner
    return login

@auth(auth_type='weixin')
def home_page():
    print('welcome to home page')

def book_page():
    print('welcome to book page')


if __name__ == '__main__':
    # show_shopping_page()
    home_page()