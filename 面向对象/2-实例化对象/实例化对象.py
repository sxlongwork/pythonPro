class People(object):
    name = ""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run......")

    def eat(self, food):
        print("eat {}".format(food))

'''
实例化对象
格式：
对象名 = 类名(参数列表)
注意，没有参数，小括号也不能省略

'''

# 实例化对象
per1 = People()
print(per1)

per2 = People()
print(per2)
