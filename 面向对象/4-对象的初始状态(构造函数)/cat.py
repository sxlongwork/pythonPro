class Cat:

    def __init__(self):
        print('初始化方法')

        # self.属性名 = 属性的初始值
        self.name = 'tom'

    def eat(self):
        print('%s 吃鱼' % self.name)

# 创建对象时python解释器会自动帮我们做两件事
# 1.给对象分配内存空间
# 3.初始化对象的属性
#
# __init__ 时python的内置方法，专门用来定义一个类具有哪些属性的方法


tom = Cat()
tom.eat()
print(tom.name)

jerry = Cat()
jerry.eat()
print(jerry.name)