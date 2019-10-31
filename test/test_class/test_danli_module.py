#coding=utf-8
# @Author: wjn

class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v
obj = Foo.get_instance()
print(obj)
obj2 = Foo.get_instance()
print(obj2)