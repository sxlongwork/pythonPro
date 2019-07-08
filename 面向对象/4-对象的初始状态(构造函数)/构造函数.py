class People(object):
    # name = ""
    # age = 0
    height = 0
    weight = 0

    # self就代表当前正在创建的对象
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self):
        print("run......")

    def eat(self, food):
        print("eat {}".format(food))

'''
构造函数：__init__() 在创建对象时会自动调用
注意：如果不显示写出构造函数，会自动添加并执行无参的构造函数

'''
per = People("xiaoming", 24)
print(per.name, per.age)
