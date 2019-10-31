#coding=utf-8
# @Author: wjn
# @Time: 2019-08-18 13:15

from conf import settings
from core import db_handler
import json

def load_current_balance(account_id):

    db_path = db_handler.dbhandler(settings.DATABASE)
    account_file = '%s/%s.json' %(db_path,account_id)
    with open (account_file) as f:
        acc_data = json.load(f)
        return acc_data

def dump_account(account_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' %(db_path,account_data['id'])
    with open(account_file,'w') as f:
        acc_data = json.dump(account_data,f)

    return True