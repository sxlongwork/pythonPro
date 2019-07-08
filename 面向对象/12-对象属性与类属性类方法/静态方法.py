"""
使用场景：
当不需要访问实例的属性和方法
也不需要访问类的属性和类方法
此时，就可以将方法定义为一个静态方法
"""
class Dog(object):

    @staticmethod
    def run():
        print("dog is running...")


# 通过类名.静态方法名 的方式调用静态方法
Dog.run()