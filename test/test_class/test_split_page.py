#coding=utf-8
# @Author: wjn

class Split_page:

    def __init__(self,page):
        try:
            p = int(page)
        except BaseException as e:
            p = 1

        self.page = p

    @property
    def start(self):
        start = (self.page - 1) * 10
        return start
    @property
    def end(self):
        end = self.page * 10
        return end


while True:
    page = input('enter page:')

    pages = []
    for i in range(100):
        pages.append(i+1)

    obj = Split_page(page)
    ret = pages[obj.start:obj.end]
    print(ret)