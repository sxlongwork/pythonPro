# self 理解
'''
1.self代表类的实例，而不是类

2.哪个对象调用方法，该方法中的self就代表哪个对象

3.self.__class__ 代表类名
'''


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


per1 = People("xiaoming", 23)
per2 = People("xianqian", 26)
per1.say_self()
per2.say_self()








