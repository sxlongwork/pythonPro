'''
object类是所有类的父类，也称为基类，或超类

继承作用：
1.简化代码，减少冗余
2.提高了代码的健壮性
3.提高了代码的安全性
4.是多态的前提

耦合性越低，内聚性越高，代码越好
继承缺点：
耦合性高
'''

# 单继承的实现
class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def run(self):
        print("run...")

    def eat(self, food):
        print("eat"+food)


class Student(Person):
    def __init__(self, name, age, money, sid):
        super(Student, self).__init__(name, age, money)

        # 子类可以有自己独有的属性
        self.sid = sid

    def stuMoney(self):
        print(self.__money)

class Worker(Person):
    def __init__(self, name, age, money):
        super(Worker, self).__init__(name, age, money)


stu1 = Student("xianqian", 24, 1000, 1)
print(stu1.name, stu1.age)
stu1.run()
# print(stu1.__money)   # 父类的私有属性字类也可以继承，但是不能直接访问,
print(stu1.getMoney())  # 需要通过get方法获取

worker1 = Worker("xiaoming", 34, 2000)
print(worker1.name, worker1.age)
worker1.eat("apple")
print(worker1.getMoney())
