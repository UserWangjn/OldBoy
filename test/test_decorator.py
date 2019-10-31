# @Author: wjn
# @Time: 2019-08-04 20:08

# 装饰器练习
import time

def logger(flag):
    def show_time(f):
        def inner():
            start = time.time()
            f()
            end = time.time()
            print('speed: %s'%(end - start))
            if flag == 'true':
                print('打印日志')
        return inner
    return show_time

@logger('true')   # foo = show_time(foo)
def foo():
    print('foo...')
    time.sleep(2)

foo()