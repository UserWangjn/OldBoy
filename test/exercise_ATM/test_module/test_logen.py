#coding=utf-8
# @Author: wjn
# @Time: 2019-08-14 21:48

import logging

# 打印错误日志功能
def error_logger():
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #     datafmt='%Y %m %ds %X',
    #     # datafmt='%a,%d %b %Y %H:%M:%S',
    #     filename='../log/error_log.out',
    #     filemode='a'
    # )
    # logging.error('')

    fh = logging.FileHandler('../log/error_log.out')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger = logging.getLogger()
    #每次调用logger都需要清空handlers，否则每调用一次，就会重复打印n+1次日志
    logger.handlers.clear()
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    # logging.error(message)
    return logger

# 记录账户流水功能
def flow_logger():
    fh = logging.FileHandler('../log/account_detail.txt')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger = logging.getLogger()
    # 每次调用logger都需要清空handlers，否则每调用一次，就会重复打印n+1次日志
    logger.handlers.clear()
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    return logger


# if __name__ == '__main__':
    # logger = error_logger()
    # logger.error('this is info')

    # logger = flow_logger()
    # logger.info('this is test')