# 断言
# 可用于调式代码，看出哪里有问题

def func(a, b):
    assert (b != 0), "b 不能为0"
    return a / b


print(func(12, 0))

