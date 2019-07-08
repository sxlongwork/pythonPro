
"""
需求：小猫爱吃鱼，小猫爱喝水
"""


class Cat:
    def eat(self):
        print("小猫吃鱼")

    def drink(self):
        print("小猫喝水")


# 创建对象
tom = Cat()

# 使用 .属性名 利用赋值语句就可以
tom.name = 'tom'

tom.eat()
tom.drink()
# print(tom)
# print("%x" % id(tom))  # %x 16进制
print('-'*30)

# 创建另一个对象
lazy_cat = Cat()
lazy_cat.age = 12
lazy_cat.eat()
lazy_cat.drink()

