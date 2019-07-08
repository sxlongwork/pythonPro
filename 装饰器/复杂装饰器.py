


def outer(func):
    def inner(name, age):
        if age < 0:
            age = 0
            func(name, age)     # 执行作为参数传过来的函数
    return inner


# 使用@符号作用于函数，相当于给函数加上装饰器
@outer      # 相当于 myprint = outer(myprint)
def myprint(name, age):
    print("{} is {} years old".format(name, age))

# myprint = outer(myprint)

myprint("xiaoming", -12)