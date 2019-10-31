#coding=utf-8
# @Author: wjn
# @Time: 2019-08-13 22:56

# import test_logen
from test_module import test_logen
from test_module import pages
import random
import json
import time


# 开户功能
def create_account(username,limit):
    # 随机生成银行卡号
    seeds = '1234567890'
    random_num = []
    for i in range(4):
        num = random.choice(seeds)
        random_num.append(num)
    # print(random_num)
    master_id = '622848'+''.join(random_num)
    # print(master_id)
    # 创建账户信息
    dic = {'account_name':username,'account':master_id,'balance':0
        ,'limit':limit,'use_limit':limit}
    # print('dic:',dic)
    # 把账户信息放入txt文件中
    data = json.dumps(dic,ensure_ascii=False,separators=(',',':'))
    # data = json.dumps(dic, ensure_ascii=False)
    # print('data:',data)
    with open('../data/{0}_{1}.txt'.format(username,master_id),'w') as f:
        f.write(data)

# 把剩余余额、额度写入数据库
def write_balance_limit(data,username,account,balance,use_limit):
    # print('data类型:',type(data))
    data['balance']=balance
    data['use_limit']=use_limit
    data = json.dumps(data,ensure_ascii=False,separators=(',',':'))
    with open('../data/{0}_{1}.txt'.format(username,account),'w') as f:
        f.write(data)

# cash充值 recharge提现
# 提现功能
def recharge(username,account,amount):
    error_logger = test_logen.error_logger()
    flow_logger = test_logen.flow_logger()
    ctime = time.strftime('%Y-%m-%d %X')
    try:
        with open('../data/{0}_{1}.txt'.format(username,account),'r') as f:
            data = f.read()
        data = json.loads(data)
        balance = data['balance']
        use_limit = data['use_limit']
        if balance >= amount:
            balance -= amount
            # 写入账户变动流水
            # ctime = time.strftime('%Y-%m-%d %X')
            flow_logger.info('>>> {0}提现{1}元,余额:{2},可用额度:{3}'.format
                             (username,amount,balance,use_limit))
            # 把剩余余额、剩余额度写入数据库
            write_balance_limit(data,username,account,balance,use_limit)
        elif (balance + use_limit - (amount - balance)*0.05) >= amount:
            fee = (amount - balance)*0.05
            # print('fee:',fee)
            use_limit = use_limit + balance - amount - fee
            balance = 0
            # 写入账户变动流水
            flow_logger.info('>>> {0}提现{1}元,余额:{2},可用额度:{3},手续费:{4}'.format
                             (username, amount, balance, use_limit,fee))
            # 把剩余余额、额度写入数据库
            write_balance_limit(data, username, account, balance, use_limit)
        else:
            # print('余额不足，提现失败')
            error_logger.error('{0}账户余额不足，提现失败'.format(username))

    except BaseException as e:
        # print('不存在的账户')
        # print(e)
        error_logger.error('不存在的账户,无法提现')
        error_logger.error(e)

# 还款接口
def repay_reg(username,account,amount):
    error_logger = test_logen.error_logger()
    flow_logger = test_logen.flow_logger()
    try:
        with open('../data/{0}_{1}.txt'.format(username,account),'r') as f:
            data = f.read()
        data = json.loads(data)
        use_limit = data['use_limit']
        limit = data['limit']
        balance = data['balance']
        if use_limit == limit:
            balance += amount
        else:
            use_limit += amount
            if use_limit > limit:
                balance = use_limit - limit + balance
                use_limit = limit
        write_balance_limit(data,username,account,balance,use_limit)
        flow_logger.info('>>> {0}还款{1}元,余额:{2},可用额度:{3}'.format
                         (username,amount,balance,use_limit))
    except BaseException as e:
        error_logger.error('还款失败，{0}账户不存在'.format(username))
        error_logger.error(e)

