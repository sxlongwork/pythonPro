class People(object):
    name = ""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run......")

    def eat(self, food):
        print("eat {}".format(food))


per = People()
'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''
# 访问属性,不赋值，会使用默认值
per.name = "xiaoming"
per.age = 15
per.height = 1.7
per.weight = 60
print(per.name, per.age, per.height, per.weight)

'''
访问方法
格式:对象名.方法名(参数列表)
括号不能省略
'''
per.run()
per.eat("apple")




