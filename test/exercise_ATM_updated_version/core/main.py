#coding=utf-8
# @Author: wjn
# @Time: 2019-08-18 13:15

from core import logger
from core import auth
from core import accounts
from core import transaction

trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}


def account_info(acc_data):
    print(user_data)

def repay(acc_data):

    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''--------BALACE INFO-------
        Credit  :   %s
        Balance :   %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('\033[33;1mInput repay amount:\033[0m').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount,only accept integer!\033[0m' % repay_amount)

        if repay_amount == 'b':
            back_flag = True

def withdraw(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''---------BALANCE INFO--------
        Credit  :    %s
        Balance :    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input('\033[33;1mInput repay amount:\033[0m').strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw',withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not valid amount,only accept integer!\033[0m' % withdraw_amount)


def logout(acc_data):
    pass

def interactive(acc_data):
    menu = u'''
    -------------WJN Bank--------
    \033[32;1m1. 账户信息
    2. 还款
    3. 取款
    4. 转账（功能未实现）
    5. 账单（功能未实现）
    6. 退出
    \033[0m'''

    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }
    exit_flag = False
    while not exit_flag:
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print('\033[31;1mOption does not exist!\033[0m')


def run():
    acc_data = auth.acc_login(user_data,access_logger)

    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)