class Father(object):
    def __init__(self, money):
        self.money = money

    def run(self):
        print("run...")

    def play(self):
        print("play...")

    def func(self):
        print("father func1")


class Mother(object):
    def __init__(self, faceValue):
        self.faceValue = faceValue

    def eat(self):
        print("eat...")

    def func(self):
        print("mother func2")


class Children(Mother, Father):
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)


child = Children(1000, 99)
print(child.money)
print(child.faceValue)
child.run()

# 如果多个父类中有同名的方法，则默认调用在前面的父类
# 当多个父类中含有同名方法时，应避免使用多继承
child.func()

# python内置属性__mro__,查看方法调用顺序
print(Children.__mro__)