"""
当父类方法无法满足子类需要时，就可以重写父类方法
如何重写？
就是在子类中重新定义一个和字类同名的方法并且实现它
"""
class Dog:
    def bark(self):
        print("汪汪。。。")


class Xiaotianquan(Dog):
    def bark(self):
        print("叫的和神一样")

    def fly(self):
        print("i can fly。。。")

xtq = Xiaotianquan()
xtq.bark()