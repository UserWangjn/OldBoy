# @Author: wjn
# @Time: 2019-08-05 23:26

def foo():
    print('ok1')
    yield 1

    print('ok2')
    yield 2
print(foo)
print(foo())
g = foo()
print(next(g))
print(next(g))
