"""
使用super().父类方法 可以调用父类同名方法
"""
class Dog:
    def bark(self):
        print("汪汪。。。")


class Xiaotianquan(Dog):
    def bark(self):
        print("叫的和神一样")
        # 调用父类方法
        super().bark()
        print("______----______")

    def fly(self):
        print("i can fly。。。")


xtq = Xiaotianquan()
xtq.bark()

