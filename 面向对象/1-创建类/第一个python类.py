'''
创建一个类
    类名：首字母大写，驼峰原则，见名知意
    类属性：驼峰原则
    类行为：方法或函数
'''
'''
类本身不占内存空间，实例化的对象占内存空间
格式：
class 类名(父类列表):
    属性
    行为

'''

class People(object):
    # 定义属性
    name = ""
    age = 0
    height = 0
    weight = 0

    # 定义行为(函数)
    # 方法的参数必须以self当第一个参数，不传参的话只写self
    # self代表类的实例(某个对象)
    def run(self):
        print("run......")

    def eat(self, food):
        print("eat {}".format(food))







