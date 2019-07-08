'''
装饰器：就是把一个函数作为参数，返回一个加强版的函数，实质就是一个返回函数的函数

可用于修改一些函数的功能，但是不能修改原函数
'''

# example 1
def add(a, b):      # 只有求和的功能
    print(a+b)


def poweradd(func):     # poweradd为一个装饰器，返回一个新函数inner，新函数是在add函数的基础上加了新的功能
    def inner(a, b):
        print("hello world")
        add(a, b)
    return inner


f = poweradd(add)
print(type(f))    # <class 'function'>
f(3, 6)
