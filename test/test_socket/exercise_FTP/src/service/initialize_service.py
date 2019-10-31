#coding=utf-8
# @Author: wjn
'''
    提供初始化用户名、密码的服务
'''

from test.test_socket.exercise_FTP.src import models

def initialize():
    username = input('请输入用户名>>>')
    pwd = input('请输入密码>>>')
    models.BaseModel.save_user(username,pwd)

def main():
    show = '''
        1.初始化FTP用户
    '''
    choice_dict = {
        '1':initialize
    }
    while 1:
        print(show)
        choice = input('请输入操作选项')
        if choice not in choice_dict:
            print('选项错误，请重新输入！')
        else:
            func = choice_dict[choice]
            ret = func()
            if ret:
                print('操作成功')
                return
            else:
                print('操作异常，请重新输入')


if __name__ == '__main__':
    initialize()