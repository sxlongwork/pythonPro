# function 定义

# 无参定义


def say_hello():
    """函数定义"""

    print("hello dear.")


say_hello()     # 函数调用


# 带有参数的定义
def get_max(a, b):      # 形参(形式参数)
    if a > b:
        print(a)
    else:
        print(b)


get_max(3, 5)       # 传递实参，与形参位置对应，个数也与形参相对应，会按顺序传参(位置参数)
get_max(b=5, a=12)  # 关键字参数调用，这里就可以与参数顺序无关了


# 默认参数
def get_square(num, lo=2):
    print(num**lo)


# get_square(5)
# get_square(4, 3)


# 可变长参数


def get_sum(*num):
    """可变长参数函数"""

    summ = 0
    for i in num:
        summ += i
    return summ


print(get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))


def print_alpha(*args):

    """可变长参数

    :param args: 代表可以传入多个参数
    """
    for i in args:
        print(i)


print_alpha("a", "b", "c")
# list1 = [1,2,3,4,5]
# print(sum(list1))
# print(set("abc").issubset(set("aabccd")))

