#coding=utf-8
# @Author: wjn
# @Time: 2019-08-16 21:24
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from test_module import credit_card_main
# 调用开户接口
# credit_card_main.create_account('王小二',30000)
# 调用提现接口
# credit_card_main.recharge('王佳宁','6228481234',20000)
# 调用还款接口
# credit_card_main.repay_reg('佳宁','6228481234',3000)
# 调用转账接口
# credit_card_main.transfer_account('王佳宁','6228481234','王小二','6228489826',50000)
# 调用商城首页接口
# credit_card_main.enter_main_page()
# 调用登录接口
# credit_card_main.login()
# 调用商城主页接口
credit_card_main.enter_main_page()