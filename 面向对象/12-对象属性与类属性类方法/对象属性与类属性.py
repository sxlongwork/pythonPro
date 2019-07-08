# 对象属性， 类属性


class Person(object):
    # 这里的属性实际上是属于类属性(用类名来调用)
    name = "xianqian"

    # 对象属性在__init__中定义
    def __init__(self, name):
        # 对象属性定义，当没有对象属性时会访问同名的类属性
        self.name = name


# 类属性可以通过类名来访问
print(Person.name)
per = Person("xiaoming")
# 对象属性的优先级大于类属性
print(per.name)
# 动态的给对象添加对象属性，该属性只对当前对象有效，新建对象没有该属性
per.age = 23
print(per.age)

# 删除对象属性
del per.name
print(per.name)     # 会访问同名的类属性

# 注意：以后不要将对象属性和类属性重名，对象属性会屏蔽类属性，但是删除对象属性后，又可以使用类属性了


print(Person.name)  # 同名的对象属性名并不影响类属性的调用








