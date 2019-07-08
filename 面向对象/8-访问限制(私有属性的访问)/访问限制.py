class People(object):
    # 私有属性，外部不能直接通过对象名.属性名的方式访问
    __sex = ""      # _People__sex
    _height = 0     # 该变量可以直接被访问，但是要把它视为私有的，不要在外部直接访问它

    # 私有属性可以通过set/get方法对外提供访问私有属性的途径
    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    # self就代表当前正在创建的对象
    def __init__(self, name, age):
        self.name = name
        self.age = age


per = People("xianqian", 19)
per.age = 22
# per.__sex = "women"   # 这里相当于给对象新增属性__sex，

# 如果要让类内部的属性和方法不被外部直接访问,在属性和方法的前面加上两个下划线(__)
# 在python中如果在属性前面加上__,则该属性就会变为私有属性，但内部可访问
# print(per.__sex)    # 直接访问时会报错，AttributeError: 'People' object has no attribute '__sex'
# 可以通过在类内部自定义共有set/get方法访问私有属性
per.setSex("women")
print(per.getSex())


# 不能直接通过对象名.私有属性的方式访问私有属性的__sex原因是因为python解释器将__sex变为了_Person__sex
# 仍然可以使用per._People__sex访问，但强烈不建议
# print(per._People__sex)

# 注意：
# 在python中类似__xxx__的属性，属于特殊变量，可以直接访问
# 在python中类似_xxx的属性，这样的实例变量外部也是可以访问的，但是按照约定的规则，当看到这样的变量时，意思是"虽然可以被访问，但是请把我视为私有变量，不要直接访问我
# print(per._height)







