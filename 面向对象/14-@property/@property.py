class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def setName(self, name):
    #     self.__name = name
    # def getName(self):
    #     return self.__name

    # 还想通过对象名.属性名的方式访问私有属性
    @property
    def name(self):
        return self.__name

    @name.setter    # 去掉下划线.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age




per = Person("xianqian", 23)
# print(per.name)
# print(per.age)

# 如果不想直接调用，可定义为私有属性
# print(per.getName())

# 如果是私有属性，并且还想通过对象名.属性名的方式调用，则需要使用@property方式
per.name = "呵呵"     # 实际是调用age(self, name)方法赋值
print(per.name)      # 实际是调用age(self)方法获取值
per.age = 25
print(per.age)

# @property 可以让受限制的属性使用.属性的方式直接访问