# 转账接口
def transfer_account(from_username,from_account,
                     to_username,to_account,amount):
    error_logger = test_logen.error_logger()
    flow_logger = test_logen.flow_logger()
    try:
        with open('../data/{0}_{1}.txt'.format
                      (from_username,from_account),'r') as f:
            data1 = f.read()
        data1 = json.loads(data1)
        from_balance = data1['balance']
        from_use_limit = data1['use_limit']
        if from_balance < amount:
            flow_logger.info('{0}账户余额不足，无法转账'.format(from_username))
        else:
            try:
                with open('../data/{0}_{1}.txt'.format(to_username,to_account),'r') as f:
                    data2 = f.read()
                data2 = json.loads(data2)
                to_balance = data2['balance']
                to_use_limit = data2['use_limit']
                to_limit = data2['limit']
                if to_use_limit < to_limit and amount >= to_limit - to_use_limit:
                    to_balance = to_balance + amount - (to_limit - to_use_limit)
                    to_use_limit = to_limit
                    # 收款方把余额、可用额度写入数据库
                    write_balance_limit(data2,to_username,to_account,to_balance,to_use_limit)
                    # 收款方日志记录
                    flow_logger.info('收到来自{0}转入的{1}元,{2}当前余额:{3},可用额度:{4}'.format
                                     (from_username,amount,to_username,to_balance,to_use_limit))

                elif to_use_limit < to_limit and amount < to_limit - to_use_limit:
                    to_use_limit += amount
                    # 收款方把余额、可用额度写入数据库
                    write_balance_limit(data2,to_username,to_account,to_balance,to_use_limit)
                    # 收款方日志记录
                    flow_logger.info('收到来自{0}转入的{1}元,{2}当前余额:{3},可用额度:{4}'.format
                                     (from_username,amount,to_username,to_balance,to_use_limit))
                else:
                    to_balance += amount
                    # 收款方把余额、可用额度写入数据库
                    write_balance_limit(data2, to_username, to_account, to_balance, to_use_limit)
                    # 收款方日志记录
                    flow_logger.info('收到来自{0}转入的{1}元,{2}当前余额:{3},可用额度:{4}'.format
                                     (from_username, amount, to_username, to_balance, to_use_limit))
                # 计算付款方剩余余额
                from_balance -= amount
                # 付款方把余额、可用额度写入数据库
                write_balance_limit(data1,from_username,from_account,from_balance,from_use_limit)
                # 付款方日志记录
                flow_logger.info('{0}账户发起转账，收款人:{1},当前余额:{2},可用额度:{3}'.format
                                 (from_username,to_username,from_balance,from_use_limit))
            except BaseException as e:
                error_logger.error('{0}账户不存在,无法转账'.format(to_username))
                error_logger.error(e)
    except BaseException as e:
        error_logger.error('{0}账户不存在,无法转账'.format(from_username))
        error_logger.error(e)

# 登录接口
def login():

    while True:
        username = input('用户名:')
        passwd = input('密码:')
        try:
            with open('../data/shopping_user.txt','r') as f:
                data = f.read()
            data = json.loads(data)
            if username in data:
                if passwd == data[username]:
                    print('用户名、密码正确，登录成功!')
                    break
                else:
                    print('密码错误，请重新输入')

            else:
                print('您输入的用户名不存在，请重新输入!')
        except BaseException as e:
            print(e)
    return username



# 进入商城主页
def enter_main_page():

    while True:
        print('''
        1.home
        2.book类
        3.日常生活类
        ''')
        choice = input('enter your choice>>>')
        if choice.strip() =='1':
            pages.home_page()
        elif choice.strip() == '2':
            pages.book_page()
        else:
            print('输入无效，重新输入')

    # ----------------------
    # print('''欢迎来到jd商城>>>
    #       1.登录
    #       2.开户
    #       3.进入商品列表
    #       4.登录网银(目前不支持该功能)''')
    # login_flag = False
    # while True:
    #     choice = input('enter your choice>>>')
    #     if choice == '1' and not login_flag:
    #         # 调用登录接口 其中登录接口返回username
    #         username = login()
    #         login_flag = True
    #     elif choice == '1' and login_flag:
    #         print('已经登录过了，当前用户名:{0}'.format(username))
    #     elif choice =='2':
    #         print('此处应该是一个注册登录账户的方法')
    #     elif choice =='3':
    #         pages.show_shopping_page()
    #         choice = input('enter your choice>>>')
    #         if not login_flag:
    #             if choice != '0':
    #                 login()
    #                 login_flag = True
    #             elif choice == '0':
    #
    #     elif choice == '4':
    #         print('目前不支持该功能，请重新选择')
    #     else:
    #         print('输入错误，请重新输入！')


if __name__ == '__main__':
    # create_account('王小二')
    recharge('王佳宁','6228481234',10000)