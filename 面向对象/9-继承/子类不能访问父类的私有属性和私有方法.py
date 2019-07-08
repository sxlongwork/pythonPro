class A:
    def __init__(self):
        self.num1 = 12
        self.__num2 = 14

    def __test(self):
        print("父类的私有属性__num2值为%d" % self.__num2)

    def test(self):
        self.__test()


class B(A):

    def demo(self):
        # 子类内部不能访问父类的私有属性
        # print(self.__num2)

        # 子类内部不能访问父类的私有方法
        # print(self.__test)

        # 子类通过调用父类的共有方法间接调用父类的私有属性和私有方法
        self.test()
        pass


b = B()
b.demo()
