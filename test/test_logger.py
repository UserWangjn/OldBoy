#coding=utf-8
# @Author: wjn
# @Time: 2019-08-15 23:41


import logging

def logger_test():
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger = logging.getLogger('hello')
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    return logger

logger_test().info('this is test')
logger_test().info('hell')