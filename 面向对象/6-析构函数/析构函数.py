"""
6-析构函数：__del__() 释放对象时自动调用
"""


class People(object):

    # self就代表当前正在创建的对象
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self不是关键字，可以换成其他表示，aaa,bbb等都可以，但self可以见名知意
    def say_self(self):
        print("I'm {},{} years old".format(self.name, self.age))

    def run(self):
        print("run......")

    def eat(self, food):
        print("eat {}".format(food))

    def __del__(self):
        print("执行析构函数")


per = People("xianqian", 25)

# 程序执行完毕会自动执行析构函数，也可以使用以下方法自动释放
del per
# print(per.name) # 会报错


# 在函数中定义的对象，会在函数执行结束时自动释放
def func():
    per2 = People("xianqian", 23)


func()

