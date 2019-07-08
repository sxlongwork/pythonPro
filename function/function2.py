# function
# 多个关键字参数，在函数内部组成一个字典，通过对字典的遍历获取传递的每一个值
def abc(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


abc(name="xiaoming", age=12, sex="girl")

# return 返回语句


def hello(a, b):
    print(a*b)
    return a*b






print(hello(2,3))

get_sum = lambda a, b: a+b


print(get_sum(2, 3))
