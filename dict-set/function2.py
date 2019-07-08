# function

# from function1 import get_max

# 定义空函数，pass命令


def nop():
    pass


# 位置参数
# def power(x):
#     return x**2


# 默认参数，当只传入一个参数时，第二个参数默认
def power(x, n=2):
    sum = 1
    while n > 0:
        sum *= x
        n -= 1
    return sum


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
print(power(4, 3))
print(power(4))
print("-"*30)


# 可变参数
def get_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


he = get_sum(3, 4, 5 ,6)  # 可传入多个参数
print(he)

