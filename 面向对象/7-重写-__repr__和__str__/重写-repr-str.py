"""
重写：就是将函数重新写一遍

__repr__():是给机器使用的，在python解释器里面直接敲对象名回车后调用
__str__():在调用print打印对象时自动调用，是给用户使用的,用于描述对象

注意：在没有__str__()时，且有__str__ == __repr__

"""


class People(object):

    # self就代表当前正在创建的对象
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        __str__函数必须返回一个字符串，自定义时需要注意
        :return:
        """
        return self.name + " " + str(self.age)


per = People("xianqian", 25)
print(per)
print(per.__str__())
print(per.__repr__())

# 作业：人开枪射击子弹
