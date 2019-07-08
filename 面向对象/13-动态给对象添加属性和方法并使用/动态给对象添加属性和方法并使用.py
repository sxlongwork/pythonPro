from types import MethodType


# 创建一个空类
class Person(object):
    # 特殊属性，可以限制动态添加的属性只能添加name,age,speak属性
    __slots__ = ("name", "age", "speak")


per = Person()

# 动态给对象添加属性,体现了python的动态性(灵活)
per.name = "tom"
print(per.name)

# 动态给对象添加方法
# from types import MethodType
def say(self):
    print("my name is "+self.name)
per.speak = MethodType(say, per)
per.speak()


# 限制对象的属性
# 解决：在定义类时，定义一个特殊的属性(__slots__),可以限制动态添加的属性
# per.weight = 200  # 不能添加该属性 AttributeError: 'Person' object has no attribute 'weight'
# print(per.weight)





