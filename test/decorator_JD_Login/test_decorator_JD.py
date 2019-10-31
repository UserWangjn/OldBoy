# @Author: wjn
# @Time: 2019-08-05 12:16


def auth(auth_type):
    def login(f):
        def inner():
            if not login_flag1:
                if auth_type == 'jingdong':
                    with open('jd_login.txt') as jd,open('weixin_login.txt') as wx:
                        line = 1
                        for i in jd:
                            if line == 1:
                                username = i[i.find('=')+1:i.find('\n'):]
                            elif line ==2:
                                passwd =  i[i.find('=')+1:i.find('\n'):]
                            line += 1
                        # print('get username:%s,get passwd:%s'%(username,passwd))
                    while True:
                        user = input('请输入用户名:')
                        pwd = input('请输入密码:')
                        if user == username and pwd == passwd:
                            print('登录成功')
                            login_flag1 = True
                            f()
                            break
                        else:
                            print('用户名或密码错误，重新输入')

                elif auth_type == 'weixin':
                    pass
            else:
                print('已经登录了，直接浏览吧')
        return inner
    return login

@auth(auth_type='jingdong','False')
def home():
    print('welcome to home page')

@auth(auth_type='jingdong')
def finance():
    print('welcome to finance page','False')

@auth(auth_type='jingdong','False')
def book():
    print('welcome to book page')


while True:
    print('''
1.home
2.finance
3.book
q退出''')
    choice = input('请选择您要进入的页面:')
    if choice.strip() == '1':
        home()
    elif choice.strip() == '2':
        finance()
    elif choice.strip() == '3':
        book()
    elif choice.strip() == 'q':
        break
    else:
        print('输入内容非法，请重新输入!')
