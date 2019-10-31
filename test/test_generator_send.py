# @Author: wjn
# @Time: 2019-08-05 23:36

def foo():
    print('ok1')
    count = yield 1
    print(count)

    print('ok2')
    yield 2

g = foo()
print(next(g))
a = g.send('wjn')
print(a)