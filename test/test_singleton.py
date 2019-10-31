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

f1 = Foo.get_instance()
print(f1)
f2 = Foo.get_instance()
print(f2)