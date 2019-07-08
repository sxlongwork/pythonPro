
# 通用装饰器


def outer(func):
    def inner(*args, **kwargs):
        # 在这里添加新功能修饰传入的函数
        print("***********")

        return func(*args, **kwargs)    # 如果func函数有返回值则在这里返回
    return inner


@outer
def myprint(name, age, sex):
    print("{} is {} years old,and is a {}".format(name, age, sex))


myprint("xiaoming", 23, "man")










