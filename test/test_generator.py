# @Author: wjn
# @Time: 2019-08-05 23:21

g = (x*2 for x in range(5))
print(g)

print(next(g))
print(next(g))

for i in g:
    print(i)