#coding=utf-8
# @Author: wjn
# @Time: 2019-08-18 13:17

import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':'%s/db' % BASE_DIR
}

LOG_LEVEL = logging.WARNING
LOG_TYPES = {
    'transaction':'transaction.log',
    'access':'access.log'
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},  # 转账
    'consume':{'action':'minus','interest':0}
}